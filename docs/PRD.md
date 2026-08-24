# Product Requirements Document

## Product Name
**Secure University Admissions Intelligence & Analytics Platform**

**Working Name:** SAIAP
**Document Version:** 2.0 (merged draft)
**Status:** Draft for team review
**Last updated:** August 22, 2026

---

## 1. Product Overview

The Secure University Admissions Intelligence & Analytics Platform is a centralized, web-based system for collecting, managing, analyzing, and visualizing university admission and applicant-source data.

The platform will help authorized university stakeholders understand where applicants originate from, how they progress through the admission funnel, which recruitment channels produce the highest conversion rates, which programs attract applicants from specific sources and regions, and where admission targets are being achieved or missed.

The platform combines admissions analytics with security controls — role-based access control, multi-factor authentication, encryption, audit logging, data masking, secure API access, and monitoring of suspicious activity — because it holds sensitive applicant PII and needs to be trustworthy by design, not as an afterthought.

Intended users: admissions teams, management, analysts, counsellors, administrators, and other authorized personnel.

---

## 2. Problem Statement

Universities receive applicants through multiple channels — social media, the university website, entrance examinations, direct enquiries, referrals, alumni, faculty, education fairs, school partnerships, advertisements, and more.

When this data is scattered across spreadsheets, admission systems, forms, and emails, management faces:

- Difficulty identifying the most effective admission sources
- Inconsistent source classification
- Limited visibility into conversion rates
- Difficulty comparing programs and campuses
- Manual, slow reporting
- Duplicate or inconsistent applicant records
- Lack of centralized auditability
- Excessive exposure of applicant information
- Difficulty spotting suspicious access or data activity

This platform addresses these problems through a centralized, secure admissions analytics system.

---

## 3. Product Goals & Success Metrics

### Primary Goals
1. Centralize admission and applicant-source information.
2. Track the complete admission funnel.
3. Identify the sources that generate applicants and enrollments.
4. Measure conversion rates by source, program, campus, geography, and academic year.
5. Provide management and operational dashboards.
6. Reduce manual reporting.
7. Provide strong authentication and authorization.
8. Protect applicant personal data.
9. Maintain tamper-evident audit records of important activities.
10. Detect data-quality and suspicious-activity patterns.
11. Support data-driven admission planning.

### Quantified Success Metrics
| Metric | Target |
|---|---|
| % of admissions correctly tagged with source | ≥ 95% |
| Dashboard load time (p95, standard views) | < 2 seconds |
| Unauthorized access incidents | 0 |
| Time to generate a source-performance report | Days (manual) → minutes |
| Weekly active adoption by admissions staff | ≥ 80% within 1 month of launch |
| Major vulnerabilities open at go-live | 0 (post pen-test) |

---

## 4. Non-Goals

- The initial release will not replace the university's complete admission ERP.
- The platform functions primarily as an intelligence, analytics, monitoring, and controlled-data-access layer.
- The MVP will not automatically make admission decisions.
- AI-generated recommendations (future phase) will be advisory only and will not independently approve or reject applicants.
- No payment/fee processing in v1.
- No native mobile app in v1 (responsive web only).

---

## 5. Target Users / Roles

| Role | Needs |
|---|---|
| **Super Administrator** | System configuration, users, roles, permissions, data sources, security settings |
| **Admissions Head** | University-wide analytics, source performance, program trends, enrollment forecasts |
| **Admissions Officer** | Applicant-level admission information and workflow visibility |
| **Counsellor** | Access to applicants assigned to them and their admission progress |
| **Data Analyst** | Aggregated/analytical data without unnecessary access to PII |
| **Management / Executive Viewer** | Read-only KPI dashboards and reports |

---

## 6. Admission Source Taxonomy

The system shall support **configurable** admission-source categories, grouped as follows. Administrators can create, deactivate, rename, and re-categorize source types over time — expect this list to evolve once real data comes in.

| Category | Sub-sources |
|---|---|
| **Social Media** | Instagram, Facebook, LinkedIn, YouTube, WhatsApp groups |
| **Digital / Web** | University Website, Google Search, Digital Advertisement |
| **Exams** | Entrance Examination, State/national exam board referral |
| **Direct Contact** | Walk-in, Phone Enquiry, Email Enquiry, Campus Visit, Open House |
| **Referrals** | Friend Referral, Student Referral, Alumni Referral, Faculty Referral, Parent Referral |
| **Partnerships & Agents** | School Partnership, College Partnership, Education Consultant |
| **Events & Campaigns** | Education Fair, Scholarship Campaign, Counselling Session |
| **Other** | Other, Unknown — reviewed periodically; if a free-text value recurs, promote it to a formal sub-source |

