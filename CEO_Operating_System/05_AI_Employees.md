# 05 — AI Employees

*ThaiBridge's AI workforce. Each AI employee has a defined mission, responsibilities, inputs, outputs, and knowledge base. Deployed through Claude, ChatGPT, or custom AI workflows.*

---

## AI Employee Roster

| # | Role | Status | Deployment Priority |
|---|------|:------:|:-------------------:|
| 1 | CEO Assistant | 🔴 Not Deployed | P0 — Week 1 |
| 2 | Sales Manager | 🔴 Not Deployed | P0 — Week 1 |
| 3 | Creator Manager | 🔴 Not Deployed | P1 — Week 2 |
| 4 | Warehouse Manager | 🔴 Not Deployed | P1 — Week 2 |
| 5 | Market Research Analyst | 🔴 Not Deployed | P1 — Week 2 |
| 6 | Business Matching Manager | 🔴 Not Deployed | P2 — Week 3 |
| 7 | Operations Manager | 🔴 Not Deployed | P2 — Week 3 |
| 8 | Finance Assistant | 🔴 Not Deployed | P2 — Week 4 |
| 9 | Content Manager | 🔴 Not Deployed | P2 — Week 4 |

---

## 1. CEO Assistant

**Mission:** Keep the CEO focused on the highest-leverage work by handling scheduling, prioritization, information retrieval, and decision preparation.

### Responsibilities
- Review weekly priorities and flag conflicts or overload
- Summarize CEO Dashboard from raw inputs before Monday review
- Draft weekly CEO update from project tracker, pipeline, and KPI data
- Research topics the CEO needs to understand before meetings
- Prepare decision memos: context, options, recommendation, risks
- Monitor inbox/slack for action items and add to task list
- Follow up on delegated tasks — check status, nudge owners

### Inputs
- CEO Dashboard (01_CEO_Dashboard.md)
- Weekly Priorities (02_Weekly_Priorities.md)
- Project Tracker (04_Project_Tracker.md)
- Client Pipeline (03_Client_Pipeline.md)
- CEO's calendar
- CEO's email / messages

### Outputs
- Weekly CEO Brief (Monday morning — top 5 things to know)
- Decision Memos (as needed — before each major decision)
- Follow-up Tracker (who owes what by when)
- Daily Task List (prioritized, time-boxed)

### Knowledge Required
- ThaiBridge Brand DNA
- ThaiBridge Service Bible (all 5 services)
- Current client roster and pipeline
- CEO's goals, preferences, and communication style
- Thai business context and cultural norms

### SOP References
- All 20 SOPs across 5 services (Service Bible)

### Future Automations
- Auto-generate weekly dashboard from raw data
- Auto-schedule meetings based on priority and availability
- Voice-to-text CEO notes → structured task extraction
- Predictive: flag decisions that are overdue

---

## 2. Sales Manager

**Mission:** Manage the client pipeline from lead to conversation. Ensure no opportunity falls through the cracks and every prospect receives timely, professional follow-up.

### Responsibilities
- Qualify inbound leads against ideal client profile
- Draft personalized outreach messages (LinkedIn, WeChat, Email)
- Prepare client-ready service summaries and case studies
- Schedule and prepare for first meetings (research prospect, draft agenda)
- Send follow-up after every meeting within 24 hours
- Track pipeline movement and flag stalled deals
- Prepare proposal drafts based on service bible pricing models
- Maintain CRM (Client Pipeline — 03_Client_Pipeline.md)

### Inputs
- Lead sources (inbound, referral, outbound target list)
- Client Pipeline (03_Client_Pipeline.md)
- Service Bible (pricing models, deliverables, workflows)
- Brand DNA (positioning, tone of voice, slogans)

### Outputs
- Personalized outreach messages
- Meeting preparation briefs
- Follow-up emails
- Proposal drafts
- Updated CRM pipeline
- Weekly pipeline report

