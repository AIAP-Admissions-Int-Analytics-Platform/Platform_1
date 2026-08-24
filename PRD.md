# Product Requirements Document

## Product Name

**Secure University Admissions Intelligence & Analytics Platform**

**Working Name:** SAIAP

**Document Version:** 1.0

---

## 1. Product Overview

The Secure University Admissions Intelligence & Analytics Platform is a centralized web-based system for collecting, managing, analyzing, and visualizing university admission and applicant-source data.

The platform will help authorized university stakeholders understand where applicants originate from, how applicants progress through the admission funnel, which recruitment channels produce the highest conversion rates, which programs attract applicants from specific sources and regions, and where admission targets are being achieved or missed.

The platform will combine admissions analytics with security controls such as role-based access control, multi-factor authentication, encryption, audit logging, data masking, secure API access, and monitoring of suspicious activity.

The system is intended for use by university admissions teams, management, analysts, counsellors, administrators, and other authorized personnel.

---

## 2. Problem Statement

Universities receive applicants through multiple channels, including social media, university websites, entrance examinations, direct enquiries, referrals, alumni, faculty, education fairs, school partnerships, advertisements, and other sources.

When this information exists across spreadsheets, admission systems, forms, emails, and other disconnected systems, management faces several problems:

- Difficulty identifying the most effective admission sources.
- Inconsistent source classification.
- Limited visibility into conversion rates.
- Difficulty comparing programs and campuses.
- Manual reporting.
- Duplicate or inconsistent applicant records.
- Lack of centralized auditability.
- Excessive exposure of applicant information.
- Difficulty identifying suspicious access or data activity.

The proposed platform addresses these problems through a centralized, secure admissions analytics system.

---

## 3. Product Goals

### Primary Goals

1. Centralize admission and applicant-source information.
2. Track the complete admission funnel.
3. Identify the sources that generate applicants and enrollments.
4. Measure conversion rates by source, program, campus, geography, and academic year.
5. Provide management dashboards and operational dashboards.
6. Reduce manual reporting.
7. Provide strong authentication and authorization.
8. Protect applicant personal data.
9. Maintain tamper-evident audit records of important activities.
10. Detect data-quality and suspicious-activity patterns.
11. Support data-driven admission planning.

---

## 4. Non-Goals

The initial release will not attempt to replace the university's complete admission ERP.

The platform will primarily function as an intelligence, analytics, monitoring, and controlled-data-access layer.

The MVP will not automatically make admission decisions.

AI-generated recommendations will be advisory only and will not independently approve or reject applicants.

---

## 5. Target Users

### Super Administrator

Responsible for system configuration, users, roles, permissions, data sources, and security settings.

### Admissions Head

Needs university-wide admissions analytics, source performance, program trends, and enrollment forecasts.

### Admissions Officer

Needs applicant-level admission information and workflow visibility.

### Counsellor

Needs access to applicants assigned to them and their admission progress.

### Data Analyst

Needs aggregated and analytical data without unnecessary access to personally identifiable information.

### Management / Executive Viewer

Needs read-only KPI dashboards and reports.

---

## 6. Admission Source Taxonomy

The system shall support configurable admission-source categories.

Initial categories may include:

- Social Media
- University Website
- Google Search
- Digital Advertisement
- Entrance Examination
- Direct Contact
- Walk-in
- Phone Enquiry
- Email Enquiry
- Friend Referral
- Student Referral
- Alumni Referral
- Faculty Referral
- Parent Referral
- School Partnership
- College Partnership
- Education Consultant
- Education Fair
- Open House
- Campus Visit
- Scholarship Campaign
- Counselling Session
- Other
- Unknown

Administrators shall be able to create, deactivate, rename, and categorize source types.

---

## 7. Admission Funnel

The platform shall model applicant progression through configurable stages.

Initial funnel:

**Lead → Enquiry → Application Started → Application Submitted → Eligibility Verified → Examination/Interview → Offer → Acceptance → Fee Payment → Enrollment**

