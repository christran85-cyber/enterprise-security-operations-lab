# 🖥️ Phase 03 — Endpoint Security Monitoring

> **Objective:** Deploy and validate Windows and Linux endpoint security telemetry and securely forward endpoint events to the centralized Wazuh infrastructure.

[← Phase 02](phase-02-network-segmentation.md) | [🏠 Main Project](../README.md) | [Phase 04 →](phase-04-wazuh-siem.md)

---

## 📑 Table of Contents

- [Phase Summary](#-phase-summary)
- [Overview](#-overview)
- [Endpoint Monitoring Architecture](#️-endpoint-monitoring-architecture)
- [Phase Objectives](#-phase-objectives)
- [Windows Endpoint Monitoring](#️-windows-endpoint-monitoring)
- [Ubuntu Endpoint Monitoring](#-ubuntu-endpoint-monitoring)
- [Wazuh Agent Connectivity](#-wazuh-agent-connectivity)
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
| **Windows Endpoint** | SOC-Windows11 |
| **Linux Endpoint** | SOC-Ubuntu |
| **Windows Telemetry** | Security Auditing, Sysmon, PowerShell |
| **Linux Telemetry** | auditd, osquery, Linux Logs |
| **Centralized Agent** | Wazuh Agent |
| **Wazuh Manager** | `10.10.10.102` |
| **Ubuntu Endpoint** | `10.50.20.100` |
| **Agent Communication** | TCP `1514` |
| **Focus** | Endpoint telemetry & centralized monitoring |
| **Next Phase** | Wazuh SIEM/XDR |

---

# 📋 Overview

Phase 3 focused on deploying and validating endpoint security monitoring across both Windows and Linux systems.

The two monitored endpoints were:

- **SOC-Windows11** — Windows 11 enterprise endpoint
- **SOC-Ubuntu** — Ubuntu Linux endpoint located in the isolated DMZ

The objective was to generate detailed endpoint telemetry, configure centralized log forwarding, and verify that both endpoints could communicate with the Wazuh security server.

The resulting monitoring architecture provides visibility into:

- Process creation
- Command-line activity
- PowerShell execution
- Windows Application events
- Linux system activity
- Linux authentication failures
- Endpoint configuration
- Security events
- Wazuh agent status

---

# 🏗️ Endpoint Monitoring Architecture

```text
              SOC-Windows11
                    │
       ┌────────────┼────────────┐
       │            │            │
       ▼            ▼            ▼
Windows Security   Sysmon    PowerShell
    Auditing
       │            │            │
       └────────────┼────────────┘
                    │
                    ▼
                Wazuh Agent
                    │
                    │
                    ▼
               SOC-Wazuh
              SIEM / XDR


               SOC-Ubuntu
                    │
       ┌────────────┼────────────┐
       │            │            │
       ▼            ▼            ▼
     auditd       osquery     Linux Logs
       │            │            │
       └────────────┼────────────┘
                    │
                    ▼
                Wazuh Agent
                    │
                TCP 1514
                    │
                    ▼
                OPNsense
                    │
                    ▼
               SOC-Wazuh
```

This phase established the endpoint telemetry foundation required for centralized SIEM/XDR analysis in Phase 4.

---

# 🎯 Phase Objectives

- [x] Configure Windows Security auditing
- [x] Enable Windows process creation auditing
- [x] Enable command-line process logging
- [x] Install Microsoft Sysmon
- [x] Validate Sysmon Event ID `1`
- [x] Enable PowerShell script-block logging
- [x] Validate PowerShell Event ID `4104`
- [x] Install Windows Wazuh Agent
- [x] Validate Windows Application logging
- [x] Install Linux auditd
- [x] Validate Linux audit events
- [x] Install osquery
- [x] Enable the osquery service
- [x] Install Ubuntu Wazuh Agent
- [x] Configure DMZ-to-Wazuh firewall access
- [x] Validate TCP `1514`
- [x] Generate controlled Linux events
- [x] Validate centralized endpoint telemetry

---

# 🪟 Windows Endpoint Monitoring

## 1. Windows Endpoint

SOC-Windows11 represents an enterprise workstation configured to generate detailed endpoint security telemetry.

### Configuration

- Microsoft Sysmon
- Wazuh Agent
- Windows Security auditing
- Process creation auditing
- Command-line process logging
- PowerShell script-block logging
- Windows Application log monitoring
- Centralized Wazuh communication

### 📸 Evidence — Windows Endpoint

![Windows Endpoint](../images/phase3-windows.png)

---

## 2. Windows Process Creation Auditing

Advanced Audit Policy was configured to record successful process creation events.

Configuration path:

```text
Computer Configuration
        ↓
Windows Settings
        ↓
Security Settings
        ↓
Advanced Audit Policy Configuration
        ↓
System Audit Policies
        ↓
Detailed Tracking
        ↓
Audit Process Creation
```

Process creation auditing was enabled for successful events.

Windows was also configured to include command-line information inside process creation events:

```text
Computer Configuration
        ↓
Administrative Templates
        ↓
System
        ↓
Audit Process Creation
        ↓
Include command line in process creation events
```

### Validation

Windows Event Viewer confirmed successful generation of:

```text
Security Event ID 4688
```

Event ID `4688` records newly created processes.

Validation confirmed:

- Audit Success events generated
- Event ID `4688`
- New Process Name recorded
- Creator Process Name recorded
- Process Command Line recorded

### 📸 Evidence — Windows Process Creation Auditing

![Windows Process Creation Auditing](../images/phase3-windows-process-auditing.png)

**Result:** ✅ Native Windows process-creation telemetry successfully validated.

---

## 3. Microsoft Sysmon

Microsoft Sysmon was installed to provide enhanced endpoint telemetry beyond standard Windows logging.

Sysmon telemetry is available through:

```text
Applications and Services Logs
        ↓
Microsoft
        ↓
Windows
        ↓
Sysmon
        ↓
Operational
```

### Sysmon Process Monitoring

Sysmon Event ID:

```text
1
```

was successfully validated.

Event ID `1` records process creation and provides detailed information including:

- Process image
- Command line
- User
- Parent process
- Process ID
- Parent process ID
- File hashes
- Process GUID

### 📸 Evidence — Sysmon

![Sysmon Events](../images/phase3-sysmon.png)

**Result:** ✅ Enhanced Sysmon process telemetry operational.

---

## 4. PowerShell Logging

PowerShell logging was configured to provide additional visibility into PowerShell activity.

PowerShell Operational logs were reviewed through Windows Event Viewer.

### Validation

PowerShell Event ID:

```text
4104
```

was generated and reviewed.

Event ID `4104` records PowerShell script-block activity and provides visibility into commands and scripts executed through PowerShell.

This telemetry is valuable for investigating suspicious PowerShell execution and administrative activity.

---

## 5. Windows Wazuh Agent

The Wazuh Agent was installed on SOC-Windows11 and registered with the centralized Wazuh manager.

The Wazuh Agent service was verified using:

```powershell
Get-Service wazuhsvc
```

The service returned:

```text
Running
```

The endpoint was configured to communicate with:

```text
Wazuh Manager: 10.10.10.102
Protocol: TCP
Port: 1514
```

Agent logs confirmed:

```text
Connected to the server ([10.10.10.102]:1514/tcp).
```

Windows Application event log monitoring was also confirmed:

```text
Analyzing event log: 'Application'.
```

### Controlled Windows Application Event

A controlled Windows Application event was generated.

The test event contained:

```text
Log: Application
Source: WazuhTest
Event ID: 1001
Level: Warning

SOC-LAB TEST: Windows Wazuh logging validation
```

This validated:

- Windows Application logging
- Controlled event generation
- Wazuh Application log monitoring
- Wazuh Agent connectivity

### 📸 Evidence — Windows Wazuh Agent

![Windows Wazuh Agent](../images/phase3-windows-wazuh.png)

**Result:** ✅ SOC-Windows11 successfully communicated with the Wazuh manager.

---

# 🐧 Ubuntu Endpoint Monitoring

## 1. Ubuntu Endpoint

SOC-Ubuntu represents the Linux endpoint and controlled security target located inside the isolated DMZ.

### Endpoint Configuration

- auditd
- osquery
- Wazuh Agent
- Linux audit logging
- System monitoring
- DMZ-to-Wazuh firewall exception
- Centralized Wazuh communication

### Network Configuration

```text
Hostname: soc-ubuntu
IP Address: 10.50.20.100
Network: 10.50.20.0/24
Gateway: 10.50.20.1
Zone: DMZ
```

### 📸 Evidence — Ubuntu Endpoint

![Ubuntu Endpoint](../images/phase3-ubuntu.png)

---

## 2. Linux Auditing with auditd

Linux security auditing was configured using `auditd`.

A controlled test file was monitored using an audit rule with the key:

```text
audit_test
```

The `ausearch` utility was used to retrieve associated security events:

```bash
sudo ausearch -k audit_test
```

Captured audit records included:

- SYSCALL
- PATH
- PROCTITLE
- CONFIG_CHANGE
- User information
- Process information
- File activity
- Successful system activity

### 📸 Evidence — Linux Security Monitoring

![Linux Security Monitoring](../images/phase3-linux-monitoring.png)

**Result:** ✅ Linux security activity successfully recorded and queried using auditd.

---

## 3. osquery Endpoint Visibility

osquery was installed to provide additional endpoint visibility and SQL-based operating-system querying.

The default Ubuntu repositories did not initially provide the required osquery package.

The official osquery repository was therefore added.

During installation, a malformed repository entry was identified and corrected before installation could continue.

After installation, the `osqueryd` daemon initially appeared:

```text
inactive
disabled
```

The service was enabled and started using:

```bash
sudo systemctl enable --now osqueryd
```

Service status was then verified as:

```text
active (running)
```

osquery provides visibility into:

- Operating system configuration
- Running processes
- Users
- Network information
- Installed software
- Services
- System configuration

This provides an additional endpoint-investigation capability alongside auditd and Wazuh.

---

# 🔗 Wazuh Agent Connectivity

## Ubuntu Wazuh Agent

The Wazuh Agent was installed and configured on SOC-Ubuntu.

The telemetry path is:

```text
SOC-Ubuntu
10.50.20.100
      │
      │ TCP 1514
      ▼
SOC-OPNsense
      │
      ▼
SOC-Wazuh
10.10.10.102
```

Because the DMZ is intentionally isolated from the Security LAN, a narrow OPNsense firewall exception was created specifically for Wazuh communication.

```text
SOC-Ubuntu
10.50.20.100
      │
      │ TCP 1514
      ▼
SOC-Wazuh
10.10.10.102

      ✅ ALLOW
```

Other unauthorized DMZ-to-Security-LAN communication remains blocked.

---

## DMZ-to-Wazuh Connectivity Validation

ICMP was not used as the primary validation method because ICMP traffic from the DMZ to the Security LAN remained intentionally blocked.

Instead, the actual Wazuh service port was tested:

```bash
nc -vz 10.10.10.102 1514
```

Successful connectivity demonstrated that the firewall permitted the required Wazuh traffic without weakening the broader segmentation policy.

---

## Wazuh Agent Enrollment

During initial enrollment, the Ubuntu Wazuh Agent temporarily reported that the Wazuh server was unavailable.

Troubleshooting included reviewing:

```bash
/var/ossec/logs/ossec.log
```

The logs initially contained connection warnings before the agent successfully authenticated with the Wazuh manager.

The enrollment sequence eventually:

1. Contacted the Wazuh manager
2. Authenticated the endpoint
3. Received a valid agent key
4. Established the Wazuh connection

Agent logs ultimately confirmed:

```text
Connected to the server ([10.10.10.102]:1514/tcp).
```

A message stating:

```text
No authentication password provided
```

also appeared during enrollment.

Because subsequent entries confirmed successful key exchange, authentication, and connectivity, this message was informational in this successful enrollment sequence rather than evidence that enrollment failed.

---

# 🧪 Validation

## Controlled Ubuntu Event

A controlled logging event was generated on Ubuntu:

```bash
sudo logger "SOC-LAB TEST: Ubuntu Wazuh logging validation"
```

The event successfully appeared in the centralized Wazuh environment.

This demonstrated:

```text
Ubuntu Endpoint
      │
      ▼
Linux Logging
      │
      ▼
Wazuh Agent
      │
      ▼
OPNsense Firewall
      │
      │ TCP 1514
      ▼
Wazuh Manager
```

---

## Wazuh Endpoint Telemetry

### 📸 Evidence — Centralized Endpoint Telemetry

![Wazuh Endpoint Telemetry](../images/phase3-ubuntu-wazuh-failed-auth-detection.png)

Wazuh Discover confirmed that endpoint telemetry was reaching the centralized environment.

The event stream included telemetry associated with:

- `SOC-Windows11`
- `soc-ubuntu`
- Wazuh manager `soc-wazuh`

This provided evidence that both monitored endpoints were communicating with the centralized Wazuh infrastructure.

---

## Ubuntu Authentication Failure Validation

Controlled failed-authentication activity was generated on SOC-Ubuntu.

Wazuh successfully received and processed the resulting authentication events.

### 📸 Evidence — Ubuntu Authentication Failure

![Ubuntu Authentication Failure](../images/phase3-wazuh-ubuntu-authentication-failure.png)

A search for:

```text
"authentication failure"
```

returned multiple matching Wazuh alerts.

The evidence confirmed:

```text
Rule ID: 5503
Rule Level: 5
Description: PAM: User login failed
```

This demonstrated that Linux authentication telemetry was reaching Wazuh and being processed by the platform's detection rules.

Detailed alert investigation and correlation are covered in Phase 4.

---

## Ubuntu Wazuh Alert Validation

### 📸 Evidence — Controlled Ubuntu Event

![Ubuntu Wazuh Alert Validation](../images/ubuntu-wazuh-alert-validation.png)

The controlled Ubuntu logging test:

```bash
sudo logger "SOC-LAB TEST: Ubuntu Wazuh logging validation"
```

was successfully located in Wazuh Discover.

The event confirmed:

- Agent: `soc-ubuntu`
- Agent IP: `10.50.20.100`
- Manager: `soc-wazuh`
- Controlled test activity reached Wazuh
- Wazuh rule processing occurred

The event included:

```text
/usr/bin/logger SOC-LAB TEST: Ubuntu Wazuh logging validation
```

This validated the complete telemetry path:

```text
Controlled Ubuntu Activity
          │
          ▼
      Linux Logging
          │
          ▼
       Wazuh Agent
          │
          ▼
   OPNsense Firewall
          │
      TCP 1514
          │
          ▼
      Wazuh Manager
          │
          ▼
     Wazuh Discover

        ✅ VALIDATED
```

---

# 🔧 Troubleshooting

Several configuration and integration problems were encountered and resolved during Phase 3.

## Windows Event IDs

Windows Security Event ID `4688` and Sysmon Event ID `1` both provide process-creation information but originate from different telemetry sources.

| Event | Source | Purpose |
|---|---|---|
| `4688` | Windows Security | Native process creation auditing |
| `1` | Microsoft Sysmon | Enhanced process creation telemetry |
| `4104` | PowerShell Operational | PowerShell script-block logging |

Understanding the difference between these sources is important during endpoint investigations.

---

## osquery Installation

Ubuntu could not initially locate the osquery package through the default repository configuration.

The official osquery repository had to be added.

A malformed repository entry was then identified and corrected before installation could proceed.

---

## osquery Service

After installation, `osqueryd` initially appeared inactive and disabled.

The issue was corrected using:

```bash
sudo systemctl enable --now osqueryd
```

The service subsequently returned:

```text
active (running)
```

---

## Wazuh Agent Connectivity

The Ubuntu Wazuh Agent initially generated server-connectivity warnings.

Rather than immediately reinstalling the agent, the logs were reviewed.

Subsequent log entries confirmed successful authentication and connection to:

```text
10.10.10.102:1514/TCP
```

---

## Firewall Validation

Because the DMZ is intentionally isolated from the Security LAN, a failed ping does not necessarily indicate that Wazuh communication is broken.

The actual service port was tested:

```bash
nc -vz 10.10.10.102 1514
```

This allowed the required Wazuh connection to be validated without weakening the segmentation policy.

---

## Firewall Rule Ordering

OPNsense evaluates firewall rules according to their configured order.

The narrow:

```text
SOC-Ubuntu → SOC-Wazuh → TCP 1514
```

allow rule must be evaluated before the broader DMZ-to-Security-LAN blocking rule.

This allows required security telemetry while maintaining network segmentation.

---

# 💡 Lessons Learned

### 1. Similar Events Can Come From Different Telemetry Sources

```text
Windows 4688
     │
     └── Native Windows Security Auditing

Sysmon Event 1
     │
     └── Enhanced Sysmon Telemetry

PowerShell 4104
     │
     └── Script-Block Logging
```

Knowing the source of an event is critical during security investigations.

---

### 2. Validate the Actual Service Port

A failed ping does not prove an application connection is broken.

For Wazuh, testing:

```bash
nc -vz 10.10.10.102 1514
```

provides stronger evidence than ICMP when ICMP is intentionally blocked.

---

### 3. Review Logs Before Reinstalling Services

The Ubuntu Wazuh Agent initially showed connectivity warnings.

Reviewing the agent logs revealed that enrollment eventually succeeded.

Reinstalling immediately would have added unnecessary troubleshooting complexity.

---

### 4. Service Installation Does Not Guarantee Service Operation

After installing osquery, `osqueryd` was still inactive.

Installation and operational status are separate validation steps.

```text
Install
   ↓
Enable
   ↓
Start
   ↓
Check Status
   ↓
Validate Function
```

---

### 5. Security Controls Must Work Together

The DMZ remained segmented while a narrow exception allowed required security telemetry.

```text
DMZ Isolation
     +
Wazuh TCP 1514 Exception
     =
Secure Monitoring
```

---

# 🧭 Endpoint Troubleshooting Methodology

A major lesson from Phase 3 was to validate each layer individually:

```text
Generate Event
      │
      ▼
Verify Local Log
      │
      ▼
Verify Security Agent
      │
      ▼
Verify Network Port
      │
      ▼
Verify Firewall Policy
      │
      ▼
Verify Manager Connection
      │
      ▼
Verify Centralized Telemetry
```

This approach makes it easier to determine whether a problem exists at the:

- Endpoint
- Logging layer
- Security agent
- Firewall
- Network
- Wazuh manager
- Centralized monitoring layer

---

# 🧠 Skills Demonstrated

| Skill | Application |
|---|---|
| **Windows Security Auditing** | Configured process creation telemetry |
| **Sysmon** | Captured enhanced Windows process activity |
| **PowerShell Logging** | Enabled script-block telemetry |
| **Linux Auditing** | Monitored Linux activity with auditd |
| **osquery** | Added SQL-based endpoint visibility |
| **Wazuh Agent Management** | Connected Windows and Linux endpoints |
| **Firewall Administration** | Allowed narrowly scoped Wazuh communication |
| **Security Logging** | Generated and validated controlled events |
| **Authentication Monitoring** | Detected Linux authentication failures |
| **Network Validation** | Tested TCP `1514` connectivity |
| **Troubleshooting** | Diagnosed repositories, services, agents and firewall rules |
| **Centralized Monitoring** | Verified endpoint telemetry in Wazuh |

---

# 📸 Evidence Summary

The original Phase 3 screenshots are reused in this reorganized documentation.

| # | Evidence | Existing Screenshot |
|---|---|---|
| 1 | Windows Endpoint | `phase3-windows.png` |
| 2 | Windows Process Creation Auditing | `phase3-windows-process-auditing.png` |
| 3 | Sysmon Events | `phase3-sysmon.png` |
| 4 | Windows Wazuh Agent | `phase3-windows-wazuh.png` |
| 5 | Ubuntu Endpoint | `phase3-ubuntu.png` |
| 6 | Linux Security Monitoring | `phase3-linux-monitoring.png` |
| 7 | Wazuh Endpoint Telemetry | `phase3-ubuntu-wazuh-failed-auth-detection.png` |
| 8 | Ubuntu Authentication Failure | `phase3-wazuh-ubuntu-authentication-failure.png` |
| 9 | Ubuntu Wazuh Alert Validation | `ubuntu-wazuh-alert-validation.png` |

No duplicate screenshots are required. These are the same evidence files used in the original Phase 3 documentation. :contentReference[oaicite:1]{index=1}

---

# 🏁 Phase Outcome

## ✅ Phase 3 Complete

Endpoint security monitoring became operational across both Windows and Linux systems.

### Windows Monitoring

```text
Windows Security Auditing
        +
Sysmon
        +
PowerShell Logging
        +
Windows Application Logs
        +
Wazuh Agent
```

### Linux Monitoring

```text
auditd
   +
osquery
   +
Linux Logs
   +
Wazuh Agent
```

Both endpoints now feed security telemetry into the centralized Wazuh infrastructure:

```text
SOC-Windows11                    SOC-Ubuntu
      │                              │
      ▼                              ▼
Windows Telemetry               Linux Telemetry
      │                              │
      ▼                              ▼
 Wazuh Agent                    Wazuh Agent
      │                              │
      └──────────────┬───────────────┘
                     │
                     ▼
                 OPNsense
                     │
                     ▼
                 SOC-Wazuh
                     │
                     ▼
             Centralized Security
                 Monitoring

                   ✅
```

Phase 3 established the endpoint telemetry infrastructure required for centralized SIEM/XDR monitoring, detection analysis, correlation, and SOC investigations.

---

# ➡️ Next Phase

**Phase 04 — Wazuh SIEM/XDR**

Phase 4 uses the endpoint telemetry established here to perform:

- Centralized alert monitoring
- Authentication-failure investigation
- Windows process investigation
- MITRE ATT&CK mapping
- File Integrity Monitoring
- Event correlation
- SOC analyst investigation

---

[← Phase 02](phase-02-network-segmentation.md) | [🏠 Back to Main Project](../README.md) | [Phase 04 →](phase-04-wazuh-siem.md)

---

### Enterprise Security Operations Lab

**SOC Operations • Detection Engineering • Endpoint Security • Network Security • Security Automation • Incident Response**
