# Enterprise Security Operations Lab

![Enterprise Security Operations Lab](images/diagram.png)

## Overview

This project demonstrates the deployment and operation of an enterprise-style Security Operations Center (SOC) environment built from the ground up using VirtualBox.

The lab uses primarily free and open-source cybersecurity tools to simulate security monitoring, threat detection, vulnerability management, network analysis, threat intelligence, incident response, digital forensics, SQL security analytics, and security automation.

The environment was designed around a resource-efficient five-primary-VM architecture. Compatible security services are consolidated, while resource-intensive tools are started only when needed.

The project provides hands-on experience with technologies and analyst workflows related to the CompTIA CySA+ CS0-004 certification.

The lab includes:

- VirtualBox
- OPNsense
- Suricata
- Wazuh SIEM/XDR
- Windows 11
- Microsoft Sysmon
- Ubuntu Linux
- auditd
- osquery
- Kali Linux
- Nmap
- Wireshark
- Greenbone/OpenVAS
- MISP
- DFIR-IRIS
- YARA
- Volatility 3
- Autopsy
- OWASP ZAP
- PostgreSQL
- SQL security analytics
- Python security automation

The objective is to create an integrated cybersecurity environment where security events can be generated, detected, investigated, correlated, documented, remediated, and validated.

---

# Environment

| Component | Purpose |
|---|---|
| VirtualBox | Virtualization platform |
| OPNsense | Firewall, NAT, routing, and segmentation |
| Suricata | Network IDS/IPS |
| Windows 11 | Windows enterprise endpoint |
| Sysmon | Windows endpoint telemetry |
| Ubuntu Linux | Linux endpoint and controlled target |
| auditd | Linux security auditing |
| osquery | Endpoint visibility and querying |
| Wazuh | SIEM/XDR and centralized monitoring |
| Kali Linux | SOC analyst workstation |
| Nmap | Network and service discovery |
| Wireshark | Packet capture and analysis |
| Greenbone/OpenVAS | Vulnerability management |
| MISP | Threat intelligence and IOC management |
| DFIR-IRIS | Incident response and case management |
| YARA | File identification and detection |
| Volatility 3 | Memory forensics |
| Autopsy | Disk and file forensics |
| OWASP ZAP | Web application security testing |
| PostgreSQL | Security operations database |
| Python | Security automation |

---

# Virtual Machine Architecture

The environment uses **five primary virtual machines**.

| VM | Role | Primary Tools |
|---|---|---|
| VM 1 | Network Security | OPNsense + Suricata |
| VM 2 | Windows Endpoint | Windows 11 + Sysmon + Wazuh Agent |
| VM 3 | Linux Endpoint / Target | Ubuntu + auditd + osquery + Wazuh Agent + vulnerable web application |
| VM 4 | Security Server | Wazuh + PostgreSQL + SecurityOpsDB + Python |
| VM 5 | SOC Analyst | Kali + Nmap + Wireshark + ZAP + YARA + Volatility 3 |

## Phase-Specific Tools

Some heavier tools are used only when required:

- Greenbone/OpenVAS
- MISP
- DFIR-IRIS
- Autopsy

This allows the lab to maintain broad security capabilities without requiring every service to run simultaneously.

---

# Network Topology

The environment uses separate VirtualBox network segments.

## Security LAN

| Setting | Value |
|---|---|
| Network | 10.50.10.0/24 |
| Gateway | 10.50.10.1 |
| Firewall | OPNsense |
| IDS/IPS | Suricata |

## DMZ

| Setting | Value |
|---|---|
| Network | 10.50.20.0/24 |
| Gateway | 10.50.20.1 |
| Purpose | Controlled vulnerable services and security testing |
| Firewall | OPNsense |

## Architecture

