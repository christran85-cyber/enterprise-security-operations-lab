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
| **Network Detection** | Suricata |
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

Instead of investigating alerts from only one security control, this phase demonstrated how a SOC analyst can correlate evidence from multiple sources.

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

The activity included:

- Network reconnaissance
- Nmap scanning
- HTTP reconnaissance
- Gobuster enumeration
- Failed SSH authentication

Suricata provided **network-level visibility**, while Wazuh provided **endpoint-level visibility**.

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

This demonstrated a fundamental SOC capability:

> Reconstructing suspicious activity using evidence collected from multiple security controls.

---

# 🏗️ Detection Architecture

The Phase 6 investigation used two primary security-monitoring perspectives.

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

## Correlation

```text
Suricata Evidence
       +
Wazuh Evidence
       │
       ▼
Source IP
Timestamp
Target
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

The reconnaissance provided the initial activity for the investigation.

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

---

## 📸 Evidence — Nmap Reconnaissance

![Nmap Reconnaissance](../images/phase6-nmap-reconnaissance.png)

This evidence documents the controlled reconnaissance generated from SOC-Kali against SOC-Ubuntu.

**Result:** ✅ Controlled reconnaissance successfully generated.

---

# 🚨 Suricata Reconnaissance Detection

Suricata detected the Kali-to-Ubuntu reconnaissance traffic.

Network-level telemetry provided visibility into:

- Source IP
- Destination IP
- Network protocol
- Ports
- Detection signature
- Event timestamp

The detection established the first half of the incident-correlation workflow.

```text
SOC-Kali
10.10.10.103
      │
      ▼
Reconnaissance
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

**Result:** ✅ Suricata detected the controlled reconnaissance activity.

---

# 🔐 Controlled SSH Authentication Testing

Controlled failed SSH authentication was generated against SOC-Ubuntu.

The purpose was to create endpoint authentication telemetry that could be investigated in Wazuh and correlated with the network evidence.

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

This provided endpoint evidence associated with activity originating from the same controlled Kali system.

---

## 📸 Evidence — Failed SSH Login

![Failed SSH Authentication](../images/phase6-ssh-failed-login.png)

The controlled SSH authentication failure generated Linux authentication telemetry on SOC-Ubuntu.

**Result:** ✅ Controlled endpoint authentication activity successfully generated.

---

# 🛡️ Wazuh SSH Detection

The Wazuh Agent on SOC-Ubuntu collected the authentication telemetry and forwarded it to the centralized Wazuh environment.

The monitoring path was:

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

Wazuh provided endpoint-level information that Suricata alone could not provide, including authentication and username context. :contentReference[oaicite:1]{index=1}

---

## 📸 Evidence — Wazuh SSH Detection

![Wazuh SSH Detection](../images/phase6-wazuh-ssh-detection.png)

**Result:** ✅ Wazuh detected the SSH authentication activity.

---

## Detailed SSH Event Investigation

The Wazuh event was expanded for deeper investigation.

The detailed event provided additional context such as:

- Source IP
- Target endpoint
- Username
- Authentication result
- Detection rule
- Alert severity
- Raw authentication information
- Timestamp

---

## 📸 Evidence — Wazuh SSH Event Details

![Wazuh SSH Event Details](../images/phase6-wazuh-ssh-event-details.png)

The detailed event provided endpoint context required for investigation.

**Result:** ✅ Endpoint event details successfully analyzed.

---

# 🗺️ MITRE ATT&CK Analysis

Wazuh provided MITRE ATT&CK context for the SSH authentication event.

This helped translate the raw security event into a standardized attacker-behavior framework.

```text
Authentication Event
       │
       ▼
Wazuh Detection
       │
       ▼
MITRE ATT&CK Mapping
       │
       ▼
Security Context
```

MITRE ATT&CK information helps analysts understand how observed behavior may relate to common adversary techniques.

It does not automatically prove malicious intent.

The event must still be evaluated in context.

---

## 📸 Evidence — MITRE ATT&CK Mapping

![Wazuh MITRE ATT&CK Mapping](../images/phase6-wazuh-mitre-mapping.png)

**Result:** ✅ Authentication activity reviewed with MITRE ATT&CK context.

---

# 🔗 Suricata and Wazuh Correlation

The network and endpoint evidence could now be compared.

Suricata provided:

```text
Source IP
Destination IP
Network Protocol
Ports
Network Signature
Timestamp
```

Wazuh provided:

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

This provided two different perspectives on related activity.

---

## 📸 Evidence — Suricata SSH Correlation

![Suricata SSH Correlation](../images/phase6-suricata-ssh-correlation.png)

This network evidence was compared with the endpoint authentication evidence recorded by Wazuh.

**Result:** ✅ Network and endpoint evidence successfully correlated.

---

# 🌐 HTTP Reconnaissance

The investigation was expanded beyond SSH authentication.

Nmap was also used to generate HTTP reconnaissance against SOC-Ubuntu.

This provided additional application-layer network telemetry.

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

---

## 📸 Evidence — Nmap Web Reconnaissance

![Suricata Nmap Web Reconnaissance](../images/phase6-suricata-nmap-web-recon.png)