The system shall maintain historical status changes.

---

## 8. Core Functional Requirements

### FR-01 Authentication

The system shall require authenticated access to protected administrative functionality.

The system should support:

- Username/email authentication
- Multi-factor authentication
- Session management
- Password recovery
- Account lockout/rate limiting
- Optional university SSO/OIDC integration

---

### FR-02 Role-Based Access Control

The system shall implement role-based permissions.

Example roles:

- SUPER_ADMIN
- SYSTEM_ADMIN
- ADMISSION_HEAD
- ADMISSION_OFFICER
- COUNSELLOR
- ANALYST
- VIEW_ONLY

Permissions shall be configurable.

---

### FR-03 Applicant Management

Authorized users shall be able to:

- Create applicant records
- View permitted applicant information
- Update permitted information
- Search applicants
- Filter applicants
- View application status
- View source information
- View admission history

The system shall prevent unauthorized users from accessing protected applicant fields.

---

### FR-04 Admission Source Management

The system shall store:

- Source category
- Source name
- Source subcategory
- Campaign
- Referral type
- Source creation date
- Active/inactive status

---

### FR-05 Referral Management

Referral sources shall support categories such as:

- Student
- Alumni
- Faculty
- Parent
- Friend
- Agent
- Other

The system shall support referral performance analysis.

---

### FR-06 Program Management

The system shall support:

- Campus
- School
- Department
- Program
- Degree type
- Intake
- Academic year

---

### FR-07 Data Import

Authorized users shall be able to import:

- CSV
- Excel

The system shall provide:

- Column mapping
- Format validation
- Duplicate detection
- Error reporting
- Import summaries
- Import audit logs

---

### FR-08 Data Quality

The system shall detect:

- Duplicate applicants
- Missing required fields
- Invalid email addresses
- Invalid phone numbers
- Invalid source mappings
- Inconsistent program codes
- Invalid dates
- Inconsistent status transitions

---

### FR-09 Dashboard

The primary dashboard shall show:

- Total leads
- Total applications
- Total offers
- Total accepted offers
- Total enrollments
- Overall conversion rate
- Admission target vs actual
- Top admission sources
- Top programs
- Regional distribution
- Admission funnel
- Year-over-year trend

---

### FR-10 Source Analytics

Users with appropriate permissions shall be able to analyze:

- Leads by source
- Applications by source
- Offers by source
- Enrollments by source
- Conversion rate by source
- Source performance by program
- Source performance by campus
- Source performance by geography
- Source performance by academic year

---

### FR-11 Program Analytics

The system shall support:

- Applications by program
- Enrollment by program
- Source by program
- Conversion by program
- Campus comparison
- Academic-year comparison

---

### FR-12 Geographic Analytics

Where collected and permitted, the system shall support:

- State-level analysis
- District-level analysis
- City-level analysis
- Country-level analysis

---

### FR-13 Funnel Analytics

Users shall be able to identify:

- Lead-to-application conversion
- Application-to-offer conversion
- Offer-to-acceptance conversion
- Acceptance-to-enrollment conversion
- Overall conversion

---

### FR-14 Reporting

Authorized users shall be able to generate:

- Daily reports
- Weekly reports
- Monthly reports
- Academic-year reports
- Source reports
- Program reports
- Campaign reports

---

### FR-15 Export

The system shall allow controlled data export.

Exports shall respect user permissions and applicable field-level restrictions.

Sensitive exports shall be logged.

---

## 9. Security Requirements

### SEC-01 Encryption

Sensitive data shall be encrypted in transit and protected at rest.

### SEC-02 Password Security

Passwords shall never be stored in plaintext.

A strong password-hashing mechanism such as Argon2id shall be used.

### SEC-03 MFA

Administrative and high-privilege accounts should require multi-factor authentication.

### SEC-04 RBAC

Every protected API resource shall enforce authorization checks.

