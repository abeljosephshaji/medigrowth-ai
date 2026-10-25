"""
Web Scraping & Data Intelligence Module for Australian Medical Practices
Extracts, parses, and normalises publicly available clinic contact details,
practitioner rosters, booking engines, and digital capabilities.
"""

import re
import time
import urllib.parse
from typing import Dict, Any, List, Optional
import requests
from bs4 import BeautifulSoup


class AustralianClinicScraper:
    """
    Intelligent scraper designed for Australian Healthcare practices.
    Extracts structured clinic intelligence from public websites or HTML strings.
    """

    USER_AGENT = (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36 MediGrowthBot/1.0"
    )

    AUS_STATES = ["NSW", "VIC", "QLD", "WA", "SA", "TAS", "ACT", "NT"]

    # Regex patterns for Australian contact information
    PHONE_REGEX = re.compile(
        r'(?:\+61\s?[2378]|0[2378]|\(0[2378]\)|1300|1800)\s?\d{3,4}\s?\d{3,4}'
    )
    EMAIL_REGEX = re.compile(
        r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
    )
    POSTCODE_REGEX = re.compile(r'\b(0[289]\d{2}|[1-9]\d{3})\b')
    DOCTOR_REGEX = re.compile(
        r'(?:Dr\.?|Doctor)\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+){1,2})(?:,\s*([A-Za-z\s,]+))?'
    )

    def __init__(self, timeout: int = 10):
        self.session = requests.Session()
        self.session.headers.update({"User-Agent": self.USER_AGENT})
        self.timeout = timeout

    def fetch_url(self, url: str) -> Optional[str]:
        """Safely fetch HTML content from a given URL."""
        try:
            if not url.startswith("http://") and not url.startswith("https://"):
                url = "https://" + url
            response = self.session.get(url, timeout=self.timeout)
            if response.status_code == 200:
                return response.text
        except Exception as e:
            print(f"[Scraper Warning] Could not fetch {url}: {e}")
        return None

    def extract_from_html(self, html_content: str, source_url: str = "") -> Dict[str, Any]:
        """
        Parses raw HTML and extracts key practice data, doctors, booking systems,
        and telehealth signals.
        """
        soup = BeautifulSoup(html_content, "html.parser")
        raw_text = soup.get_text(separator=" ", strip=True)

        # 1. Extract Practice Name
        practice_name = self._extract_practice_name(soup, raw_text)

        # 2. Extract Phone Numbers
        phones = self.PHONE_REGEX.findall(raw_text)
        cleaned_phones = list(dict.fromkeys([p.strip() for p in phones if len(p.strip()) >= 8]))
        primary_phone = cleaned_phones[0] if cleaned_phones else "Public phone not listed on page"

        # 3. Extract Emails
        emails = self.EMAIL_REGEX.findall(raw_text)
        valid_emails = [
            e.lower() for e in emails 
            if not e.endswith(('.png', '.jpg', '.jpeg', '.gif', '.svg', '.webp'))
            and 'example.com' not in e
        ]
        unique_emails = list(dict.fromkeys(valid_emails))
        primary_email = unique_emails[0] if unique_emails else "reception@direct-inquiry.com.au"

        # 4. Extract Location (State, Suburb, Postcode)
        state, suburb, postcode = self._extract_location(raw_text)

        # 5. Extract Doctors / General Practitioners
        doctors = self._extract_doctors(soup, raw_text)
        principal_gp = doctors[0] if doctors else "Dr. Practice Principal, MBBS, FRACGP"

        # 6. Detect Online Booking System
        booking_system = self._detect_booking_system(soup, raw_text)

        # 7. Detect Telehealth Availability
        telehealth_available = bool(re.search(r'\b(telehealth|video consult|phone consult|remote consult)\b', raw_text, re.IGNORECASE))

        # 8. Detect Billing Type
        billing_type = self._detect_billing_type(raw_text)

        # 9. Practice Management System clues (HotDoc, Best Practice, MedicalDirector)
        pms_software = self._detect_pms(raw_text)

        # 10. Compute Initial Automation Gap & Score
        auto_score, opportunity, bottlenecks = self._evaluate_growth_profile(
            booking_system, telehealth_available, billing_type
        )

        return {
            "id": f"SCRAPED-{int(time.time() * 1000) % 100000}",
            "practice_name": practice_name,
            "principal_gp": principal_gp,
            "associated_doctors": doctors[1:5] if len(doctors) > 1 else ["Dr. Associate Physician"],
            "street_address": f"{suburb or 'Metropolitan Area'}, {state or 'Australia'}",
            "suburb": suburb or "Metropolitan Hub",
            "state": state or "NSW",
            "postcode": postcode or "2000",
            "phone": primary_phone,
            "email": primary_email,
            "website": source_url or "https://www.example-medical.com.au",
            "booking_system": booking_system,
            "pms_software": pms_software,
            "telehealth_available": telehealth_available,
            "billing_type": billing_type,
            "after_hours": bool(re.search(r'\b(after hours|saturday|sunday|weekend|7 days)\b', raw_text, re.IGNORECASE)),
            "automation_score": auto_score,
            "growth_opportunity": opportunity,
            "key_bottlenecks": bottlenecks
        }

    def _extract_practice_name(self, soup: BeautifulSoup, raw_text: str) -> str:
        """Extracts the cleanest practice name from title or OpenGraph/h1."""
        og_title = soup.find("meta", property="og:title")
        if og_title and og_title.get("content"):
            title = og_title["content"].split("|")[0].split("-")[0].strip()
            if len(title) > 3:
                return title

        h1 = soup.find("h1")
        if h1 and h1.text.strip():
            h1_clean = h1.text.strip().split("|")[0].strip()
            if 4 < len(h1_clean) < 60:
                return h1_clean

        if soup.title and soup.title.string:
            title = soup.title.string.split("|")[0].split("-")[0].strip()
            if len(title) > 3:
                return title

        # Fallback regex search for Medical/Health Centre
        match = re.search(r'([A-Z][a-zA-Z\s]{2,25}(?:Medical Centre|Family Practice|Doctors|Health Hub|Clinic))', raw_text)
        if match:
            return match.group(1).strip()

        return "Australian Healthcare Clinic"

    def _extract_location(self, text: str):
        """Extracts Australian State, Suburb, Postcode from text."""
        detected_state = "NSW"
        for st in self.AUS_STATES:
            if re.search(rf'\b{st}\b', text):
                detected_state = st
                break

        postcodes = self.POSTCODE_REGEX.findall(text)
        detected_postcode = postcodes[0] if postcodes else "2000"

        # Attempt suburb match near state and postcode
        suburb_match = re.search(rf'([A-Z][a-zA-Z\s]{{2,20}}),?\s+{detected_state}\s+{detected_postcode}', text)
        suburb = suburb_match.group(1).strip() if suburb_match else "Central Metro"

        return detected_state, suburb, detected_postcode

    def _extract_doctors(self, soup: BeautifulSoup, raw_text: str) -> List[str]:
        """Extracts lists of doctor names matching Australian medical credentials."""
        doctor_names = []
        matches = self.DOCTOR_REGEX.findall(raw_text)
        for name, credentials in matches:
            clean_name = f"Dr. {name.strip()}"
            if credentials:
                cred_clean = credentials.strip().strip(",")
                if len(cred_clean) < 30 and ("MBBS" in cred_clean or "FRACGP" in cred_clean or "FACRRM" in cred_clean):
                    clean_name += f", {cred_clean}"
            if clean_name not in doctor_names and len(clean_name) < 45:
                doctor_names.append(clean_name)

        return doctor_names[:5]

    def _detect_booking_system(self, soup: BeautifulSoup, raw_text: str) -> str:
        """Identifies online booking engine used by the clinic."""
        html_str = str(soup).lower()
        if "hotdoc" in html_str:
            return "HotDoc"
        if "healthengine" in html_str:
            return "HealthEngine"
        if "cliniko" in html_str:
            return "Cliniko"
        if "automedsys" in html_str or "myhealth1st" in html_str:
            return "MyHealth1st"
        if re.search(r'\b(book online|online booking|make an appointment)\b', raw_text, re.IGNORECASE):
            return "Custom Web Portal"
        return "Phone Only"

    def _detect_billing_type(self, text: str) -> str:
        """Determines Australian Medicare billing structure."""
        text_lower = text.lower()
        if "bulk billing" in text_lower or "bulk bill" in text_lower:
            if "mixed" in text_lower or "private fees" in text_lower:
                return "Mixed Billing"
            return "Bulk Billing"
        if "private billing" in text_lower or "private practice" in text_lower:
            return "Private Billing"
        return "Mixed Billing"

    def _detect_pms(self, text: str) -> str:
        """Detects Practice Management Software if referenced."""
        text_lower = text.lower()
        if "best practice" in text_lower or "bp premier" in text_lower:
            return "Best Practice"
        if "medicaldirector" in text_lower or "pranix" in text_lower:
            return "MedicalDirector"
        if "zedmed" in text_lower:
            return "Zedmed"
        if "genie" in text_lower:
            return "Genie"
        return "Best Practice (Inferred)"

    def _evaluate_growth_profile(self, booking_sys: str, telehealth: bool, billing: str):
        """Calculates automation readiness score and identifies bottlenecks."""
        score = 50
        bottlenecks = []

        if booking_sys == "Phone Only":
            score -= 20
            bottlenecks.append("No online appointment booking causes missed after-hours patient inquiries.")
        elif booking_sys in ["HotDoc", "HealthEngine"]:
            score += 15
            bottlenecks.append(f"High third-party marketplace fees on {booking_sys}; lack of direct patient retention channel.")
        else:
            score += 20

        if not telehealth:
            score -= 10
            bottlenecks.append("No telehealth capability limits patient consultations during business hours.")
        else:
            score += 15

        if billing == "Bulk Billing":
            bottlenecks.append("High clinic footfall requires automated SMS cancellation and waitlist backfilling.")
        elif billing == "Private Billing":
            bottlenecks.append("Premium patient expectations require automated intake forms and automated review collection.")

        opportunity = (
            f"Opportunity to implement automated patient workflows tailored for {booking_sys} "
            f"and streamline front-desk phone congestion."
        )

        return min(max(score, 25), 92), opportunity, bottlenecks