```text
                         INTERNET
                            |
                     OPNsense VM
                 Firewall + Suricata
                            |
              +-------------+-------------+
              |                           |
        SECURITY LAN                     DMZ
       10.50.10.0/24               10.50.20.0/24
              |                           |
       +------+------+              Ubuntu Target
       |             |              + Web App
   Windows 11      Kali
   Endpoint       Analyst
       |             |
       +------+------+
              |
       Wazuh/Security VM
       |
       +-- Wazuh SIEM/XDR
       +-- PostgreSQL
       +-- SecurityOpsDB
       +-- Python Automation
```

### Architecture Snapshot

![Network Architecture](images/arch2.png)

---

# Project Objectives

- Build an enterprise-style cybersecurity environment in VirtualBox
- Configure network segmentation
- Deploy a firewall
- Implement IDS/IPS monitoring
- Monitor Windows and Linux endpoints
- Deploy centralized SIEM/XDR monitoring
- Collect and correlate security logs
- Perform network discovery
- Analyze network traffic
- Conduct vulnerability assessments
- Analyze CVSS and prioritize vulnerabilities
- Perform threat intelligence analysis
- Investigate Indicators of Compromise
- Manage incident-response cases
- Perform file, memory, and disk analysis
- Test web application security
- Build a security operations SQL database
- Apply SQL skills to cybersecurity data
- Automate security operations with Python
- Conduct end-to-end SOC investigations
- Document remediation and validation

---

# Phase 1: VirtualBox Enterprise Environment

## Build the Virtual Lab

VirtualBox provides the virtualization platform for the entire project.

Five primary virtual machines are created.

### VM 1 — OPNsense

- Firewall
- Routing
- NAT
- Network segmentation
- Suricata IDS/IPS

### VM 2 — Windows 11

- Windows endpoint
- Sysmon
- Wazuh Agent
- Windows Event Logs
- PowerShell logging

### VM 3 — Ubuntu

- Linux endpoint
- auditd
- osquery
- Wazuh Agent
- Controlled vulnerable web application

### VM 4 — Security Server

- Wazuh SIEM/XDR
- PostgreSQL
- SecurityOpsDB
- Python

### VM 5 — Kali Linux

- SOC analyst workstation
- Nmap
- Wireshark
- OWASP ZAP
- YARA
- Volatility 3

## Tasks

- Install VirtualBox
- Create five primary VMs
- Create Security LAN
- Create DMZ
- Configure network adapters
- Configure internet connectivity
- Verify communication
- Verify segmentation

### Snapshot 1 — VirtualBox VM Inventory

![VirtualBox VM Inventory](images/phase1-vms.png)

### Snapshot 2 — VirtualBox Network Configuration

![VirtualBox Network](images/phase1-network.png)

### Snapshot 3 — Windows 11 Network Configuration

![Windows 11 Network Configuration](images/windows11-opnsense-network-config.png)

The Windows 11 SOC endpoint successfully received an IP address from the OPNsense DHCP server on the internal security network.

- IPv4 Address: `10.10.10.123`
- Subnet Mask: `255.255.255.0`
- Default Gateway: `10.10.10.1`

### Snapshot 4 — Windows 11 Network Validation

![Windows 11 Network Validation](images/windows11-network-validation.png)

Connectivity testing confirmed that the Windows 11 endpoint could successfully communicate through the OPNsense security gateway.

- OPNsense gateway (`10.10.10.1`) — reachable
- Internet (`8.8.8.8`) — reachable
- DNS resolution (`google.com`) — successful
- Packet loss — `0%`


### Outcome

A segmented virtual enterprise environment provides the foundation for the security operations lab.

---

# Phase 2: OPNsense Firewall and Segmentation

## Configure OPNsense

OPNsense functions as the primary firewall and gateway.

### Tasks

- Configure WAN
- Configure Security LAN
- Configure DMZ
- Configure NAT
- Configure DHCP
- Create firewall rules
- Restrict inter-network traffic
- Enable security logging

### Snapshot 1 — OPNsense Dashboard