---

## 7. Admission Funnel

The platform shall model applicant progression through configurable stages.

**Initial funnel:**
`Lead → Enquiry → Application Started → Application Submitted → Eligibility Verified → Examination/Interview → Offer → Acceptance → Fee Payment → Enrollment`

The system shall maintain historical status changes for every applicant (full audit trail of stage transitions, not just current state).

---

## 8. Core Functional Requirements

### FR-01 Authentication
Authenticated access required for all protected functionality. Support:
- Username/email authentication
- Multi-factor authentication
- Session management
- Password recovery
- Account lockout/rate limiting
- Optional university SSO/OIDC integration

### FR-02 Role-Based Access Control
Configurable, granular permissions per role: `SUPER_ADMIN`, `SYSTEM_ADMIN`, `ADMISSION_HEAD`, `ADMISSION_OFFICER`, `COUNSELLOR`, `ANALYST`, `VIEW_ONLY`.

### FR-03 Applicant Management
Authorized users can create, view (permitted fields only), update, search, and filter applicant records; view application status, source information, and admission history. Unauthorized users are blocked from protected fields — enforced at the API layer, not just hidden in the UI.

### FR-04 Admission Source Management
Store: source category, source name, source subcategory, campaign, referral type, creation date, active/inactive status.

### FR-05 Referral Management
Referral categories: Student, Alumni, Faculty, Parent, Friend, Agent, Other. Supports referral performance analysis.

### FR-06 Program Management
Supports Campus, School, Department, Program, Degree type, Intake, Academic year.

### FR-07 Data Import
CSV/Excel import with: column mapping, format validation, duplicate detection, error reporting, import summaries, and import audit logs.

### FR-08 Data Quality
Detects: duplicate applicants, missing required fields, invalid emails/phone numbers, invalid source mappings, inconsistent program codes, invalid dates, inconsistent status transitions.

### FR-09 Dashboard
Primary dashboard shows: total leads, applications, offers, accepted offers, enrollments, overall conversion rate, admission target vs. actual, top sources, top programs, regional distribution, admission funnel, year-over-year trend.

### FR-10 Source Analytics
Leads/applications/offers/enrollments by source; conversion rate by source; source performance by program, campus, geography, and academic year.

### FR-11 Program Analytics
Applications and enrollment by program; source by program; conversion by program; campus and academic-year comparison.

### FR-12 Geographic Analytics
State, district, city, and country-level analysis, where collected and permitted.

### FR-13 Funnel Analytics
Lead-to-application, application-to-offer, offer-to-acceptance, and acceptance-to-enrollment conversion, plus overall conversion.

### FR-14 Reporting
Daily, weekly, monthly, academic-year, source, program, and campaign reports.

### FR-15 Export
Controlled export respecting user permissions and field-level restrictions. Sensitive exports are logged and watermarked with exporter's name/timestamp.

---

## 9. Security Requirements

| ID | Requirement |
|---|---|
| **SEC-01 Encryption** | Sensitive data encrypted in transit (TLS 1.2+) and protected at rest (AES-256). |
| **SEC-02 Password Security** | Never stored in plaintext; strong hashing (e.g., Argon2id). |
| **SEC-03 MFA** | Required for administrative and high-privilege accounts. |
| **SEC-04 RBAC** | Every protected API resource enforces authorization checks server-side. |
| **SEC-05 API Security** | Input validation, authentication, authorization, rate limiting, secure error handling, request-size limits, parameterized DB operations. |
| **SEC-06 Data Masking** | PII masked for users who don't require full access. |
| **SEC-07 Audit Logging** | Records login success/failure, MFA failure, role changes, applicant access/updates, bulk imports/exports, sensitive data exports, permission failures, admin config changes. |
| **SEC-08 Security Monitoring** | Flags repeated failed auth, unusual access volume, repeated authorization failures, abnormally large exports, unexpected admin activity. |
| **SEC-09 Session Security** | Secure expiration, renewal, and invalidation controls; shorter timeouts for PII-heavy roles. |
| **SEC-10 Secure Development** | OWASP ASVS as security baseline; OWASP Top 10 as risk-awareness reference. Pen test required before go-live. |