### SEC-05 API Security

The API shall implement:

- Input validation
- Authentication
- Authorization
- Rate limiting
- Secure error handling
- Request-size limits
- Parameterized database operations

### SEC-06 Data Masking

Personally identifiable information shall be masked for users who do not require full access.

### SEC-07 Audit Logging

The platform shall record important security and data events, including:

- Login success
- Login failure
- MFA failure
- Role changes
- Applicant access
- Applicant updates
- Bulk imports
- Bulk exports
- Sensitive data exports
- Permission failures
- Administrative configuration changes

### SEC-08 Security Monitoring

The system shall identify suspicious activity patterns such as:

- Repeated failed authentication
- Unusual access volume
- Repeated authorization failures
- Abnormally large exports
- Unexpected administrative activity

### SEC-09 Session Security

Sessions shall use secure expiration, renewal, and invalidation controls.

### SEC-10 Secure Development

Development and verification shall use OWASP ASVS as a security baseline and OWASP Top 10 as a risk-awareness reference.

---

## 10. Privacy Requirements

The system shall follow privacy-by-design principles.

Requirements include:

- Collect only required information.
- Clearly define processing purposes.
- Restrict access to personal information.
- Mask unnecessary personal information.
- Maintain configurable retention policies.
- Log sensitive access.
- Provide mechanisms for authorized data-management processes.
- Protect backups.
- Avoid unnecessary replication of personal information.

The final legal and operational requirements shall be reviewed against applicable Indian data-protection requirements and university policy.

---

## 11. Analytics Requirements

### KPI Engine

The system shall calculate:

**Conversion Rate**

`enrollments / leads × 100`

**Application Conversion**

`applications / leads × 100`

**Offer Conversion**

`offers / applications × 100`

**Enrollment Conversion**

`enrollments / offers × 100`

Additional KPIs may include:

- Source contribution
- Program contribution
- Target achievement
- Year-over-year growth
- Average processing time
- Counsellor workload

---

## 12. Advanced Analytics

Future versions may include:

### Enrollment Forecasting

Predict expected enrollment based on:

- Historical enrollment
- Application volume
- Offer volume
- Acceptance rate
- Source trends
- Program trends

### Anomaly Detection

Detect:

- Sudden source spikes
- Unusual application volumes
- Duplicate patterns
- Suspicious administrative activity
- Abnormal exports

### Natural Language Analytics

Authorized users may query the dashboard using natural language.

Example:

> Which source produced the highest enrollment conversion for B.Tech programs this academic year?

The system shall return an analytical response based on authorized data.

---

## 13. Audit & Compliance

The system shall maintain audit records for critical operations.

Audit records should contain:

- User
- Action
- Resource
- Timestamp
- Source IP where appropriate
- Result
- Relevant metadata

Audit records shall be protected against unauthorized modification.

---

## 14. Non-Functional Requirements

### Performance

Dashboard pages should normally load within an acceptable response time under expected institutional load.

### Availability

The platform should support reliable operation during peak admission periods.

### Scalability

The architecture should support growth in:

- Applicants
- Programs
- Campuses
- Academic years
- Users
- Data sources

### Maintainability

The system should use modular services and documented APIs.

### Usability

The dashboard should be usable by non-technical admissions staff.

### Accessibility

The UI should follow appropriate accessibility principles.

---

## 15. Suggested Technical Architecture

### Frontend

- Next.js
- TypeScript
- Tailwind CSS
- Apache ECharts

### Backend

- Python
- FastAPI
- SQLAlchemy
- Pydantic

### Database

- PostgreSQL

### Cache / Queue

- Redis

### Authentication

- OIDC / SSO
- MFA
- Keycloak or university identity provider

### Data Processing

- Python
- Pandas
- OpenPyXL

### Deployment

- Docker
- Nginx
- Linux
- CI/CD pipeline

### Monitoring

- Prometheus
- Grafana
- Centralized logs

---

## 16. Core Data Entities

