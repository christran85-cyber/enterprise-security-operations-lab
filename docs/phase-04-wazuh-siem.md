# 🛡️ Phase 04 — Wazuh SIEM/XDR

> **Objective:** Validate centralized SIEM/XDR monitoring with Wazuh by investigating Windows and Linux security events, analyzing detection rules and severity, mapping activity to MITRE ATT&CK, and validating File Integrity Monitoring.

[← Phase 03](phase-03-endpoint-monitoring.md) | [🏠 Main Project](../README.md) | [Phase 05 →](phase-05-suricata-ids.md)

---

## 📑 Table of Contents

- [Phase Summary](#-phase-summary)
- [Overview](#-overview)
- [SIEM Architecture](#️-siem-architecture)
- [Phase Objectives](#-phase-objectives)
- [Wazuh Platform Validation](#️-wazuh-platform-validation)
- [Connected Agents](#-connected-agents)
- [Ubuntu Authentication Investigation](#-ubuntu-authentication-investigation)
- [MITRE ATT&CK Analysis](#-mitre-attck-analysis)
- [Windows Process Investigation](#-windows-process-investigation)
- [File Integrity Monitoring](#-file-integrity-monitoring)
- [Event Correlation](#-event-correlation)
- [Commands Used](#-commands-used)
- [Validation](#-validation)
- [Troubleshooting](#-troubleshooting)
- [Lessons Learned](#-lessons-learned)
- [Skills Demonstrated](#-skills-demonstrated)
- [Evidence Summary](#-evidence-summary)
- [Phase Outcome](#-phase-outcome)

---

# 📊 Phase Summary

| Category | Details |
|---|---|
| **Status** | ✅ Complete |
| **Platform** | Wazuh SIEM/XDR |
| **Wazuh Server** | SOC-Wazuh |
| **Manager IP** | `10.10.10.102` |
| **Windows Agent** | SOC-Windows11 |
| **Linux Agent** | soc-ubuntu |
| **Authentication Detection** | Rule `5503` — Level `5` |
| **Windows Process Detection** | Rule `67027` |
| **FIM Detection** | Rule `554` |
| **Framework** | MITRE ATT&CK |
| **Focus** | Centralized detection, investigation & correlation |
| **Next Phase** | Suricata IDS/IPS |

---

# 📋 Overview

Phase 4 moved the lab from basic endpoint telemetry collection into centralized **Security Information and Event Management (SIEM)** and **Extended Detection and Response (XDR)** operations.

The endpoint monitoring configured in Phase 3 provided telemetry from:

```text
SOC-Windows11
      +
SOC-Ubuntu
      │
      ▼
Wazuh Agents
      │
      ▼
SOC-Wazuh
```

Phase 4 focused on analyzing that telemetry from a SOC analyst perspective.

The work included:

- Wazuh platform validation
- Agent connectivity validation
- Centralized Windows monitoring
- Centralized Linux monitoring
- Authentication-failure investigation
- Wazuh rule analysis
- Severity analysis
- MITRE ATT&CK mapping
- Windows process investigation
- File Integrity Monitoring
- File creation detection
- File modification detection
- Hash and metadata analysis
- Event correlation
- SIEM troubleshooting

The objective was not simply to confirm that events existed.

The objective was to follow a SOC workflow:

```text
Event
  ↓
Detection
  ↓
Alert
  ↓
Investigate
  ↓
Correlate
  ↓
Add Context
  ↓
Document Findings
```

---

# 🏗️ SIEM Architecture

```text
              SOC-Windows11
                    │
                    │
               Wazuh Agent
                    │
                    │
                    ▼
               ┌───────────┐
               │ SOC-Wazuh │
               │ SIEM/XDR  │
               └─────┬─────┘
                     ▲
                     │
                     │
               Wazuh Agent
                     │
                     │
                SOC-Ubuntu
                10.50.20.100
```

The complete telemetry path is:

```text
Endpoint Activity
       │
       ▼
Local Security Log
       │
       ▼
Wazuh Agent
       │
       ▼
Wazuh Manager
       │
       ▼
Decoder / Rule
       │
       ▼
Security Alert
       │
       ▼
Wazuh Dashboard
       │
       ▼
SOC Analyst
```

---

# 🎯 Phase Objectives

- [x] Validate Wazuh SIEM/XDR operation
- [x] Validate Wazuh Indexer
- [x] Validate Wazuh Manager
- [x] Validate Wazuh Dashboard
- [x] Validate Filebeat
- [x] Confirm Windows Agent connectivity
- [x] Confirm Ubuntu Agent connectivity
- [x] Investigate Linux authentication failures
- [x] Analyze Wazuh rules and severity
- [x] Review MITRE ATT&CK context
- [x] Investigate Windows process telemetry
- [x] Validate File Integrity Monitoring
- [x] Detect controlled file creation
- [x] Detect controlled file modification
- [x] Review FIM hashes and metadata
- [x] Correlate related security events
- [x] Troubleshoot Wazuh Dashboard connectivity

---

# ⚙️ Wazuh Platform Validation

Wazuh was deployed on the dedicated **SOC-Wazuh** virtual machine.

The platform provides the centralized security-monitoring layer for the lab.

Core components include:

```text
Wazuh Dashboard
      │
      ▼
Wazuh Manager
      │
      ▼
Wazuh Indexer
      ▲
      │
   Filebeat
```

The Wazuh Dashboard is accessible from:

```text
https://10.10.10.102
```

The environment uses a self-signed certificate.

---

## 📸 Evidence — Wazuh Dashboard

![Wazuh Dashboard](../images/phase4-dashboard.png)

The dashboard provides centralized visibility into endpoint alerts and security events.

**Result:** ✅ Wazuh Dashboard operational.

---

# 🔗 Connected Agents

Both monitored endpoints were successfully connected to Wazuh.

The Wazuh environment showed:

```text
Active:           2
Pending:          0
Disconnected:     0
Never Connected:  0
```

Connected endpoints:

```text
SOC-Windows11
      │
      └── ACTIVE

soc-ubuntu
      │
      └── ACTIVE
```

This validated the endpoint telemetry infrastructure established during Phase 3.

---

## 📸 Evidence — Connected Wazuh Agents

![Wazuh Connected Agents](../images/phase4-agents.png)

**Result:** ✅ Both monitored endpoints successfully connected to Wazuh.

---

# 🚨 Ubuntu Authentication Investigation

Controlled authentication failures from the Ubuntu endpoint were investigated through Wazuh.

The Linux endpoint:

```text
soc-ubuntu
10.50.20.100
```

generated authentication telemetry that was forwarded through the Wazuh Agent.

The resulting alert identified:

```text
Rule ID:     5503
Rule Level:  5
Description: PAM: User login failed
```

The detection path was:

```text
Authentication Failure
        │
        ▼
Linux PAM
        │
        ▼
Linux Security Log
        │
        ▼
Wazuh Agent
        │
        ▼
Wazuh Manager
        │
        ▼
Rule 5503
        │
        ▼
Level 5 Alert
        │
        ▼
SOC Investigation
```

This demonstrated that Wazuh could transform raw authentication telemetry into a security alert suitable for analyst investigation.

---

## Alert Analysis

The investigation included:

- Agent name
- Endpoint IP
- Rule ID
- Rule level
- Rule description
- Authentication information
- Event timestamp
- Associated security context

Instead of looking only at the alert title, the event was expanded to understand the underlying context.

---

# 🗺️ MITRE ATT&CK Analysis

Wazuh provides MITRE ATT&CK context for supported detections.

This allows the analyst to move from:

```text
What happened?
```

to:

```text
What type of adversary behavior could this activity represent?
```

The investigation process became:

```text
Raw Event
    │
    ▼
Wazuh Detection
    │
    ▼
Rule / Severity
    │
    ▼
MITRE ATT&CK Context
    │
    ▼
Analyst Interpretation
```

MITRE ATT&CK mapping does not automatically prove malicious intent.

Instead, it provides a standardized framework for understanding how detected behavior may relate to known adversary techniques.

---

# 🪟 Windows Process Investigation

Windows process telemetry generated during Phase 3 was investigated through Wazuh.

The Windows endpoint provides multiple telemetry sources:

```text
Windows Security Auditing
        +
Sysmon
        +
PowerShell Logging
        +
Wazuh Agent
```

A Windows process event was analyzed through Wazuh using:

```text
Rule 67027
```

The investigation focused on:

- Endpoint
- User
- Process
- Parent process
- Command line
- Event timestamp
- Wazuh rule
- Associated event context

This demonstrated the difference between:

```text
Collecting Logs
```

and:

```text
Investigating Security Telemetry
```

---

# 📁 File Integrity Monitoring

File Integrity Monitoring was validated using controlled file activity.

FIM allows Wazuh to monitor important files and directories for changes.

The controlled validation included:

```text
Create File
    │
    ▼
Wazuh FIM
    │
    ▼
Detect Change
    │
    ▼
Generate Alert
    │
    ▼
Modify File
    │
    ▼
Detect New Change
    │
    ▼
Compare Metadata / Hash
```

Wazuh successfully generated FIM telemetry for the controlled changes.

The investigation included:

- File path
- File event
- Modification information
- Hash information
- Metadata
- Rule information

The FIM alert was associated with:

```text
Rule ID: 554
```

This demonstrated that Wazuh could identify changes to monitored files rather than relying only on process or authentication telemetry.

---

# 🔗 Event Correlation

Individual alerts become more useful when they are examined together.

Phase 4 correlated multiple security-data sources:

```text
Authentication Activity
          +
Process Activity
          +
File Changes
          │
          ▼
      Wazuh SIEM
          │
          ▼
 Analyst Investigation
```

The analyst reviewed:

- Event timestamps
- Agent information
- Rule IDs
- Severity
- Event descriptions
- MITRE ATT&CK context
- Process information
- File information
- Related endpoint activity

This demonstrated a core SOC concept:

> A single event may provide limited context, while multiple related events can provide a clearer picture of endpoint activity.

---

# 💻 Commands Used

The following commands were used to validate and troubleshoot the Wazuh platform during Phase 4.

---

## 🛡️ Check Wazuh Indexer

```bash
sudo systemctl status wazuh-indexer
```

Expected:

```text
active (running)
```

The Wazuh Indexer stores and indexes security data used by the platform.

---

## ⚙️ Check Wazuh Manager

```bash
sudo systemctl status wazuh-manager
```

Expected:

```text
active (running)
```

The Wazuh Manager receives and analyzes security telemetry from connected agents.

---

## 🖥️ Check Wazuh Dashboard

```bash
sudo systemctl status wazuh-dashboard
```

Expected:

```text
active (running)
```

This verifies the web interface used by the SOC analyst.

---

## 📡 Check Filebeat

```bash
sudo systemctl status filebeat
```

Expected:

```text
active (running)
```

Filebeat participates in the Wazuh data pipeline.

---

## 🧪 Test Filebeat Output

```bash
sudo filebeat test output
```

The test validates:

```text
URL Parsing
     ↓
Host Parsing
     ↓
DNS Lookup
     ↓
TCP Connection
     ↓
TLS Handshake
     ↓
Server Communication
```

A successful result provides evidence that Filebeat can communicate with the configured indexer.

---

## 🌐 Check Wazuh API Port

```bash
sudo ss -lntp | grep 55000
```

Command breakdown:

```text
ss            Display network sockets
-l            Listening sockets
-n            Numeric addresses and ports
-t            TCP sockets
-p            Process information
grep 55000    Filter for Wazuh API port
```

The Wazuh API uses:

```text
TCP 55000
```

---

## 🔄 Restart Wazuh Dashboard

```bash
sudo systemctl restart wazuh-dashboard
```

Only the affected dashboard service was restarted instead of rebooting the entire Wazuh server.

---

## 📋 Command Reference

| Purpose | Command |
|---|---|
| Check Indexer | `sudo systemctl status wazuh-indexer` |
| Check Manager | `sudo systemctl status wazuh-manager` |
| Check Dashboard | `sudo systemctl status wazuh-dashboard` |
| Check Filebeat | `sudo systemctl status filebeat` |
| Test Filebeat output | `sudo filebeat test output` |
| Check API port | `sudo ss -lntp \| grep 55000` |
| Restart Dashboard | `sudo systemctl restart wazuh-dashboard` |

---

# 🧪 Validation

Phase 4 validated the complete centralized security-monitoring workflow.

---

## Endpoint Connectivity

Both monitored endpoints were active:

```text
SOC-Windows11 ───► Wazuh
                     ▲
                     │
soc-ubuntu ──────────┘

2 Active Agents
0 Disconnected
```

**Result:** ✅ Endpoint communication validated.

---

## Authentication Detection

Ubuntu authentication failures generated:

```text
Rule 5503
Level 5
PAM: User login failed
```

**Result:** ✅ Linux authentication detection validated.

---

## Windows Process Detection

Windows process activity was visible through Wazuh and associated with:

```text
Rule 67027
```

**Result:** ✅ Windows process investigation validated.

---

## File Integrity Monitoring

Controlled file creation and modification generated FIM telemetry associated with:

```text
Rule 554
```

**Result:** ✅ File Integrity Monitoring validated.

---

# 🚨 Wazuh Security Alerts

The Wazuh Security Events interface was used to review centralized endpoint detections.

This view allowed the analyst to:

- Review alert severity
- Identify the affected endpoint
- Review Wazuh rule information
- Examine timestamps
- Expand individual events
- Investigate event details
- Search related telemetry

---

## 📸 Evidence — Wazuh Security Alerts

![Wazuh Security Alerts](../images/phase4-alerts.png)

The security-alert view provided centralized visibility into endpoint detections and allowed individual events to be expanded for investigation.

**Result:** ✅ Security alerts successfully generated and investigated.

---

# 🔧 Troubleshooting

Phase 4 included significant Wazuh platform troubleshooting.

This was important because a SIEM contains multiple interconnected components.

A problem in the web interface does not automatically mean the entire SIEM is unavailable.

---

## Wazuh Dashboard Error

At one point, the Wazuh Dashboard displayed:

```text
Something went wrong.
```

Instead of reinstalling Wazuh, each platform component was checked independently.

### Check Indexer

```bash
sudo systemctl status wazuh-indexer
```

Result:

```text
active (running)
```

### Check Dashboard

```bash
sudo systemctl status wazuh-dashboard
```

Result:

```text
active (running)
```

### Check Manager

```bash
sudo systemctl status wazuh-manager
```

Result:

```text
active (running)
```

### Check Filebeat

```bash
sudo systemctl status filebeat
```

Result:

```text
active (running)
```

This demonstrated that the core Wazuh services were operational even though the web interface displayed an error.

---

## Filebeat Pipeline Validation

The next troubleshooting step was:

```bash
sudo filebeat test output
```

The test successfully validated:

- URL parsing
- Host parsing
- DNS lookup
- TCP connectivity
- TLS handshake
- Server communication

This provided evidence that the data pipeline could communicate with the indexer.

---

## API Port Validation

The Wazuh API port was checked using:

```bash
sudo ss -lntp | grep 55000
```

Port:

```text
55000
```

was listening.

This provided another layer of evidence that the Wazuh environment remained operational.

---

## Targeted Service Restart

Instead of rebooting the entire server, only the dashboard service was restarted:

```bash
sudo systemctl restart wazuh-dashboard
```

The dashboard recovered.

The endpoint page initially continued to display an error, but after waiting and retrying, the interface loaded and displayed both active agents.

---

## Troubleshooting Workflow

```text
Dashboard Error
      │
      ▼
Check Indexer
      │
      ▼
Check Manager
      │
      ▼
Check Dashboard
      │
      ▼
Check Filebeat
      │
      ▼
Test Data Pipeline
      │
      ▼
Check API Port
      │
      ▼
Restart Only Affected Service
      │
      ▼
Validate Again
```

This avoided unnecessary reinstallation of the security platform.

---

# 💡 Lessons Learned

## 1. A Dashboard Error Does Not Mean the Entire SIEM Failed

When the Wazuh Dashboard showed an error, the underlying services remained operational.

The correct response was to validate each component rather than immediately reinstall the platform.

---

## 2. Troubleshoot Complex Platforms by Component

Wazuh consists of multiple interconnected services.

```text
Dashboard
   +
Manager
   +
Indexer
   +
Filebeat
```

Each component should be checked independently.

---

## 3. Detection Requires Context

An alert by itself does not provide a complete investigation.

Useful context includes:

```text
Who?
What?
When?
Where?
Which endpoint?
Which rule?
What severity?
What process?
What file?
What MITRE technique?
What happened before and after?
```

---

## 4. MITRE ATT&CK Adds Context, Not Proof

MITRE ATT&CK mapping helps categorize behavior.

It does not automatically mean that every mapped event represents a real attack.

The analyst must still evaluate the activity in context.

---

## 5. File Integrity Monitoring Adds Another Detection Layer

Authentication, process monitoring, and FIM answer different security questions.

```text
Authentication
     │
     ▼
Who attempted access?


Process Monitoring
     │
     ▼
What executed?


File Integrity Monitoring
     │
     ▼
What file changed?
```

Combining these sources improves investigation quality.

---

## 6. Controlled Testing Proves Detection Capability

A configuration screen alone does not prove a detection capability works.

A stronger validation method is:

```text
Configure
    │
    ▼
Generate Controlled Activity
    │
    ▼
Detect
    │
    ▼
Investigate
    │
    ▼
Validate Evidence
```

---

## 7. Correlation Provides Better Context

Multiple related events provide a more complete view of endpoint activity than isolated alerts.

This is one of the primary benefits of centralized SIEM monitoring.

---

# 🧭 SOC Investigation Methodology

Phase 4 established a repeatable analyst workflow:

```text
Alert
  │
  ▼
Identify Endpoint
  │
  ▼
Review Rule
  │
  ▼
Review Severity
  │
  ▼
Inspect Raw Event
  │
  ▼
Review MITRE Context
  │
  ▼
Search Related Events
  │
  ▼
Correlate Activity
  │
  ▼
Document Findings
```

This methodology became the foundation for later incident-response phases.

---

# 🧠 Skills Demonstrated

| Skill | Application |
|---|---|
| **SIEM Administration** | Operated centralized Wazuh infrastructure |
| **XDR Monitoring** | Investigated endpoint security telemetry |
| **Linux Authentication Analysis** | Investigated PAM authentication failures |
| **Windows Event Analysis** | Investigated Windows process activity |
| **Detection Analysis** | Reviewed Wazuh rule IDs and severity |
| **MITRE ATT&CK** | Added standardized adversary-behavior context |
| **File Integrity Monitoring** | Detected controlled file changes |
| **Hash Analysis** | Reviewed file-change metadata and hashes |
| **Event Correlation** | Connected related endpoint activity |
| **SOC Investigation** | Followed alert-to-investigation workflow |
| **Linux Administration** | Validated Wazuh services with systemd |
| **Network Troubleshooting** | Checked API listening ports |
| **Pipeline Validation** | Tested Filebeat output |
| **Service Recovery** | Restarted only the affected dashboard service |
| **Troubleshooting** | Diagnosed a multi-component SIEM platform |

---

# 📸 Evidence Summary

The original Phase 4 screenshots are reused in this reorganized documentation.

| # | Evidence | Existing Screenshot |
|---|---|---|
| 1 | Wazuh Dashboard | `phase4-dashboard.png` |
| 2 | Connected Wazuh Agents | `phase4-agents.png` |
| 3 | Wazuh Security Alerts | `phase4-alerts.png` |

### Image Paths Used

```text
../images/phase4-dashboard.png
../images/phase4-agents.png
../images/phase4-alerts.png
```

No duplicate screenshots are required.

---

# 🏁 Phase Outcome

## ✅ Phase 4 Complete

Phase 4 successfully demonstrated centralized SIEM/XDR monitoring and SOC investigation using Wazuh.

The completed work included:

- Centralized Windows security monitoring
- Centralized Linux security monitoring
- Wazuh service validation
- Authentication-failure investigation
- Wazuh rule and severity analysis
- MITRE ATT&CK mapping
- Windows process investigation
- Controlled File Integrity Monitoring
- File creation detection
- File modification detection
- File hash and metadata analysis
- Event-context investigation
- SOC-style alert correlation
- Security-agent troubleshooting
- Wazuh platform troubleshooting
- Layered SIEM connectivity troubleshooting

The completed workflow was:

```text
Endpoint Activity
       │
       ▼
Security Telemetry
       │
       ▼
Wazuh Agent
       │
       ▼
Wazuh Manager
       │
       ▼
Detection Rules
       │
       ▼
Security Alert
       │
       ▼
Analyst Investigation
       │
       ▼
MITRE ATT&CK Context
       │
       ▼
Event Correlation
       │
       ▼
Document Findings

       ✅
```

Phase 4 moved the project beyond basic log collection and into centralized security monitoring and investigation.

The Wazuh SIEM/XDR environment was now ready to integrate network-based detection through Suricata.

---

# ➡️ Next Phase

## Phase 05 — Suricata IDS/IPS

Phase 5 introduces network intrusion detection using Suricata on OPNsense.

The next phase includes:

- Suricata configuration
- ET Open rules
- IDS/IPS monitoring
- Controlled Nmap reconnaissance
- Kali-to-Ubuntu traffic generation
- Custom detection rules
- EVE event analysis
- Alert validation
- IDS troubleshooting

---

[← Phase 03](phase-03-endpoint-monitoring.md) | [🏠 Back to Main Project](../README.md) | [Phase 05 →](phase-05-suricata-ids.md)

---

### Enterprise Security Operations Lab

**SOC Operations • SIEM/XDR • Detection Engineering • Endpoint Security • Network Security • Incident Response**
