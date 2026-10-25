"""
Unit & Integration Test Suite for MediGrowth AI
Validates all endpoints, scraper logic, and AI campaign generator.
"""

import unittest
from app import app, clinics_db

class TestMediGrowth(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_stats_endpoint(self):
        res = self.client.get("/api/stats")
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertIn("total_clinics", data)
        self.assertIn("total_doctors", data)
        self.assertIn("telehealth_rate", data)
        self.assertGreater(data["total_clinics"], 10)

    def test_clinics_endpoint(self):
        res = self.client.get("/api/clinics")
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertIsInstance(data, list)
        self.assertGreater(len(data), 0)

    def test_clinics_filter_state(self):
        res = self.client.get("/api/clinics?state=NSW")
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        for c in data:
            self.assertEqual(c["state"], "NSW")

    def test_generate_campaign(self):
        res = self.client.post("/api/generate-campaign", json={"clinic_id": "GP-NSW-001"})
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertIn("cold_email", data)
        self.assertIn("linkedin_message", data)
        self.assertIn("phone_script", data)
        self.assertIn("audit_roadmap", data)
        self.assertIn("Sydney Central Medical Centre", data["practice_name"])

    def test_scrape_extract(self):
        sample_text = (
            "Carlton Family Medical Centre. Principal: Dr. Andrew Miller, MBBS, FRACGP. "
            "Call (03) 9347 1100 or email reception@carltonfamily.com.au. Located in Melbourne VIC 3053. "
            "Book online via HotDoc."
        )
        res = self.client.post("/api/scrape-extract", json={"raw_text": sample_text})
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertTrue(data["success"])
        clinic = data["extracted_clinic"]
        self.assertEqual(clinic["state"], "VIC")
        self.assertIn("03", clinic["phone"])

    def test_export_csv(self):
        res = self.client.get("/api/export-csv")
        self.assertEqual(res.status_code, 200)
        self.assertIn("text/csv", res.content_type)
        self.assertIn(b"Practice Name", res.data)

if __name__ == "__main__":
    unittest.main()