Suricata detected the web-reconnaissance traffic.

**Result:** ✅ HTTP reconnaissance successfully observed by Suricata.

---

# 🚨 ET Open Nmap Detection

Suricata's ET Open rules provided additional context for the HTTP reconnaissance.

The detection identified activity associated with the **Nmap Scripting Engine**.

This was important because application-layer information provided more context than simply identifying:

```text
Source IP
Destination IP
Port
```

Instead, the detection provided information about the tool responsible for the traffic.

The original Phase 6 investigation specifically identified an ET Open detection for the Nmap HTTP User-Agent. :contentReference[oaicite:2]{index=2}

---

## 📸 Evidence — ET Open Nmap Details

![ET Open Nmap Detection](../images/phase6-incident1-suricata-nmap-details.png)

The alert demonstrated how IDS signatures can identify application-layer characteristics associated with reconnaissance tools.

**Result:** ✅ Nmap HTTP reconnaissance identified through ET Open detection.

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

Gobuster activity generated additional Suricata evidence that could be compared with the earlier reconnaissance.

---

## 📸 Evidence — Gobuster Alerts

![Suricata Gobuster Alerts](../images/phase6-suricata-gobuster-alerts.png)

The alerts demonstrate network visibility during controlled web enumeration.

**Result:** ✅ Gobuster enumeration generated observable network-security telemetry.

---

# 🧩 Incident Correlation

The investigation combined the available evidence into a single activity sequence.

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

Instead, multiple data sources were used to understand the activity.

---

## 📸 Evidence — Wazuh SSH Correlation

![Wazuh SSH Correlation](../images/phase6-incident1-wazuh-ssh-correlation.png)

This evidence documents the Wazuh side of the correlated investigation.

---

## 📸 Evidence — Wazuh SSH Attack Investigation

![Wazuh SSH Attack](../images/phase6-wazuh-ssh-attack.png)

This provides additional endpoint evidence associated with the SSH portion of the controlled incident.

**Result:** ✅ Multi-source security evidence successfully reconstructed into a correlated investigation.

---

# 💻 Commands Used

The following commands represent the primary controlled testing performed during the Phase 6 investigation.

## Nmap Reconnaissance

Target:

```text
10.50.20.100
```

Nmap was used from SOC-Kali to generate controlled reconnaissance against SOC-Ubuntu.

Example Phase 6 reconnaissance workflow:

```bash
nmap 10.50.20.100
```

The generated traffic was then verified in Suricata.

---

## Service and Version Discovery

Service reconnaissance can be performed against the controlled target using:

```bash
nmap -sV 10.50.20.100
```

This provides service information while generating network telemetry that can be investigated through Suricata.

---

## SSH Authentication Test

SSH was used from SOC-Kali against the controlled Ubuntu target:

```bash
ssh <test-user>@10.50.20.100
```

A controlled failed login generated authentication telemetry for Wazuh investigation.

> Use the same controlled test account/username documented in your lab rather than real credentials.

---

## HTTP Reconnaissance

Nmap HTTP functionality was used against the controlled Ubuntu web service to generate application-layer reconnaissance traffic.

The resulting HTTP activity was investigated through Suricata and ET Open detections.

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

The resulting Suricata alerts were documented as Phase 6 evidence.

---

## Command Reference

| Purpose | Tool / Command |
|---|---|
| Network reconnaissance | `nmap 10.50.20.100` |
| Service discovery | `nmap -sV 10.50.20.100` |
| SSH test | `ssh <test-user>@10.50.20.100` |
| Web reconnaissance | Nmap HTTP reconnaissance |
| Web enumeration | Gobuster |
| Network investigation | Suricata / OPNsense |
| Endpoint investigation | Wazuh |
| Correlation | Source IP + target + timestamp + activity |

---

# 🧪 Validation

Phase 6 validated the end-to-end monitoring workflow.

| Test | Detection Source | Result |
|---|---|---|
| Nmap reconnaissance | Suricata | ✅ Detected |
| Kali-to-Ubuntu reconnaissance | Suricata | ✅ Detected |
| Failed SSH authentication | Wazuh | ✅ Detected |
| SSH event details | Wazuh | ✅ Investigated |
| MITRE ATT&CK context | Wazuh | ✅ Validated |
| SSH network evidence | Suricata | ✅ Correlated |
| HTTP reconnaissance | Suricata | ✅ Detected |
| Nmap HTTP User-Agent | ET Open / Suricata | ✅ Detected |
| Gobuster enumeration | Suricata | ✅ Observed |
| Cross-platform correlation | Suricata + Wazuh | ✅ Completed |

The complete workflow was:

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

Phase 6 reinforced that successful traffic generation does not automatically prove that monitoring is operational.

Multiple layers must work correctly:

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

When expected evidence is missing, the investigation should proceed layer by layer.

## Network Detection Troubleshooting

Verify:

1. Source can reach the target.
2. Traffic crosses OPNsense.
3. Suricata is running.
4. Suricata is processing packets.
5. The correct interface is monitored.
6. Relevant detection rules are enabled.
7. Alerts are appearing in Suricata.

## Endpoint Detection Troubleshooting

