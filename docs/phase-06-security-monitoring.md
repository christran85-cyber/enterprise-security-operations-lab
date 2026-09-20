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

Phase 6 combined the endpoint-monitoring capabilities established with **Wazuh** and the network-detection capabilities established with **Suricata**.

Instead of investigating alerts from only one security control, this phase demonstrated how a SOC analyst can correlate evidence from multiple security sources.

Controlled security activity originated from:

```text
SOC-Kali
10.10.10.103
```

and targeted:

```text
SOC-Ubuntu
10.50.20.100
```

The controlled activity included:

- Network reconnaissance
- Nmap scanning
- HTTP reconnaissance
- Gobuster enumeration
- Failed SSH authentication

Suricata provided **network-level visibility**, while Wazuh provided **endpoint-level visibility**.

The goal was to combine both perspectives into a single investigation.

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

This phase demonstrated a fundamental SOC capability:

> Reconstructing suspicious activity using evidence collected from multiple security controls.

---

# 🏗️ Detection Architecture

Phase 6 used two primary security-monitoring perspectives.

## Network Perspective

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
    ├── Port
    ├── Signature
    └── Application Data
```

Suricata provided visibility into activity crossing the network.

---

## Endpoint Perspective

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

Wazuh provided visibility into what occurred on the endpoint.

---

## Correlation

```text
Suricata Evidence
       +
Wazuh Evidence
       │
       ▼
Source IP
Destination
Timestamp
Activity
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
- [x] Compare source IP addresses
- [x] Compare destination IP addresses
- [x] Compare timestamps
- [x] Reconstruct suspicious activity
- [x] Document investigation evidence

---

# 🔍 Controlled Nmap Reconnaissance

SOC-Kali was used to generate controlled reconnaissance against SOC-Ubuntu.

```text
Source:
SOC-Kali
10.10.10.103

Target:
SOC-Ubuntu
10.50.20.100
```

The traffic path was:

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

The controlled reconnaissance provided the initial network activity for the Phase 6 investigation.

---

## 📸 Evidence — Nmap Reconnaissance

![Nmap Reconnaissance](../images/phase6-nmap-reconnaissance.png)

The reconnaissance originated from SOC-Kali and targeted the Ubuntu system located in the DMZ.

**Result:** ✅ Controlled reconnaissance successfully generated.

---

# 🚨 Suricata Reconnaissance Detection

Suricata detected the Kali-to-Ubuntu reconnaissance traffic.

Network telemetry provided visibility into:

- Source IP
- Destination IP
- Protocol
- Ports
- Detection signature
- Event timestamp

The detection path was:

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

---

## 📸 Evidence — Suricata Reconnaissance Detection

![Suricata Reconnaissance Detection](../images/phase6-suricata-recon-detection.png)

The Suricata alert provided network evidence associated with the controlled reconnaissance.

**Result:** ✅ Suricata successfully detected the reconnaissance activity.

---

# 🔐 Controlled SSH Authentication Testing

Controlled failed SSH authentication was generated against SOC-Ubuntu.

The purpose was to generate endpoint authentication telemetry that could be investigated through Wazuh and compared with the network evidence.

```text
SOC-Kali
10.10.10.103
      │
      │ SSH Authentication
      ▼
SOC-Ubuntu
10.50.20.100
      │
      ▼
Authentication Failure
```

This created a second source of security evidence associated with the same controlled source system.

---

## 📸 Evidence — Failed SSH Authentication

![Failed SSH Authentication](../images/phase6-ssh-failed-login.png)

The failed SSH login generated Linux authentication telemetry on SOC-Ubuntu.

**Result:** ✅ Controlled endpoint authentication activity successfully generated.

---

# 🛡️ Wazuh SSH Detection

The Wazuh Agent on SOC-Ubuntu collected the authentication telemetry and forwarded it to the centralized Wazuh environment.

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

Wazuh provided endpoint context that network monitoring alone could not provide.

This included information related to:

- Authentication result
- Username
- Source IP
- Target endpoint
- Wazuh rule
- Alert severity
- Timestamp

---

## 📸 Evidence — Wazuh SSH Detection

![Wazuh SSH Detection](../images/phase6-wazuh-ssh-detection.png)

The Wazuh alert demonstrated successful endpoint detection of the controlled SSH authentication activity.

**Result:** ✅ SSH authentication activity detected by Wazuh.

---

## Detailed SSH Event Investigation

The Wazuh event was expanded for deeper investigation.

