# 🤖 Phase 13 — Python Security Automation & Automated SOC Email Alerting

> **Objective:** Build a Python-based security automation workflow that processes security events, generates reports, integrates Wazuh with the Gmail API using OAuth 2.0, and automatically delivers SOC email notifications when qualifying Wazuh security events are detected.

[← Phase 12](phase-12-web-security.md) | [🏠 Main Project](../README.md) | [Phase 14 →](phase-14-end-to-end-soc-response.md)

---

## 📑 Table of Contents

- [Phase Summary](#-phase-summary)
- [Overview](#-overview)
- [Automation Architecture](#️-automation-architecture)
- [Phase Objectives](#-phase-objectives)
- [Security Event Dataset](#-security-event-dataset)
- [JSON Validation](#-json-validation)
- [Python Security Event Analysis](#-python-security-event-analysis)
- [Security Report Generation](#-security-report-generation)
- [CSV Export](#-csv-export)
- [Gmail API Integration](#-gmail-api-integration)
- [OAuth 2.0 Configuration](#-oauth-20-configuration)
- [Gmail Send Scope](#-gmail-send-scope)
- [Wazuh Email Integration](#-wazuh-email-integration)
- [Custom Wazuh Integration](#-custom-wazuh-integration)
- [Automated Alert Workflow](#-automated-alert-workflow)
- [End-to-End Validation](#-end-to-end-validation)
- [Commands and Configuration](#-commands-and-configuration)
- [Troubleshooting](#-troubleshooting)
- [Security Considerations](#-security-considerations)
- [Lessons Learned](#-lessons-learned)
- [Skills Demonstrated](#-skills-demonstrated)
- [Evidence Summary](#-evidence-summary)
- [VirtualBox Snapshot](#-virtualbox-snapshot)
- [Phase Outcome](#-phase-outcome)
- [Next Phase](#️-next-phase)

---

# 📊 Phase Summary

| Category | Details |
|---|---|
| **Status** | ✅ Complete |
| **Primary Language** | Python 3 |
| **Security Data Format** | JSON |
| **Reporting Format** | TXT / CSV |
| **SIEM** | Wazuh |
| **Wazuh Server** | SOC-Wazuh `10.10.10.102` |
| **Security Sources** | Wazuh / Suricata |
| **Email Provider** | Gmail |
| **Email Interface** | Gmail API |
| **Authentication** | OAuth 2.0 |
| **OAuth Scope** | `gmail.send` |
| **Wazuh Integration** | Custom Integration |
| **Alert Threshold** | Wazuh Level 5+ |
| **Python Environment** | Dedicated Virtual Environment |
| **Primary Skill** | Security Automation |
| **Final Validation** | Automated SOC Email Successfully Delivered |

---

# 📋 Overview

Phase 13 introduced **Python security automation and automated SOC email alerting** into the Enterprise Security Operations Lab.

Previous phases established:

- Endpoint monitoring
- Wazuh SIEM/XDR
- Suricata IDS
- Centralized logging
- Event correlation
- Vulnerability management
- Threat intelligence
- Incident response
- Web application security assessment

Phase 13 added an automated response layer.

The phase began with structured security-event processing using:

```text
JSON
  │
  ▼
Python
  │
  ├── Event Analysis
  ├── Severity Classification
  ├── Security Reporting
  └── CSV Export
```

The automation was then extended into Wazuh.

A custom integration connected qualifying Wazuh alerts to a Python script using the Gmail API.

The final workflow became:

```text
Security Event
      │
      ▼
Wazuh Detection
      │
      ▼
Wazuh Integratord
      │
      ▼
Custom Integration
      │
      ▼
Python Automation
      │
      ▼
Gmail API
      │
      ▼
OAuth 2.0
      │
      ▼
SOC Email Alert
```

The completed phase demonstrated how security telemetry can move from passive monitoring into automated SOC notification.

---

# 🏗️ Automation Architecture

The Phase 13 automation architecture was:

```text
                Security Events
                     │
          ┌──────────┴──────────┐
          │                     │
          ▼                     ▼
       Suricata               Wazuh
          │                     │
          └──────────┬──────────┘
                     │
                     ▼
               Wazuh Manager
              10.10.10.102
                     │
                     ▼
              Wazuh Integratord
                     │
                     ▼
          custom-phase13-email
                     │
                     ▼
          Python Email Automation
                     │
                     ▼
                 Gmail API
                     │
                     ▼
                  OAuth 2.0
                     │
                     ▼
             SOC Email Inbox
```

A separate Python analysis workflow was also created:

```text
security_events.json
        │
        ▼
analyze_events.py
        │
        ├── Count Events
        ├── Group by Source
        ├── Group by Severity
        ├── Display Events
        └── Identify Alerts
        │
        ▼
Security Report
        │
        ▼
export_csv.py
        │
        ▼
CSV Security Report
```

Together, these workflows demonstrated both:

```text
Security Data Analysis
          +
Automated SOC Notification
```

---

# 🎯 Phase Objectives

- [x] Create structured security-event data
- [x] Store security events in JSON
- [x] Validate JSON syntax
- [x] Build a Python security-event analyzer
- [x] Count events by security source
- [x] Count events by severity
- [x] Display individual event information
- [x] Identify high-priority events
- [x] Generate a security report
- [x] Export security-event data to CSV
- [x] Configure Gmail API access
- [x] Configure OAuth 2.0
- [x] Apply least-privilege Gmail permissions
- [x] Use the `gmail.send` scope
- [x] Complete OAuth authorization
- [x] Validate Gmail API email delivery
- [x] Create a dedicated Python environment
- [x] Protect the OAuth token
- [x] Create a custom Wazuh integration
- [x] Configure Wazuh Integratord
- [x] Trigger Python automation from Wazuh
- [x] Generate an automated SOC email
- [x] Validate end-to-end alert delivery
- [x] Document troubleshooting and lessons learned

---

# 📁 Security Event Dataset

A structured JSON dataset was created:

```text
security_events.json
```

The dataset contained five sample security events representing telemetry from:

```text
Suricata
Wazuh
```

The dataset provided structured fields that could be consumed by Python rather than manually reviewing individual logs.

The processing workflow was:

```text
Security Events
      │
      ▼
security_events.json
      │
      ▼
Python
      │
      ▼
Analysis
```

Using JSON provided a structured method for passing security information between systems and automation scripts.

---

# ✅ JSON Validation

Before processing the security-event dataset, the JSON structure was validated.

This was important because malformed JSON would prevent Python from correctly parsing the event data.

The validation workflow was:

```text
Create JSON
    │
    ▼
Validate Syntax
    │
    ▼
Load into Python
    │
    ▼
Process Events
```

## 📸 Evidence — JSON Validation

![Phase 13 JSON Validation](../images/phase13-json-validation.png)

**Result:** ✅ Security-event JSON successfully validated.

---

# 🐍 Python Security Event Analysis

The primary analysis script was:

```text
analyze_events.py
```

The script processed the events stored in:

```text
security_events.json
```

The automation analyzed:

- Event source
- Severity
- Timestamp
- Event information
- High-priority security events

The script generated counts by source and severity and displayed individual event information.

The workflow was:

```text
security_events.json
        │
        ▼
analyze_events.py
        │
        ├── Parse JSON
        ├── Count Sources
        ├── Count Severities
        ├── Process Timestamps
        ├── Display Events
        └── Identify Alerts
```

This reduced the need to manually count and categorize security events.

## 📸 Evidence — Python Security Event Analysis

![Phase 13 Python Security Event Analysis](../images/phase13-python-security-event-analysis.png)

**Result:** ✅ Python successfully processed and categorized the security events.

---

# 📄 Security Report Generation

The Python analysis was extended to generate a security report.

The report file was:

```text
phase13-security-report.txt
```

The report summarized the analyzed security-event information in a format that could be reviewed independently of the Python script.

The workflow became:

```text
JSON Events
    │
    ▼
Python Analysis
    │
    ▼
Security Report
```

This demonstrated how automated security analysis can generate analyst-readable output.

## 📸 Evidence — Security Report

![Phase 13 Security Report](../images/phase13-security-report.png)

**Result:** ✅ Security report successfully generated.

---

# 📊 CSV Export

A second Python script was created:

```text
export_csv.py
```

The script exported structured security-event information into:

```text
phase13-security-events.csv
```

CSV provides a format that can be used by:

- Spreadsheet applications
- Reporting systems
- Additional Python scripts
- Data-analysis platforms
- Security reporting workflows

The automation path became:

```text
security_events.json
        │
        ▼
export_csv.py
        │
        ▼
phase13-security-events.csv
```

## 📸 Evidence — CSV Security Report

![Phase 13 CSV Security Report](../images/phase13-csv-security-report.png)

**Result:** ✅ Security events successfully exported to CSV.

---

# 📧 Gmail API Integration

The next stage extended the automation from local analysis into automated email notification.

Instead of using a traditional Gmail application password, Phase 13 used:

```text
Gmail API
    +
OAuth 2.0
```

A Google Cloud project was configured for the integration:

```text
SOC Security Automation
```

The Gmail API was enabled for the project.

## 📸 Evidence — Gmail API Enabled

![Phase 13 Gmail API Enabled](../images/phase13-gmail-api-enabled.png)

This provided the API interface used by the Python automation.

**Result:** ✅ Gmail API enabled.

---

# 🔐 OAuth 2.0 Configuration

OAuth 2.0 was used to authorize the Python automation.

The authorization model avoided storing the Gmail account password inside the Python script.

The workflow was:

```text
Python Script
     │
     ▼
OAuth 2.0
     │
     ▼
Google Authorization
     │
     ▼
Access Token
     │
     ▼
Gmail API
```

The OAuth consent configuration was set up for the security automation project.

During testing, the authorization flow used:

```python
flow.run_local_server(port=0)
```

This opened a local authorization workflow and returned credentials to the Python application after successful authentication.

A test user was added to the OAuth configuration to permit authorization while the application remained in testing mode.

---

# 🔑 Gmail Send Scope

The automation was configured with the least-privilege Gmail scope required for the project:

```text
gmail.send
```

The automation did not require broad mailbox access.

The permission model was:

```text
Automation Requirement
        │
        ▼
Send Security Email
        │
        ▼
gmail.send
```

## 📸 Evidence — Gmail OAuth Send Scope

![Phase 13 Gmail OAuth Send Scope](../images/phase13-gmail-oauth-send-scope.png)

This demonstrated the principle of least privilege.

**Result:** ✅ OAuth scope limited to email sending.

---

# 🧪 Gmail API Alert Test

Before connecting the email automation directly to Wazuh, Gmail API delivery was tested independently.

This separated:

```text
Email/API Problem
```

from:

```text
Wazuh Integration Problem
```

The test validated:

```text
Python
   │
   ▼
OAuth Credentials
   │
   ▼
Gmail API
   │
   ▼
Email Delivery
```

## 📸 Evidence — Gmail API Alert Success

![Phase 13 Gmail API Alert Success](../images/phase13-gmail-api-alert-success.png)

**Result:** ✅ Python successfully sent a security email using Gmail API.

---

# 📬 Security Alert Received

The test message was verified in the destination mailbox.

## 📸 Evidence — Gmail Security Alert Received

![Phase 13 Gmail Security Alert Received](../images/phase13-gmail-security-alert-received.png)

This proved that:

- OAuth authentication worked
- Gmail API access worked
- Python could construct the message
- Gmail accepted the request
- The destination mailbox received the security notification

---

# 🔗 Wazuh Email Integration

After validating Gmail API delivery independently, the Python automation was connected to Wazuh.

The integration directory included:

```text
/var/ossec/integrations/phase13-email/
```

The environment contained the Python Gmail automation and OAuth credentials required for sending alerts.

Important components included:

```text
gmail_api_alert.py
token.json
venv/
```

The OAuth token was protected because it provides authorization to the Gmail API.

A dedicated Python environment was also used for the integration.

The final integration path was:

```text
Wazuh
   │
   ▼
Integratord
   │
   ▼
Custom Executable
   │
   ▼
Python
   │
   ▼
Gmail API
```

---

# ⚙️ Custom Wazuh Integration

A custom Wazuh executable was configured:

```text
/var/ossec/integrations/custom-phase13-email
```

The custom integration acted as the connection between:

```text
Wazuh Integratord
```

and:

```text
Python Email Automation
```

The integration was configured in:

```text
/var/ossec/etc/ossec.conf
```

The configuration allowed qualifying Wazuh alerts to invoke the custom email integration.

The alert threshold was configured for:

```text
Level 5+
```

and JSON alert data was passed into the integration workflow.

Conceptually:

```xml
<integration>
  <name>custom-phase13-email</name>
  <level>5</level>
  <alert_format>json</alert_format>
</integration>
```

The integration workflow was:

```text
Wazuh Alert
    │
    ▼
Alert Level Check
    │
    ▼
Integratord
    │
    ▼
custom-phase13-email
    │
    ▼
Python Script
```

---

# 🔔 Automated Alert Workflow

Once the custom integration was operational, the full pipeline became:

```text
Security Event
      │
      ▼
Wazuh Detection
      │
      ▼
Alert Level Evaluation
      │
      ▼
Wazuh Integratord
      │
      ▼
custom-phase13-email
      │
      ▼
gmail_api_alert.py
      │
      ▼
OAuth Token
      │
      ▼
Gmail API
      │
      ▼
SOC Security Email
```

This transformed Wazuh from a system that required an analyst to manually inspect the dashboard into one capable of automatically notifying the SOC through email.

---

# 📬 Automated SOC Email Alert

A qualifying event was used to validate automated alert delivery.

The resulting message included live security-alert information such as:

- Severity
- Source
- Event description
- Source IP when available
- Destination IP when available
- Phase identification

## 📸 Evidence — Automated SOC Email Alert Delivery

![Phase 13 Automated SOC Email Alert Delivery](../images/phase13-automated-soc-email-alert-delivery.png)

This evidence demonstrates successful automated SOC notification delivery.

---

# 📩 SOC Email Alert Received

The resulting alert was also verified from the receiving mailbox.

## 📸 Evidence — SOC Email Alert Received

![Phase 13 SOC Email Alert Received](../images/phase13-soc-email-alert-received.png)

**Result:** ✅ Automated security notification successfully received.

---

# 🔄 End-to-End Validation

The final Phase 13 validation demonstrated the complete automation pipeline.

```text
Security Event
      │
      ▼
Wazuh
      │
      ▼
Security Detection
      │
      ▼
Wazuh Integratord
      │
      ▼
custom-phase13-email
      │
      ▼
Python Automation
      │
      ▼
Gmail API
      │
      ▼
OAuth 2.0
      │
      ▼
SOC Email Alert

      ✅
```

This demonstrated that the components were not merely working independently.

They were functioning as one integrated security automation pipeline.

---

# 💻 Commands and Configuration

Phase 13 involved Python, Linux, Wazuh, OAuth, and Gmail API configuration.

## JSON Event File

```text
security_events.json
```

Purpose:

```text
Store structured Suricata and Wazuh security events
for automated Python processing.
```

---

## Python Analysis Script

```text
analyze_events.py
```

Purpose:

```text
Parse security events, count events by source and
severity, process timestamps, display event details,
and identify security alerts.
```

---

## CSV Export Script

```text
export_csv.py
```

Purpose:

```text
Export security-event data into a structured CSV
report.
```

---

## Security Report

```text
phase13-security-report.txt
```

---

## CSV Report

```text
phase13-security-events.csv
```

---

## Wazuh Integration Directory

```bash
/var/ossec/integrations/phase13-email/
```

The integration directory contained components including:

```text
gmail_api_alert.py
token.json
venv/
```

---

## Custom Wazuh Integration

```bash
/var/ossec/integrations/custom-phase13-email
```

The custom executable was given the required execution permissions so Wazuh Integratord could invoke it.

---

## Wazuh Configuration

The integration was configured in:

```bash
/var/ossec/etc/ossec.conf
```

Conceptual configuration:

```xml
<integration>
  <name>custom-phase13-email</name>
  <level>5</level>
  <alert_format>json</alert_format>
</integration>
```

---

## OAuth Authorization

The local OAuth flow used:

```python
flow.run_local_server(port=0)
```

The browser-based authorization flow generated the credentials required by the automation.

---

# 🔧 Troubleshooting

Phase 13 involved troubleshooting across several independent technologies.

This made it one of the most technically involved phases of the project.

---

## 1. Python Formatting and Logic

During development, Python formatting and f-string issues were corrected.

The script was retested after each correction.

The process reinforced:

```text
Write
  │
  ▼
Execute
  │
  ▼
Read Error
  │
  ▼
Correct
  │
  ▼
Retest
```

---

## 2. OAuth 403 Access Denied

The initial OAuth authorization attempt returned an access-denied response.

The issue was resolved by adding the Gmail account as an authorized test user in the OAuth consent configuration.

The troubleshooting path was:

```text
OAuth Request
     │
     ▼
403 Access Denied
     │
     ▼
Review Consent Configuration
     │
     ▼
Add Test User
     │
     ▼
Retry Authentication
     │
     ▼
Authorization Successful
```

---

## 3. OAuth Credential Handling

During early testing, an authentication-flow issue occurred around credential initialization.

The OAuth flow and credential handling were corrected before continuing.

This reinforced the importance of testing the API independently before adding Wazuh to the workflow.

---

## 4. Integration Permissions

At one point the Wazuh integration produced no visible output.

Permissions and executable status were checked.

The integration required the correct Linux execution permissions so Wazuh could invoke the script.

The troubleshooting process was:

```text
Wazuh Alert
    │
    ▼
Integration Called?
    │
    ▼
Executable?
    │
    ▼
Permissions Correct?
    │
    ▼
Python Environment Available?
    │
    ▼
OAuth Token Accessible?
    │
    ▼
Gmail API Request
```

After correcting the execution environment and permissions, validation passed.

---

## 5. Test Components Independently

A major troubleshooting improvement was separating the system into layers.

```text
Layer 1
JSON
   │
   ▼
Layer 2
Python
   │
   ▼
Layer 3
Gmail API
   │
   ▼
Layer 4
OAuth
   │
   ▼
Layer 5
Wazuh Integration
   │
   ▼
Layer 6
End-to-End Alert
```

Each component was validated independently before testing the complete pipeline.

This made it easier to identify which layer was responsible for a failure.

---

# 🔐 Security Considerations

The email automation was implemented with several security considerations.

## Least Privilege

The Gmail API scope was restricted to:

```text
gmail.send
```

rather than granting broad mailbox access.

---

## OAuth Instead of Password Storage

The automation used:

```text
OAuth 2.0
```

rather than embedding a Gmail account password in the Python script.

---

## Token Protection

The OAuth token stored under the Wazuh integration environment was treated as a protected credential.

```text
token.json
```

should not be published to GitHub.

---

## Git Repository Protection

Credential files should be excluded from source control.

For example:

```gitignore
token.json
credentials.json
*.secret
```

The portfolio should demonstrate the integration without exposing authentication credentials.

---

## Dedicated Python Environment

A dedicated Python environment reduced dependency conflicts and separated the automation dependencies from the system Python environment.

---

# 💡 Lessons Learned

## 1. JSON and Python Serve Different Roles

JSON stored structured security data.

Python processed and acted on that data.

```text
JSON
 │
 └── Data

Python
 │
 └── Logic / Automation
```

---

## 2. Automation Reduces Manual SOC Work

Instead of manually reviewing every event, Python can:

- Parse events
- Categorize them
- Count them
- Identify important events
- Generate reports
- Trigger notifications

---

## 3. APIs Connect Independent Systems

The Gmail API allowed the Python security automation to communicate with Gmail programmatically.

```text
Python
   │
   ▼
API
   │
   ▼
Gmail
```

---

## 4. OAuth Is Authorization, Not the Email Service

The Gmail API performs the email operation.

OAuth 2.0 controls whether the application is authorized to perform that operation.

```text
OAuth
  │
  └── Permission

Gmail API
  │
  └── Action
```

---

## 5. Least Privilege Applies to APIs

The automation required the ability to send mail.

It did not require full access to the mailbox.

Therefore:

```text
gmail.send
```

was the appropriate scope.

---

## 6. Test Integrations in Layers

The most effective development process was:

```text
Test JSON
    ↓
Test Python
    ↓
Test Gmail API
    ↓
Test OAuth
    ↓
Test Wazuh Integration
    ↓
Test Full Pipeline
```

Testing everything simultaneously would have made troubleshooting much harder.

---

## 7. Linux Permissions Matter in Automation

A script that works manually may still fail when executed by another service.

Execution context and permissions must be validated.

---

## 8. Successful Manual Execution Does Not Prove Automation

Manually running the email script demonstrated that Python and Gmail worked.

It did not prove Wazuh could automatically invoke the integration.

Both tests were necessary.

---

## 9. Successful Wazuh Detection Does Not Prove Email Delivery

Likewise:

```text
Wazuh Alert Generated
        ≠
Email Delivered
```

The entire chain had to be validated.

---

## 10. End-to-End Testing Is Critical

The strongest evidence was the final result:

```text
Security Event
      ↓
Wazuh
      ↓
Integration
      ↓
Python
      ↓
Gmail API
      ↓
SOC Inbox
```

Each layer contributed to the successful automation.

---

## 11. Credentials Should Never Be Stored in Portfolio Code

OAuth tokens and client credentials should remain protected and excluded from public repositories.

A portfolio should demonstrate architecture and implementation without exposing secrets.

---

## 12. Security Automation Still Requires Human Investigation

The email alert improves response time, but it does not replace analyst judgment.

The automated workflow:

```text
Detects
   ↓
Notifies
```

The analyst still:

```text
Validates
   ↓
Investigates
   ↓
Responds
```

---

# 🧠 Skills Demonstrated

| Skill | Application |
|---|---|
| **Python** | Built security-event automation |
| **JSON** | Structured security-event data |
| **CSV** | Exported security reporting data |
| **Security Automation** | Automated event processing and notification |
| **Wazuh** | Integrated SIEM alerts with custom automation |
| **Wazuh Integratord** | Triggered external security workflow |
| **Linux** | Configured scripts, directories, and permissions |
| **Gmail API** | Sent programmatic security notifications |
| **OAuth 2.0** | Implemented delegated API authorization |
| **Least Privilege** | Limited API scope to `gmail.send` |
| **API Integration** | Connected Python with Gmail |
| **Virtual Environments** | Isolated Python dependencies |
| **Credential Security** | Protected OAuth tokens |
| **Alert Engineering** | Converted Wazuh events into SOC notifications |
| **Troubleshooting** | Diagnosed Python, OAuth, permissions, and integration issues |
| **End-to-End Testing** | Validated complete automated workflow |
| **SOC Operations** | Improved alert visibility and response workflow |

---

# 📸 Evidence Summary

The Phase 13 screenshots already stored in the repository include:

| # | Evidence | Screenshot |
|---|---|---|
| 1 | JSON Validation | `phase13-json-validation.png` |
| 2 | Python Security Event Analysis | `phase13-python-security-event-analysis.png` |
| 3 | Security Report | `phase13-security-report.png` |
| 4 | CSV Security Report | `phase13-csv-security-report.png` |
| 5 | Gmail API Enabled | `phase13-gmail-api-enabled.png` |
| 6 | Gmail OAuth Send Scope | `phase13-gmail-oauth-send-scope.png` |
| 7 | Gmail API Alert Success | `phase13-gmail-api-alert-success.png` |
| 8 | Gmail Security Alert Received | `phase13-gmail-security-alert-received.png` |
| 9 | Automated SOC Email Alert Delivery | `phase13-automated-soc-email-alert-delivery.png` |
| 10 | SOC Email Alert Received | `phase13-soc-email-alert-received.png` |

Because this document is stored under:

```text
docs/
```

the correct image path is:

```text
../images/<filename>
```

For example:

```markdown
![Phase 13 Automated SOC Alert](../images/phase13-automated-soc-email-alert-delivery.png)
```

No existing screenshot needs to be renamed.

---

# 💾 VirtualBox Snapshot

Phase 13 changed the Wazuh environment significantly because the custom email integration, Python environment, OAuth token, and Wazuh configuration were installed there.

The completed state should be preserved on:

```text
SOC-Wazuh
```

## Snapshot Name

```text
Phase 13 - Automated SOC Email Alerting Complete
```

## Snapshot Description

```text
Phase 13 completed.

Implemented Python security automation and automated
SOC email notification.

Completed:
- JSON security-event processing
- Python event analysis
- Security report generation
- CSV export
- Gmail API configuration
- OAuth 2.0 authorization
- gmail.send least-privilege scope
- Dedicated Python email environment
- Protected OAuth token
- Custom Wazuh email integration
- Wazuh Integratord configuration
- Level 5+ JSON alert integration
- Automated Gmail API security notification
- End-to-end SOC email alert validation

Validated pipeline:

Security Event
→ Wazuh Detection
→ Wazuh Integratord
→ custom-phase13-email
→ Python Automation
→ Gmail API / OAuth 2.0
→ SOC Email Alert
```

> The VirtualBox snapshot is a VM recovery checkpoint and does not need to exist as a PNG inside the GitHub `images` folder unless a separate screenshot of the VirtualBox snapshot was intentionally captured.

---

# 🏁 Phase Outcome

## ✅ Phase 13 Complete

Phase 13 successfully transformed the Enterprise Security Operations Lab from a primarily monitoring-focused environment into an environment capable of **automated security-event processing and SOC notification**.

The first automation workflow demonstrated:

```text
Security Events
      │
      ▼
JSON
      │
      ▼
Python
      │
      ├── Analysis
      ├── Classification
      ├── Reporting
      └── CSV Export
```

The second workflow integrated the automation directly with Wazuh:

```text
Security Event
      │
      ▼
Wazuh Detection
      │
      ▼
Wazuh Integratord
      │
      ▼
custom-phase13-email
      │
      ▼
Python Automation
      │
      ▼
Gmail API
      │
      ▼
OAuth 2.0
      │
      ▼
SOC Email Alert

      ✅
```

The final automated email contained live alert fields from the Wazuh integration, proving that the notification pipeline operated end to end.

Phase 13 demonstrated:

- Structured security-event processing
- Python security automation
- JSON parsing
- Automated reporting
- CSV export
- API integration
- OAuth 2.0 authorization
- Least-privilege API permissions
- Wazuh custom integrations
- Linux permissions management
- Automated SOC notification
- Credential protection
- End-to-end security workflow validation

The completed workflow was:

**Detect → Process → Analyze → Integrate → Notify → Validate**

This automation prepared the lab for the final phase, where the previously built security controls are combined into a complete SOC incident-detection and response workflow.

---

# ➡️ Next Phase

## Phase 14 — End-to-End SOC Incident Detection, Correlation & Response

Phase 14 combines the major components developed throughout the project.

The final workflow includes:

- Controlled reconnaissance
- Controlled SSH authentication failures
- Suricata detection
- Wazuh detection
- Level 10 correlation
- MITRE ATT&CK mapping
- Automated SOC notification capability
- DFIR-IRIS case management
- Asset and IOC documentation
- Incident timeline
- Investigation tasks
- Containment and remediation assessment
- Formal incident closure

The final phase demonstrates the complete SOC lifecycle:

```text
Generate
   ↓
Detect
   ↓
Correlate
   ↓
Notify
   ↓
Investigate
   ↓
Respond
   ↓
Document
   ↓
Close
```

---

[← Phase 12](phase-12-web-security.md) | [🏠 Back to Main Project](../README.md) | [Phase 14 →](phase-14-end-to-end-soc-response.md)

---

### Enterprise Security Operations Lab

**Python • JSON • Wazuh • Security Automation • Gmail API • OAuth 2.0 • Automated SOC Alerting**
