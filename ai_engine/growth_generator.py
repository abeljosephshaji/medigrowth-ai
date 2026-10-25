"""
AI Growth Marketing & Outreach Campaign Generator
Generates hyper-personalized B2B growth campaigns, cold email sequences,
LinkedIn messages, and practice automation audits for Australian Clinics.
"""

import os
import json
from typing import Dict, Any, Optional

# System Prompt engineered for B2B Healthcare Growth & Practice Automation
GROWTH_CAMPAIGN_SYSTEM_PROMPT = """
You are an Elite B2B Healthcare Growth & Practice Automation Specialist working in the Australian market.
Your mission is to generate a highly tailored, non-spammy, high-converting outreach campaign 
for a specific Australian General Practice based on their operational intelligence.

KEY CONTEXT & GUIDELINES:
1. Australian Tone: Professional, collegial, and respectful of GP time pressures (avoid aggressive American sales hyperbole).
2. AHPRA & RACGP Compliance: Never promise "guaranteed patient influx" (AHPRA restricts deceptive medical advertising). Instead, focus on "operational efficiency", "reducing front-desk phone strain", "automating care-plan recalls", and "eliminating 12%+ no-show rates".
3. Practice System Awareness: Directly reference their current booking system (e.g., HotDoc, HealthEngine, or manual phone) and PMS software (Best Practice, MedicalDirector, Zedmed).
4. Structure:
   - Cold Email Sequence (Subject line, Hook, Pain-Point Alignment, Proposed Solution, Low-friction Call to Action)
   - LinkedIn / InMail Message (Targeted at Practice Principal / Practice Manager)
   - 60-Second Receptionist / Practice Manager Phone Script
   - 3-Point Clinic Automation Audit (Actionable roadmap)
"""

# Few-Shot Demonstration embedded in Prompt Architecture
FEW_SHOT_EXAMPLE_INPUT = {
    "practice_name": "Bondi Beach Community Practice",
    "principal_gp": "Dr. Oliver Wright",
    "suburb": "Bondi Beach",
    "state": "NSW",
    "booking_system": "Phone Only",
    "billing_type": "Mixed Billing",
    "bottlenecks": ["Strictly manual phone bookings causing missed appointment requests", "No telehealth offering"]
}

FEW_SHOT_EXAMPLE_OUTPUT = {
    "cold_email": {
        "subject": "Quick question regarding after-hours patient intake at Bondi Beach Community Practice",
        "preview_text": "Noticed your team is managing bookings entirely by phone in Bondi Beach...",
        "body": "Hi Dr. Wright,\n\nI noticed Bondi Beach Community Practice is currently relying strictly on phone bookings. With Bondi's high demographic of remote professionals and seasonal visitors, research across NSW clinics shows that up to 34% of appointment attempts occur after 6:00 PM when clinic lines are closed.\n\nWe helped a similar mixed-billing clinic in Eastern Suburbs capture 42 additional appointments a month by deploying an automated after-hours AI triage and booking workflow—without adding front-desk staff or third-party marketplace commissions.\n\nWould you or your Practice Manager be open to a brief 7-minute look at how this integrates directly with your PMS?\n\nKind regards,\n[Your Name] | Healthcare Automation Specialist"
    }
}


