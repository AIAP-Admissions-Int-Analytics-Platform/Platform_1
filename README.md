# SAIAP — Secure University Admissions Intelligence & Analytics Platform

A centralized, secure dashboard for tracking university admissions by source
(social media, direct contact, exams, referrals, and more), with role-based
access, audit logging, and funnel/conversion analytics.

## Repo Layout

```
saiap/
├── backend/            # FastAPI + SQLAlchemy API (Member 1 — Backend Engineer)
├── frontend/            # Next.js + TypeScript dashboard (Delna — Frontend Engineer)
├── data-engineering/     # ETL, import pipelines, data quality (Member 2 — Data Engineer)
├── security/             # Threat model, policies, security configs (Member 4 — Security/IAM)
├── devops/                # Docker, CI/CD, monitoring (Member 5 — Analytics/DevSecOps)
├── docs/                  # PRD and reference docs
└── tickets/               # Task breakdown per role (import into GitHub Issues/Jira/Trello)
```

## Where to Start
1. Read `docs/PRD.md` — the full requirements.
2. Read `GETTING_STARTED.md` — Week 1 setup checklist for every role.
3. Open `tickets/TICKETS.csv` and import into your project management tool
   (GitHub Issues, Jira, Trello, Linear all accept CSV import).
4. Each role folder has its own `README.md` with setup instructions specific
   to that part of the stack.

## Tech Stack (suggested — see PRD section 14 for the lighter-weight alternative)
- Backend: Python, FastAPI, SQLAlchemy, PostgreSQL
- Frontend: Next.js, TypeScript, Tailwind CSS, Apache ECharts
- Auth: OIDC/SSO + MFA (Keycloak or university IdP)
- Infra: Docker, Redis, CI/CD, Prometheus/Grafana

## Local Dev (once backend/frontend skeletons are filled in)
```bash
cp .env.example .env      # fill in secrets
docker compose -f devops/docker/docker-compose.yml up --build
```
