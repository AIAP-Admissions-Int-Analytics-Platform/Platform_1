"""
SAIAP backend entrypoint.

This is a minimal skeleton — see tickets BE-01 through BE-11 for the build-out
plan. Each router below is a stub; implement them under app/api/.
"""
from fastapi import FastAPI

app = FastAPI(
    title="SAIAP API",
    description="Secure University Admissions Intelligence & Analytics Platform",
    version="0.1.0",
)


@app.get("/health")
def health_check():
    """Basic liveness check — used by Docker/CI/monitoring."""
    return {"status": "ok"}


# TODO (BE-04): include auth router
# TODO (BE-06): include applicants router
# TODO (BE-07): include sources router
# TODO (BE-08): include programs router
# TODO (BE-09): include referrals router