The detailed event provided additional context including:

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

---

## 📸 Evidence — Wazuh SSH Event Details

![Wazuh SSH Event Details](../images/phase6-wazuh-ssh-event-details.png)

The detailed Wazuh event provided endpoint-level context for the authentication activity.

**Result:** ✅ Endpoint event details successfully investigated.

---

# 🗺️ MITRE ATT&CK Analysis

The Wazuh authentication event was reviewed with MITRE ATT&CK context.

MITRE ATT&CK provides a standardized framework for categorizing behaviors associated with adversary tactics and techniques.

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

MITRE ATT&CK mapping does not automatically prove that an event is malicious.

Instead, it helps the analyst understand how the observed activity may relate to known security behaviors.

---

## 📸 Evidence — MITRE ATT&CK Mapping

![Wazuh MITRE ATT&CK Mapping](../images/phase6-wazuh-mitre-mapping.png)

The authentication event was reviewed alongside its MITRE ATT&CK information.

**Result:** ✅ Authentication activity reviewed with MITRE ATT&CK context.

---

# 🔗 Suricata and Wazuh Correlation

The network and endpoint evidence could now be compared.

### Suricata provided:

```text
Source IP
Destination IP
Protocol
Ports
Network Signature
Timestamp
```

### Wazuh provided:

```text
Source IP
Target Endpoint
Username
Authentication Result
Detection Rule
Severity
Timestamp
MITRE ATT&CK Context
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

This allowed the analyst to compare two different perspectives of related activity.

---

## 📸 Evidence — Suricata SSH Correlation

![Suricata SSH Correlation](../images/phase6-suricata-ssh-correlation.png)

The Suricata network evidence was compared with the endpoint authentication evidence recorded by Wazuh.

**Result:** ✅ Network and endpoint evidence successfully correlated.

---

# 🌐 HTTP Reconnaissance

The investigation was expanded beyond SSH authentication.

Nmap was also used to generate HTTP reconnaissance against SOC-Ubuntu.

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

This produced additional application-layer network telemetry.

---

## 📸 Evidence — Nmap Web Reconnaissance

![Suricata Nmap Web Reconnaissance](../images/phase6-suricata-nmap-web-recon.png)

Suricata detected the web-reconnaissance traffic generated from SOC-Kali.

**Result:** ✅ HTTP reconnaissance successfully observed by Suricata.

---

# 🚨 ET Open Nmap Detection

Suricata's ET Open rules provided additional context for the HTTP reconnaissance.

The detection identified activity associated with the Nmap Scripting Engine.

This demonstrated how IDS signatures can provide more information than simply identifying:

```text
Source IP
Destination IP
Destination Port
```

Application-layer signatures can provide information about the tool or behavior responsible for the traffic.

---

## 📸 Evidence — ET Open Nmap Details

![ET Open Nmap Detection](../images/phase6-incident1-suricata-nmap-details.png)

The ET Open alert provided additional context for the Nmap-generated HTTP reconnaissance.

**Result:** ✅ Nmap HTTP reconnaissance identified through Suricata ET Open detection.

---

# 📂 Gobuster Enumeration

Controlled web enumeration was also generated using Gobuster.

This expanded the investigation from basic reconnaissance into repeated HTTP enumeration.

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

Gobuster generated additional network telemetry that could be analyzed through Suricata.

---

## 📸 Evidence — Gobuster Alerts

![Suricata Gobuster Alerts](../images/phase6-suricata-gobuster-alerts.png)

The alerts demonstrate network visibility during controlled web enumeration.

**Result:** ✅ Gobuster enumeration generated observable network-security telemetry.

---

# 🧩 Incident Correlation

The investigation combined the available evidence into a single sequence of controlled activity.

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
      └──── SSH Authentication Activity
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

Multiple security controls were used to understand the activity.

---

## 📸 Evidence — Wazuh SSH Correlation

![Wazuh SSH Correlation](../images/phase6-incident1-wazuh-ssh-correlation.png)

This evidence documents the Wazuh side of the correlated investigation.

---

## 📸 Evidence — Wazuh SSH Investigation

![Wazuh SSH Investigation](../images/phase6-wazuh-ssh-attack.png)

This provides additional endpoint evidence associated with the SSH portion of the controlled activity.

**Result:** ✅ Multi-source security evidence successfully reconstructed into a correlated investigation.

---

# 💻 Commands Used

The following commands and tools were used to generate controlled activity during Phase 6.

---

## Nmap Reconnaissance

SOC-Kali generated reconnaissance against SOC-Ubuntu:

```bash
nmap 10.50.20.100
```

Target:

```text
SOC-Ubuntu
10.50.20.100
```

The resulting network activity was investigated through Suricata.

---

## Service Discovery

Nmap service detection was used to gather additional information about exposed services:

```bash
nmap -sV 10.50.20.100
```

This generated additional network telemetry for Suricata analysis.

---

## SSH Authentication Test

SSH was used from SOC-Kali against the controlled Ubuntu target:

```bash
ssh <test-user>@10.50.20.100
```

Controlled failed authentication generated Linux security telemetry that was collected by Wazuh.

---

## HTTP Reconnaissance

Nmap HTTP reconnaissance was used against the controlled Ubuntu web service.

The resulting traffic was investigated through Suricata and ET Open detections.

---

## Gobuster Enumeration

Gobuster was used against the controlled SOC-Ubuntu web service.

The traffic followed:

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
Suricata Detection
```

