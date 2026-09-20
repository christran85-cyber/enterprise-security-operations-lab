# 🤖 Phase 08 — Security Automation & Response

> **Objective:** Integrate PostgreSQL security data with Python automation to retrieve security incidents, evaluate severity, automatically update incident status, create an audit trail, and validate the resulting database changes.

[← Phase 07](phase-07-vulnerability-management.md) | [🏠 Main Project](../README.md) | [Phase 09 →](phase-09-threat-intelligence.md)

---

## 📑 Table of Contents

- [Phase Summary](#-phase-summary)
- [Overview](#-overview)
- [Security Automation Architecture](#️-security-automation-architecture)
- [Phase Objectives](#-phase-objectives)
- [PostgreSQL Incident Records](#-postgresql-incident-records)
- [SecurityOpsDB Incident Query](#-securityopsdb-incident-query)
- [Python Security Automation](#-python-security-automation)
- [Severity-Based Response Logic](#-severity-based-response-logic)
- [Automation Processing](#️-automation-processing)
- [Automation Audit Logging](#-automation-audit-logging)
- [Incident Status Validation](#-incident-status-validation)
- [Python PostgreSQL Reporting](#-python-postgresql-reporting)
- [End-to-End Validation](#-end-to-end-validation)
- [Commands Used](#-commands-used)
- [Troubleshooting](#-troubleshooting)
- [Validation Methodology](#-validation-methodology)
- [Lessons Learned](#-lessons-learned)
- [Skills Demonstrated](#-skills-demonstrated)
- [Evidence Summary](#-evidence-summary)
- [Phase Outcome](#-phase-outcome)

---

# 📊 Phase Summary

| Category | Details |
|---|---|
| **Status** | ✅ Complete |
| **Automation Host** | SOC-Wazuh |
| **Database** | PostgreSQL |
| **Security Database** | SecurityOpsDB |
| **Automation Language** | Python 3 |
| **Database Integration** | psycopg |
| **Security Data** | Incident records |
| **Response Logic** | Severity-based |
| **High Severity** | Escalated |
| **Medium Severity** | Reviewed |
| **Audit Capability** | Automation log |
| **Primary Skill** | Security automation |
| **Workflow** | Store → Query → Analyze → Decide → Update → Audit → Validate |

---

# 📋 Overview

Phase 8 expanded the Enterprise Security Operations Lab from manual security investigation into **database-driven security automation**.

Previous phases established:

- Endpoint monitoring
- Network IDS detection
- SIEM analysis
- Event correlation
- Vulnerability assessment
- Security remediation

Phase 8 introduced automation into that workflow.

Security incident information was stored inside:

```text
PostgreSQL
     │
     ▼
SecurityOpsDB
```

Python then retrieved those incident records and automatically evaluated their severity.

```text
Security Incident
       │
       ▼
PostgreSQL SecurityOpsDB
       │
       ▼
Python Automation
       │
       ▼
Retrieve Incident
       │
       ▼
Evaluate Severity
       │
       ├──── High ────► Escalated
       │
       ├──── Medium ──► Reviewed
       │
       └──── Low ─────► Reviewed
       │
       ▼
Update Incident
       │
       ▼
Create Audit Record
       │
       ▼
Validate Database
```

The goal was not to replace the SOC analyst.

The goal was to demonstrate how repeatable processing tasks can be automated while maintaining an auditable record of the actions performed.

---

# 🏗️ Security Automation Architecture

Phase 8 connected security telemetry, PostgreSQL, and Python.

```text
          Security Telemetry
                 │
          ┌──────┴──────┐
          │             │
          ▼             ▼
        Wazuh        Suricata
          │             │
          └──────┬──────┘
                 │
                 ▼
          Security Incident
                 │
                 ▼
       PostgreSQL SecurityOpsDB
                 │
                 ▼
          Python Automation
                 │
          ┌──────┴──────┐
          │             │
          ▼             ▼
    Incident Data   Severity Logic
          │             │
          └──────┬──────┘
                 │
                 ▼
         Automated Decision
                 │
          ┌──────┴──────┐
          │             │
          ▼             ▼
      Escalated       Reviewed
          │             │
          └──────┬──────┘
                 │
                 ▼
           Incident Table
                 │
                 ▼
          Automation Log
                 │
                 ▼
           SOC Validation
```

### SOC-Wazuh

Served as the security server and automation host.

### PostgreSQL

Provided structured storage for security operations data.

### SecurityOpsDB

Stored:

- Security incidents
- Severity information
- Detection information
- Incident status
- Automation records

### Python

Provided the logic required to:

- Connect to PostgreSQL
- Retrieve incidents
- Evaluate severity
- Determine response actions
- Update incident status
- Create audit records

---

# 🎯 Phase Objectives

- [x] Use PostgreSQL as a security operations data store
- [x] Create and query security incident records
- [x] Connect Python to PostgreSQL
- [x] Retrieve incidents programmatically
- [x] Evaluate incident severity using Python
- [x] Determine automated response actions
- [x] Escalate high-severity incidents
- [x] Route medium-severity incidents for review
- [x] Update incident status in PostgreSQL
- [x] Create automation audit records
- [x] Validate automated database modifications
- [x] Generate security information from PostgreSQL
- [x] Troubleshoot Python logic
- [x] Troubleshoot PostgreSQL queries
- [x] Troubleshoot Linux permissions
- [x] Validate the workflow end-to-end
- [x] Document automation evidence

---

# 🗄️ PostgreSQL Incident Records

Security incidents were stored inside the PostgreSQL `SecurityOpsDB` database.

The records represented activity demonstrated earlier in the Enterprise Security Operations Lab.

Example incidents included:

```text
Incident 1

Type: SSH Brute Force
Severity: High
Detected By: Wazuh + Suricata
```

and:

```text
Incident 2

Type: Network Reconnaissance
Severity: Medium
Detected By: Suricata
```

These records provided structured data that could be processed programmatically instead of requiring manual review of every record.

## 📸 Evidence — PostgreSQL Incident Records

![PostgreSQL Incident Records](../images/phase8-postgresql-incident-records.png)

This establishes the security incident data used by the automation workflow.

**Result:** ✅ Security incident records successfully stored in PostgreSQL.

---

# 🔎 SecurityOpsDB Incident Query

The incident table was queried before automation to establish the starting database state.

The query returned information including:

- Incident ID
- Incident type
- Severity
- Incident status
- Detection source

Conceptually:

```sql
SELECT * FROM incidents;
```

This provided a baseline before Python modified any records.

## 📸 Evidence — SecurityOpsDB Incident Query

![SecurityOpsDB Incident Query](../images/phase8-securityops-incident-query.png)

**Result:** ✅ Security incident data successfully retrieved from SecurityOpsDB.

---

# 🐍 Python Security Automation

A Python script named:

```text
securityops_automation.py
```

was developed to automate incident processing.

The script connected Python with PostgreSQL and performed the following workflow:

```text
Connect to SecurityOpsDB
        │
        ▼
Retrieve Incidents
        │
        ▼
Process Each Incident
        │
        ▼
Read Severity
        │
        ▼
Determine Response
        │
        ▼
Update Incident Status
        │
        ▼
Insert Automation Log
        │
        ▼
Commit Changes
```

Python therefore acted as the decision and automation layer between the security incident data and the database.

## 📸 Evidence — Python Security Automation

![Python Security Automation](../images/phase8-python-automation.png)

This evidence documents the Python automation used to process PostgreSQL security incidents.

**Result:** ✅ Python successfully integrated with the security operations database.

---

# 🚦 Severity-Based Response Logic

The automation evaluated incident severity and selected a predefined response.

The final logic was:

```text
Incident
   │
   ▼
Severity
   │
   ├──── High
   │       │
   │       ▼
   │  IMMEDIATE REVIEW
   │       │
   │       ▼
   │   Escalated
   │
   ├──── Medium
   │       │
   │       ▼
   │  STANDARD REVIEW
   │       │
   │       ▼
   │    Reviewed
   │
   └──── Low
           │
           ▼
      STANDARD REVIEW
           │
           ▼
        Reviewed
```

This demonstrated basic security orchestration logic.

### High Severity

High-severity incidents required additional analyst attention.

```text
High → Escalated
```

### Medium Severity

Medium-severity incidents followed the standard review workflow.

```text
Medium → Reviewed
```

### Low Severity

Low-severity incidents could also be routed into the standard review workflow.

```text
Low → Reviewed
```

The automation assisted the analyst by consistently applying predefined decision logic.

---

# ⚙️ Automation Processing

The Python script retrieved incident records and processed them individually.

For each incident, the automation performed:

1. Retrieve incident data
2. Read severity
3. Determine response action
4. Update incident status
5. Create automation-log entry
6. Continue to the next incident

The processing workflow was:

```text
PostgreSQL Incident
        │
        ▼
Python Processing
        │
        ▼
Severity Evaluation
        │
        ▼
Automated Response
        │
        ▼
Database UPDATE
        │
        ▼
Automation Audit Log
```

## 📸 Evidence — Python Automation Processing

![Python Automation Processing](../images/phase8-python-automation-processing.png)

This evidence demonstrates the Python script processing security incidents according to their severity.

**Result:** ✅ Incident records successfully processed by the automation.

---

# 📝 Automation Audit Logging

Automated security actions should be auditable.

Phase 8 therefore recorded the actions performed by Python in an automation audit log.

The audit record provided evidence that an automated decision occurred.

Conceptually:

```text
Incident
    │
    ▼
Automated Decision
    │
    ▼
Database Update
    │
    ▼
Automation Log Entry
```

This is important because an analyst should be able to determine:

- What action occurred
- Which incident was affected
- Why the automation selected the action
- Whether the database was changed

## 📸 Evidence — Automation Audit Log

![Python Automation Audit Log](../images/phase8-python-automation-audit-log.png)

**Result:** ✅ Automated actions successfully recorded for auditability.

---

# ✅ Incident Status Validation

After running the automation, the incident table was queried again.

The expected state transition was:

```text
BEFORE
──────

SSH Brute Force
High
Investigated

Network Reconnaissance
Medium
Investigated
```

After automation:

```text
AFTER
─────

SSH Brute Force
High
Escalated

Network Reconnaissance
Medium
Reviewed
```

This demonstrated that the Python script did not simply display decisions.

It actually modified the PostgreSQL incident records.

## 📸 Evidence — Incident Status Automation Verified

![Incident Status Automation Verified](../images/phase8-incident-status-automation-verified.png)

**Result:** ✅ Automated incident-status modifications successfully verified.

---

# 📊 Python PostgreSQL Reporting

Python was also used to retrieve and display structured security information from PostgreSQL.

This demonstrated that Python could function as both:

- An automation engine
- A reporting interface

The reporting workflow was:

```text
SecurityOpsDB
      │
      ▼
Python Query
      │
      ▼
Incident Data
      │
      ▼
Structured Output
```

## 📸 Evidence — Python PostgreSQL Report

![Python PostgreSQL Report](../images/phase8-python-postgresql-report.png)

**Result:** ✅ Python successfully generated security information from PostgreSQL records.

---

# 🔄 End-to-End Validation

The complete Phase 8 automation pipeline was validated from beginning to end.

```text
Security Incident
       │
       ▼
SecurityOpsDB
       │
       ▼
Python Retrieval
       │
       ▼
Severity Evaluation
       │
       ▼
Automated Decision
       │
       ▼
Incident UPDATE
       │
       ▼
Automation Log INSERT
       │
       ▼
Database Query
       │
       ▼
Final Validation
```

The final validation confirmed that:

- Incident records existed
- Python retrieved the records
- Severity was evaluated
- Correct actions were selected
- Incident statuses changed
- Audit records were generated
- Database changes were independently verified

## 📸 Evidence — End-to-End Automation Validation

![End-to-End Automation Validation](../images/phase8-automation-validation.png)

**Result:** ✅ Complete database-driven security automation workflow validated.

---

# 💻 Commands Used

The following commands were used during Phase 8 development and validation.

## Python Syntax Validation

Before executing the script against PostgreSQL:

```bash
python3 -m py_compile securityops_automation.py
```

No output indicated successful Python compilation.

This validated Python syntax but did not prove the automation logic was correct.

```text
Valid Syntax ≠ Correct Logic
```

---

## Copy Automation Script

During troubleshooting, the script was copied to `/tmp`:

```bash
sudo cp securityops_automation.py /tmp/securityops_automation.py
```

---

## Set Script Permissions

```bash
sudo chmod 644 /tmp/securityops_automation.py
```

This provided the required read permissions while maintaining controlled file access.

---

## Execute Under PostgreSQL OS Account

The script was executed under the PostgreSQL operating-system account:

```bash
sudo -u postgres python3 /tmp/securityops_automation.py
```

This allowed the script to operate using the required PostgreSQL execution context.

---

## PostgreSQL Incident Query

The incident records were queried before and after automation.

Conceptually:

```sql
SELECT * FROM incidents;
```

The actual database schema was verified during the project rather than assuming field names.

---

## Automation Log Validation

The automation log was queried after Python execution to confirm that actions were recorded.

Conceptually:

```sql
SELECT * FROM automation_log;
```

The final database queries provided independent confirmation that the automation produced the expected changes.

---

# 🔧 Troubleshooting

Phase 8 included several important troubleshooting scenarios involving Python, PostgreSQL, Linux permissions, and automation logic. :contentReference[oaicite:1]{index=1}

## Python Syntax Validation

The script was first checked using:

```bash
python3 -m py_compile securityops_automation.py
```

Successful compilation demonstrated that the Python syntax was valid.

However:

```text
Successful Compilation
        ≠
Correct Automation Logic
```

The database behavior still needed to be tested.

---

## Python Indentation and Processing Logic

During development, Python indentation affected where database operations occurred inside the incident-processing loop.

The final structure ensured that **each incident independently performed**:

1. Severity evaluation
2. Incident status update
3. Automation-log insertion

This reinforced an important Python principle:

> Indentation controls program behavior, not simply visual formatting.

---

## PostgreSQL Column Name Validation

During database validation, an incorrect column was referenced:

```text
detect_by
```

PostgreSQL identified the actual column as:

```text
detected_by
```

After correcting the query, the incident records were returned successfully.

This demonstrated why database schemas should be verified instead of relying on assumed field names.

---

## Linux File Permissions and Execution Context

The automation initially required the correct execution context to access PostgreSQL.

The script was copied to `/tmp`:

```bash
sudo cp securityops_automation.py /tmp/securityops_automation.py
```

Permissions were set:

```bash
sudo chmod 644 /tmp/securityops_automation.py
```

The script was then executed as the PostgreSQL OS account:

```bash
sudo -u postgres python3 /tmp/securityops_automation.py
```

This demonstrated the relationship between:

- Linux permissions
- User context
- PostgreSQL authentication
- Application access

---

## Database State Reset During Testing

During repeated testing, incident statuses were reset to:

```text
Investigated
```

before rerunning the automation.

This established a known starting condition:

```text
Investigated
     │
     ├──── High ────► Escalated
     │
     └──── Medium ──► Reviewed
```

Testing from a known baseline made it easier to determine whether the automation produced the expected result.

---

# 🧪 Validation Methodology

Phase 8 validated automation at multiple layers.

```text
Python Source Code
       │
       ▼
Syntax Validation
       │
       ▼
Script Execution
       │
       ▼
Console Output
       │
       ▼
Incident Table
       │
       ▼
Automation Log
       │
       ▼
Final Database Query
```

A successful automation was **not** considered validated simply because the Python script finished without an error.

Validation confirmed:

1. The script executed.
2. Expected records were retrieved.
3. Correct severity decisions were made.
4. Intended database records changed.
5. Audit records were generated.
6. Final database state matched the expected result.

---

# 💡 Lessons Learned

## 1. Security Data Benefits From Structured Storage

PostgreSQL provided a structured method for storing security operations information.

This made security records easier to:

- Query
- Process
- Update
- Audit
- Automate

---

## 2. Python Can Automate Repetitive SOC Processing

Python retrieved security incidents directly from PostgreSQL and processed them according to predefined rules.

This reduced repetitive manual processing.

---

## 3. Severity Can Drive Automated Decisions

Phase 8 demonstrated:

```text
High
  │
  ▼
Escalated

Medium
  │
  ▼
Reviewed
```

This is a simple example of automated security triage.

---

## 4. High-Risk Events Should Preserve Human Oversight

Automation escalated high-severity events rather than attempting an uncontrolled high-impact response.

This keeps the analyst involved where additional investigation may be required.

---

## 5. Automated Actions Require an Audit Trail

An automation system should record what actions it performs.

Without an audit trail, it becomes difficult to:

- Validate automation
- Investigate mistakes
- Determine what changed
- Establish accountability

---

## 6. Successful Compilation Does Not Prove Correct Behavior

```text
python3 -m py_compile
```

only validates syntax.

It does not prove:

- Database connectivity
- Correct SQL
- Correct response logic
- Correct database updates

---

## 7. Python Indentation Directly Affects Automation Logic

Incorrect indentation can cause:

- Updates to occur outside loops
- Records to be skipped
- Audit entries to be created incorrectly
- Logic to run at the wrong time

---

## 8. Verify the Database Schema

The `detect_by` versus `detected_by` issue demonstrated that SQL queries should be based on the actual schema.

---

## 9. Error Messages Are Useful Troubleshooting Evidence

PostgreSQL's error message helped identify the incorrect column name.

Errors should be analyzed rather than treated simply as failures.

---

## 10. Linux Execution Context Matters

A script may have valid code but still fail because of:

- File permissions
- User permissions
- Database authentication
- Execution context

---

## 11. Test Automation From a Known State

Resetting incident status to:

```text
Investigated
```

created a predictable starting point.

That made it possible to compare:

```text
Expected Result
       vs.
Actual Result
```

---

## 12. Automation Must Be Independently Validated

The script's console output alone was not enough.

The database itself was queried afterward to verify the changes.

---

## 13. Automation Should Assist Analysts

The automation handled repetitive incident processing while preserving analyst involvement for higher-risk decisions.

---

## 14. Security Automation Should Be Deterministic

Given the same incident severity and starting state, the automation should produce the same expected result.

This improves reliability and testability.

---

## 15. Automation Is Only Valuable When It Can Be Audited

The key lesson from Phase 8 was:

> **Automation is only valuable when its actions can be verified and audited.**

---

# 🧠 Skills Demonstrated

| Skill | Application |
|---|---|
| **Security Automation** | Automated incident processing |
| **Python** | Developed response logic |
| **PostgreSQL** | Stored and queried security data |
| **SQL** | Retrieved and validated incident information |
| **psycopg** | Connected Python to PostgreSQL |
| **Incident Triage** | Used severity to determine response |
| **SOC Automation** | Automated repetitive analyst workflow |
| **Database Updates** | Modified incident status programmatically |
| **Audit Logging** | Recorded automated actions |
| **Linux Administration** | Managed permissions and execution context |
| **Troubleshooting** | Diagnosed Python, SQL, and permission issues |
| **Schema Validation** | Corrected database-field assumptions |
| **Testing** | Reset and retested known database states |
| **Validation** | Independently confirmed database changes |
| **Documentation** | Preserved automation evidence and lessons |

---

# 📸 Evidence Summary

Phase 8 contains **8 original screenshots** documenting the automation workflow. :contentReference[oaicite:2]{index=2}

| # | Evidence | Screenshot |
|---|---|---|
| 1 | PostgreSQL Incident Records | `phase8-postgresql-incident-records.png` |
| 2 | SecurityOpsDB Incident Query | `phase8-securityops-incident-query.png` |
| 3 | Python Security Automation | `phase8-python-automation.png` |
| 4 | Python Automation Processing | `phase8-python-automation-processing.png` |
| 5 | Python Automation Audit Log | `phase8-python-automation-audit-log.png` |
| 6 | Incident Status Automation Verified | `phase8-incident-status-automation-verified.png` |
| 7 | Python PostgreSQL Report | `phase8-python-postgresql-report.png` |
| 8 | End-to-End Automation Validation | `phase8-automation-validation.png` |

Because this document is located inside:

```text
/docs/
```

the correct image path is:

```text
../images/<filename>
```

No Phase 8 screenshots need to be renamed or duplicated.

---

# 🏁 Phase Outcome

## ✅ Phase 8 Complete

Phase 8 successfully demonstrated a database-driven security automation and response workflow using PostgreSQL and Python.

Security incidents representing previously observed security activity were stored inside:

```text
SecurityOpsDB
```

Python retrieved those records and evaluated their severity.

The response logic produced:

```text
SSH Brute Force
     │
     ▼
High Severity
     │
     ▼
IMMEDIATE REVIEW
     │
     ▼
Escalated
```

and:

```text
Network Reconnaissance
     │
     ▼
Medium Severity
     │
     ▼
STANDARD REVIEW
     │
     ▼
Reviewed
```

The automation then:

```text
Security Incident
       │
       ▼
PostgreSQL
       │
       ▼
Python
       │
       ▼
Retrieve
       │
       ▼
Analyze
       │
       ▼
Decide
       │
       ▼
Update
       │
       ▼
Audit
       │
       ▼
Validate

       ✅
```

Final PostgreSQL queries confirmed both:

- Automated incident-status changes
- Audit records documenting those actions

The completed workflow was:

```text
Store → Query → Analyze → Decide → Update → Audit → Validate
```

Phase 8 extended the Enterprise Security Operations Lab beyond security monitoring and investigation by introducing **repeatable, deterministic, and auditable security-response automation**.

---

# ➡️ Next Phase

## Phase 09 — Threat Intelligence & IOC Correlation

Phase 9 expands the SOC workflow by introducing external threat intelligence and Indicator of Compromise analysis.

The next phase includes:

- External threat-intelligence data
- IPSum malicious-IP feed
- IOC processing
- Python IOC lookup
- Malicious-IP detection
- PostgreSQL integration
- Automatic incident creation
- Threat-intelligence attribution
- IOC correlation and validation

---

[← Phase 07](phase-07-vulnerability-management.md) | [🏠 Back to Main Project](../README.md) | [Phase 09 →](phase-09-threat-intelligence.md)

---

### Enterprise Security Operations Lab

**Security Automation • Python • PostgreSQL • SQL • Incident Triage • Audit Logging • SOC Workflow Automation**