![OPNsense Dashboard](images/phase2-dashboard.png)

### Snapshot 2 — Interfaces

![OPNsense Interfaces](images/phase2-interfaces.png)

### Snapshot 3 — Firewall Rules

![Firewall Rules](images/phase2-firewall-rules.png)

### Outcome

Network traffic is segmented, controlled, and logged by the firewall.

---

# Phase 3: Endpoint Security Monitoring

## Windows 11

The Windows VM represents an enterprise workstation.

### Configuration

- Sysmon
- Wazuh Agent
- Windows Event Logging
- PowerShell logging
- Security auditing

### Snapshot 1 — Windows Endpoint

![Windows Endpoint](images/phase3-windows.png)

### Snapshot 2 — Sysmon Events

![Sysmon](images/phase3-sysmon.png)

### Snapshot 3 — Wazuh Agent

![Windows Wazuh](images/phase3-windows-wazuh.png)

---

## Ubuntu Linux

Ubuntu represents a Linux endpoint and controlled security target.

### Configuration

- auditd
- osquery
- Wazuh Agent
- Authentication logging
- System logging

### Snapshot 4 — Ubuntu Endpoint

![Ubuntu Endpoint](images/phase3-ubuntu.png)

### Snapshot 5 — Linux Security Logs

![Linux Monitoring](images/phase3-linux-monitoring.png)

### Outcome

Windows and Linux systems generate endpoint telemetry for centralized security monitoring.

---

# Phase 4: Wazuh SIEM/XDR

## Centralized Security Monitoring

Wazuh is deployed on the Security Server.

### Data Sources

- Windows Event Logs
- Sysmon
- Linux logs
- auditd
- osquery
- OPNsense
- Suricata

### Monitoring

- Authentication events
- Process activity
- File integrity
- Endpoint telemetry
- Network events
- Security alerts
- Log correlation

### Snapshot 1 — Wazuh Dashboard

![Wazuh Dashboard](images/phase4-dashboard.png)

### Snapshot 2 — Connected Agents

![Wazuh Agents](images/phase4-agents.png)

### Snapshot 3 — Security Alerts

![Wazuh Alerts](images/phase4-alerts.png)

### Outcome

Security events from multiple systems can be monitored and correlated from a centralized platform.

---

# Phase 5: Suricata IDS/IPS

## Network Threat Detection

Suricata runs with OPNsense to monitor network traffic.

### Detection Capabilities

- Port scans
- Reconnaissance
- Suspicious connections
- Protocol anomalies
- IDS signatures
- Known malicious traffic patterns

## Detection Flow

```text
Network Traffic
      |
      v
   OPNsense
      |
      v
   Suricata
      |
      v
     Wazuh
      |
      v
   SOC Alert
```

### Snapshot 1 — Suricata

![Suricata](images/phase5-suricata.png)

### Snapshot 2 — IDS Alert

![Suricata Alert](images/phase5-alert.png)

### Snapshot 3 — Alert in Wazuh

![Wazuh IDS Alert](images/phase5-wazuh.png)

### Outcome

Network detections can be correlated with endpoint telemetry in Wazuh.

---

# Phase 6: Network Security Analysis

## Nmap

Nmap is used from the Kali analyst workstation for authorized discovery of the lab environment.

### Tasks

- Host discovery
- Port identification
- Service identification
- Version detection
- Asset documentation

Example:

```bash
nmap -sV 10.50.10.0/24
```

### Snapshot 1 — Nmap Results

![Nmap](images/phase6-nmap.png)

---

## Wireshark

Wireshark provides packet-level analysis.

### Analysis

- TCP/IP
- DNS
- HTTP
- Network connections
- Protocol behavior
- Suspicious traffic

### Snapshot 2 — Packet Capture

![Wireshark](images/phase6-wireshark.png)

### Snapshot 3 — Packet Analysis

