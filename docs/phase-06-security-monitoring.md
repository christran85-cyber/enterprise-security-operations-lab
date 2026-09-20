# 🔎 Phase 06 — Security Monitoring & Event Correlation

> **Objective:** Generate controlled suspicious activity, investigate detections across Suricata and Wazuh, and correlate network and endpoint telemetry to reconstruct security activity using a SOC analyst workflow.

[← Phase 05](phase-05-suricata-ids.md) | [🏠 Main Project](../README.md) | [Phase 07 →](phase-07-vulnerability-management.md)

---

## 📑 Table of Contents

- [Phase Summary](#-phase-summary)
- [Overview](#-overview)
- [Detection Architecture](#️-detection-architecture)
- [Phase Objectives](#-phase-objectives)
- [Controlled Nmap Reconnaissance](#-controlled-nmap-reconnaissance)
- [Suricata Reconnaissance Detection](#-suricata-reconnaissance-detection)
- [Controlled SSH Authentication Testing](#-controlled-ssh-authentication-testing)
- [Wazuh SSH Detection](#-wazuh-ssh-detection)
- [MITRE ATT&CK Analysis](#️-mitre-attck-analysis)
- [Suricata and Wazuh Correlation](#-suricata-and-wazuh-correlation)
- [HTTP Reconnaissance](#-http-reconnaissance)
- [ET Open Nmap Detection](#-et-open-nmap-detection)
- [Gobuster Enumeration](#-gobuster-enumeration)
- [Incident Correlation](#-incident-correlation)
- [Commands Used](#-commands-used)
- [Validation](#-validation)
- [Troubleshooting Methodology](#-troubleshooting-methodology)
- [Lessons Learned](#-lessons-learned)
- [Skills Demonstrated](#-skills-demonstrated)
- [Evidence Summary](#-evidence-summary)
- [Phase Outcome](#-phase-outcome)

---

# 📊 Phase Summary

| Category | Details |
|---|---|
| **Status** | ✅ Complete |
| **Network Detection** | Suricata IDS/IPS |
| **Endpoint Detection** | Wazuh SIEM/XDR |
| **Traffic Source** | SOC-Kali `10.10.10.103` |
| **Target** | SOC-Ubuntu `10.50.20.100` |
| **Network Security** | OPNsense + Suricata |
| **Reconnaissance** | Nmap |
| **Web Enumeration** | Gobuster |
| **Endpoint Activity** | SSH authentication |
| **Threat Context** | MITRE ATT&CK |
| **Primary Skill** | Multi-source event correlation |
| **Workflow** | Generate → Detect → Investigate → Correlate → Document |

---

# 📋 Overview

Phase 6 combined the network-detection capabilities of **Suricata** with the endpoint-monitoring capabilities of **Wazuh**.

Instead of analyzing alerts from only one security platform, this phase demonstrated how a SOC analyst can correlate network and endpoint evidence to reconstruct controlled suspicious activity.

The controlled source was:

```text
SOC-Kali
10.10.10.103
```

The controlled target was:

```text
SOC-Ubuntu
10.50.20.100
```

Activity included:

- Nmap reconnaissance
- Network scanning
- HTTP reconnaissance
- Gobuster enumeration
- Failed SSH authentication

Suricata provided network visibility while Wazuh provided endpoint visibility.

```text
               SOC-Kali
              10.10.10.103
                    │
                    │
        Controlled Security Activity
                    │
                    ▼
               OPNsense
                    │
             ┌──────┴──────┐
             │             │
             ▼             ▼
         Suricata      SOC-Ubuntu
        Network IDS    10.50.20.100
             │             │
             │             ▼
             │        Wazuh Agent
             │             │
             └──────┬──────┘
                    │
                    ▼
             SOC Investigation
                    │
                    ▼
             Event Correlation
```

The goal was to demonstrate a fundamental SOC workflow:

```text
Generate
   ↓
Detect
   ↓
Investigate
   ↓
Correlate
   ↓
Document
```

---

# 🏗️ Detection Architecture

## Network Perspective

Suricata provided network-level evidence.

```text
SOC-Kali
    │
    ▼
OPNsense
    │
    ▼
Suricata
    │
    ├── Source IP
    ├── Destination IP
    ├── Protocol
    ├── Ports
    ├── Signature
    └── Application Data
```

---

## Endpoint Perspective

Wazuh provided endpoint-level evidence.

```text
SOC-Ubuntu
    │
    ▼
Linux Authentication
    │
    ▼
Wazuh Agent
    │
    ▼
Wazuh Manager
    │
    ├── Username
    ├── Authentication Result
    ├── Source IP
    ├── Rule
    ├── Severity
    └── MITRE ATT&CK
```

---

## Correlation

The two perspectives were combined using common indicators.

```text
Suricata Evidence
       +
Wazuh Evidence
       │
       ▼
Source IP
Destination
Timestamp
Observed Activity
       │
       ▼
Correlated Investigation
```

---

# 🎯 Phase Objectives

- [x] Generate controlled reconnaissance
- [x] Detect reconnaissance with Suricata
- [x] Generate controlled SSH authentication failures
- [x] Detect SSH failures with Wazuh
- [x] Review detailed Wazuh SSH events
- [x] Review MITRE ATT&CK mappings
- [x] Correlate Suricata and Wazuh telemetry
- [x] Generate HTTP reconnaissance
- [x] Identify Nmap HTTP activity
- [x] Analyze ET Open Nmap detection
- [x] Generate Gobuster enumeration
- [x] Detect Gobuster-related network activity
- [x] Compare source and destination addresses
- [x] Compare event timestamps
- [x] Reconstruct controlled suspicious activity
- [x] Document investigation evidence

---

# 🔍 Controlled Nmap Reconnaissance

SOC-Kali generated controlled reconnaissance against SOC-Ubuntu.

```text
Source
SOC-Kali
10.10.10.103

        │
        │ Nmap
        ▼

Target
SOC-Ubuntu
10.50.20.100
```

The traffic crossed OPNsense and was inspected by Suricata.

```text
SOC-Kali
     │
     │ Nmap Reconnaissance
     ▼
OPNsense
     │
     ▼
Suricata
     │
     ▼
SOC-Ubuntu
```

## 📸 Evidence — Nmap Reconnaissance

![Nmap Reconnaissance](../images/phase6-nmap-reconnaissance.png)

The reconnaissance originated from SOC-Kali and targeted SOC-Ubuntu in the DMZ.

**Result:** ✅ Controlled reconnaissance successfully generated.

---

# 🚨 Suricata Reconnaissance Detection

Suricata detected the Kali-to-Ubuntu reconnaissance traffic.

The network alert provided visibility into:

- Source IP
- Destination IP
- Protocol
- Ports
- Detection signature
- Timestamp

```text
SOC-Kali
10.10.10.103
      │
      ▼
Reconnaissance
      │
      ▼
OPNsense
      │
      ▼
Suricata
      │
      ▼
Network Alert
```

## 📸 Evidence — Suricata Reconnaissance Detection

![Suricata Reconnaissance Detection](../images/phase6-suricata-recon-detection.png)

The Suricata alert provided network evidence associated with the controlled reconnaissance.

**Result:** ✅ Suricata successfully detected reconnaissance activity.

---

# 🔐 Controlled SSH Authentication Testing

Controlled failed SSH authentication was generated from SOC-Kali against SOC-Ubuntu.

```text
SOC-Kali
10.10.10.103
      │
      │ SSH
      ▼
SOC-Ubuntu
10.50.20.100
      │
      ▼
Authentication Failure
```

This generated endpoint authentication telemetry that could be analyzed in Wazuh.

## 📸 Evidence — Failed SSH Authentication

![Failed SSH Authentication](../images/phase6-ssh-failed-login.png)

The controlled failed SSH login generated Linux authentication telemetry on SOC-Ubuntu.

**Result:** ✅ Controlled endpoint authentication activity generated.

---

# 🛡️ Wazuh SSH Detection

The Wazuh Agent on SOC-Ubuntu collected the authentication telemetry and forwarded it to the Wazuh Manager.

```text
Failed SSH Login
       │
       ▼
Linux Authentication Log
       │
       ▼
Wazuh Agent
       │
       ▼
Wazuh Manager
       │
       ▼
Detection Rule
       │
       ▼
Security Alert
```

Wazuh provided endpoint context including:

- Authentication result
- Username
- Source information
- Target endpoint
- Detection rule
- Severity
- Timestamp

## 📸 Evidence — Wazuh SSH Detection

![Wazuh SSH Detection](../images/phase6-wazuh-ssh-detection.png)

**Result:** ✅ Wazuh detected the controlled SSH authentication activity.

---

## Detailed SSH Event Investigation

The Wazuh event was expanded for deeper investigation.

The detailed event provided information such as:

```text
Source IP
Target Endpoint
Username
Authentication Result
Detection Rule
Alert Severity
Timestamp
Raw Event Information
```

## 📸 Evidence — Wazuh SSH Event Details

![Wazuh SSH Event Details](../images/phase6-wazuh-ssh-event-details.png)

The detailed event provided endpoint-level context for the SSH authentication activity.

**Result:** ✅ Wazuh event details successfully investigated.

---

# 🗺️ MITRE ATT&CK Analysis

The Wazuh authentication event was reviewed with MITRE ATT&CK context.

MITRE ATT&CK provides a standardized framework for describing adversary behaviors.

```text
Authentication Event
       │
       ▼
Wazuh Detection
       │
       ▼
Detection Rule
       │
       ▼
MITRE ATT&CK
       │
       ▼
Analyst Context
```

MITRE ATT&CK mapping does not automatically prove malicious activity.

Instead, it gives the analyst standardized context for understanding the behavior represented by the alert.

## 📸 Evidence — MITRE ATT&CK Mapping

![Wazuh MITRE ATT&CK Mapping](../images/phase6-wazuh-mitre-mapping.png)

**Result:** ✅ Authentication activity reviewed with MITRE ATT&CK context.

---

# 🔗 Suricata and Wazuh Correlation

The network and endpoint evidence were compared.

### Suricata Evidence

```text
Source IP
Destination IP
Protocol
Ports
Network Signature
Timestamp
```

### Wazuh Evidence

```text
Source IP
Target Endpoint
Username
Authentication Result
Detection Rule
Severity
Timestamp
MITRE ATT&CK
```

The primary correlation points were:

```text
Source IP
    +
Destination
    +
Timestamp
    +
Observed Activity
```

## 📸 Evidence — Suricata SSH Correlation

![Suricata SSH Correlation](../images/phase6-suricata-ssh-correlation.png)

The Suricata network evidence was compared with the endpoint authentication evidence recorded by Wazuh.

**Result:** ✅ Network and endpoint evidence successfully correlated.

---

# 🌐 HTTP Reconnaissance

The controlled investigation was expanded beyond SSH.

Nmap generated HTTP reconnaissance against SOC-Ubuntu.

```text
SOC-Kali
     │
     │ HTTP Reconnaissance
     ▼
OPNsense
     │
     ▼
Suricata
     │
     ▼
SOC-Ubuntu
```

This generated application-layer network telemetry for Suricata analysis.

## 📸 Evidence — Nmap Web Reconnaissance

![Suricata Nmap Web Reconnaissance](../images/phase6-suricata-nmap-web-recon.png)

**Result:** ✅ HTTP reconnaissance successfully observed by Suricata.

---

# 🚨 ET Open Nmap Detection

Suricata's ET Open rules provided additional context for the HTTP reconnaissance.

The detection identified activity associated with Nmap.

This demonstrated the value of application-layer IDS signatures.

Instead of only identifying:

```text
Source IP
Destination IP
Port
```

the detection could provide additional information about the tool or behavior responsible for the traffic.

## 📸 Evidence — ET Open Nmap Details

![ET Open Nmap Detection](../images/phase6-incident1-suricata-nmap-details.png)

The ET Open alert provided additional context for the Nmap-generated reconnaissance.

**Result:** ✅ Nmap reconnaissance identified through Suricata ET Open detection.

---

# 📂 Gobuster Enumeration

Controlled web enumeration was also generated using Gobuster.

```text
SOC-Kali
     │
     │ Gobuster
     ▼
SOC-Ubuntu Web Service
     │
     ▼
HTTP Requests
     │
     ▼
Suricata
     │
     ▼
Network Alerts
```

This expanded the controlled investigation beyond simple port scanning.

## 📸 Evidence — Gobuster Alerts

![Suricata Gobuster Alerts](../images/phase6-suricata-gobuster-alerts.png)

The Suricata alerts demonstrate visibility into controlled web enumeration.

**Result:** ✅ Gobuster activity generated observable network-security telemetry.

---

# 🧩 Incident Correlation

The available evidence was combined into a single controlled activity sequence.

```text
SOC-Kali
10.10.10.103
      │
      ├──── Nmap Reconnaissance
      │
      ├──── HTTP Reconnaissance
      │
      ├──── Gobuster Enumeration
      │
      └──── SSH Authentication
                  │
                  ▼
             SOC-Ubuntu
            10.50.20.100
                  │
        ┌─────────┴─────────┐
        │                   │
        ▼                   ▼
    Suricata              Wazuh
Network Telemetry    Endpoint Telemetry
        │                   │
        └─────────┬─────────┘
                  │
                  ▼
            SOC Correlation
                  │
                  ▼
        Reconstructed Activity
```

The investigation did not depend on a single alert.

Multiple sources of security evidence were compared to understand the broader activity.

## 📸 Evidence — Wazuh SSH Correlation

![Wazuh SSH Correlation](../images/phase6-incident1-wazuh-ssh-correlation.png)

This evidence documents the Wazuh side of the correlated investigation.

---

## 📸 Evidence — Wazuh SSH Investigation

![Wazuh SSH Investigation](../images/phase6-wazuh-ssh-attack.png)

This provides additional endpoint evidence associated with the controlled SSH activity.

**Result:** ✅ Multi-source evidence successfully reconstructed into a correlated SOC investigation.

---

# 💻 Commands Used

The following commands and tools were used during Phase 6.

## Nmap Reconnaissance

```bash
nmap 10.50.20.100
```

Purpose:

```text
Generate controlled reconnaissance against SOC-Ubuntu.
```

---

## Service Discovery

```bash
nmap -sV 10.50.20.100
```

Purpose:

```text
Identify exposed services and generate additional
network telemetry for Suricata analysis.
```

---

## SSH Authentication Testing

```bash
ssh <test-user>@10.50.20.100
```

Purpose:

```text
Generate controlled authentication telemetry
for Wazuh investigation.
```

Only the controlled lab account was used for testing.

---

## HTTP Reconnaissance

Nmap HTTP reconnaissance was performed against the controlled Ubuntu web service.

The resulting HTTP traffic was inspected by Suricata.

---

## Gobuster Enumeration

Gobuster was used against the controlled SOC-Ubuntu web service.

```text
Gobuster
   │
   ▼
HTTP Requests
   │
   ▼
SOC-Ubuntu
   │
   ▼
Suricata
```

The resulting network telemetry was reviewed through Suricata.

---

## Command Reference

| Purpose | Command / Tool |
|---|---|
| Network reconnaissance | `nmap 10.50.20.100` |
| Service discovery | `nmap -sV 10.50.20.100` |
| SSH authentication test | `ssh <test-user>@10.50.20.100` |
| HTTP reconnaissance | Nmap |
| Web enumeration | Gobuster |
| Network investigation | Suricata / OPNsense |
| Endpoint investigation | Wazuh |
| Correlation | Source IP + destination + timestamp + activity |

---

# 🧪 Validation

Phase 6 validated the complete multi-source monitoring workflow.

| Test | Detection Source | Result |
|---|---|---|
| Nmap reconnaissance | Suricata | ✅ Detected |
| Kali-to-Ubuntu reconnaissance | Suricata | ✅ Detected |
| Failed SSH authentication | Wazuh | ✅ Detected |
| SSH event details | Wazuh | ✅ Investigated |
| MITRE ATT&CK context | Wazuh | ✅ Validated |
| SSH network evidence | Suricata | ✅ Correlated |
| HTTP reconnaissance | Suricata | ✅ Detected |
| Nmap activity | ET Open / Suricata | ✅ Detected |
| Gobuster enumeration | Suricata | ✅ Observed |
| Cross-platform correlation | Suricata + Wazuh | ✅ Completed |

The complete workflow was:

```text
Controlled Activity
        │
        ▼
Network / Endpoint Telemetry
        │
        ▼
Security Detection
        │
        ▼
Alert Investigation
        │
        ▼
Event Correlation
        │
        ▼
Incident Reconstruction
        │
        ▼
Documentation

        ✅
```

---

# 🔧 Troubleshooting Methodology

Phase 6 reinforced that successful traffic generation does not automatically prove that monitoring is operational.

Multiple layers must function correctly.

```text
Traffic Generation
       │
       ▼
Network Connectivity
       │
       ▼
OPNsense Routing
       │
       ▼
Suricata Inspection
       │
       ▼
Target Service
       │
       ▼
Endpoint Logging
       │
       ▼
Wazuh Agent
       │
       ▼
Wazuh Manager
       │
       ▼
Security Alert
```

When expected evidence is missing, troubleshooting should proceed layer by layer.

## Network Detection Troubleshooting

Verify:

1. SOC-Kali can reach SOC-Ubuntu.
2. Traffic crosses OPNsense.
3. Suricata is running.
4. Suricata is processing packets.
5. The correct interface is monitored.
6. Detection rules are enabled.
7. Alerts appear in Suricata.

## Endpoint Detection Troubleshooting

Verify:

1. The activity reached SOC-Ubuntu.
2. Ubuntu generated the expected local event.
3. The Wazuh Agent is running.
4. The agent can communicate with the Wazuh Manager.
5. Wazuh received the event.
6. Wazuh processed the event.
7. A detection rule generated an alert.

This prevents incorrectly assuming that a missing alert automatically means the security platform failed.

---

# 💡 Lessons Learned

## 1. One Alert Rarely Provides the Complete Picture

A network alert may show suspicious communication without showing what happened on the endpoint.

An endpoint alert may show failed authentication without showing the network activity that occurred before it.

Combining both provides stronger context.

---

## 2. Network and Endpoint Telemetry Complement Each Other

```text
Suricata
   │
   ├── Network Activity
   ├── Protocol
   ├── Ports
   └── Signatures

Wazuh
   │
   ├── Endpoint Activity
   ├── Username
   ├── Authentication Result
   ├── Detection Rule
   └── MITRE ATT&CK
```

Together, they provide a more complete investigation.

---

## 3. Network Reconnaissance Can Appear Before Endpoint Events

Reconnaissance may occur before authentication attempts or other endpoint activity.

Suricata can therefore provide earlier context in an investigation timeline.

---

## 4. ET Open Signatures Add Application Context

IDS signatures can identify characteristics associated with reconnaissance tools.

This provides more information than IP addresses and ports alone.

---

## 5. Wazuh Provides Endpoint Context

Wazuh provides endpoint and authentication information that network monitoring alone cannot provide.

---

## 6. Source IP and Time Are Valuable Correlation Points

Security platforms can often be correlated using:

```text
Source IP
   +
Destination
   +
Timestamp
   +
Observed Behavior
```

---

## 7. MITRE ATT&CK Adds Standardized Context

MITRE ATT&CK helps translate raw alerts into recognizable security behaviors.

```text
Raw Event
    │
    ▼
Detection
    │
    ▼
MITRE ATT&CK
    │
    ▼
Security Context
```

---

## 8. Controlled Testing Validates Security Controls

Controlled activity provides repeatable evidence that monitoring systems can observe expected behavior.

---

## 9. Traffic Generation Alone Is Not Validation

Successfully running Nmap, Gobuster, or SSH does not prove monitoring worked.

The corresponding security alert must also be confirmed.

---

## 10. End-to-End Monitoring Requires Every Layer

Network connectivity, IDS operation, endpoint logging, agent collection, and SIEM processing must all function correctly.

---

## 11. Correlation Is a Core SOC Skill

Phase 6 demonstrated the workflow:

```text
Generate
   ↓
Detect
   ↓
Investigate
   ↓
Correlate
   ↓
Document
```

This workflow became the foundation for later incident-response phases.

---

# 🧠 Skills Demonstrated

| Skill | Application |
|---|---|
| **SOC Monitoring** | Investigated security activity across multiple controls |
| **Event Correlation** | Correlated Suricata and Wazuh evidence |
| **Network IDS Analysis** | Investigated Suricata detections |
| **SIEM Analysis** | Investigated Wazuh endpoint alerts |
| **Nmap** | Generated controlled reconnaissance |
| **SSH Analysis** | Investigated authentication failures |
| **HTTP Reconnaissance** | Generated web reconnaissance |
| **Gobuster** | Generated controlled HTTP enumeration |
| **ET Open Analysis** | Investigated Nmap-related network detection |
| **MITRE ATT&CK** | Added standardized threat context |
| **Incident Reconstruction** | Combined network and endpoint evidence |
| **Detection Validation** | Confirmed expected security alerts |
| **Troubleshooting** | Validated the monitoring pipeline layer by layer |
| **Documentation** | Preserved investigation evidence and findings |

---

# 📸 Evidence Summary

Phase 6 contains **12 original screenshots** documenting the monitoring and event-correlation workflow.

| # | Evidence | Screenshot |
|---|---|---|
| 1 | Nmap Reconnaissance | `phase6-nmap-reconnaissance.png` |
| 2 | Suricata Reconnaissance Detection | `phase6-suricata-recon-detection.png` |
| 3 | Failed SSH Authentication | `phase6-ssh-failed-login.png` |
| 4 | Wazuh SSH Detection | `phase6-wazuh-ssh-detection.png` |
| 5 | Wazuh SSH Event Details | `phase6-wazuh-ssh-event-details.png` |
| 6 | Wazuh MITRE Mapping | `phase6-wazuh-mitre-mapping.png` |
| 7 | Suricata SSH Correlation | `phase6-suricata-ssh-correlation.png` |
| 8 | Suricata Nmap Web Reconnaissance | `phase6-suricata-nmap-web-recon.png` |
| 9 | ET Open Nmap Details | `phase6-incident1-suricata-nmap-details.png` |
| 10 | Suricata Gobuster Alerts | `phase6-suricata-gobuster-alerts.png` |
| 11 | Wazuh SSH Correlation | `phase6-incident1-wazuh-ssh-correlation.png` |
| 12 | Wazuh SSH Investigation | `phase6-wazuh-ssh-attack.png` |

All screenshots are stored in the repository's existing:

```text
/images/
```

directory.

Because this documentation is located under `/docs/`, the correct relative path is:

```text
../images/<filename>
```

No Phase 6 screenshots need to be renamed or uploaded again.

---

# 🏁 Phase Outcome

## ✅ Phase 6 Complete

Phase 6 successfully demonstrated an end-to-end security monitoring and event-correlation workflow.

Controlled activity originated from:

```text
SOC-Kali
10.10.10.103
```

and targeted:

```text
SOC-Ubuntu
10.50.20.100
```

Suricata provided network visibility into:

- Reconnaissance
- HTTP traffic
- Network communication
- Nmap activity
- ET Open detections
- Gobuster enumeration

Wazuh provided endpoint visibility into:

- Failed SSH authentication
- Source information
- Authentication context
- Detection rules
- Alert severity
- Raw endpoint events
- MITRE ATT&CK mappings

The evidence was correlated:

```text
              SOC-Kali
             10.10.10.103
                   │
       ┌───────────┼───────────┐
       │           │           │
       ▼           ▼           ▼
     Nmap       Gobuster      SSH
       │           │           │
       └───────────┼───────────┘
                   │
                   ▼
              SOC-Ubuntu
             10.50.20.100
                   │
          ┌────────┴────────┐
          │                 │
          ▼                 ▼
      Suricata            Wazuh
       Network           Endpoint
      Telemetry          Telemetry
          │                 │
          └────────┬────────┘
                   │
                   ▼
             Correlation
                   │
                   ▼
        Incident Reconstruction

                   ✅
```

Phase 6 demonstrated a core SOC analyst capability:

> **Reconstructing suspicious activity using evidence collected from multiple security controls.**

The resulting workflow was:

```text
Generate → Detect → Investigate → Correlate → Document
```

This prepared the lab for vulnerability assessment and remediation in Phase 7.

---

# ➡️ Next Phase

## Phase 07 — Vulnerability Assessment & Remediation

Phase 7 moves from security monitoring into vulnerability management.

The next phase focuses on:

- Nmap service discovery
- Vulnerability identification
- Risk assessment
- Apache assessment
- Apache hardening
- Remediation
- Validation scanning
- Before-and-after comparison

---

[← Phase 05](phase-05-suricata-ids.md) | [🏠 Back to Main Project](../README.md) | [Phase 07 →](phase-07-vulnerability-management.md)

---

### Enterprise Security Operations Lab

**SOC Operations • Event Correlation • Suricata • Wazuh SIEM/XDR • MITRE ATT&CK • Network Security Monitoring**
