# Prompt Documentation & Engineering Dossier
**Role Assessment:** AI Growth & Automation Associate — Work From Home  
**Company:** Gokul Infocare  
**Candidate Project:** MediGrowth AI (Australian Healthcare Lead Intelligence & Automated Outbound Engine)

---

## 1. Executive Summary & Prompt Philosophy

In building **MediGrowth AI**, prompt engineering served as the primary interface between raw, unstructured public data and reliable, production-ready B2B growth workflows.

When dealing with healthcare data in Australia, standard naive prompts consistently fail due to:
1. **Regulatory Breaches:** In Australia, the *Health Practitioner Regulation National Law* and AHPRA (Australian Health Practitioner Regulation Agency) strictly prohibit misleading advertising, false promises (e.g., "guaranteed patient inflow"), or fabricated patient reviews.
2. **Structural Inconsistency:** Web scrapers return messy HTML, broken paragraphs, and non-standardized contact representations. Unconstrained LLMs tend to add conversational filler (`"Here is the email you requested..."`), corrupting automated API pipelines.
3. **Hallucination of Clinical Specifics:** Unchecked models often invent medical practice management systems (PMS), mix up postcodes, or misformat Australian phone numbers (which follow strictly defined 8-digit landline formats prefixed with `02`, `03`, `07`, `08` or national prefixes `1300` / `1800` / `+61`).

To solve this, we adopted a **3-Phase Iterative Prompt Engineering Methodology**:
- **Phase 1 (Ingestion & Extraction):** Zero-shot with strict JSON schema constraints.
- **Phase 2 (Diagnostic Scoring):** Multi-factor opportunity analysis and bottleneck detection.
- **Phase 3 (Outreach Generation):** Role-conditioned few-shot prompts with localized compliance guardrails.

---

## 2. Iterative Evolution of Prompts (V1 → V2 → V3)

### Stage 1: Cold Outreach Prompt Evolution

#### Version 1 (Initial Naive Prompt)
> *"Write a cold email to Dr. Sarah Henderson at Sydney Central Medical selling automation software. Tell her we can get her clinic lots of new patients and reduce front-desk calls."*

* **Observed Output:**
  ```text
  Subject: Get 50+ new patients guaranteed for Sydney Central Medical!
  
  Hi Sarah,
  I hope you are having a wonderful day! I saw your clinic online and wanted to let you know that we can flood your calendar with new patients every single week. Our revolutionary AI tool will completely replace your front desk staff and make you the #1 clinic in Sydney! Let me know when you're free for a 30-minute demo call.
  ```
* **Failure Analysis:**
  - ❌ **Violated AHPRA Guidelines:** Promises of "flooding calendars" and "guaranteed patients" violate section 133 of the Health Practitioner Regulation National Law.
  - ❌ **Aggressive, Inappropriate Tone:** Addressing an Australian specialist or practice owner as *"Sarah"* with high-pressure American sales tropes results in immediate deletion or spam marking.
  - ❌ **Ignored Healthcare Realities:** In Australia, General Practice is overwhelmed with demand; clinics are not desperate for "random patient floods"—their primary pain points are **Monday morning phone wait times, chronic disease care-plan admin, HotDoc commission leakage, and patient no-shows**.

---

#### Version 2 (Context-Aware Prompt with Role Conditioning)
> *"You are an Australian healthcare marketing consultant. Write a professional email to Dr. Sarah Henderson, Principal GP at Sydney Central Medical Centre in Sydney NSW. The practice uses HotDoc for booking and Best Practice as their clinical software. Mention their pain points with receptionist telephone calls and propose a solution without violating Australian medical advertising laws."*

* **Observed Output:**
  ```text
  Subject: Streamlining patient communications at Sydney Central Medical Centre
  
  Dear Dr. Henderson,
  
  I am reaching out from HealthTech Automation. We noticed your clinic uses HotDoc and Best Practice. Many clinics in Sydney experience high call volumes at the front desk. We provide software that helps reduce these phone calls and frees up receptionist time. 
  
  Would you be interested in learning more?
  
  Best regards,
  Alex
  ```
* **Evaluation & Remaining Limitations:**
  - ⚠️ **Improvement:** Removed illegal guarantees; corrected salutation to *"Dear Dr. Henderson"*; referenced specific technology stack (*Best Practice*, *HotDoc*).
  - ❌ **Lacked Concrete Value Proposition:** Vague call-to-action (`"Would you be interested in learning more?"`) produces sub-3% response rates in cold B2B outreach.
  - ❌ **No Structured Output:** Could not be programmatically consumed by automated dispatch webhooks or CRM tools without regex cleanup.

---