![Packet Analysis](images/phase6-packet-analysis.png)

### Outcome

Network discovery and packet captures provide evidence for security investigations.

---

# Phase 7: Vulnerability Management

## Greenbone/OpenVAS

Greenbone/OpenVAS is brought online during vulnerability-management activities.

It does not need to remain running throughout the entire project.

## Vulnerability Lifecycle

```text
Asset Discovery
      |
      v
Vulnerability Scan
      |
      v
Analyze Findings
      |
      v
CVSS / Risk Priority
      |
      v
Remediation
      |
      v
Rescan
      |
      v
Validation
```

### Tasks

1. Identify assets
2. Configure scan targets
3. Perform scans
4. Review vulnerabilities
5. Analyze CVSS
6. Prioritize findings
7. Remediate
8. Rescan
9. Validate remediation

### Snapshot 1 — OpenVAS Scan

![OpenVAS Scan](images/phase7-scan.png)

### Snapshot 2 — Findings

![OpenVAS Findings](images/phase7-results.png)

### Snapshot 3 — Vulnerability Detail

![Vulnerability Detail](images/phase7-detail.png)

### Snapshot 4 — Rescan

![OpenVAS Rescan](images/phase7-rescan.png)

### Outcome

The complete vulnerability-management lifecycle is demonstrated.

---

# Phase 8: Security Operations SQL Database

## PostgreSQL SecurityOpsDB

PostgreSQL is installed on the Security Server.

The custom `SecurityOpsDB` database stores security information generated throughout the project.

## Tables

```text
Assets
Users
SecurityEvents
Alerts
Vulnerabilities
Incidents
Indicators
NetworkConnections
ScanResults
RemediationActions
IncidentAudit
```

## SQL Skills Demonstrated

- CREATE TABLE
- INSERT
- UPDATE
- DELETE
- SELECT
- WHERE
- JOIN
- GROUP BY
- ORDER BY
- COUNT
- SUM
- AVG
- Date/time functions
- Views
- Triggers
- Functions
- Audit tables

## Example — Critical Vulnerabilities

```sql
SELECT
    Assets.Hostname,
    COUNT(Vulnerabilities.VulnerabilityID) AS CriticalFindings
FROM Assets
JOIN Vulnerabilities
    ON Assets.AssetID = Vulnerabilities.AssetID
WHERE Vulnerabilities.Severity = 'Critical'
GROUP BY Assets.Hostname
ORDER BY CriticalFindings DESC;
```

## Example — Security Events by Source

```sql
SELECT
    SourceIP,
    COUNT(*) AS EventCount
FROM SecurityEvents
GROUP BY SourceIP
ORDER BY EventCount DESC;
```

### Snapshot 1 — SecurityOpsDB

![SecurityOpsDB](images/phase8-database.png)

### Snapshot 2 — Tables

![SecurityOpsDB Tables](images/phase8-tables.png)

### Snapshot 3 — JOIN Analysis

![SQL JOIN](images/phase8-join.png)

### Snapshot 4 — Security Analytics

![SQL Analytics](images/phase8-analytics.png)

### Snapshot 5 — Trigger / Audit

![SQL Audit](images/phase8-audit.png)

### Outcome

SQL is used directly for cybersecurity data storage, correlation, investigation, and reporting.

---

# Phase 9: Threat Intelligence with MISP

## Threat Intelligence

MISP is used as a phase-specific threat intelligence platform.

### IOC Types

- IP addresses
- Domains
- URLs
- File hashes
- Threat indicators

## Workflow

```text
Security Event
      |
      v
Indicator Identified
      |
      v
     MISP
      |
      v
IOC Correlation
      |
      v
Investigation
```

### Snapshot 1 — MISP Dashboard

![MISP Dashboard](images/phase9-misp.png)

### Snapshot 2 — IOC

![MISP IOC](images/phase9-ioc.png)

### Snapshot 3 — IOC Correlation

