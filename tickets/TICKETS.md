# Task Breakdown by Role

Generated from `TICKETS.csv`. Import that file into GitHub Issues, Jira, Trello, or Linear for tracking — this file is for quick reading.


## Project Lead

| ID | Title | Phase | Priority | Est. (days) |
|---|---|---|---|---|
| LEAD-01 | Taxonomy sign-off workshop | 1 - Requirements & Architecture | High | 1 |
| LEAD-02 | Resolve open questions | 1 - Requirements & Architecture | High | 1 |
| LEAD-03 | Coordinate UAT with admissions staff | 6 - Deployment & Testing | High | 2 |

**LEAD-01 — Taxonomy sign-off workshop**  
Validate source taxonomy with real admissions staff per PRD sec 6

**LEAD-02 — Resolve open questions**  
Answer PRD sec 18 items with stakeholders before build

**LEAD-03 — Coordinate UAT with admissions staff**  
User acceptance testing session before launch


## Backend Engineer

| ID | Title | Phase | Priority | Est. (days) |
|---|---|---|---|---|
| BE-01 | Set up FastAPI project skeleton | 1 - Requirements & Architecture | High | 1 |
| BE-02 | Design DB schema (SQLAlchemy models) | 1 - Requirements & Architecture | High | 3 |
| BE-03 | Set up Alembic migrations | 2 - Core Platform | Medium | 1 |
| BE-04 | Implement authentication endpoints | 2 - Core Platform | High | 3 |
| BE-05 | Implement RBAC middleware | 2 - Core Platform | High | 2 |
| BE-06 | Build Applicant CRUD APIs | 2 - Core Platform | High | 3 |
| BE-07 | Build Admission Source management APIs | 2 - Core Platform | Medium | 2 |
| BE-08 | Build Program/Campus/Department APIs | 2 - Core Platform | Medium | 2 |
| BE-09 | Build Referral management APIs | 2 - Core Platform | Medium | 1 |
| BE-10 | Implement export endpoints | 3 - Dashboard | Medium | 2 |
| BE-11 | Write OpenAPI documentation | 3 - Dashboard | Low | 2 |

**BE-01 — Set up FastAPI project skeleton**  
Create app structure (api/models/core/services) config and health check endpoint

**BE-02 — Design DB schema (SQLAlchemy models)**  
Model core entities from PRD sec 15: Users Roles Permissions Applicants Applications Programs Sources etc

**BE-03 — Set up Alembic migrations**  
Initialize migration tooling against the schema from BE-02

**BE-04 — Implement authentication endpoints**  
Login password recovery session management account lockout

**BE-05 — Implement RBAC middleware**  
Server-side permission checks on every protected endpoint per SEC-04

**BE-06 — Build Applicant CRUD APIs**  
Create/read/update/search/filter with field-level permission enforcement

**BE-07 — Build Admission Source management APIs**  
CRUD for source category/name/subcategory/campaign per FR-04

**BE-08 — Build Program/Campus/Department APIs**  
CRUD for program hierarchy per FR-06

**BE-09 — Build Referral management APIs**  
Referral categories and performance analysis endpoints per FR-05

**BE-10 — Implement export endpoints**  
Controlled export respecting permissions logging and watermarking per FR-15

**BE-11 — Write OpenAPI documentation**  
Ensure all endpoints documented with request/response schemas


## Data Engineer

| ID | Title | Phase | Priority | Est. (days) |
|---|---|---|---|---|
| DE-01 | Define CSV/Excel import mapping spec | 1 - Requirements & Architecture | High | 2 |
| DE-02 | Build import validation pipeline | 2 - Core Platform | High | 3 |
| DE-03 | Build source-mapping normalization logic | 2 - Core Platform | High | 2 |
| DE-04 | Build data quality checks | 2 - Core Platform | Medium | 2 |
| DE-05 | Build duplicate applicant detection | 2 - Core Platform | Medium | 2 |
| DE-06 | Historical data migration script | 3 - Dashboard | Medium | 3 |
| DE-07 | Build import audit logging | 3 - Dashboard | Low | 1 |

**DE-01 — Define CSV/Excel import mapping spec**  
Column mapping format for admissions data imports per FR-07

**DE-02 — Build import validation pipeline**  
Format validation duplicate detection error reporting using Pandas

**DE-03 — Build source-mapping normalization logic**  
Map raw/free-text source values to the taxonomy in PRD sec 6

**DE-04 — Build data quality checks**  
Detect missing fields invalid emails/phones inconsistent codes per FR-08

**DE-05 — Build duplicate applicant detection**  
Fuzzy-match duplicate applicant records across imports

**DE-06 — Historical data migration script**  
Migrate existing spreadsheet/legacy data into the new schema

**DE-07 — Build import audit logging**  
Log every import job with summary and errors per FR-07


## Frontend Engineer (Delna)

| ID | Title | Phase | Priority | Est. (days) |
|---|---|---|---|---|
| FE-01 | Set up Next.js + TypeScript + Tailwind skeleton | 1 - Requirements & Architecture | High | 1 |
| FE-02 | Wireframe dashboard funnel and applicant table | 1 - Requirements & Architecture | High | 2 |
| FE-03 | Build login + MFA UI | 2 - Core Platform | High | 2 |
| FE-04 | Build role-aware navigation/layout shell | 2 - Core Platform | High | 2 |
| FE-05 | Build main dashboard KPI cards | 3 - Dashboard | High | 3 |
| FE-06 | Build source analytics charts | 3 - Dashboard | High | 3 |
| FE-07 | Build funnel visualization | 3 - Dashboard | High | 2 |
| FE-08 | Build applicant table with filters/search | 3 - Dashboard | Medium | 3 |
| FE-09 | Build CSV/Excel import UI | 3 - Dashboard | Medium | 3 |
| FE-10 | Build report export UI | 3 - Dashboard | Medium | 2 |
| FE-11 | Responsive and accessibility pass | 4 - Security Hardening | Low | 2 |