---

## Command Reference

| Purpose | Tool / Command |
|---|---|
| Network reconnaissance | `nmap 10.50.20.100` |
| Service discovery | `nmap -sV 10.50.20.100` |
| SSH authentication test | `ssh <test-user>@10.50.20.100` |
| HTTP reconnaissance | Nmap HTTP reconnaissance |
| Web enumeration | Gobuster |
| Network investigation | Suricata / OPNsense |
| Endpoint investigation | Wazuh |
| Correlation | Source IP + destination + timestamp + activity |

---

# 🧪 Validation

Phase 6 validated the multi-source monitoring workflow.

| Test | Detection Source | Result |
|---|---|---|
| Nmap reconnaissance | Suricata | ✅ Detected |
| Kali-to-Ubuntu reconnaissance | Suricata | ✅ Detected |
| Failed SSH authentication | Wazuh | ✅ Detected |
| SSH event details | Wazuh | ✅ Investigated |
| MITRE ATT&CK context | Wazuh | ✅ Validated |
| SSH network evidence | Suricata | ✅ Correlated |
| HTTP reconnaissance | Suricata | ✅ Detected |
| Nmap HTTP activity | ET Open / Suricata | ✅ Detected |
| Gobuster enumeration | Suricata | ✅ Observed |
| Cross-platform correlation | Suricata + Wazuh | ✅ Completed |

The complete validation workflow was:

```text
Generate
   │
   ▼
Detect
   │
   ▼
Investigate
   │
   ▼
Correlate
   │
   ▼
Document

   ✅
```

---

# 🔧 Troubleshooting Methodology

Phase 6 reinforced that successfully generating traffic does not automatically prove that monitoring is operational.

Multiple layers must work correctly.

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

---

## Network Detection Troubleshooting

Verify:

1. SOC-Kali can reach SOC-Ubuntu.
2. Traffic crosses OPNsense.
3. Suricata is running.
4. Suricata is processing packets.
5. The correct interface is monitored.
6. Relevant detection rules are enabled.
7. Alerts appear in Suricata.

---

## Endpoint Detection Troubleshooting

Verify:

1. The activity reached SOC-Ubuntu.
2. Ubuntu generated the expected local log.
3. The Wazuh Agent is running.
4. The Wazuh Agent can communicate with the Wazuh Manager.
5. The event was collected.
6. Wazuh processed the event.
7. A Wazuh rule generated the expected alert.

This prevents incorrectly assuming that a missing alert automatically means the monitoring platform is broken.

---

# 💡 Lessons Learned

## 1. One Alert Rarely Provides the Complete Picture

A network alert may identify suspicious communication without showing what happened on the endpoint.

An endpoint alert may identify failed authentication without showing the network activity that preceded it.

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
   ├── Rule
   └── MITRE ATT&CK