![MISP Investigation](images/phase9-correlation.png)

### Outcome

Threat intelligence is used to enrich and correlate security investigations.

---

# Phase 10: Incident Response with DFIR-IRIS

## Incident Case Management

DFIR-IRIS is used during the incident-response phase.

### Case Information

- Incident description
- Severity
- Affected systems
- IOCs
- Evidence
- Investigation notes
- Timeline
- Containment
- Remediation
- Resolution

## Incident Lifecycle

```text
Detection
   |
   v
Analysis
   |
   v
Investigation
   |
   v
Containment
   |
   v
Eradication
   |
   v
Recovery
   |
   v
Lessons Learned
```

### Snapshot 1 — DFIR-IRIS Dashboard

![DFIR-IRIS](images/phase10-dfir.png)

### Snapshot 2 — Incident Case

![Incident Case](images/phase10-case.png)

### Snapshot 3 — Timeline

![Incident Timeline](images/phase10-timeline.png)

### Outcome

Security investigations are documented and managed as structured incident-response cases.

---

# Phase 11: Digital Forensics and File Analysis

## YARA

YARA rules are created to identify suspicious test files.

### Snapshot 1 — YARA Rule

![YARA Rule](images/phase11-yara-rule.png)

### Snapshot 2 — YARA Detection

![YARA Detection](images/phase11-yara-detection.png)

---

## Volatility 3

Volatility 3 is used for memory analysis.

### Analysis

- Processes
- Network connections
- Memory artifacts
- Suspicious activity

### Snapshot 3 — Volatility

![Volatility](images/phase11-volatility.png)

---

## Autopsy

Autopsy is used when disk or file-system forensic analysis is required.

### Analysis

- File systems
- Deleted files
- Metadata
- Timeline information
- Evidence artifacts

### Snapshot 4 — Autopsy Investigation

![Autopsy](images/phase11-autopsy.png)

### Outcome

Multiple forensic techniques are used to analyze endpoint evidence.

---

# Phase 12: Web Application Security

## OWASP ZAP

A deliberately vulnerable web application is hosted inside the isolated lab environment.

OWASP ZAP is used from Kali to analyze the application.

### Testing

- Application discovery
- Passive scanning
- Controlled active scanning
- HTTP analysis
- Security header analysis
- Vulnerability identification

### Snapshot 1 — Vulnerable Web Application

![Vulnerable Web Application](images/phase12-webapp.png)

### Snapshot 2 — ZAP Scan

![OWASP ZAP](images/phase12-zap.png)

### Snapshot 3 — Findings

![ZAP Findings](images/phase12-findings.png)

### Outcome

Web application security findings are incorporated into the broader security-analysis workflow.

---

# Phase 13: Python Security Automation

## Automation

Python is used to automate repetitive security-analysis tasks.

### Tasks

- Parse logs
- Process JSON
- Process CSV
- Import vulnerability results
- Import security events
- Search IOCs
- Query PostgreSQL
- Generate reports
- Calculate security statistics

## Automation Flow

```text
Wazuh / Suricata / OpenVAS
            |
            v
      Security Data
            |
            v
          Python
            |
            v
     Parse / Normalize
            |
            v
      SecurityOpsDB
            |
            v
       SQL Analysis
            |
            v
      Security Report
```

### Snapshot 1 — Python Script

![Python Script](images/phase13-python.png)

### Snapshot 2 — Script Execution

![Python Execution](images/phase13-execution.png)

### Snapshot 3 — SQL Import

![Python SQL Import](images/phase13-import.png)

### Outcome

Python connects security data sources with SQL analysis and reduces repetitive analyst work.

---

# Phase 14: Enterprise SOC Investigation

## End-to-End Security Scenario

The final phase integrates the tools and skills demonstrated throughout the project.

Controlled security events are generated only against systems owned and isolated inside the VirtualBox environment.

## Example Events

