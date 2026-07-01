# CRM System — ThaiBridge Client Database

*Every client tracked end-to-end. Designed for AI employee management. One record = one company.*

---

## 1. CRM Database Schema

### Client Record

| # | Field | Type | Required | Description |
|---|-------|------|:--------:|-------------|
| 1 | **Company Name** | Text | ✅ | Legal or operating name |
| 2 | **Contact Person** | Text | ✅ | Primary decision-maker |
| 3 | **Title** | Text | — | CEO, Founder, Marketing Director, etc. |
| 4 | **Country** | Text | ✅ | China / Thailand / Other |
| 5 | **Industry** | Select | ✅ | Beauty, Electronics, F&B, Fashion, Manufacturing, Other |
| 6 | **Website** | URL | — | Company website or e-commerce store |
| 7 | **Source** | Select | ✅ | Google, LinkedIn, WeChat, Referral, Conference, Other |
| 8 | **Interested Service** | Multi-Select | ✅ | Warehouse, Creator, Matching, Research, Execution |
| 9 | **Current Stage** | Select | ✅ | See Stage Definitions below |
| 10 | **Quotation Status** | Select | — | Not Sent, Sent, Under Review, Accepted, Declined |
| 11 | **Quotation Value** | Number | — | Estimated or actual project value (USD) |
| 12 | **Project Status** | Select | — | Not Started, In Progress, On Track, At Risk, Complete |
| 13 | **Priority** | Select | ✅ | P0 (Hot), P1 (Warm), P2 (Cool), P3 (Cold) |
| 14 | **Budget Range** | Select | — | <$3K, $3K-$10K, $10K-$30K, $30K+ |
| 15 | **Next Action** | Text | ✅ | What needs to happen next |
| 16 | **Follow-up Date** | Date | ✅ | When to follow up |
| 17 | **Owner** | Text | ✅ | Who is responsible (CEO, Account Manager, AI) |
| 18 | **Notes** | Text | — | Free text — any relevant context |
| 19 | **Meeting Records** | Text (log) | — | Date + summary of each meeting |
| 20 | **Proposal File** | File Link | — | Link to proposal document |
| 21 | **Contract Status** | Select | — | Not Started, Draft, Sent, Signed, Archived |
| 22 | **Contract File** | File Link | — | Link to signed contract |
| 23 | **Project Start** | Date | — | Actual start date |
| 24 | **Project End** | Date | — | Actual completion date |
| 25 | **Case Study** | Boolean | — | Has client agreed to be a case study? |
| 26 | **Case Study File** | File Link | — | Link to case study document |
| 27 | **Referral Source** | Text | — | Who referred this client (if applicable) |
| 28 | **Referral Given** | Boolean | — | Has this client referred others? |
| 29 | **NPS Score** | Number | — | Net Promoter Score (0–10) |
| 30 | **Lifetime Value** | Number | — | Total revenue from this client to date |
| 31 | **Created Date** | Date | ✅ | When record was created |
| 32 | **Last Updated** | Date | ✅ | When record was last modified |

### Schema as JSON (for AI / programmatic use)

```json
{
  "clientId": "string",
  "companyName": "string",
  "contactPerson": "string",
  "title": "string",
  "country": "CN | TH | OTHER",
  "industry": "BEAUTY | ELECTRONICS | FNB | FASHION | MANUFACTURING | OTHER",
  "website": "string",
  "source": "GOOGLE | LINKEDIN | WECHAT | REFERRAL | CONFERENCE | OTHER",
  "interestedServices": ["WAREHOUSE", "CREATOR", "MATCHING", "RESEARCH", "EXECUTION"],
  "currentStage": "LEAD | QUALIFIED | MEETING | PROPOSAL | NEGOTIATION | WON | EXECUTING | COMPLETED | REFERRAL | LOST",
  "quotationStatus": "NOT_SENT | SENT | UNDER_REVIEW | ACCEPTED | DECLINED",
  "quotationValue": "number",
  "projectStatus": "NOT_STARTED | IN_PROGRESS | ON_TRACK | AT_RISK | COMPLETE",
  "priority": "P0 | P1 | P2 | P3",
  "budgetRange": "LOW | MID | HIGH | ENTERPRISE",
  "nextAction": "string",
  "followUpDate": "date",
  "owner": "string",
  "notes": "string",
  "meetingRecords": [{"date": "date", "summary": "string"}],
  "proposalFile": "url",
  "contractStatus": "NOT_STARTED | DRAFT | SENT | SIGNED | ARCHIVED",
  "contractFile": "url",
  "projectStart": "date",
  "projectEnd": "date",
  "caseStudy": "boolean",
  "caseStudyFile": "url",
  "referralSource": "string",
  "referralGiven": "boolean",
  "npsScore": "number",
  "lifetimeValue": "number",
  "createdDate": "date",
  "lastUpdated": "date"
}
```

---

## 2. Client Stage Definitions

### Stage: LEAD