---

## 10. Privacy Requirements

Privacy-by-design principles:
- Collect only required information.
- Clearly define processing purposes.
- Restrict access to personal information.
- Mask unnecessary personal information.
- Maintain configurable retention policies.
- Log sensitive access.
- Provide mechanisms for authorized data-management processes (correction/deletion requests).
- Protect backups.
- Avoid unnecessary replication of personal information.

Final legal and operational requirements should be reviewed against applicable data-protection law for the institution's jurisdiction (e.g., India's DPDP Act, or GDPR/FERPA if relevant) and university policy.

---

## 11. Analytics Requirements

### KPI Engine
- **Conversion Rate:** `enrollments / leads × 100`
- **Application Conversion:** `applications / leads × 100`
- **Offer Conversion:** `offers / applications × 100`
- **Enrollment Conversion:** `enrollments / offers × 100`

Additional KPIs: source contribution, program contribution, target achievement, year-over-year growth, average processing time, counsellor workload.

### Advanced Analytics (Future / Phase 5+)
- **Enrollment Forecasting** — predict expected enrollment from historical enrollment, application/offer volume, acceptance rate, source and program trends.
- **Anomaly Detection** — sudden source spikes, unusual application volumes, duplicate patterns, suspicious admin activity, abnormal exports.
- **Natural Language Analytics** — authorized users query the dashboard in plain language (e.g., "Which source produced the highest enrollment conversion for B.Tech this academic year?") and get an analytical response scoped to their authorized data.

---

## 12. Audit & Compliance

Audit records maintained for critical operations, containing: user, action, resource, timestamp, source IP (where appropriate), result, and relevant metadata. Audit records are protected against unauthorized modification (append-only / tamper-evident).

---

## 13. Non-Functional Requirements

| Category | Requirement |
|---|---|
| **Performance** | Dashboard pages load within an acceptable response time under expected institutional load — target p95 < 2 seconds for standard views. |
| **Availability** | Reliable operation during peak admission periods. |
| **Scalability** | Architecture supports growth in applicants, programs, campuses, academic years, users, and data sources. |
| **Maintainability** | Modular services, documented APIs. |
| **Usability** | Usable by non-technical admissions staff. |
| **Accessibility** | UI follows appropriate accessibility principles. |

---

## 14. Suggested Technical Architecture

| Layer | Choice |
|---|---|
| **Frontend** | Next.js, TypeScript, Tailwind CSS, Apache ECharts |
| **Backend** | Python, FastAPI, SQLAlchemy, Pydantic |
| **Database** | PostgreSQL |
| **Cache / Queue** | Redis |
| **Authentication** | OIDC/SSO, MFA, Keycloak or university identity provider |
| **Data Processing** | Python, Pandas, OpenPyXL |
| **Deployment** | Docker, Nginx, Linux, CI/CD pipeline |
| **Monitoring** | Prometheus, Grafana, centralized logs |

*If the team is more comfortable with a Node.js/Express backend and React frontend with Recharts/Chart.js instead, that's a reasonable lighter-weight alternative — pick whichever stack the team already knows well, since this project's differentiator is security and data modeling, not framework choice.*

---

## 15. Core Data Entities

Users · Roles · Permissions · Applicants · Applications · Admissions · Programs · Departments · Campuses · Sources · Source Categories · Referrals · Campaigns · Exams · Exam Results · Counsellors · Application Status History · Audit Logs · Login Events · Data Import Jobs · Data Quality Issues

---

## 16. Five-Person Team Allocation

| # | Role | Responsibilities |
|---|---|---|
| 1 | **Backend Engineer** | Backend architecture, API development, authentication endpoints, applicant/admission/source APIs, validation, database integration |
| 2 | **Data Engineer** | ETL pipelines, Excel/CSV ingestion, data cleaning and normalization, duplicate detection, data quality, source mapping |
| 3 | **Frontend & Dashboard Engineer** | UI/UX, dashboard, charts, filters, tables, reports, data visualization, responsive design |
| 4 | **Cybersecurity & IAM Engineer** | Threat modeling, RBAC, MFA, encryption, secure sessions, API security, security testing, audit logging, data masking, security monitoring |
| 5 | **Analytics & DevSecOps Engineer** | KPI engine, advanced analytics, forecasting, anomaly detection, Docker, CI/CD, deployment, monitoring, backup and recovery |