Verify:

1. The activity actually reached SOC-Ubuntu.
2. Ubuntu generated the expected local log.
3. The Wazuh Agent is running.
4. The agent can reach the Wazuh Manager.
5. The event was collected.
6. Wazuh processed the event.
7. A detection rule generated an alert.

This avoids assuming that a missing alert automatically means the detection platform is broken.

---

# 💡 Lessons Learned

The original Phase 6 investigation produced several important SOC lessons. :contentReference[oaicite:3]{index=3}

## 1. One Alert Rarely Provides the Complete Picture

A network alert may identify suspicious communication without showing what happened on the endpoint.

An endpoint alert may identify a failed authentication without showing the network activity that preceded it.

Combining both provides better context.

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

Together, they provide stronger investigation evidence.

---

## 3. Suricata Can Identify Reconnaissance Before Endpoint Events

Network reconnaissance can occur before authentication attempts or other endpoint activity.

Network IDS telemetry can therefore provide earlier context in an incident timeline.

---

## 4. ET Open Signatures Add Application Context

The Nmap HTTP User-Agent detection demonstrated that IDS signatures can identify information about the tool generating the traffic.

This provides more context than IP addresses and ports alone.

---

## 5. Wazuh Provides Endpoint Context

Wazuh provided authentication information that network monitoring alone could not provide, including username and authentication results.

---

## 6. Source IP and Time Are Valuable Correlation Points

Two different security platforms can often be correlated using:

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

It helps move the investigation from:

```text
Raw Alert
```

to:

```text
Recognizable Security Behavior
```

---

## 8. Controlled Testing Validates Security Controls

Controlled attack simulation provides repeatable evidence that monitoring systems can observe expected activity.

---

## 9. Traffic Generation Alone Is Not Validation

Successfully running Nmap, Gobuster, or SSH does not prove the security monitoring system worked.

The resulting alert must be confirmed in the corresponding security platform.

---

## 10. End-to-End Monitoring Requires Every Layer

Network connectivity, IDS operation, endpoint logging, Wazuh Agent collection, and SIEM ingestion must all function correctly.

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

This is a fundamental SOC analyst workflow.

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
| **ET Open Analysis** | Investigated Nmap User-Agent detection |
| **MITRE ATT&CK** | Added adversary-behavior context |
| **Incident Reconstruction** | Combined network and endpoint evidence |
| **Detection Validation** | Confirmed expected security alerts |
| **Troubleshooting** | Validated the monitoring pipeline layer by layer |
| **Documentation** | Preserved investigation evidence and findings |

---

# 📸 Evidence Summary

Your original Phase 6 documentation contains **12 screenshots**. :contentReference[oaicite:4]{index=4}

| # | Evidence | Screenshot |
|---|---|---|
| 1 | Nmap reconnaissance | `phase6-nmap-reconnaissance.png` |
| 2 | Suricata reconnaissance detection | `phase6-suricata-recon-detection.png` |
| 3 | Failed SSH authentication | `phase6-ssh-failed-login.png` |
| 4 | Wazuh SSH detection | `phase6-wazuh-ssh-detection.png` |
| 5 | Wazuh SSH event details | `phase6-wazuh-ssh-event-details.png` |
| 6 | Wazuh MITRE mapping | `phase6-wazuh-mitre-mapping.png` |
| 7 | Suricata SSH correlation | `phase6-suricata-ssh-correlation.png` |
| 8 | Suricata Nmap web reconnaissance | `phase6-suricata-nmap-web-recon.png` |
| 9 | ET Open Nmap details | `phase6-incident1-suricata-nmap-details.png` |
| 10 | Suricata Gobuster alerts | `phase6-suricata-gobuster-alerts.png` |
| 11 | Wazuh SSH correlation | `phase6-incident1-wazuh-ssh-correlation.png` |
| 12 | Wazuh SSH attack evidence | `phase6-wazuh-ssh-attack.png` |

All screenshots use:

```text
../images/<filename>
```

No Phase 6 evidence needs to be renamed or duplicated.

---

# 🏁 Phase Outcome

## ✅ Phase 6 Complete

Phase 6 successfully demonstrated an end-to-end security incident generation, detection, investigation, and correlation workflow.

Controlled reconnaissance, HTTP enumeration, and SSH authentication activity were generated from:

```text
SOC-Kali
10.10.10.103
```

against:

```text
SOC-Ubuntu
10.50.20.100
```

Suricata provided network-level visibility into:

- Reconnaissance
- HTTP activity
- Network communication
- Nmap Scripting Engine activity
- ET Open detections
- Gobuster enumeration

Wazuh provided endpoint-level visibility into:

- Failed SSH authentication
- Source IP
- Invalid username
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
- Apache hardening
- Remediation
- Validation scanning
- Before-and-after security comparison

---

[← Phase 05](phase-05-suricata-ids.md) | [🏠 Back to Main Project](../README.md) | [Phase 07 →](phase-07-vulnerability-management.md)

---

### Enterprise Security Operations Lab

**SOC Operations • Event Correlation • Suricata • Wazuh SIEM/XDR • MITRE ATT&CK • Network Security Monitoring**