| Attribute | Value |
|-----------|-------|
| **Goal** | Identify potential clients who match our ideal client profile |
| **Owner** | AI Sales Manager |
| **Entry Condition** | Company identified through search, referral, content, or outbound |
| **Exit Condition** | First contact made (→ QUALIFIED) or confirmed not a fit (→ LOST) |
| **Typical Duration** | 0–3 days |
| **AI Tasks** | Research company, verify fit, draft outreach message |
| **Human Tasks** | Approve outreach, personalize message if needed |

### Stage: QUALIFIED

| Attribute | Value |
|-----------|-------|
| **Goal** | Confirm the lead matches ideal client profile and is worth pursuing |
| **Owner** | AI Sales Manager → CEO |
| **Entry Condition** | First contact made, initial response received |
| **Exit Condition** | Meeting scheduled (→ MEETING) or no response after 3 follow-ups (→ LOST) |
| **Typical Duration** | 1–7 days |
| **AI Tasks** | Qualify against ICP checklist, schedule meeting, send prep brief |
| **Human Tasks** | Review qualification, approve meeting |

### Stage: MEETING

| Attribute | Value |
|-----------|-------|
| **Goal** | Understand client's needs, assess mutual fit, agree on next steps |
| **Owner** | CEO / Account Manager |
| **Entry Condition** | First meeting completed |
| **Exit Condition** | Clear scope defined (→ PROPOSAL) or not a fit (→ LOST) |
| **Typical Duration** | 1–3 days post-meeting |
| **AI Tasks** | Meeting prep (research), meeting notes, draft needs analysis |
| **Human Tasks** | Conduct meeting, make fit decision, approve needs analysis |

### Stage: PROPOSAL

| Attribute | Value |
|-----------|-------|
| **Goal** | Deliver a tailored proposal and quotation that the client wants to sign |
| **Owner** | CEO / AI Sales Manager |
| **Entry Condition** | Needs analysis complete, scope and pricing defined |
| **Exit Condition** | Proposal accepted (→ NEGOTIATION or → WON) or declined (→ LOST) |
| **Typical Duration** | 1–7 days |
| **AI Tasks** | Generate proposal draft, format quotation, track status |
| **Human Tasks** | Customize proposal, send to client, follow up |

### Stage: NEGOTIATION

| Attribute | Value |
|-----------|-------|
| **Goal** | Reach mutual agreement on scope, timeline, pricing, and terms |
| **Owner** | CEO |
| **Entry Condition** | Client wants to proceed but needs adjustments |
| **Exit Condition** | Terms agreed (→ WON) or cannot agree (→ LOST) |
| **Typical Duration** | 1–14 days |
| **AI Tasks** | Document scope changes, update quotation, flag risky concessions |
| **Human Tasks** | Negotiate, make judgment calls on pricing and scope |

### Stage: WON

| Attribute | Value |
|-----------|-------|
| **Goal** | Formalize the relationship — signed contract, paid invoice, project queued |
| **Owner** | CEO / AI Operations Manager |
| **Entry Condition** | Agreement reached on all terms |
| **Exit Condition** | Contract signed + payment received (→ EXECUTING) |
| **Typical Duration** | 1–5 days |
| **AI Tasks** | Generate contract, send invoice, schedule kickoff |
| **Human Tasks** | Review and sign contract |

### Stage: EXECUTING

| Attribute | Value |
|-----------|-------|
| **Goal** | Deliver all project work on time, on budget, to quality standards |
| **Owner** | Account Manager + Service Leads |
| **Entry Condition** | Contract signed, project kicked off |
| **Exit Condition** | All deliverables completed and signed off (→ COMPLETED) |
| **Typical Duration** | 4 weeks – 12 months |
| **AI Tasks** | Weekly reports, issue detection, progress tracking |
| **Human Tasks** | Service delivery, client communication, issue resolution |

### Stage: COMPLETED

| Attribute | Value |
|-----------|-------|
| **Goal** | Close the project professionally and transition to retainer or end |
| **Owner** | Account Manager |
| **Entry Condition** | All deliverables completed and client has signed off |
| **Exit Condition** | Client transitions to retainer (→ REFERRAL eligible) or engagement ends |
| **Typical Duration** | 1–2 weeks |
| **AI Tasks** | Generate final report, send NPS survey, archive project docs |
| **Human Tasks** | Final client meeting, transition handover, ask for referral |

### Stage: REFERRAL

| Attribute | Value |
|-----------|-------|
| **Goal** | Turn satisfied clients into our primary growth engine |
| **Owner** | CEO + AI Sales Manager |
| **Entry Condition** | Client is happy (NPS ≥ 8) and project is complete or ongoing |
| **Exit Condition** | Referral received → new LEAD created in pipeline |
| **Typical Duration** | Ongoing |
| **AI Tasks** | Track referral status, send referral templates, log referrals |
| **Human Tasks** | Ask for referral, thank referrer, nurture relationship |

### Stage: LOST