The initial data model shall include:

- Users
- Roles
- Permissions
- Applicants
- Applications
- Admissions
- Programs
- Departments
- Campuses
- Sources
- Source Categories
- Referrals
- Campaigns
- Exams
- Exam Results
- Counsellors
- Application Status History
- Audit Logs
- Login Events
- Data Import Jobs
- Data Quality Issues

---

## 17. Five-Person Team Allocation

### Member 1 — Backend Engineer

Responsible for:

- Backend architecture
- API development
- Authentication endpoints
- Applicant APIs
- Admission APIs
- Source APIs
- Validation
- Database integration

### Member 2 — Data Engineer

Responsible for:

- ETL pipelines
- Excel/CSV ingestion
- Data cleaning
- Data normalization
- Duplicate detection
- Data quality
- Data-source mapping

### Member 3 — Frontend & Dashboard Engineer

Responsible for:

- UI/UX
- Dashboard
- Charts
- Filters
- Tables
- Reports
- Data visualization
- Responsive design

### Member 4 — Cybersecurity & IAM Engineer

Responsible for:

- Threat modeling
- RBAC
- MFA
- Encryption
- Secure sessions
- API security
- Security testing
- Audit logging
- Data masking
- Security monitoring

### Member 5 — Analytics & DevSecOps Engineer

Responsible for:

- KPI engine
- Advanced analytics
- Forecasting
- Anomaly detection
- Docker
- CI/CD
- Deployment
- Monitoring
- Backup and recovery

---

## 18. Development Phases

### Phase 1 — Requirements & Architecture

- Requirements gathering
- Threat modeling
- Database design
- API specification
- UI wireframes

### Phase 2 — Core Platform

- Authentication
- Database
- Backend APIs
- Applicant management
- Source management

### Phase 3 — Dashboard

- KPI cards
- Source analytics
- Funnel
- Program analytics
- Geographic analytics

### Phase 4 — Security Hardening

- RBAC
- MFA
- Encryption
- Audit logs
- Rate limiting
- Security headers
- Vulnerability testing

### Phase 5 — Advanced Analytics

- Forecasting
- Anomaly detection
- Advanced reports

### Phase 6 — Deployment & Testing

- CI/CD
- Docker deployment
- Performance testing
- Security testing
- Backup testing
- User acceptance testing

---

## 19. Success Criteria

The system will be considered successful when:

1. Authorized users can securely log in.
2. Different roles receive appropriate permissions.
3. Admission records can be imported and validated.
4. Applicants can be associated with admission sources.
5. Admission funnel metrics are correctly calculated.
6. Management can view source performance.
7. Program and geographic analytics are available.
8. Sensitive information is restricted according to user privileges.
9. Critical user actions are recorded in audit logs.
10. Security testing identifies and addresses major application vulnerabilities.
11. Reports can be generated without exposing unauthorized information.
12. The system can handle realistic university admission datasets.

---

## 20. MVP Definition

The Minimum Viable Product shall contain:

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

Potential future capabilities include:

- University SSO integration
- Mobile application
- CRM integration
- Admission ERP integration
- Marketing campaign integration
- WhatsApp/communication analytics
- AI forecasting
- AI-based anomaly detection
- Natural-language analytics
- Automated management reports
- Advanced fraud/duplicate detection
- Multi-campus federation
- Cross-year cohort analysis

---

## 22. Final Product Vision

The final system should evolve from a dashboard into a university-level admissions intelligence platform.

The long-term goal is:

**Capture → Secure → Normalize → Analyze → Predict → Act**

The platform should enable university decision-makers to answer:

> Where are our students coming from?

> Which recruitment channels actually convert?

> Which programs need more recruitment effort?

> Which regions are growing or declining?

> Are our admission targets on track?

> Are there unusual data or access patterns?

> What should the university prioritize next?

All of this should be delivered while maintaining strong access controls, privacy-aware data handling, and a complete audit trail.