### Knowledge Required
- ThaiBridge Service Bible (all services, pricing, deliverables)
- ThaiBridge Brand DNA (positioning, tone, what we are / aren't)
- Ideal client profile per service
- Competitor landscape (who else does cross-border China-Thailand?)
- Common objections and responses

### SOP References
- SOP-LE-001 (Client Onboarding)

### Future Automations
- AI-powered lead scoring (which leads are most likely to convert)
- Auto-generate proposals from service bible templates
- Predictive: best time to follow up based on engagement signals
- CRM auto-update from email and meeting transcripts

---

## 3. Creator Manager

**Mission:** Manage and grow the vetted Thai creator network. Match creators to brand campaigns with data, not guesswork.

### Responsibilities
- Maintain creator database with verified stats and performance history
- Source new creators matching network gaps (category, platform, tier)
- Conduct initial creator screening (audience audit, engagement check, brand safety)
- Match creators to client briefs based on audience overlap and past performance
- Generate creator shortlists for client campaigns
- Monitor creator campaign performance and update scoring
- Flag underperforming creators for review
- Manage creator communication in Thai (briefs, feedback, scheduling)

### Inputs
- Creator database (TODO: build)
- Client campaign briefs
- Campaign performance data
- Platform analytics (TikTok, Instagram, YouTube)

### Outputs
- Creator Portfolio (for client review)
- Creator Performance Scorecards (post-campaign)
- Network Health Report (monthly)
- New Creator Recommendations (weekly)

### Knowledge Required
- Thai social media landscape (TikTok, IG, YouTube creator ecosystem)
- Engagement rate benchmarks by platform and category
- Creator pricing norms by tier in Thailand
- ThaiBridge Creator Network SOPs (SOP-CR-001 through SOP-CR-004)

### SOP References
- SOP-CR-001 (Creator Vetting)
- SOP-CR-002 (Campaign Briefing)
- SOP-CR-003 (Content Review)
- SOP-CR-004 (Campaign Reporting)

### Future Automations
- AI creator matching (brief → ranked creator list with fit scores)
- Automated fake follower / engagement fraud detection
- Real-time creator performance dashboard
- Predictive: which creators will perform best for which brand categories

---

## 4. Warehouse Manager

**Mission:** Ensure every warehouse partner maintains SLA compliance and every client's inventory is accurately tracked.

### Responsibilities
- Maintain vetted warehouse database with capability profiles
- Match client requirements to warehouse partners
- Conduct initial warehouse screening and site visit preparation
- Monitor daily SLA compliance across all active warehouse clients
- Generate weekly inventory reconciliation reports
- Flag warehouse issues before clients notice them
- Prepare monthly warehouse performance reports
- Maintain backup warehouse shortlist per client

### Inputs
- Warehouse database (TODO: build)
- Client requirements documents
- WMS data (inventory levels, order fulfillment times)
- Client e-commerce platform data

### Outputs
- Warehouse Comparison Matrix (for client selection)
- Weekly Inventory Reconciliation Report (bilingual)
- Monthly SLA Performance Report
- Issue Alerts (real-time when SLA breached)

### Knowledge Required
- Thai logistics and warehousing market
- WMS systems common in Thailand
- E-commerce platform logistics requirements (Shopee, Lazada, TikTok Shop)
- ThaiBridge Warehouse SOPs (SOP-WH-001 through SOP-WH-004)

### SOP References
- SOP-WH-001 (Warehouse Site Visit)
- SOP-WH-002 (Client Onboarding)
- SOP-WH-003 (Weekly Inventory Reconciliation)
- SOP-WH-004 (Issue Escalation)

### Future Automations
- AI auto-reconciliation: WMS data ↔ e-commerce platform data
- AI SLA monitoring: automatic alert when orders breach time threshold
- Predictive capacity planning: when will client outgrow current warehouse
- Auto-generate bilingual inventory reports

---

## 5. Market Research Analyst

**Mission:** Deliver category-specific market intelligence grounded in primary Thai consumer data — not desktop research.

### Responsibilities
- Design research methodology for client engagements
- Conduct competitive audits (pricing, distribution, positioning)
- Analyze consumer interview data for themes and insights
- Map distribution channels for client categories
- Review regulatory requirements for product categories
- Synthesize findings into go-to-market recommendations
- Generate draft market research reports

### Inputs
- Client research briefs and scoping documents
- Field research data (store visit notes, price audits, consumer interview transcripts)
- E-commerce platform data (Shopee, Lazada)
- Social media listening data

### Outputs
- Research Plan (methodology, timeline, key questions)
- Competitive Audit Report
- Consumer Insights Report
- Market Entry Recommendation
- Executive Presentation

### Knowledge Required
- Thai consumer market categories (beauty, electronics, F&B, fashion)
- Research methodology (qualitative and quantitative)
- Thai retail landscape (modern trade, traditional trade, e-commerce)
- ThaiBridge Market Research SOPs (SOP-MR-001 through SOP-MR-004)

### SOP References
- SOP-MR-001 (Research Scoping)
- SOP-MR-002 (Competitive Audit)
- SOP-MR-003 (Consumer Interview)
- SOP-MR-004 (Report Delivery)

### Future Automations
- AI competitive monitoring (auto-track competitor pricing, new SKUs, promotions)
- AI consumer interview transcription + theme extraction (Thai language)
- AI report generation (first draft from structured field data)
- Predictive market sizing model

---

## 6. Business Matching Manager

**Mission:** Find, vet, and facilitate partnerships between Chinese clients and Thai businesses.

### Responsibilities
- Search partner network for candidates matching client requirements
- Conduct initial partner screening and qualification
- Prepare due diligence materials (reference checks, financial review)
- Facilitate bilingual introduction meetings
- Support negotiation with cultural context and term comparisons
- Monitor partnership health post-signing
- Maintain vetted partner database

### Inputs
- Ideal Partner Profile documents
- Partner database (TODO: build)
- Industry association and trade body contacts
- Partner screening call notes

### Outputs
- Partner Longlist Summary
- Partner Evaluation Report
- Contract Summary with cultural notes
- 90-Day Partnership Health Check
- Quarterly Partnership Performance Review

### Knowledge Required
- Thai business landscape across industries
- Cross-cultural negotiation norms (China ↔ Thailand)
- Thai corporate structures, common deal terms
- ThaiBridge Business Matching SOPs (SOP-BM-001 through SOP-BM-004)

### SOP References
- SOP-BM-001 (Partner Screening Call)
- SOP-BM-002 (Partner Site Visit)
- SOP-BM-003 (Bilingual Negotiation Facilitation)
- SOP-BM-004 (Partnership Health Check 90-Day)

### Future Automations
- AI partner matching (profile → ranked candidates)
- AI due diligence assistant (auto-check public records, news, social media)
- AI contract term comparison against market norms
- Predictive partnership health monitoring

---

## 7. Operations Manager

**Mission:** Keep all client operations running smoothly. Track tasks across workstreams. Catch issues before they become problems.

### Responsibilities
- Maintain project tracker for all active client engagements
- Monitor task completion across all workstreams
- Generate weekly client progress reports
- Track and escalate issues per SOP-LE-003
- Coordinate between service leads (warehouse, creator, matching, research)
- Manage client onboarding per SOP-LE-001
- Prepare monthly performance dashboards

### Inputs
- Project Tracker (04_Project_Tracker.md)
- Service lead status updates
- Client communication threads
- Issue tracker

### Outputs
- Weekly Client Progress Reports
- Monthly Performance Dashboards
- Issue Escalation Alerts
- Cross-workstream Status Summary

### Knowledge Required
- All 5 ThaiBridge services (workflows, deliverables, timelines)
- Project management methodology
- Client communication standards
- ThaiBridge Local Execution SOPs (SOP-LE-001 through SOP-LE-004)

### SOP References
- SOP-LE-001 (Client Onboarding)
- SOP-LE-002 (Weekly Client Reporting)
- SOP-LE-003 (Issue Escalation)
- SOP-LE-004 (Client Transition)

### Future Automations
- Auto-generate weekly client reports from workstream data
- AI issue detection (anomaly monitoring across all workstreams)
- Real-time client operations dashboard
- Predictive timeline management (when will tasks complete based on historical data)

---

## 8. Finance Assistant

**Mission:** Track revenue, expenses, and financial health. Ensure invoices go out on time and nothing falls through.

### Responsibilities
- Generate monthly client invoices based on retainer agreements
- Track third-party costs passed through to clients
- Maintain revenue tracker (by service, by client, by month)
- Prepare monthly P&L summary
- Flag unpaid invoices
- Track business expenses
- Support pricing decisions with cost and margin data

### Inputs
- Signed client agreements (retainer amounts, payment terms)
- Third-party invoices (warehouse, creator, registration fees)
- Business expense receipts
- Bank account transactions

### Outputs
- Monthly client invoices
- Revenue Dashboard
- Monthly P&L Summary
- Accounts Receivable Aging Report
- Expense Report

### Knowledge Required
- ThaiBridge pricing models (all 5 services)
- Client agreement terms
- Basic accounting principles
- Thai tax and invoicing requirements

### SOP References
- All service pricing models (Service Bible, Section 7 in each)

### Future Automations
- Auto-generate invoices from retainer data and third-party costs
- Auto-reconcile bank transactions
- Cash flow forecasting
- Tax preparation assistance

---

## 9. Content Manager

**Mission:** Maintain consistent, high-quality brand presence across all channels — website, social media, client communications.

### Responsibilities
- Maintain website content (service descriptions, case studies, updates)
- Draft LinkedIn posts aligned with brand voice
- Prepare WeChat official account content (Chinese language)
- Create client-facing document templates (proposals, reports, presentations)
- Manage brand asset library (logos, photos, templates)
- Draft email newsletters and client updates
- Ensure all external content passes Brand DNA tone-of-voice check

### Inputs
- Brand DNA (tone of voice, positioning, slogans)
- Website (index.html, all pages)
- Service Bible (service descriptions)
- Client success stories (anonymized, with permission)
- Industry news and trends

### Outputs
- Website content updates
- Social media posts
- Client document templates
- Brand asset library (organized, versioned)
- Monthly content calendar

### Knowledge Required
- ThaiBridge Brand DNA (complete)
- ThaiBridge tone of voice guidelines
- Chinese and English copywriting
- LinkedIn and WeChat content best practices
- SEO fundamentals

### SOP References
- Brand DNA — Tone of Voice section
- Brand DNA — Brand Guardrails (Always / Never)

### Future Automations
- AI content generation (first drafts in brand voice)
- Auto-schedule social media posts
- Website content freshness monitoring (flag outdated pages)
- Multi-language content versioning (CN / EN / TH)

---

## AI Employee Deployment Roadmap

### Phase 1: Foundation (Week 1–2)
- Deploy CEO Assistant (Claude Project with OS file access)
- Deploy Sales Manager (Claude Project with pipeline + service bible)
- Set up shared knowledge base: Brand DNA + Service Bible + SOPs

### Phase 2: Service AI (Week 2–4)
- Deploy Creator Manager, Warehouse Manager, Market Research Analyst
- Feed each with service-specific SOPs and knowledge
- Begin using for real client work

### Phase 3: Operations (Week 3–6)
- Deploy Business Matching Manager, Operations Manager
- Deploy Finance Assistant, Content Manager
- Integrate AI outputs into weekly operating rhythm

### Phase 4: Automation (Month 2–3)
- Identify highest-ROI automation opportunities from each role's Future Automations
- Build automated workflows (Zapier, Make, or custom)
- Measure time saved per role

---

*05_AI_Employees.md · ThaiBridge CEO Operating System V1.0*
*Owner: CEO / CTO · Review: Monthly (deployment progress + role performance)*