**FE-01 — Set up Next.js + TypeScript + Tailwind skeleton**  
Project scaffold with routing and design tokens

**FE-02 — Wireframe dashboard funnel and applicant table**  
Low-fidelity wireframes reviewed with the team before build

**FE-03 — Build login + MFA UI**  
Auth flow screens wired to BE-04

**FE-04 — Build role-aware navigation/layout shell**  
Nav and page access differ per role from FR-02

**FE-05 — Build main dashboard KPI cards**  
Totals conversion rate target vs actual per FR-09

**FE-06 — Build source analytics charts**  
Leads/applications/offers/enrollments by source per FR-10

**FE-07 — Build funnel visualization**  
Stage-by-stage conversion view per FR-13

**FE-08 — Build applicant table with filters/search**  
Filterable by program campus source date counsellor

**FE-09 — Build CSV/Excel import UI**  
Upload mapping preview and validation results screens

**FE-10 — Build report export UI**  
PDF/Excel export respecting permissions per FR-15

**FE-11 — Responsive and accessibility pass**  
Verify usability on tablet/mobile widths and a11y basics


## Security Engineer

| ID | Title | Phase | Priority | Est. (days) |
|---|---|---|---|---|
| SEC-01 | Threat model the system | 1 - Requirements & Architecture | High | 2 |
| SEC-02 | Decide and implement auth approach | 2 - Core Platform | High | 2 |
| SEC-03 | Implement MFA | 2 - Core Platform | High | 2 |
| SEC-04 | Implement encryption config | 2 - Core Platform | High | 2 |
| SEC-05 | Implement audit logging service | 3 - Dashboard | High | 3 |
| SEC-06 | Implement PII data masking | 3 - Dashboard | High | 2 |
| SEC-07 | Implement rate limiting and account lockout | 4 - Security Hardening | High | 1 |
| SEC-08 | Set security headers | 4 - Security Hardening | Medium | 1 |
| SEC-09 | Run OWASP ASVS checklist review | 4 - Security Hardening | High | 2 |
| SEC-10 | Coordinate penetration test | 6 - Deployment & Testing | High | 3 |
| SEC-11 | Build security monitoring/alerting | 4 - Security Hardening | Medium | 2 |

**SEC-01 — Threat model the system**  
STRIDE pass on schema and API surface documented in security/docs

**SEC-02 — Decide and implement auth approach**  
SSO/OIDC vs standalone + MFA based on PRD open question 1

**SEC-03 — Implement MFA**  
Multi-factor auth for admin and high-privilege accounts per SEC-03

**SEC-04 — Implement encryption config**  
TLS in transit AES-256 at rest per SEC-01

**SEC-05 — Implement audit logging service**  
Central append-only log per SEC-07 covering all listed events

**SEC-06 — Implement PII data masking**  
Mask sensitive fields for roles without full access per SEC-06

**SEC-07 — Implement rate limiting and account lockout**  
Protect auth endpoints from brute force per SEC-05

**SEC-08 — Set security headers**  
CSP HSTS and related headers across the app

**SEC-09 — Run OWASP ASVS checklist review**  
Baseline review against SEC-10 before launch

**SEC-10 — Coordinate penetration test**  
Internal or external pen test before go-live per PRD sec 9

**SEC-11 — Build security monitoring/alerting**  
Flag suspicious activity patterns per SEC-08


## DevOps Engineer

| ID | Title | Phase | Priority | Est. (days) |
|---|---|---|---|---|
| OPS-01 | Set up Docker Compose for local dev | 1 - Requirements & Architecture | High | 1 |
| OPS-02 | Set up CI pipeline | 1 - Requirements & Architecture | Medium | 1 |
| OPS-04 | Set up centralized logging | 4 - Security Hardening | Medium | 2 |
| OPS-05 | Set up monitoring dashboards | 4 - Security Hardening | Low | 2 |
| OPS-06 | Implement backup and recovery | 4 - Security Hardening | High | 2 |
| OPS-09 | Production deployment pipeline | 6 - Deployment & Testing | High | 2 |

**OPS-01 — Set up Docker Compose for local dev**  
Postgres Redis backend and frontend running together locally

**OPS-02 — Set up CI pipeline**  
Lint and test on every push

**OPS-04 — Set up centralized logging**  
Aggregate app and audit logs for review

**OPS-05 — Set up monitoring dashboards**  
Prometheus/Grafana for app health

**OPS-06 — Implement backup and recovery**  
Automated backups with a tested restore process

**OPS-09 — Production deployment pipeline**  
CI/CD to staging and production environments


## Analytics Engineer

| ID | Title | Phase | Priority | Est. (days) |
|---|---|---|---|---|
| OPS-07 | Build forecasting prototype | 5 - Advanced Analytics | Low | 3 |
| OPS-08 | Build anomaly detection prototype | 5 - Advanced Analytics | Low | 3 |

**OPS-07 — Build forecasting prototype**  
Enrollment forecasting model per sec 11 advanced analytics

**OPS-08 — Build anomaly detection prototype**  
Flag source spikes and unusual volumes per sec 11


## DevOps/Analytics Engineer

| ID | Title | Phase | Priority | Est. (days) |
|---|---|---|---|---|
| OPS-03 | Implement KPI calculation engine | 3 - Dashboard | High | 2 |

**OPS-03 — Implement KPI calculation engine**  
Conversion/application/offer/enrollment rate calculations per sec 11
