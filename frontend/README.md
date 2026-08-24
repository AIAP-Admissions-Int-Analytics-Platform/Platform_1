# Frontend — Next.js Dashboard

Owned by: **Frontend Engineer (Delna)**

## Setup
```bash
cd frontend
npm install
npm run dev
```
Visit http://localhost:3000

## Structure
```
src/
├── pages/         # Route-level pages (dashboard, applicants, sources, login...)
├── components/     # Reusable UI (KPI cards, charts, tables, filters)
└── lib/             # API client, auth helpers, chart config
```

## Your first tickets
See `../tickets/TICKETS.md` under "Frontend Engineer" — start with FE-01 and FE-02.

## Notes
- Don't wait on the backend to be fully built — mock API responses matching
  the OpenAPI contract (see BE-11) and swap in the real client later.
- Role-based UI (FE-04) is a UX nicety, not a security boundary — the backend
  enforces RBAC regardless of what the frontend shows or hides.
- Charting library suggested in the PRD: Apache ECharts. Recharts/Chart.js are
  fine substitutes if the team knows them better.
