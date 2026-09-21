# 🛡️ Enterprise Security Operations Lab

![Enterprise Security Operations Lab](images/diagram.png)

> **Enterprise-style SOC homelab demonstrating network security, SIEM/XDR, IDS, endpoint monitoring, detection engineering, vulnerability management, threat intelligence, security automation, incident response, and end-to-end SOC investigation.**

---

## 📑 Table of Contents

- [Project Overview](#-project-overview)
- [Lab Architecture](#️-lab-architecture)
- [Network Architecture](#-network-architecture)
- [SOC Workflow](#-soc-workflow)
- [Project Highlights](#-project-highlights)
- [Project Documentation](#-project-documentation)
- [Technology Stack](#️-technology-stack)
- [Skills Demonstrated](#-skills-demonstrated)
- [Detection & Investigation](#-detection--investigation)
- [Security Automation](#-security-automation)
- [Troubleshooting Experience](#-troubleshooting-experience)
- [Repository Structure](#-repository-structure)
- [Project Outcome](#-project-outcome)
- [Disclaimer](#️-disclaimer)

---

# 📋 Project Overview

The **Enterprise Security Operations Lab** is a multi-system cybersecurity homelab designed to simulate the technologies and workflows used by a Security Operations Center.

The environment was built from the ground up in VirtualBox using a resource-efficient five-primary-VM architecture.

The project integrates:

- Network segmentation
- Firewall administration
- IDS monitoring
- Windows endpoint telemetry
- Linux endpoint monitoring
- SIEM/XDR
- Centralized logging
- Detection and event correlation
- Vulnerability assessment
- Threat intelligence
- Python security automation
- PostgreSQL security operations
- Web application security
- API integration
- Automated SOC email notification
- Incident response
- Case management
- MITRE ATT&CK mapping

The goal was not simply to install security tools.

The goal was to build an environment where security activity could move through a complete operational lifecycle:

```text
Generate
   ↓
Monitor
   ↓
Detect
   ↓
Correlate
   ↓
Automate
   ↓
Investigate
   ↓
Respond
   ↓
Document
   ↓
Validate
```

---

# 🏗️ Lab Architecture

The environment uses five primary virtual machines.

| System | Role | Primary Technologies |
|---|---|---|
| **SOC-OPNsense** | Firewall / Network Security | OPNsense, Suricata |
| **SOC-Windows11** | Windows Endpoint | Windows 11, Sysmon, Wazuh Agent |
| **SOC-Ubuntu** | Linux Endpoint / DMZ Target | Ubuntu, auditd, osquery, Wazuh Agent, Apache, OWASP Juice Shop |
| **SOC-Wazuh** | Security Server | Wazuh, PostgreSQL, SecurityOpsDB, Python Automation |
| **SOC-Kali** | Analyst Workstation | Kali Linux, Nmap, web-security and investigation tools, DFIR-IRIS |

### Core Architecture

```text
                         Internet / NAT
                              │
                              ▼
                        SOC-OPNsense
                    Firewall + Suricata
                              │
              ┌───────────────┴───────────────┐
              │                               │
              ▼                               ▼
          SOC-LAN                           SOC-DMZ
       10.10.10.0/24                    10.50.20.0/24
              │                               │
       ┌──────┼──────┐                        │
       │      │      │                        │
       ▼      ▼      ▼                        ▼
    Windows  Wazuh   Kali                  Ubuntu
              │                               │
              └──────── Security Telemetry ───┘
                              │
                              ▼
                            Wazuh
                              │
                 ┌────────────┼────────────┐
                 │            │            │
                 ▼            ▼            ▼
             Detection    Correlation   Automation
                                           │
                                           ▼
                                       SOC Email
                                           │
                                           ▼
                                        Analyst
                                           │
                                           ▼
                                       DFIR-IRIS
                                           │
                                           ▼
                                    Incident Response
```

---

# 🌐 Network Architecture

## Security LAN

```text
Network: 10.10.10.0/24
Gateway: 10.10.10.1
```

Primary systems include:

```text
SOC-OPNsense
SOC-Windows11
SOC-Wazuh
SOC-Kali
```

## DMZ

```text
Network: 10.50.20.0/24
Gateway: 10.50.20.1
```

Primary target:

```text
SOC-Ubuntu
10.50.20.100
```

OPNsense controls communication between network segments while Suricata provides network IDS visibility.

The segmented design allows controlled security testing while preserving network boundaries.

---

# 🔄 SOC Workflow

The completed environment demonstrates a complete security-operations workflow.

```text
Security Activity
       │
       ▼
OPNsense / Suricata
       │
       ▼
Endpoint Telemetry
       │
       ▼
Wazuh SIEM/XDR
       │
       ▼
Detection
       │
       ▼
Correlation
       │
       ▼
Python Automation
       │
       ▼
SOC Notification
       │
       ▼
Analyst Investigation
       │
       ▼
DFIR-IRIS
       │
       ▼
Incident Response
       │
       ▼
Documentation / Closure
```

This provides hands-on experience across the security-event lifecycle rather than focusing on one isolated security product.

---

# ⭐ Project Highlights

### 🛡️ Network Segmentation

Built separate Security LAN and DMZ networks using OPNsense with controlled firewall rules between security zones.

### 🔎 Endpoint Monitoring

Implemented Windows and Linux security telemetry using:

```text
Sysmon
Windows Event Logging
auditd
osquery
Wazuh Agents
```

### 📊 SIEM/XDR

Deployed Wazuh for:

- Centralized security monitoring
- Authentication detection
- Windows process monitoring
- File Integrity Monitoring
- Event correlation
- MITRE ATT&CK mapping

### 🚨 Network IDS

Configured Suricata on OPNsense and validated detections using controlled reconnaissance and HTTP activity.

### 🔗 Event Correlation

Correlated network and endpoint activity to reconstruct security events across multiple systems.

### 🔐 Vulnerability Management

Performed service discovery, vulnerability assessment, remediation, and post-remediation validation.

### 🤖 Security Automation

Integrated Python with PostgreSQL SecurityOpsDB to process incidents and automate security workflow decisions.

### 🌐 Threat Intelligence

Processed external IOC intelligence and correlated known malicious IP addresses against local security data.

### 📡 Centralized Logging

Forwarded network security telemetry into Wazuh for centralized analysis.

### 🗂️ Incident Response

Deployed DFIR-IRIS and performed structured incident investigations with:

- Cases
- Assets
- IOCs
- Timelines
- Tasks
- Findings
- Closure

### 🌍 Web Application Security

Deployed OWASP Juice Shop and performed controlled:

- Service discovery
- Technology fingerprinting
- Vulnerability enumeration
- Security analysis
- Application troubleshooting

### 📧 Automated SOC Alerting

Built a custom:

```text
Wazuh
  ↓
Python
  ↓
Gmail API
  ↓
OAuth 2.0
  ↓
SOC Email
```

notification pipeline.

### 🏁 End-to-End Incident Response

Completed a controlled SSH incident investigation from activity generation through detection, correlation, investigation, response assessment, documentation, and formal closure.

---

# 📚 Project Documentation

Detailed implementation, commands, troubleshooting, evidence, screenshots, and lessons learned are separated into individual phase documents.

| Phase | Documentation | Focus |
|---|---|---|
| **01** | [VirtualBox Environment](docs/phase-01-virtualbox-environment.md) | Lab foundation and VM deployment |
| **02** | [Network Segmentation](docs/phase-02-network-segmentation.md) | OPNsense, LAN/DMZ, firewall rules |
| **03** | [Endpoint Monitoring](docs/phase-03-endpoint-monitoring.md) | Windows, Linux, Sysmon, auditd, osquery |
| **04** | [Wazuh SIEM/XDR](docs/phase-04-wazuh-siem.md) | SIEM deployment, alerts, FIM |
| **05** | [Suricata IDS](docs/phase-05-suricata-ids.md) | IDS deployment and detection |
| **06** | [Security Monitoring](docs/phase-06-security-monitoring.md) | Detection and event correlation |
| **07** | [Vulnerability Management](docs/phase-07-vulnerability-management.md) | Assessment, remediation, validation |
| **08** | [Security Automation](docs/phase-08-security-automation.md) | Python, PostgreSQL, SecurityOpsDB |
| **09** | [Threat Intelligence](docs/phase-09-threat-intelligence.md) | IOC processing and correlation |
| **10** | [Centralized Logging](docs/phase-10-centralized-logging.md) | OPNsense → Wazuh telemetry |
| **11** | [Incident Response](docs/phase-11-incident-response.md) | DFIR-IRIS case management |
| **12** | [Web Application Security](docs/phase-12-web-security.md) | Juice Shop, Nmap, WhatWeb, Nikto |
| **13** | [Email Automation](docs/phase-13-email-automation.md) | Python, Gmail API, OAuth 2.0, Wazuh |
| **14** | [End-to-End SOC Response](docs/phase-14-end-to-end-soc-response.md) | Detection → correlation → IR → closure |

> Each phase contains its own technical evidence and troubleshooting history so the main README remains concise and easy to review.

---

# 🛠️ Technology Stack

| Category | Technologies |
|---|---|
| **Virtualization** | VirtualBox |
| **Firewall / Routing** | OPNsense |
| **Network IDS** | Suricata |
| **SIEM / XDR** | Wazuh |
| **Windows Telemetry** | Sysmon, Windows Event Logs |
| **Linux Telemetry** | auditd, osquery |
| **Analyst Platform** | Kali Linux |
| **Network Discovery** | Nmap |
| **Web Security** | OWASP Juice Shop, WhatWeb, Nikto |
| **Incident Response** | DFIR-IRIS |
| **Database** | PostgreSQL / SecurityOpsDB |
| **Automation** | Python |
| **Data Formats** | JSON, CSV |
| **Threat Intelligence** | IOC feeds / IPSum |
| **API Integration** | Gmail API |
| **Authorization** | OAuth 2.0 |
| **Framework** | MITRE ATT&CK |

---

# 🧠 Skills Demonstrated

## SOC Operations

- Security monitoring
- Alert triage
- Event investigation
- Network telemetry analysis
- Endpoint telemetry analysis
- Cross-system correlation
- Incident documentation
- Case closure

## Network Security

- Firewall administration
- Network segmentation
- LAN/DMZ architecture
- IDS monitoring
- Firewall-rule validation
- Service discovery
- Controlled reconnaissance

## SIEM / Detection Engineering

- Wazuh administration
- Agent deployment
- Authentication monitoring
- Process monitoring
- File Integrity Monitoring
- Rule analysis
- Alert severity analysis
- MITRE ATT&CK mapping
- Raw JSON log validation

## Security Automation

- Python scripting
- JSON parsing
- CSV reporting
- PostgreSQL integration
- API integration
- OAuth 2.0
- Custom Wazuh integrations
- Automated SOC notifications

## Vulnerability Management

- Asset discovery
- Service enumeration
- Vulnerability scanning
- Security hardening
- Remediation
- Rescanning
- Validation

## Incident Response

- Case creation
- Asset documentation
- IOC documentation
- Timeline reconstruction
- Investigation tasks
- Containment assessment
- Remediation assessment
- Recovery assessment
- Formal incident closure

---

# 🔍 Detection & Investigation

The project generated controlled security activity to validate monitoring and investigation capabilities.

Examples include:

```text
Nmap Reconnaissance
        │
        ▼
Suricata Detection
```

```text
SSH Authentication Failures
        │
        ▼
Wazuh Authentication Detection
        │
        ▼
Repeated Event Correlation
        │
        ▼
Rule 2502 — Level 10
```

```text
Windows File Modification
        │
        ▼
Wazuh File Integrity Monitoring
```

```text
Threat Intelligence IOC
        │
        ▼
Python IOC Lookup
        │
        ▼
SecurityOpsDB Incident
```

The emphasis throughout the project was on validating detections with controlled activity and supporting conclusions with evidence.

---

# 🤖 Security Automation

A major project focus was moving beyond manual monitoring.

## PostgreSQL Automation

```text
Security Incident
      │
      ▼
SecurityOpsDB
      │
      ▼
Python
      │
      ▼
Decision Logic
      │
      ▼
Status Update
      │
      ▼
Audit Log
```

## Automated SOC Notification

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
Python
      │
      ▼
OAuth 2.0
      │
      ▼
Gmail API
      │
      ▼
SOC Email Alert
```

This demonstrated practical integration between SIEM telemetry, Python automation, APIs, databases, and analyst workflows.

---

# 🔧 Troubleshooting Experience

The project intentionally documents troubleshooting rather than showing only successful final configurations.

Examples include:

- Wazuh agent connectivity
- TCP validation across segmented networks
- OPNsense firewall-rule ordering
- Suricata configuration vs service state
- Suricata packet-processing validation
- False-positive detection tuning
- Wazuh FIM XML configuration errors
- PostgreSQL schema/column errors
- Python logic and formatting errors
- Linux file permissions
- Docker application availability
- OAuth 2.0 authorization errors
- Wazuh custom integration execution
- Timezone alignment during incident investigation

One of the most important lessons throughout the project was:

```text
Configuration Valid
       ≠
Service Running
       ≠
Traffic / Events Being Processed
       ≠
End-to-End Workflow Validated
```

Each layer must be tested independently.

---

# 📁 Repository Structure

```text
enterprise-security-operations-lab/
│
├── README.md
│
├── docs/
│   ├── phase-01-virtualbox-environment.md
│   ├── phase-02-network-segmentation.md
│   ├── phase-03-endpoint-monitoring.md
│   ├── phase-04-wazuh-siem.md
│   ├── phase-05-suricata-ids.md
│   ├── phase-06-security-monitoring.md
│   ├── phase-07-vulnerability-management.md
│   ├── phase-08-security-automation.md
│   ├── phase-09-threat-intelligence.md
│   ├── phase-10-centralized-logging.md
│   ├── phase-11-incident-response.md
│   ├── phase-12-web-security.md
│   ├── phase-13-email-automation.md
│   └── phase-14-end-to-end-soc-response.md
│
├── images/
│   └── Project screenshots and evidence
│
├── scripts/
│   └── Security automation scripts
│
├── configs/
│   └── Sanitized configuration examples
│
└── reports/
    └── Security assessment and automation reports
```

Detailed screenshots remain in `images/` and are referenced from the individual phase documents.

---

# 🏁 Project Outcome

## ✅ Enterprise Security Operations Lab Complete

The final environment demonstrates a practical security-operations lifecycle:

```text
BUILD
  │
  ▼
SEGMENT
  │
  ▼
MONITOR
  │
  ▼
DETECT
  │
  ▼
CORRELATE
  │
  ▼
AUTOMATE
  │
  ▼
INVESTIGATE
  │
  ▼
RESPOND
  │
  ▼
DOCUMENT
  │
  ▼
IMPROVE
```

The final Phase 14 investigation demonstrated the integration of multiple security layers:

```text
Controlled Security Activity
          │
          ▼
Suricata + Wazuh
          │
          ▼
Detection & Correlation
          │
          ▼
SOC Investigation
          │
          ▼
DFIR-IRIS Case Management
          │
          ▼
Response Assessment
          │
          ▼
Formal Case Closure
```

The project demonstrates hands-on experience building, troubleshooting, integrating, and operating security technologies rather than only completing isolated tool installations.

---

# 🎯 Portfolio Focus

This repository is designed to demonstrate practical experience relevant to roles including:

```text
SOC Analyst
Cybersecurity Analyst
Security Operations Analyst
Junior Security Engineer
Cloud / Infrastructure Security
```

The project emphasizes:

- Technical implementation
- Security operations
- Troubleshooting
- Detection validation
- Automation
- Investigation methodology
- Documentation
- Evidence-based conclusions

---

# 📸 Evidence

Technical evidence is stored under:

```text
images/
```

and linked directly from the corresponding phase documentation.

This keeps the main README concise while preserving detailed technical proof for reviewers who want to investigate a specific phase.

---

# 🔐 Security & Credential Handling

Sensitive authentication material is intentionally excluded from the public portfolio.

Examples include:

```text
OAuth tokens
API credentials
Client secrets
Passwords
Private authentication material
```

Only sanitized configuration examples and technical evidence should be committed.

---

# ⚠️ Disclaimer

All scanning, authentication testing, vulnerability assessment, and security-event generation documented in this repository was performed inside an authorized personal lab environment.

The techniques demonstrated here are intended for:

- Defensive security education
- Security monitoring
- Detection engineering
- Incident response practice
- Authorized security testing

---

## 🛡️ Enterprise Security Operations Lab

**Wazuh • Suricata • OPNsense • Python • PostgreSQL • DFIR-IRIS • Gmail API • OAuth 2.0 • MITRE ATT&CK**

**Status: ✅ Complete — 14/14 Phases**