*One person (typically the Backend Engineer or a rotating lead) should also own overall project coordination — stakeholder communication with the admissions office, taxonomy sign-off, and timeline tracking — even if it's not a full-time role.*

---

## 17. Development Phases & Suggested Timeline

| Phase | Focus | Suggested Duration |
|---|---|---|
| **1. Requirements & Architecture** | Requirements gathering, threat modeling, database design, API spec, UI wireframes, taxonomy sign-off with admissions staff | Weeks 1–2 |
| **2. Core Platform** | Authentication, database, backend APIs, applicant management, source management | Weeks 3–5 |
| **3. Dashboard** | KPI cards, source analytics, funnel, program analytics, geographic analytics | Weeks 5–7 |
| **4. Security Hardening** | RBAC, MFA, encryption, audit logs, rate limiting, security headers, vulnerability testing | Weeks 7–8 |
| **5. Advanced Analytics** *(optional for v1)* | Forecasting, anomaly detection, advanced reports | Weeks 8–9 (or defer to v2) |
| **6. Deployment & Testing** | CI/CD, Docker deployment, performance testing, security/pen testing, backup testing, UAT with admissions staff | Weeks 9–10 |

---

## 18. Open Questions (resolve before build starts)
1. Does the university already have an SSO/IdP the platform should integrate with?
2. What existing systems currently hold admission data (exam portal, Google Forms, spreadsheets)? Any APIs available for automated ingestion?
3. Which data protection regulation applies (institution's country/state)?
4. Who are the actual end users of the "Executive Viewer" role — leadership, marketing, both?
5. Is marketing spend data available to calculate cost-per-admission by channel, or is this purely a volume/conversion tracker for v1?
6. Should Phase 5 (forecasting, anomaly detection) be in scope for the initial launch, or deferred to a v2 release?

---

## 19. Success Criteria

The system is successful when:
1. Authorized users can securely log in.
2. Different roles receive appropriate permissions.
3. Admission records can be imported and validated.
4. Applicants are correctly associated with admission sources.
5. Admission funnel metrics are correctly calculated.
6. Management can view source performance.
7. Program and geographic analytics are available.
8. Sensitive information is restricted according to user privileges.
9. Critical user actions are recorded in audit logs.
10. Security testing identifies and resolves major vulnerabilities before launch.
11. Reports can be generated without exposing unauthorized information.
12. The system handles realistic university admission dataset volumes.

---

## 20. MVP Definition

- Secure login
- RBAC
- Applicant management
- Source management
- CSV/Excel import
- PostgreSQL database
- Dashboard
- Source analytics
- Program analytics
- Admission funnel
- Filters
- Audit logging
- Data masking
- Basic security monitoring

---

## 21. Future Enhancements

University SSO integration · Mobile application · CRM integration · Admission ERP integration · Marketing campaign integration · WhatsApp/communication analytics · AI forecasting · AI-based anomaly detection · Natural-language analytics · Automated management reports · Advanced fraud/duplicate detection · Multi-campus federation · Cross-year cohort analysis

---

## 22. Final Product Vision

The long-term goal:

**Capture → Secure → Normalize → Analyze → Predict → Act**

The platform should let university decision-makers answer:
> Where are our students coming from? Which recruitment channels actually convert? Which programs need more recruitment effort? Which regions are growing or declining? Are our admission targets on track? Are there unusual data or access patterns? What should the university prioritize next?

All of this delivered while maintaining strong access controls, privacy-aware data handling, and a complete audit trail.

---

## Appendix: Sample Applicant Record Fields (quick reference)
- Applicant/Student ID (internal, not national ID)
- Name, contact info (PII — access-restricted, masked by default)
- Program applied to, campus, academic year/intake
- Application date / admission date
- Primary source, sub-source, campaign
- Referral type (if applicable)
- Counsellor/officer assigned
- Funnel status (Lead / Enquiry / Application / Offer / Acceptance / Enrollment / Rejected / Withdrawn)
- Status change history (timestamped)
