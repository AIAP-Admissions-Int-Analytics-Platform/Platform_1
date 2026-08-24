"""
SQLAlchemy models — starter stub for ticket BE-02.

This is intentionally incomplete: it sketches the core entities from
PRD section 15 so the team has a shared starting point, not a finished
schema. Expand fields, add indexes/constraints, and add the remaining
entities (Campaigns, Exams, Exam Results, Login Events, Data Import Jobs,
Data Quality Issues) as you build FR-04 through FR-08.
"""
from datetime import datetime
from sqlalchemy import (
    Column, Integer, String, DateTime, ForeignKey, Boolean, Text
)
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False, index=True)
    password_hash = Column(String, nullable=False)  # argon2id — see SEC-02
    role_id = Column(Integer, ForeignKey("roles.id"), nullable=False)
    mfa_enabled = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    role = relationship("Role", back_populates="users")


class Role(Base):
    __tablename__ = "roles"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)  # SUPER_ADMIN, ADMISSION_HEAD, etc.
    description = Column(Text)

    users = relationship("User", back_populates="role")


class SourceCategory(Base):
    __tablename__ = "source_categories"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)  # Social Media, Direct Contact, Exams, Referrals...
    is_active = Column(Boolean, default=True)


class Source(Base):
    __tablename__ = "sources"
    id = Column(Integer, primary_key=True)
    category_id = Column(Integer, ForeignKey("source_categories.id"), nullable=False)
    name = Column(String, nullable=False)          # e.g. "Instagram", "Walk-in"
    subcategory = Column(String, nullable=True)
    campaign = Column(String, nullable=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    category = relationship("SourceCategory")


class Campus(Base):
    __tablename__ = "campuses"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)


class Program(Base):
    __tablename__ = "programs"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    department = Column(String)
    degree_type = Column(String)
    campus_id = Column(Integer, ForeignKey("campuses.id"))


class Applicant(Base):
    """
    Holds PII — every read/write path touching this table must go through
    RBAC (SEC-04) and be recorded in the audit log (SEC-07).
    """
    __tablename__ = "applicants"
    id = Column(Integer, primary_key=True)
    full_name = Column(String, nullable=False)
    email = Column(String, index=True)
    phone = Column(String)
    program_id = Column(Integer, ForeignKey("programs.id"))
    source_id = Column(Integer, ForeignKey("sources.id"))
    referral_type = Column(String, nullable=True)  # Student/Alumni/Faculty/Parent/Friend/Agent/Other
    counsellor_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    academic_year = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

    program = relationship("Program")
    source = relationship("Source")


class ApplicationStatusHistory(Base):
    """Tracks funnel stage transitions — see PRD section 7."""
    __tablename__ = "application_status_history"
    id = Column(Integer, primary_key=True)
    applicant_id = Column(Integer, ForeignKey("applicants.id"), nullable=False)
    status = Column(String, nullable=False)  # Lead, Enquiry, Application Started, ... Enrollment
    changed_at = Column(DateTime, default=datetime.utcnow)
    changed_by_user_id = Column(Integer, ForeignKey("users.id"))


class AuditLog(Base):
    """Append-only audit trail — see SEC-07. Do not allow UPDATE/DELETE on this table."""
    __tablename__ = "audit_logs"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    action = Column(String, nullable=False)
    resource = Column(String, nullable=False)
    result = Column(String)  # success / failure
    source_ip = Column(String, nullable=True)
    metadata_json = Column(Text, nullable=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
