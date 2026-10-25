"""
Sample Pre-Enriched Dataset of Australian General Practices and Clinics
Contains authentic Australian healthcare practice structures, suburbs, postcodes,
booking software, and automation gap assessments for demonstration and testing.
"""

AUSTRALIAN_GP_DATA = [
    {
        "id": "GP-NSW-001",
        "practice_name": "Sydney Central Medical Centre",
        "principal_gp": "Dr. Sarah Henderson, MBBS, FRACGP",
        "associated_doctors": ["Dr. Mark Liu", "Dr. Amanda Chen", "Dr. David Kelly"],
        "street_address": "Level 1, 580 George Street",
        "suburb": "Sydney",
        "state": "NSW",
        "postcode": "2000",
        "phone": "+61 2 9267 8900",
        "email": "reception@sydneycentralmed.com.au",
        "website": "https://www.sydneycentralmed.com.au",
        "booking_system": "HotDoc",
        "pms_software": "Best Practice",
        "telehealth_available": True,
        "billing_type": "Mixed Billing",
        "after_hours": True,
        "automation_score": 78,
        "growth_opportunity": "High patient volume; currently paying high marketplace fees on HotDoc. Prime candidate for a direct white-label patient recall & SMS confirmation workflow.",
        "key_bottlenecks": [
            "HotDoc dependency with recurring commission costs",
            "Peak morning phone wait times exceeding 12 minutes",
            "Manual chronic disease care plan reminders"
        ]
    },
    {
        "id": "GP-NSW-002",
        "practice_name": "Surry Hills Family & Sports Doctors",
        "principal_gp": "Dr. Lachlan Thomas, BMed, FRACGP",
        "associated_doctors": ["Dr. Elena Rossi", "Dr. James Fletcher"],
        "street_address": "412 Crown Street",
        "suburb": "Surry Hills",
        "state": "NSW",
        "postcode": "2010",
        "phone": "+61 2 9360 4421",
        "email": "admin@surryhillsdoctors.com.au",
        "website": "https://www.surryhillsdoctors.com.au",
        "booking_system": "HealthEngine",
        "pms_software": "MedicalDirector",
        "telehealth_available": True,
        "billing_type": "Private Billing",
        "after_hours": False,
        "automation_score": 62,
        "growth_opportunity": "High-income demographic with 30% Allied Health crossover. Can automate cross-referral bookings to in-house physio and clinical psychology.",
        "key_bottlenecks": [
            "Manual paper-based intake forms for new patients",
            "No automated post-consultation Google review generation",
            "Under-utilized weekend telehealth slots"
        ]
    },
    {
        "id": "GP-NSW-003",
        "practice_name": "Bondi Beach Community Practice",
        "principal_gp": "Dr. Oliver Wright, MBBS, DipChildHealth",
        "associated_doctors": ["Dr. Sophie Campbell", "Dr. Ben Miller"],
        "street_address": "120 Campbell Parade",
        "suburb": "Bondi Beach",
        "state": "NSW",
        "postcode": "2026",
        "phone": "+61 2 9130 5588",
        "email": "hello@bondibeachpractice.com.au",
        "website": "https://www.bondibeachpractice.com.au",
        "booking_system": "Phone Only",
        "pms_software": "Best Practice",
        "telehealth_available": False,
        "billing_type": "Mixed Billing",
        "after_hours": False,
        "automation_score": 34,
        "growth_opportunity": "Zero digital booking capability. Adding an automated AI web-booking widget and SMS triage will capture 45+ after-hours tourist/surfer inquiries weekly.",
        "key_bottlenecks": [
            "Strictly manual phone bookings causing missed appointment requests",
            "No telehealth offering despite heavy traveler and remote worker patient base",
            "Manual SMS reminders prone to human error"
        ]
    },
    {
        "id": "GP-NSW-004",
        "practice_name": "Parramatta Metro Health Hub",
        "principal_gp": "Dr. Rajesh Sharma, MBBS, FRACGP, FACRRM",
        "associated_doctors": ["Dr. Anita Patel", "Dr. Tariq Al-Mansoor", "Dr. Claire Zhang"],
        "street_address": "Suite 4, 150 Church Street",
        "suburb": "Parramatta",
        "state": "NSW",
        "postcode": "2150",
        "phone": "+61 2 9687 3311",
        "email": "practice.manager@parramattamedhub.com.au",
        "website": "https://www.parramattamedhub.com.au",
        "booking_system": "HotDoc",
        "pms_software": "Zedmed",
        "telehealth_available": True,
        "billing_type": "Bulk Billing",
        "after_hours": True,
        "automation_score": 71,
        "growth_opportunity": "High patient churn and no-show rate (~14%). An automated 2-way WhatsApp/SMS confirmation bot can reduce no-shows by 60%.",
        "key_bottlenecks": [
            "High no-show rates on Bulk-Billed consultation slots",
            "Multilingual patient base struggling with English-only reception",
            "Disorganized pathology result follow-up pipeline"
        ]
    },
    {
        "id": "GP-VIC-001",
        "practice_name": "Melbourne CBD Medical Clinic",
        "principal_gp": "Dr. Catherine Vance, MBBS, FRACGP",
        "associated_doctors": ["Dr. Liam O'Connor", "Dr. Wei Zhou", "Dr. Jessica Bell"],
        "street_address": "Shop 3, 250 Collins Street",
        "suburb": "Melbourne",
        "state": "VIC",
        "postcode": "3000",
        "phone": "+61 3 9650 1199",
        "email": "info@melbcbdmedical.com.au",
        "website": "https://www.melbcbdmedical.com.au",
        "booking_system": "HotDoc",
        "pms_software": "Best Practice",
        "telehealth_available": True,
        "billing_type": "Mixed Billing",
        "after_hours": True,
        "automation_score": 82,
        "growth_opportunity": "Corporate executive health checkups. Automated B2B corporate health portal can add $120k ARR in corporate retainer accounts.",
        "key_bottlenecks": [
            "Manual corporate invoicing and employer billing reconciliations",
            "Overloaded reception during lunch hour rush (12pm - 2pm)"
        ]
    },
    {
        "id": "GP-VIC-002",
        "practice_name": "South Yarra Holistic Health Clinic",
        "principal_gp": "Dr. Sebastian Thorne, BMedSc, MBBS, FRACGP",
        "associated_doctors": ["Dr. Maya Lin", "Dr. Julian Pearce"],
        "street_address": "52 Toorak Road",
        "suburb": "South Yarra",
        "state": "VIC",
        "postcode": "3141",
        "phone": "+61 3 9866 7744",
        "email": "concierge@southyarrahealth.com.au",
        "website": "https://www.southyarrahealth.com.au",
        "booking_system": "Custom Web Portal",
        "pms_software": "Genie",
        "telehealth_available": True,
        "billing_type": "Private Billing",
        "after_hours": False,
        "automation_score": 68,
        "growth_opportunity": "Premium aesthetics and preventative longevity screenings. Automated email nurture sequence for high-ticket skin cancer and longevity programs.",
        "key_bottlenecks": [
            "Lead drop-off between inquiry and completed aesthetic consultation",
            "No structured automated follow-up for preventive blood panel checkups"
        ]
    },
    {
        "id": "GP-VIC-003",
        "practice_name": "Brunswick Community Medical Group",
        "principal_gp": "Dr. Freya Lindqvist, MBBS, FRACGP",
        "associated_doctors": ["Dr. Samira Khan", "Dr. Leo Evans"],
        "street_address": "288 Sydney Road",
        "suburb": "Brunswick",
        "state": "VIC",
        "postcode": "3056",
        "phone": "+61 3 9380 9901",
        "email": "reception@brunswickmedicalgroup.com.au",
        "website": "https://www.brunswickmedicalgroup.com.au",
        "booking_system": "HealthEngine",
        "pms_software": "MedicalDirector",
        "telehealth_available": True,
        "billing_type": "Mixed Billing",
        "after_hours": False,
        "automation_score": 59,
        "growth_opportunity": "Young millennial/Gen-Z demographic preferring text-based asynchronous triage. Implementing an AI chat widget will convert 35% more web visitors.",
        "key_bottlenecks": [
            "No interactive triage chatbot for standard queries (script repeats, vaccine info)",
            "Manual script renewal approval process tying up doctor administrative time"
        ]
    },
    {
        "id": "GP-VIC-004",
        "practice_name": "St Kilda Bay Doctors",
        "principal_gp": "Dr. Harrison Scott, MBBS, FACRRM",
        "associated_doctors": ["Dr. Rachel Green", "Dr. Anthony Ross"],
        "street_address": "14 Acland Street",
        "suburb": "St Kilda",
        "state": "VIC",
        "postcode": "3182",
        "phone": "+61 3 9534 8820",
        "email": "contact@stkildabaydoctors.com.au",
        "website": "https://www.stkildabaydoctors.com.au",
        "booking_system": "HotDoc",
        "pms_software": "Best Practice",
        "telehealth_available": True,
        "billing_type": "Bulk Billing",
        "after_hours": True,
        "automation_score": 65,
        "growth_opportunity": "Large volume of recurrent prescriptions. AI repeat-prescription workflow can liberate 10 hours/week of GP admin overhead.",
        "key_bottlenecks": [
            "Doctor burnout caused by manual prescription renewal requests",
            "Slow intake of seasonal flu and travel vaccine campaigns"
        ]
    },
    {
        "id": "GP-QLD-001",
        "practice_name": "Brisbane City Doctors & Specialists",
        "principal_gp": "Dr. Timothy Higgins, MBBS, FRACGP",
        "associated_doctors": ["Dr. Chloe Davenport", "Dr. Kevin Tran", "Dr. Natalie Hughes"],
        "street_address": "Level 2, 240 Queen Street",
        "suburb": "Brisbane City",
        "state": "QLD",
        "postcode": "4000",
        "phone": "+61 7 3221 3377",
        "email": "info@brisbanecitydoctors.com.au",
        "website": "https://www.brisbanecitydoctors.com.au",
        "booking_system": "HotDoc",
        "pms_software": "Best Practice",
        "telehealth_available": True,
        "billing_type": "Mixed Billing",
        "after_hours": False,
        "automation_score": 75,
        "growth_opportunity": "Expansion into workplace corporate vaccination packages. Automated campaign outreach to CBD corporate HR directors.",
        "key_bottlenecks": [
            "Lack of proactive outbound outreach for executive health check programs",
            "Manual paperwork for corporate influenza clinics"
        ]
    },
    {
        "id": "GP-QLD-002",
        "practice_name": "Fortitude Valley Medical & Skin Clinic",
        "principal_gp": "Dr. Angela Morrison, MBBS, MMed(Skin Cancer)",
        "associated_doctors": ["Dr. Peter Finch", "Dr. Mei Ling Wong"],
        "street_address": "680 Ann Street",
        "suburb": "Fortitude Valley",
        "state": "QLD",
        "postcode": "4006",
        "phone": "+61 7 3852 9010",
        "email": "skin@fortitudevalleymed.com.au",
        "website": "https://www.fortitudevalleymed.com.au",
        "booking_system": "HotDoc",
        "pms_software": "MedicalDirector",
        "telehealth_available": True,
        "billing_type": "Private Billing",
        "after_hours": True,
        "automation_score": 72,
        "growth_opportunity": "Annual skin check recalls. Automated SMS reminder workflow triggered 11 months post-biopsy drives 40% automated re-bookings.",
        "key_bottlenecks": [
            "Lost revenue from overdue annual skin cancer recalls",
            "No automated photo submission workflow prior to mole excision bookings"
        ]
    },
    {
        "id": "GP-QLD-003",
        "practice_name": "Gold Coast Family Healthcare",
        "principal_gp": "Dr. Bradley Cooper, BMed, FRACGP",
        "associated_doctors": ["Dr. Lisa Ray", "Dr. Daniel Fox"],
        "street_address": "25 Surfers Paradise Boulevard",
        "suburb": "Surfers Paradise",
        "state": "QLD",
        "postcode": "4217",
        "phone": "+61 7 5592 1100",
        "email": "contact@gcfamilyhealth.com.au",
        "website": "https://www.gcfamilyhealth.com.au",
        "booking_system": "Phone Only",
        "pms_software": "Best Practice",
        "telehealth_available": False,
        "billing_type": "Mixed Billing",
        "after_hours": False,
        "automation_score": 40,
        "growth_opportunity": "Tourist hotspot with zero online self-service booking. Implementing an integrated booking engine will capture 60+ emergency & tourist appointments weekly.",
        "key_bottlenecks": [
            "Reception line constantly busy during morning tourist spikes",
            "No digital patient registration form causing physical queue in waiting room"
        ]
    },
    {
        "id": "GP-WA-001",
        "practice_name": "Perth Central Medical Practice",
        "principal_gp": "Dr. Cameron Stewart, MBBS, FRACGP",
        "associated_doctors": ["Dr. Zara Johnston", "Dr. Aaron Murphy", "Dr. Grace Kelly"],
        "street_address": "125 St Georges Terrace",
        "suburb": "Perth",
        "state": "WA",
        "postcode": "6000",
        "phone": "+61 8 9481 2233",
        "email": "admin@perthcentralmedical.com.au",
        "website": "https://www.perthcentralmedical.com.au",
        "booking_system": "HotDoc",
        "pms_software": "Best Practice",
        "telehealth_available": True,
        "billing_type": "Mixed Billing",
        "after_hours": True,
        "automation_score": 80,
        "growth_opportunity": "FIFO (Fly-In Fly-Out) medical clearance and remote worker telehealth subscription packages. AI automation can fast-track pre-employment medical reports.",
        "key_bottlenecks": [
            "Slow turnaround on FIFO pre-employment fitness questionnaires",
            "Manual coordinator phone calls to schedule audiometry and spirometry"
        ]
    },
    {
        "id": "GP-WA-002",
        "practice_name": "Fremantle Port Family Practice",
        "principal_gp": "Dr. Penelope Vance, MBBS, DipObst",
        "associated_doctors": ["Dr. Simon Bell", "Dr. Hannah Cox"],
        "street_address": "84 Adelaide Street",
        "suburb": "Fremantle",
        "state": "WA",
        "postcode": "6160",
        "phone": "+61 8 9335 1877",
        "email": "care@fremantleportpractice.com.au",
        "website": "https://www.fremantleportpractice.com.au",
        "booking_system": "HealthEngine",
        "pms_software": "Zedmed",
        "telehealth_available": True,
        "billing_type": "Bulk Billing",
        "after_hours": False,
        "automation_score": 54,
        "growth_opportunity": "Chronic pediatric and immunization tracking. Automated vaccine schedule reminders linked to Australian Immunisation Register (AIR).",
        "key_bottlenecks": [
            "Heavy manual checking of pediatric vaccine due dates",
            "High rate of last-minute cancellations without automatic re-booking waitlist"
        ]
    },
    {
        "id": "GP-SA-001",
        "practice_name": "Adelaide Hills Doctors & Wellness",
        "principal_gp": "Dr. Andrew MacIntyre, BMBS, FRACGP",
        "associated_doctors": ["Dr. Catherine Hill", "Dr. Thomas Clark"],
        "street_address": "18 Mt Barker Road",
        "suburb": "Stirling",
        "state": "SA",
        "postcode": "5152",
        "phone": "+61 8 8339 6000",
        "email": "reception@adelaidehillsdocs.com.au",
        "website": "https://www.adelaidehillsdocs.com.au",
        "booking_system": "HotDoc",
        "pms_software": "Best Practice",
        "telehealth_available": True,
        "billing_type": "Private Billing",
        "after_hours": False,
        "automation_score": 67,
        "growth_opportunity": "Elderly patient chronic disease management. Automated quarterly care plan review notifications and Home Medicine Review (HMR) referrals.",
        "key_bottlenecks": [
            "Manual tracking of 721/723 GP Care Plan eligibility milestones",
            "Missed Medicare billing incentive items due to lack of automation triggers"
        ]
    },
    {
        "id": "GP-SA-002",
        "practice_name": "North Adelaide Family Clinic",
        "principal_gp": "Dr. Stephanie Ward, MBBS, FRACGP",
        "associated_doctors": ["Dr. Richard Taylor", "Dr. Emily Davies"],
        "street_address": "120 O'Connell Street",
        "suburb": "North Adelaide",
        "state": "SA",
        "postcode": "5006",
        "phone": "+61 8 8267 4333",
        "email": "info@northadelaideclinic.com.au",
        "website": "https://www.northadelaideclinic.com.au",
        "booking_system": "HealthEngine",
        "pms_software": "MedicalDirector",
        "telehealth_available": True,
        "billing_type": "Mixed Billing",
        "after_hours": True,
        "automation_score": 70,
        "growth_opportunity": "Specialist referral loop automation. Auto-notifying referring specialists when patient consults are completed.",
        "key_bottlenecks": [
            "Slow snail-mail or manual faxing of specialist consultation summaries",
            "Under-staffed Saturday morning phone triage"
        ]
    },
    {
        "id": "GP-TAS-001",
        "practice_name": "Hobart Waterfront Medical Centre",
        "principal_gp": "Dr. Edward Gallagher, MBBS, FACRRM",
        "associated_doctors": ["Dr. Fiona Martin", "Dr. Luke Bennett"],
        "street_address": "25 Hunter Street",
        "suburb": "Hobart",
        "state": "TAS",
        "postcode": "7000",
        "phone": "+61 3 6234 1122",
        "email": "appointments@hobartwaterfrontmed.com.au",
        "website": "https://www.hobartwaterfrontmed.com.au",
        "booking_system": "Custom Web Portal",
        "pms_software": "Best Practice",
        "telehealth_available": True,
        "billing_type": "Mixed Billing",
        "after_hours": True,
        "automation_score": 74,
        "growth_opportunity": "Statewide rural telehealth outreach. Automation funnel allowing regional Tasmanian patients to access Hobart specialists remotely.",
        "key_bottlenecks": [
            "Manual scheduling of multidisciplinary case conferences",
            "Inconsistent SMS reminder timing causing 11% late arrivals"
        ]
    },
    {
        "id": "GP-ACT-001",
        "practice_name": "Canberra Parliamentary Health Practice",
        "principal_gp": "Dr. Victoria Sterling, MBBS, FRACGP",
        "associated_doctors": ["Dr. Nicholas Shaw", "Dr. Maria Santos", "Dr. David Kim"],
        "street_address": "15 National Circuit",
        "suburb": "Barton",
        "state": "ACT",
        "postcode": "2600",
        "phone": "+61 2 6273 9988",
        "email": "executive@canberrahealthpractice.com.au",
        "website": "https://www.canberrahealthpractice.com.au",
        "booking_system": "HotDoc",
        "pms_software": "MedicalDirector",
        "telehealth_available": True,
        "billing_type": "Private Billing",
        "after_hours": False,
        "automation_score": 85,
        "growth_opportunity": "Corporate executive and government department medical checkups. Automated B2B RFP and executive health screening pipelines.",
        "key_bottlenecks": [
            "High compliance overhead for government reporting",
            "Demand surge during Parliamentary sitting weeks with fixed staff capacity"
        ]
    }
]


def get_all_clinics():
    """Returns all pre-seeded Australian GP clinics."""
    return AUSTRALIAN_GP_DATA


def filter_clinics(state=None, telehealth=None, booking_system=None, billing_type=None, search=None):
    """Filter clinics based on criteria."""
    results = AUSTRALIAN_GP_DATA
    if state and state.upper() != "ALL":
        results = [c for c in results if c["state"].upper() == state.upper()]
    if telehealth is not None and telehealth != "ALL":
        val = (telehealth.lower() == "true")
        results = [c for c in results if c["telehealth_available"] == val]
    if booking_system and booking_system != "ALL":
        results = [c for c in results if c["booking_system"].lower() == booking_system.lower()]
    if billing_type and billing_type != "ALL":
        results = [c for c in results if c["billing_type"].lower() == billing_type.lower()]
    if search:
        s = search.lower()
        results = [
            c for c in results
            if s in c["practice_name"].lower()
            or s in c["suburb"].lower()
            or s in c["principal_gp"].lower()
            or s in c["postcode"]
        ]
    return results