| Attribute | Value |
|-----------|-------|
| **Goal** | Learn from the loss and stay connected for future opportunities |
| **Owner** | AI Sales Manager |
| **Entry Condition** | Client declines or deal falls through at any stage |
| **Exit Condition** | Re-engagement in 3–6 months OR permanently archived |
| **Typical Duration** | Indefinite (archived) |
| **AI Tasks** | Log loss reason, schedule re-engagement check-in, analyze patterns |
| **Human Tasks** | Exit gracefully, leave door open |

---

## 3. Stage Transition Rules

```
LEAD ──(contacted)──→ QUALIFIED ──(meeting done)──→ MEETING ──(scoped)──→ PROPOSAL
  │                       │                            │                      │
  └──(not a fit)──→ LOST  └──(no response)──→ LOST    └──(not a fit)──→ LOST  └──(declined)──→ LOST

PROPOSAL ──(accepted, no changes)──→ WON
    │
    └──(accepted, with changes)──→ NEGOTIATION ──(agreed)──→ WON
                                        │
                                        └──(cannot agree)──→ LOST

WON ──(contract signed)──→ EXECUTING ──(delivered)──→ COMPLETED ──(happy)──→ REFERRAL
                                │                          │
                                └──(terminated)──→ LOST    └──(ended)──→ Archive

REFERRAL ──(referral received)──→ LEAD (new)
```

### Quick-Reference Rules

| From | To | Trigger |
|------|----|---------|
| LEAD → QUALIFIED | First contact made and response received |
| LEAD → LOST | Not a fit or unresponsive after research |
| QUALIFIED → MEETING | Meeting scheduled and completed |
| QUALIFIED → LOST | No response after 3 follow-ups or not a fit |
| MEETING → PROPOSAL | Needs analyzed, scope clear, client wants proposal |
| MEETING → LOST | Not a fit after meeting |
| PROPOSAL → NEGOTIATION | Client wants to proceed but needs changes |
| PROPOSAL → WON | Client accepts without changes |
| PROPOSAL → LOST | Client declines proposal |
| NEGOTIATION → WON | Agreement reached |
| NEGOTIATION → LOST | Cannot agree |
| WON → EXECUTING | Contract signed, payment received |
| EXECUTING → COMPLETED | All deliverables done, client sign-off |
| EXECUTING → LOST | Early termination |
| COMPLETED → REFERRAL | Client NPS ≥ 8, willing to refer |
| REFERRAL → LEAD | Referral received → new pipeline entry |

---

## 4. Priority System

| Priority | Code | Definition | Response Time | Action |
|:--------:|:----:|------------|:------------:|--------|
| **Hot** | P0 | Active deal in negotiation or closing. Active project at risk. | ≤ 2 hours | Immediate attention |
| **Warm** | P1 | Active deal in proposal or meeting stage. Active project on track. | ≤ 24 hours | This week |
| **Cool** | P2 | Qualified lead not yet in meeting. Completed project — referral ask pending. | ≤ 72 hours | This month |
| **Cold** | P3 | Lead not yet contacted. Lost deal — re-engagement scheduled. | ≤ 1 week | When capacity allows |

---

## 5. AI Employee CRM Integration

### AI Sales Manager

- **Reads:** All LEAD through NEGOTIATION stage records
- **Writes:** Meeting notes, follow-up tasks, proposal drafts, stage transitions
- **Alerts:** Stalled deals (>7 days no movement), overdue follow-ups, hot leads needing CEO attention

### AI Operations Manager

- **Reads:** All WON through COMPLETED stage records
- **Writes:** Weekly progress reports, project status updates, issue logs
- **Alerts:** Projects at risk, overdue deliverables, client communication gaps

### CEO Assistant

- **Reads:** Entire CRM
- **Writes:** Weekly pipeline summary, priority queue, CEO briefing notes
- **Alerts:** Revenue-at-risk, client concentration warnings, stage bottlenecks

---

## 6. Weekly CRM Review

*Every Monday 9:00 AM ICT — AI generates, CEO reviews*

| Check | Question |
|-------|----------|
| Pipeline Health | How many deals at each stage? Total pipeline value? |
| Movement | Which deals advanced this week? Which stalled? |
| New Leads | How many new leads entered? Source breakdown? |
| At Risk | Any deals stuck >14 days at same stage? |
| Follow-ups | Any overdue follow-ups? |
| Wins | Any deals won this week? Onboarding started? |
| Losses | Any deals lost? Reason documented? |
| Referrals | Any referral asks made? Any received? |

---

## 7. CRM Tool Recommendation

### Phase 1: Manual (Current)
- Markdown file: `03_Client_Pipeline.md` in CEO Operating System
- Update manually each week
- Works for 0–20 clients

### Phase 2: Spreadsheet (Month 1–3)
- Google Sheets with columns matching this schema
- Shared with team
- AI can read/write via Google Sheets API

### Phase 3: CRM Software (Month 3–6)
- TODO: Evaluate HubSpot (free tier), Pipedrive, or Notion database
- Must support: custom fields, pipeline view, email integration, API access
- AI integration capability is the primary selection criterion

---

*CRM-System.md · ThaiBridge Business Operating System V1.0*
*Sprint 01 · P2 Complete*