- Failed authentication
- Network reconnaissance
- Port scanning
- Suspicious PowerShell activity
- Unexpected network connections
- File integrity changes
- Suspicious test files
- IOC matches
- Vulnerability findings
- Web application security findings

## Investigation Workflow

```text
Controlled Security Event
          |
          v
Endpoint / Network Telemetry
          |
          v
Suricata + Sysmon + auditd
          |
          v
        Wazuh
          |
          v
       SOC Alert
          |
          v
Analyst Investigation
          |
          +--> Nmap
          +--> Wireshark
          +--> YARA
          +--> Volatility
          +--> Autopsy
          +--> ZAP
          |
          v
      SQL Analysis
          |
          v
     SecurityOpsDB
          |
          v
     MISP Correlation
          |
          v
    DFIR-IRIS Case
          |
          v
      Containment
          |
          v
      Remediation
          |
          v
    OpenVAS Rescan
          |
          v
       Validation
          |
          v
   Final Incident Report
```

### Snapshot 1 — Security Event

![Security Event](images/phase14-event.png)

### Snapshot 2 — Wazuh Detection

![Wazuh Detection](images/phase14-wazuh.png)

### Snapshot 3 — Suricata Detection

![Suricata Detection](images/phase14-suricata.png)

### Snapshot 4 — Investigation

![Investigation](images/phase14-investigation.png)

### Snapshot 5 — SQL Correlation

![SQL Analysis](images/phase14-sql.png)

### Snapshot 6 — MISP Correlation

![MISP Correlation](images/phase14-misp.png)

### Snapshot 7 — DFIR-IRIS Case

![DFIR-IRIS Case](images/phase14-dfir.png)

### Snapshot 8 — Remediation

![Remediation](images/phase14-remediation.png)

### Snapshot 9 — Validation

![Validation](images/phase14-validation.png)

### Outcome

The final scenario demonstrates a complete security operations workflow:

**Detect → Analyze → Investigate → Correlate → Respond → Remediate → Validate → Report**

---

# CySA+ CS0-004 Skills Demonstrated

## Security Operations

- SIEM/XDR monitoring
- Endpoint telemetry
- Network monitoring
- IDS/IPS analysis
- Firewall analysis
- Log analysis
- IOC analysis
- Threat intelligence
- Security automation

## Vulnerability Management

- Asset discovery
- Vulnerability scanning
- CVSS analysis
- Risk prioritization
- Remediation
- Rescanning
- Validation

## Incident Response

- Detection
- Analysis
- Investigation
- Containment
- Eradication
- Recovery
- Evidence analysis
- Incident documentation
- Lessons learned

## Security Analysis

- Network discovery
- Packet analysis
- Endpoint analysis
- Log correlation
- SQL security analytics
- Threat intelligence correlation
- File analysis
- Memory analysis
- Disk forensics
- Web application analysis

---

# Technology Stack

```text
VirtualBox
|
+-- VM 1: OPNsense
|   +-- Firewall
|   +-- NAT
|   +-- Segmentation
|   +-- Suricata
|
+-- VM 2: Windows 11
|   +-- Sysmon
|   +-- Wazuh Agent
|
+-- VM 3: Ubuntu
|   +-- auditd
|   +-- osquery
|   +-- Wazuh Agent
|   +-- Vulnerable Web Application
|
+-- VM 4: Security Server
|   +-- Wazuh
|   +-- PostgreSQL
|   +-- SecurityOpsDB
|   +-- Python
|
+-- VM 5: Kali Analyst
    +-- Nmap
    +-- Wireshark
    +-- OWASP ZAP
    +-- YARA
    +-- Volatility 3

Phase-Specific Tools
|
+-- Greenbone/OpenVAS
+-- MISP
+-- DFIR-IRIS
+-- Autopsy
```

---

# Repository Structure

