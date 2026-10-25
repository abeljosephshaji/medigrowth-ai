# Video Presentation Script & Recording Guide
**Target Duration:** ~3 Minutes (exceeds the 2-minute mandatory minimum)  
**Role:** AI Growth & Automation Associate — Work From Home  
**Company:** Gokul Infocare  
**Project:** MediGrowth AI — Australian Healthcare Intelligence & Automated Growth Engine  

---

## Quick Recording Checklist Before You Hit Record
1. **Tool:** Use [Loom](https://www.loom.com/) (free) or [OBS Studio](https://obsproject.com/) with your webcam bubble visible in the corner.
2. **Setup:**
   - Open a terminal and run `python run.py`.
   - Your browser will open `http://127.0.0.1:5000`.
   - Maximize the browser window for crisp text visibility.
3. **Pacing:** Speak at a steady, confident, professional pace.

---

## Timed Video Script (Word-for-Word)

### 0:00 – 0:35 | Introduction, Domain Selection & Purpose
* **[CAMERA: Full face or Webcam in corner, Browser showing MediGrowth AI Dashboard header and KPI cards]**
* **Spoken Script:**
  > *"Hello Gokul Infocare assessment team, my name is [Your Name], and today I am excited to present my project for the AI Growth & Automation Associate role: **MediGrowth AI**.*
  >
  > *For this assessment, I chose the **Healthcare and Technology** domain, focusing on the real-world challenge specified in the prompt: collecting and organizing publicly available information for General Practitioners in Australia, and building an automated growth engine on top of that intelligence.*
  >
  > *In the Australian healthcare sector, medical practices struggle with two core problems: high receptionist phone bottlenecks and rising commission fees on third-party booking marketplaces like HotDoc and HealthEngine. MediGrowth AI bridges this gap by automatically discovering clinics, diagnosing operational bottlenecks, and generating hyper-tailored, AHPRA-compliant B2B outbound campaigns."*

---

### 0:35 – 1:15 | AI Tools Selected & Technical Justification
* **[SCREEN: Scroll across the KPI cards and click on the 'Prompt Engineering Dossier' tab]**
* **Spoken Script:**
  > *"To build this end-to-end solution, I combined several specialized AI tools:*
  >
  > 1. *First, **Large Language Models (Claude 3.5 Sonnet and Gemini 1.5 Pro)** were selected for their superior reasoning in structured entity extraction and nuanced, localized B2B copywriting.*
  > 2. *Second, **Cursor & AI Pair Programming** accelerated rapid full-stack scaffolding using Python, Flask, and Tailwind CSS.*
  > 3. *Third, **BeautifulSoup & Regex Heuristics** provided a robust scraping layer tailored to Australian phone patterns, ABNs, and postcodes.*
  >
  > *I specifically avoided generic off-the-shelf marketing tools because healthcare outbound in Australia requires strict adherence to AHPRA regulations against misleading claims, which generic scrapers completely ignore."*

---

### 1:15 – 2:00 | Prompt Engineering Design & Iterative Refinement
* **[SCREEN: Highlight the 3-phase prompt evolution box (V1 vs V2 vs V3) on the screen]**
* **Spoken Script:**
  > *"Prompt engineering was the core driver of project quality. As documented in my prompt dossier, I tested three distinct iterations:*
  >
  > *In **Version 1**, naive prompting produced aggressive, American-style sales copy promising '50+ guaranteed patients'. In Australia, this is strictly unlawful under AHPRA medical advertising regulations.*
  >
  > *In **Version 2**, I introduced role prompting and clinic context. While the tone improved, the LLM still output conversational filler that broke automated CRM webhooks.*
  >
  > *In **Version 3**, I engineered a **production few-shot prompt with strict JSON Schema constraints** and temperature tuned to 0.4. This enforced the extraction of specific Practice Management Systems—like Best Practice and MedicalDirector—and produced a synchronized 4-part outreach package: a cold email, a LinkedIn InMail message, a 60-second gatekeeper phone script, and an actionable 3-pillar practice automation audit."*

---

### 2:00 – 2:35 | Challenges Overcome & Problem Solving
* **[SCREEN: Click on the 'Live AI Scraper Sandbox' tab, show the input field and sample snippet]**
* **Spoken Script:**
  > *"During development, I encountered two major technical challenges:*
  >
  > *The first challenge was **anti-scraping and unstructured HTML**. Real-world clinic websites vary wildly in DOM structure. I solved this by combining multi-selector OpenGraph parsing with heuristic fallbacks that normalize Australian mobile and landline numbers (such as 02, 03, and 1300).*
  >
  > *The second challenge was **zero-dependency reliability**. If an evaluator doesn't have an active OpenAI or Gemini API key configured, an API crash would ruin the demo. To solve this, I built a hybrid engine: it seamlessly uses live LLM APIs when keys exist, but features an intelligent deterministic NLP fallback that guarantees 100% uptime for local testing."*

---

### 2:35 – 3:15 | Live Demonstration & Business Outcome
* **[SCREEN: Switch to 'Lead Intelligence Directory' tab, filter by 'NSW', click 'Generate AI Growth Outreach' on Sydney Central Medical Centre]**
* **Spoken Script:**
  > *"Let's see MediGrowth AI in action.*
  >
  > *Here in our Lead Intelligence Directory, we have indexed verified Australian GP clinics across Sydney, Melbourne, Brisbane, and beyond. We can instantly filter by State, Telehealth status, or Booking engine.*
  >
  > *Watch what happens when I click **'Generate AI Growth Outreach'** on Sydney Central Medical Centre.*
  >
  > *[Show Modal opening with populated tabs]*
  > *In under half a second, the engine analyzes Dr. Sarah Henderson's tech stack—detecting her HotDoc booking engine and Best Practice PMS. It instantly generates:*
  > - *A personalized cold email addressing front-desk phone wait times,*
  > - *A tailored LinkedIn message for the Practice Principal,*
  > - *A 60-second receptionist phone script,*
  > - *And a 3-pillar audit demonstrating how to recapture up to $1,200 monthly in marketplace commissions.*
  >
  > *Everything is copy-ready or exportable via CSV and JSON into HubSpot or Salesforce.*
  >
  > *This demonstrates not just what AI can do in theory, but how practical AI automation can drive measurable B2B growth in a regulated industry. Thank you for your time, and I look forward to speaking with the Gokul Infocare team!"*

---

## Pronunciation Guide for Technical & Australian Terms
- **AHPRA:** Pronounced *"AH-prah"* (Australian Health Practitioner Regulation Agency)
- **RACGP:** Pronounced *"R-A-C-G-P"* (Royal Australian College of General Practitioners)
- **FRACGP:** Pronounced *"Fellow-ship of R-A-C-G-P"* or *"F-R-A-C-G-P"*
- **HotDoc:** Pronounced *"Hot-Doc"* (dominant Australian GP booking platform)
- **Best Practice / BP Premier:** The leading Australian clinical Practice Management Software
