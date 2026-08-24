# Backend — FastAPI

Owned by: **Backend Engineer** (with pairing from Data Engineer on schema, Security Engineer on auth/RBAC)

## Setup
```bash
cd backend
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```
Visit http://localhost:8000/docs for the auto-generated API docs.

## Structure
```
app/
├── main.py          # FastAPI app entrypoint
├── api/              # Route handlers (one module per resource)
├── models/            # SQLAlchemy models (see PRD sec 15 for entity list)
├── core/               # Config, security/auth helpers, dependencies
└── services/            # Business logic (kept out of route handlers)
```

## Your first tickets
See `../tickets/TICKETS.md` under "Backend Engineer" — start with BE-01 and BE-02.

## Notes
- Every protected endpoint must enforce RBAC server-side (SEC-04) — don't rely
  on the frontend to hide things.
- Use Pydantic schemas for all request/response validation.
- Parameterize all DB queries (SQLAlchemy ORM does this by default — avoid raw SQL).