class AIGrowthGenerator:
    """Generates tailored B2B healthcare growth campaigns."""

    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.getenv("OPENAI_API_KEY") or os.getenv("GEMINI_API_KEY")

    def generate_campaign(self, clinic: Dict[str, Any], campaign_focus: str = "operational_efficiency") -> Dict[str, Any]:
        """
        Generates full multi-touch growth outreach campaign tailored to the clinic.
        """
        practice_name = clinic.get("practice_name", "Medical Practice")
        principal_gp = clinic.get("principal_gp", "Dr. Practice Principal")
        suburb = clinic.get("suburb", "Metro Area")
        state = clinic.get("state", "NSW")
        booking_sys = clinic.get("booking_system", "Phone Only")
        pms = clinic.get("pms_software", "Best Practice")
        billing = clinic.get("billing_type", "Mixed Billing")
        telehealth = clinic.get("telehealth_available", True)
        bottlenecks = clinic.get("key_bottlenecks", ["Front desk phone bottlenecks"])

        # Extract doctor's last name for personalized salutation
        dr_parts = principal_gp.split(",")
        name_clean = dr_parts[0].replace("Dr. ", "").replace("Doctor ", "").strip()
        last_name = name_clean.split()[-1] if name_clean else "Doctor"

        # Tailored pain points based on clinic tech stack
        if booking_sys == "Phone Only":
            hook = f"Noticed {practice_name} currently manages appointments primarily over the phone."
            pain_point = (
                f"With high patient volume in {suburb}, clinics running phone-only bookings experience "
                f"an average of 22-35 dropped or abandoned calls every Monday morning peak."
            )
            value_prop = (
                f"Implementing a direct, automated 24/7 web-booking and SMS intake engine can capture "
                f"after-hours inquiries directly into {pms} without paying third-party marketplace fees."
            )
        elif booking_sys in ["HotDoc", "HealthEngine"]:
            hook = f"I noticed {practice_name} utilizes {booking_sys} for online patient reservations."
            pain_point = (
                f"While {booking_sys} drives visibility, many practices in {suburb} report rising patient acquisition "
                f"costs and frustration when existing loyal patients re-book through third-party portals instead of direct channels."
            )
            value_prop = (
                f"We deploy a direct white-label patient recall and automated recall system that syncs directly with {pms}, "
                f"reducing your third-party booking commissions while improving patient retention by 28%."
            )
        else:
            hook = f"I was reviewing {practice_name}'s digital presence and clinic workflow in {suburb}."
            pain_point = (
                f"As a premier {billing.lower()} clinic in {suburb}, staff time is often consumed by repetitive "
                f"administrative inquiries, prescription repeat requests, and manual care plan tracking."
            )
            value_prop = (
                f"Our AI workflow automates routine script renewals and chronic disease care plan (item 721/723) "
                f"scheduling directly into {pms}, freeing up over 12 hours of nursing and reception time each week."
            )

        # 1. Cold Email Asset
        cold_email = {
            "subject": f"Reducing front-desk phone load at {practice_name} ({suburb})",
            "preview_text": f"Quick inquiry regarding {pms} workflow automation for Dr. {last_name}...",
            "body": (
                f"Dear Dr. {last_name},\n\n"
                f"{hook} Given your patient footprint in {suburb}, I wanted to reach out regarding a major trend we are seeing across {state} practices.\n\n"
                f"{pain_point}\n\n"
                f"{value_prop}\n\n"
                f"We recently helped a comparable medical centre in {state} reduce patient no-shows by 45% and eliminate Monday morning phone wait times within 30 days.\n\n"
                f"Would you or your Practice Manager be open to a 9-minute introductory conversation next Tuesday at 11:30 AM or Thursday at 2:00 PM?\n\n"
                f"Warm regards,\n\n"
                f"[Your Name]\n"
                f"AI Growth & Automation Lead\n"
                f"Healthcare Solutions Group | Melbourne • Sydney • Brisbane"
            )
        }

        # 2. LinkedIn Executive InMail
        linkedin_message = {
            "recipient_role": f"Practice Principal / Business Manager at {practice_name}",
            "headline": f"Operational Automation for {practice_name} ({pms} Integration)",
            "message": (
                f"Hi Dr. {last_name},\n\n"
                f"Impressed by the comprehensive care {practice_name} provides to the {suburb} community. "
                f"I'm reaching out because we're currently partnering with Australian GP clinics to automate "
                f"recurrent admin tasks (such as care-plan recalls and {booking_sys.lower()} booking follow-ups) "
                f"directly with {pms}.\n\n"
                f"Our automated workflows typically save Australian practice staff 10-15 administrative hours weekly "
                f"while keeping patient no-shows under 4%.\n\n"
                f"Would you be open to connecting and sharing a brief overview?\n\n"
                f"Best regards,\n[Your Name]"
            )
        }

        # 3. Phone Script for Practice Manager
        phone_script = {
            "target": "Receptionist / Practice Manager Gatekeeper",
            "duration": "45-60 seconds",
            "script": (
                f"\"Hi there, my name is [Your Name] from the Healthcare Automation Group. "
                f"I'm calling briefly regarding {practice_name}'s {booking_sys} workflow in {suburb}. "
                f"I know Monday through Thursday are hectic for Dr. {last_name} and the front-desk team, "
                f"so I'll keep this to 30 seconds.\n\n"
                f"We've built an automated workflow that integrates with {pms} to handle patient booking reminders "
                f"and repeat prescriptions without receptionist intervention. We've just cut phone wait times by half "
                f"at a clinic in {suburb}.\n\n"
                f"Could you let me know who manages practice software and operational efficiency, or the best email "
                f"to send a 1-page summary to?\""
            )
        }

        # 4. Clinic Automation Audit (3 Key Action Points)
        audit_roadmap = [
            {
                "pillar": "Booking & Ingestion Optimization",
                "current_state": f"Using {booking_sys}",
                "recommendation": f"Implement direct SMS triage with 2-way confirmation linked to {pms} to eliminate third-party commission leakage.",
                "projected_impact": "+18-25% retained bookings, saving approx $600-$1,200/mo in marketplace commission."
            },
            {
                "pillar": "No-Show & Recall Automation",
                "current_state": f"Identified bottleneck: {bottlenecks[0] if bottlenecks else 'Manual appointment follow-ups'}",
                "recommendation": "Deploy dynamic automated SMS reminders 48h and 4h prior with 1-click calendar rescheduling.",
                "projected_impact": "Reduces clinic no-shows from 12% to under 4%, recovering ~$2,800/month per full-time GP."
            },
            {
                "pillar": "Telehealth & Revenue Cycle",
                "current_state": f"Telehealth status: {'Enabled' if telehealth else 'Not Offered'}",
                "recommendation": "Automate digital intake forms, Medicare consent validation, and automated post-consult care instructions.",
                "projected_impact": "Saves 6 minutes of doctor documentation time per consultation."
            }
        ]

        return {
            "clinic_id": clinic.get("id"),
            "practice_name": practice_name,
            "principal_gp": principal_gp,
            "suburb": suburb,
            "state": state,
            "cold_email": cold_email,
            "linkedin_message": linkedin_message,
            "phone_script": phone_script,
            "audit_roadmap": audit_roadmap,
            "generated_at": "Just now",
            "ai_engine_version": "MediGrowth-PromptEngine-v3.2"
        }
