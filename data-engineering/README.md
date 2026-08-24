# Data Engineering — Import & ETL

Owned by: **Data Engineer** (pairs closely with Backend Engineer on schema)

## What lives here
- `scripts/` — import validation, cleaning, and source-mapping scripts (Pandas)
- `mappings/` — column-mapping specs for CSV/Excel imports (DE-01)

## Your first tickets
See `../tickets/TICKETS.md` under "Data Engineer" — start with DE-01, then
pair with the Backend Engineer on the schema (BE-02) before building DE-02.

## Notes
- The source taxonomy (PRD sec 6) is the single most important thing to get
  right here — a wrong mapping means every downstream chart is wrong.
- Keep "Other"/free-text values visible in a report so the taxonomy can be
  updated as real data comes in (see PRD sec 6 note).
