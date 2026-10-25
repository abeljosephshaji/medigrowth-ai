# Assessment Submission Guide & Email Template
**Position:** AI Growth & Automation Associate — Work From Home  
**Company:** Gokul Infocare  
**Recipient Email:** `jobs@gokulinfocare.com`  
**Evaluation Model:** First-come, first-served basis (Submit as soon as possible!)

---

## 📋 The 3 Required Deliverables Checklist

- [ ] **1. Video Presentation (Minimum 2 Minutes):**
  - Record your screen using [Loom](https://www.loom.com/) (recommended) or OBS Studio.
  - Follow the word-for-word script provided in [`VIDEO_PRESENTATION_SCRIPT.md`](file:///c:/Users/USER/Downloads/AiProject/VIDEO_PRESENTATION_SCRIPT.md).
  - Ensure your recording link is set to *"Anyone with the link can view"*.

- [ ] **2. Prompt Documentation:**
  - Complete, structured prompt dossier is prepared in [`PROMPT_DOCUMENTATION.md`](file:///c:/Users/USER/Downloads/AiProject/PROMPT_DOCUMENTATION.md).
  - Can be attached as a file or linked via GitHub/Google Drive.

- [ ] **3. Project Link & Code Access:**
  - Share your GitHub repository or a shared Google Drive folder containing the `AiProject` files.
  - Double check permissions: *"Anyone on the internet with the link can view/download"*.

---

## 🚀 How to Push to GitHub in 60 Seconds

Run the following commands in PowerShell from `c:\Users\USER\Downloads\AiProject`:

```powershell
# 1. Initialize git (if not already initialized)
git init

# 2. Add all files
git add .

# 3. Create your initial commit
git commit -m "feat: complete MediGrowth AI assessment project for Gokul Infocare"

# 4. Create a new repository on your GitHub account (named e.g. 'medigrowth-ai' or 'gokul-ai-assessment')
# 5. Link and push:
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/medigrowth-ai.git
git push -u origin main
```

*(Alternatively, zip the `AiProject` folder, upload to Google Drive, and ensure the share link is set to "Anyone with the link can view").*

---

## ✉️ Ready-to-Send Email Template for `jobs@gokulinfocare.com`

**To:** `jobs@gokulinfocare.com`  
**Subject:** Application Submission: AI Growth & Automation Associate Assessment — [Your Full Name]  

```text
Dear Gokul Infocare Hiring Team,

Thank you for the opportunity to complete Task 1 of the assessment for the AI Growth & Automation Associate (Work From Home) position.

I have thoroughly reviewed the job description, understand that the working hours, salary, and start times are fixed and non-negotiable, and confirm my full availability.

To demonstrate my practical AI, prompt engineering, and automation capabilities, I created "MediGrowth AI" — an intelligent Australian Healthcare Lead Intelligence and Outbound Growth Engine that collects, normalizes, and extracts intelligence from Australian General Practices and automatically generates tailored B2B outreach and practice automation audits.

Below are the three required submission components:

1. Video Presentation (Walkthrough & Approach):
   Link: [INSERT YOUR LOOM / GOOGLE DRIVE VIDEO LINK HERE]
   (Duration: ~3 minutes. Covers AI tool selection, prompt engineering iterations, technical challenges, and a live demonstration of the platform.)

2. Prompt Documentation:
   Link: [INSERT GITHUB LINK TO PROMPT_DOCUMENTATION.md OR GOOGLE DRIVE LINK]
   (Detailed breakdown of our 3-phase prompt evolution from naive V1 to production V3 with few-shot examples, JSON schema constraints, and AHPRA compliance guardrails.)

3. Project Repository & Live Code:
   GitHub Repository: [INSERT YOUR GITHUB REPOSITORY LINK HERE]
   Google Drive Backup: [INSERT GOOGLE DRIVE ZIP LINK (OPTIONAL)]

Quick Highlights of the Project:
• Web Scraping & Data Intelligence: Ingests Australian GP directory data, extracting principal doctors, FRACGP qualifications, local phone formats, postcodes, booking systems (HotDoc, HealthEngine), and PMS software.
• AI Growth & Outbound Automation: Diagnoses practice bottlenecks (e.g. receptionist phone overload, marketplace commission leakage) and generates synchronized cold emails, LinkedIn InMails, and phone scripts.
• Interactive Dashboard: Full-stack responsive web application with real-time filtering, live scraping sandbox, and 1-click CSV lead export.
• Reliability: Includes automated unit test suite (100% pass) and deterministic offline fallback.

I enjoyed turning this idea into a functional, production-ready outcome and look forward to hearing your thoughts and moving to the next stage of the selection process.

Kind regards,

[Your Full Name]
[Your Phone Number]
[Your LinkedIn Profile URL]
[Your City / Location]
```
