# Security — Threat Model, Policies, Configs

Owned by: **Security/IAM Engineer**

## What lives here
- `docs/` — threat model (SEC-01), OWASP ASVS review notes (SEC-09)
- `policies/` — data retention, access control, and incident response policy drafts

## Your first tickets
See `../tickets/TICKETS.md` under "Security Engineer" — start with SEC-01
(threat model) before much code exists elsewhere; it's cheaper to change a
schema/API surface now than after Phase 2 is built.

## Non-negotiables (from PRD sections 9–10)
- Every protected API endpoint enforces RBAC server-side.
- Passwords hashed with Argon2id — never plaintext, never reversible encryption.
- PII masked by default for roles that don't need full access.
- All sensitive access/export events logged to an append-only audit trail.
- MFA required for admin and high-privilege roles.
- Pen test completed before go-live (SEC-10 / LEAD-03 in tickets).