```text
enterprise-security-operations-lab/
|
+-- README.md
|
+-- images/
|   +-- front.png
|   +-- network-architecture.png
|   +-- phase1-vms.png
|   +-- phase1-network.png
|   +-- phase2-dashboard.png
|   +-- phase2-interfaces.png
|   +-- phase2-firewall-rules.png
|   +-- phase3-windows.png
|   +-- phase3-sysmon.png
|   +-- phase3-windows-wazuh.png
|   +-- phase3-ubuntu.png
|   +-- phase3-linux-monitoring.png
|   +-- phase4-dashboard.png
|   +-- phase4-agents.png
|   +-- phase4-alerts.png
|   +-- phase5-suricata.png
|   +-- phase5-alert.png
|   +-- phase5-wazuh.png
|   +-- phase6-nmap.png
|   +-- phase6-wireshark.png
|   +-- phase6-packet-analysis.png
|   +-- phase7-scan.png
|   +-- phase7-results.png
|   +-- phase7-detail.png
|   +-- phase7-rescan.png
|   +-- phase8-database.png
|   +-- phase8-tables.png
|   +-- phase8-join.png
|   +-- phase8-analytics.png
|   +-- phase8-audit.png
|   +-- phase9-misp.png
|   +-- phase9-ioc.png
|   +-- phase9-correlation.png
|   +-- phase10-dfir.png
|   +-- phase10-case.png
|   +-- phase10-timeline.png
|   +-- phase11-yara-rule.png
|   +-- phase11-yara-detection.png
|   +-- phase11-volatility.png
|   +-- phase11-autopsy.png
|   +-- phase12-webapp.png
|   +-- phase12-zap.png
|   +-- phase12-findings.png
|   +-- phase13-python.png
|   +-- phase13-execution.png
|   +-- phase13-import.png
|   +-- phase14-event.png
|   +-- phase14-wazuh.png
|   +-- phase14-suricata.png
|   +-- phase14-investigation.png
|   +-- phase14-sql.png
|   +-- phase14-misp.png
|   +-- phase14-dfir.png
|   +-- phase14-remediation.png
|   +-- phase14-validation.png
|
+-- sql/
|   +-- schema.sql
|   +-- security-queries.sql
|   +-- views.sql
|   +-- triggers.sql
|
+-- scripts/
|   +-- security-automation.py
|
+-- yara/
|   +-- detection-rules.yar
|
+-- reports/
    +-- incident-reports/
```

---

# Key Takeaways

This project demonstrates the construction and operation of an enterprise-style cybersecurity environment using a resource-efficient five-primary-VM architecture.

The lab integrates network security, Windows and Linux endpoint monitoring, SIEM/XDR, IDS/IPS, vulnerability management, threat intelligence, incident response, digital forensics, web application security, SQL analytics, and Python automation.

Instead of assigning every security application its own permanent VM, compatible services are consolidated and resource-intensive tools are used only when required.

This approach provides hands-on experience with a broad security toolset while maintaining reasonable CPU and memory requirements.

SQL and Python are integrated directly into the security operations workflow for data analysis, automation, correlation, reporting, and incident investigation.

---

# Disclaimer

This project is intended for educational and defensive cybersecurity training purposes only.

All scanning, testing, traffic generation, vulnerability assessment, and security analysis documented in this repository is performed against systems owned and isolated within the VirtualBox lab environment.

---

# Final Outcome

**Enterprise Security Operations Lab**

**5 Primary Virtual Machines + Phase-Specific Security Tools**

**VirtualBox + OPNsense + Suricata + Windows 11 + Sysmon + Ubuntu + auditd + osquery + Wazuh + Kali Linux + Nmap + Wireshark + Greenbone/OpenVAS + MISP + DFIR-IRIS + YARA + Volatility 3 + Autopsy + OWASP ZAP + PostgreSQL + SQL + Python**

**Detect → Analyze → Investigate → Correlate → Respond → Remediate → Validate → Report**
