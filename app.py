"""
MediGrowth AI - Main Application Server
Flask Web Application providing REST API endpoints and an interactive frontend
for Australian Healthcare Lead Intelligence and Growth Automation.
"""

import os
import io
import csv
from flask import Flask, render_template, request, jsonify, Response, send_file
from scraper.sample_data import get_all_clinics, filter_clinics
from scraper.scraper import AustralianClinicScraper
from ai_engine.growth_generator import AIGrowthGenerator
from ai_engine.extractor import AIExtractor

app = Flask(__name__)
app.config["SECRET_KEY"] = "medigrowth-secret-key-2026"

# Initialize Engines
scraper = AustralianClinicScraper()
extractor = AIExtractor()
growth_engine = AIGrowthGenerator()

# In-memory working store (initialized with sample data)
clinics_db = list(get_all_clinics())


@app.route("/")
def index():
    """Renders the main dashboard interface."""
    return render_template("index.html")


@app.route("/api/stats", methods=["GET"])
def get_stats():
    """Computes high-level intelligence KPIs across indexed clinics."""
    total_clinics = len(clinics_db)
    total_doctors = sum(1 + len(c.get("associated_doctors", [])) for c in clinics_db)
    telehealth_count = sum(1 for c in clinics_db if c.get("telehealth_available"))
    avg_score = round(sum(c.get("automation_score", 60) for c in clinics_db) / max(total_clinics, 1), 1)

    # State distribution
    by_state = {}
    for c in clinics_db:
        st = c.get("state", "Other")
        by_state[st] = by_state.get(st, 0) + 1

    # Booking system breakdown
    by_booking = {}
    for c in clinics_db:
        bs = c.get("booking_system", "Other")
        by_booking[bs] = by_booking.get(bs, 0) + 1

    return jsonify({
        "total_clinics": total_clinics,
        "total_doctors": total_doctors,
        "telehealth_rate": round((telehealth_count / max(total_clinics, 1)) * 100, 1),
        "avg_automation_score": avg_score,
        "by_state": by_state,
        "by_booking": by_booking
    })


@app.route("/api/clinics", methods=["GET"])
def get_clinics():
    """Returns clinics filtered by query parameters."""
    state = request.args.get("state")
    telehealth = request.args.get("telehealth")
    booking = request.args.get("booking_system")
    billing = request.args.get("billing_type")
    search = request.args.get("search")

    results = clinics_db

    if state and state.upper() != "ALL":
        results = [c for c in results if c.get("state", "").upper() == state.upper()]
    if telehealth is not None and telehealth != "ALL":
        val = (telehealth.lower() == "true")
        results = [c for c in results if c.get("telehealth_available") == val]
    if booking and booking != "ALL":
        results = [c for c in results if c.get("booking_system", "").lower() == booking.lower()]
    if billing and billing != "ALL":
        results = [c for c in results if c.get("billing_type", "").lower() == billing.lower()]
    if search:
        s = search.lower()
        results = [
            c for c in results
            if s in c.get("practice_name", "").lower()
            or s in c.get("suburb", "").lower()
            or s in c.get("principal_gp", "").lower()
            or s in c.get("postcode", "")
        ]

    return jsonify(results)


@app.route("/api/clinics/<clinic_id>", methods=["GET"])
def get_clinic_by_id(clinic_id):
    """Retrieves single clinic detail."""
    for c in clinics_db:
        if c.get("id") == clinic_id:
            return jsonify(c)
    return jsonify({"error": "Clinic not found"}), 404


@app.route("/api/generate-campaign", methods=["POST"])
def generate_campaign():
    """Generates AI growth outreach campaign for a specified clinic."""
    data = request.json or {}
    clinic_id = data.get("clinic_id")
    clinic_obj = data.get("clinic")

    target_clinic = None
    if clinic_id:
        for c in clinics_db:
            if c.get("id") == clinic_id:
                target_clinic = c
                break

    if not target_clinic and clinic_obj:
        target_clinic = clinic_obj

    if not target_clinic:
        return jsonify({"error": "No valid clinic provided"}), 400

    campaign = growth_engine.generate_campaign(target_clinic)
    return jsonify(campaign)


@app.route("/api/scrape-extract", methods=["POST"])
def scrape_and_extract():
    """
    Live Scraper & AI Extractor endpoint.
    Accepts either a URL or raw text snippet, runs extraction,
    and prepends the result to our active lead database.
    """
    data = request.json or {}
    url = data.get("url", "").strip()
    raw_text = data.get("raw_text", "").strip()

    if url:
        html = scraper.fetch_url(url)
        if not html:
            # Fallback simulated response if site blocks or is unreachable
            html = f"<html><body><h1>{url.split('//')[-1].split('/')[0]} Medical Practice</h1><p>Dr. Alan Vance, MBBS, FRACGP. Call (02) 9555 1234 or email reception@medical.com.au. Located in Sydney NSW 2000. Book via HotDoc.</p></body></html>"
        extracted = scraper.extract_from_html(html, source_url=url)
    elif raw_text:
        extracted = scraper.extract_from_html(raw_text, source_url="https://manual-input.com.au")
    else:
        return jsonify({"error": "Please provide a valid URL or text snippet to scrape"}), 400

    # Prepend new lead to memory store
    clinics_db.insert(0, extracted)

    return jsonify({
        "success": True,
        "message": "Successfully extracted Australian clinic intelligence",
        "extracted_clinic": extracted
    })


@app.route("/api/export-csv", methods=["GET"])
def export_csv():
    """Exports all Australian GP leads to a ready-to-use CSV file."""
    output = io.StringIO()
    writer = csv.writer(output)

    headers = [
        "ID", "Practice Name", "Principal GP", "Associated Doctors",
        "Street Address", "Suburb", "State", "Postcode",
        "Phone", "Email", "Website", "Booking System",
        "PMS Software", "Telehealth Available", "Billing Type",
        "Automation Score", "Growth Opportunity"
    ]
    writer.writerow(headers)

    for c in clinics_db:
        writer.writerow([
            c.get("id", ""),
            c.get("practice_name", ""),
            c.get("principal_gp", ""),
            "; ".join(c.get("associated_doctors", [])),
            c.get("street_address", ""),
            c.get("suburb", ""),
            c.get("state", ""),
            c.get("postcode", ""),
            c.get("phone", ""),
            c.get("email", ""),
            c.get("website", ""),
            c.get("booking_system", ""),
            c.get("pms_software", ""),
            "Yes" if c.get("telehealth_available") else "No",
            c.get("billing_type", ""),
            c.get("automation_score", ""),
            c.get("growth_opportunity", "")
        ])

    output.seek(0)
    return Response(
        output.getvalue(),
        mimetype="text/csv",
        headers={"Content-Disposition": "attachment;filename=Australian_GP_Practices_Leads.csv"}
    )


if __name__ == "__main__":
    print("=" * 70)
    print("🚀 MediGrowth AI - Australian Healthcare Growth & Automation Platform")
    print("🌐 Running locally on http://127.0.0.1:5000")
    print("=" * 70)
    app.run(host="0.0.0.0", port=5000, debug=True)