```

Together, they provide a more complete investigation.

---

## 3. Suricata Can Provide Early Reconnaissance Context

Network reconnaissance may occur before authentication attempts or other endpoint activity.

Network IDS telemetry can therefore provide earlier context in an incident timeline.

---

## 4. ET Open Signatures Add Application Context

The Nmap HTTP detection demonstrated that IDS signatures can identify characteristics associated with reconnaissance tools.

This provides more context than IP addresses and ports alone.

---

## 5. Wazuh Provides Endpoint Context

Wazuh provided authentication information that network monitoring alone could not provide.

This included endpoint and authentication-related information.

---

## 6. Source IP and Time Are Valuable Correlation Points

Different security platforms can often be correlated using:

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

## 7. MITRE ATT&CK Helps Translate Raw Events

MITRE ATT&CK provides a standardized framework for describing security behaviors.

It helps move an investigation from:

```text
Raw Alert
```

toward:

```text
Recognizable Security Behavior
```

---

## 8. Controlled Testing Validates Security Controls

Controlled security testing provides repeatable evidence that monitoring systems can observe expected activity.

---

## 9. Traffic Generation Alone Is Not Validation

Successfully running Nmap, Gobuster, or SSH does not prove that monitoring worked.

The resulting alert must be confirmed in the corresponding security platform.

---

## 10. End-to-End Monitoring Requires Every Layer

Network connectivity, IDS operation, endpoint logging, Wazuh Agent collection, and SIEM processing must all function correctly.

---

## 11. Correlation Is a Core SOC Workflow

Phase 6 demonstrated:

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
| **SOC Monitoring** | Investigated security events across multiple controls |
| **Event Correlation** | Correlated Suricata and Wazuh evidence |
| **Network IDS Analysis** | Investigated Suricata detections |
| **SIEM Analysis** | Investigated Wazuh endpoint alerts |
| **Nmap** | Generated controlled reconnaissance |
| **SSH Analysis** | Investigated authentication failures |
| **HTTP Reconnaissance** | Generated and investigated web reconnaissance |
| **Gobuster** | Generated controlled HTTP enumeration |
| **ET Open Analysis** | Investigated Nmap-related detection |
| **MITRE ATT&CK** | Added adversary-behavior context |
| **Incident Reconstruction** | Combined network and endpoint evidence |
| **Detection Validation** | Confirmed expected security alerts |
| **Troubleshooting** | Validated the monitoring pipeline layer by layer |
| **Documentation** | Preserved investigation evidence and findings |

---

# 📸 Evidence Summary

Phase 6 contains **12 screenshots** documenting the security-monitoring and event-correlation workflow.

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

### Image Paths

```text
../images/phase6-nmap-reconnaissance.png
../images/phase6-suricata-recon-detection.png
../images/phase6-ssh-failed-login.png
../images/phase6-wazuh-ssh-detection.png
../images/phase6-wazuh-ssh-event-details.png
../images/phase6-wazuh-mitre-mapping.png
../images/phase6-suricata-ssh-correlation.png
../images/phase6-suricata-nmap-web-recon.png
../images/phase6-incident1-suricata-nmap-details.png
../images/phase6-suricata-gobuster-alerts.png
../images/phase6-incident1-wazuh-ssh-correlation.png
../images/phase6-wazuh-ssh-attack.png
```

No Phase 6 screenshots need to be renamed or duplicated.

---

# 🏁 Phase Outcome

## ✅ Phase 6 Complete

Phase 6 successfully demonstrated an end-to-end security incident generation, detection, investigation, and correlation workflow.

Controlled reconnaissance, HTTP enumeration, and SSH authentication activity originated from:

```text
SOC-Kali
10.10.10.103
```

and targeted:

```text
SOC-Ubuntu
10.50.20.100
```

Suricata provided network-level visibility into:

- Reconnaissance
- HTTP activity
- Network communication
- Nmap activity
- ET Open detections
- Gobuster enumeration

Wazuh provided endpoint-level visibility into:

- Failed SSH authentication
- Source information
- Authentication context
- Alert severity
- Raw authentication events
- MITRE ATT&CK mappings

The evidence was then correlated:

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

The phase demonstrated a core SOC analyst capability:

> **Reconstructing suspicious activity using evidence collected from multiple security controls.**

Phase 6 established the workflow:

```text
Generate → Detect → Investigate → Correlate → Document
```

and prepared the environment for vulnerability assessment and remediation.

---

# ➡️ Next Phase

## Phase 07 — Vulnerability Assessment & Remediation

Phase 7 moves from security monitoring into vulnerability management.

The next phase focuses on:

- Nmap service discovery
- Vulnerability identification
- Risk assessment
- Apache security assessment
- Apache hardening
- Remediation
- Validation scanning
- Before-and-after security comparison

---

[← Phase 05](phase-05-suricata-ids.md) | [🏠 Back to Main Project](../README.md) | [Phase 07 →](phase-07-vulnerability-management.md)

---

### Enterprise Security Operations Lab

**SOC Operations • Event Correlation • Suricata • Wazuh SIEM/XDR • MITRE ATT&CK • Network Security Monitoring**