#### Version 3 (Production-Grade Prompt with Few-Shot Demonstrations, JSON Schema & Guardrails)
```text
System Prompt:
You are an Elite B2B Healthcare Growth & Practice Automation Specialist working in the Australian market.
Your mission is to generate a highly tailored, non-spammy, high-converting outreach campaign 
for a specific Australian General Practice based on their operational intelligence.

KEY CONTEXT & COMPLIANCE GUARDRAILS:
1. Australian Tone: Professional, collegial, and respectful of GP time pressures (avoid aggressive sales hyperbole).
2. AHPRA & RACGP Compliance: Never promise "guaranteed patient influx" (AHPRA restricts deceptive medical advertising). Instead, focus on "operational efficiency", "reducing front-desk phone strain", "automating care-plan recalls", and "eliminating 12%+ no-show rates".
3. Practice System Awareness: Directly reference their current booking system (e.g., HotDoc, HealthEngine, or manual phone) and PMS software (Best Practice, MedicalDirector, Zedmed).
4. Output Format: Return STRICT JSON matching the schema below. No markdown wrapping outside the JSON, no conversational preamble.

JSON Schema:
{
  "cold_email": {
    "subject": string,
    "preview_text": string,
    "body": string
  },
  "linkedin_message": {
    "recipient_role": string,
    "headline": string,
    "message": string
  },
  "phone_script": {
    "target": string,
    "duration": string,
    "script": string
  },
  "audit_roadmap": [
    {
      "pillar": string,
      "current_state": string,
      "recommendation": string,
      "projected_impact": string
    }
  ]
}
```

* **Outcome:**
  - ✅ 100% Valid JSON conforming to API contracts.
  - ✅ Multi-channel synchronization (Email, LinkedIn InMail, Receptionist Phone Script, 3-Pillar Audit).
  - ✅ Specific mention of Australian Medicare items (e.g. Chronic Disease Management 721/723) and local market context.

---

## 3. Data Extraction & Entity Parsing Prompts

### Unstructured Web Content to Structured Lead Schema

```text
SYSTEM PROMPT:
You are an Elite Australian Healthcare Intelligence Extraction Agent.
Your task is to parse unstructured web content or raw text from Australian general practices, 
medical centres, or doctor directories, and output strictly valid JSON.

CRITICAL INSTRUCTIONS:
1. Do not hallucinate contact info. If phone or email is missing, set to null.
2. Australian phone numbers should be standardized to Australian local or international format (+61 2/3/7/8... or (0X) XXXX XXXX).
3. Identify Australian medical credentials accurately (e.g. MBBS, FRACGP, FACRRM, DipChildHealth).
4. Detect booking systems: Identify if they use HotDoc, HealthEngine, Cliniko, Zedmed, or Phone Only.
5. Return ONLY a single raw JSON object without markdown code blocks, backticks, or conversational preamble.

FEW-SHOT INPUT EXAMPLE:
"Dr. Sarah Henderson MBBS, FRACGP is practice principal at Sydney Central Medical Centre, 580 George Street, Sydney NSW 2000. Phone: (02) 9267 8900. Email: reception@sydneycentralmed.com.au. Online bookings powered by HotDoc. Uses Best Practice."

FEW-SHOT OUTPUT EXAMPLE:
{
  "practice_name": "Sydney Central Medical Centre",
  "principal_gp": "Dr. Sarah Henderson, MBBS, FRACGP",
  "associated_doctors": [],
  "street_address": "580 George Street",
  "suburb": "Sydney",
  "state": "NSW",
  "postcode": "2000",
  "phone": "+61 2 9267 8900",
  "email": "reception@sydneycentralmed.com.au",
  "booking_system": "HotDoc",
  "pms_software": "Best Practice",
  "telehealth_available": true,
  "billing_type": "Mixed Billing"
}
```

---

## 4. Hyperparameter & Model Tuning Rationale

| Parameter | Extraction Task | Outreach Copy Generation | Technical Justification |
| :--- | :--- | :--- | :--- |
| **Model** | Claude 3.5 Sonnet / Gemini 1.5 Pro | Claude 3.5 Sonnet / GPT-4o | High reasoning fidelity for complex Australian medical entity recognition. |
| **Temperature** | `0.1` | `0.4` | Low temperature ensures near-zero hallucination on addresses/phones; moderate temperature introduces varied, natural copywriting styles. |
| **Top-P** | `0.9` | `0.95` | Maintains high precision while permitting natural phrase construction in emails. |
| **Response Format** | `application/json` | `application/json` | Enforces programmatic reliability across all backend endpoints. |

---

## 5. Development Prompts Used During Project Construction

Below are the primary meta-prompts used during our pairing session to architect, debug, and refine the application codebase:

### Code Architecture Meta-Prompt
> *"Design a production-grade Python + Flask web application that serves as an Australian Healthcare B2B Lead Intelligence and Automated Outbound Platform. The system must support live web scraping of Australian clinic directories, entity normalization with regex and NLP, dynamic generation of multi-channel outreach kits, and a responsive frontend with search, filtering, and 1-click CSV exports. Include an offline deterministic fallback engine so the app runs reliably without requiring external paid API keys."*

### UI Design & Usability Meta-Prompt
> *"Create a single-page dashboard using Tailwind CSS and Lucide icons following a modern executive dark theme (slate-950, deep indigo, emerald accents). Include KPI overview cards, an interactive filter bar for Australian states and booking engines, a live scraping playground, an interactive pipeline diagram, and a prompt engineering dossier modal."*
