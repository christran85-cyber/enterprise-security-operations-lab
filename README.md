# Enterprise Security Operations Lab

![Enterprise Security Operations Lab](images/diagram2.png)

## Overview

This project demonstrates the deployment and operation of an enterprise-style cybersecurity environment built from the ground up using VirtualBox.

The lab uses primarily free and open-source security tools to simulate the technologies and workflows used by security analysts and Security Operations Center (SOC) teams. Windows 11 and Microsoft Sysmon are included for Windows endpoint monitoring.

The project includes:

* VirtualBox virtualization
* OPNsense firewall and network segmentation
* Suricata IDS/IPS
* Wazuh SIEM/XDR
* Windows 11 endpoint monitoring
* Linux endpoint monitoring
* Sysmon
* auditd
* osquery
* Greenbone/OpenVAS vulnerability scanning
* Nmap network discovery
* Wireshark packet analysis
* MISP threat intelligence
* DFIR-IRIS incident response
* YARA detection rules
* Volatility 3 memory forensics
* Autopsy digital forensics
* OWASP ZAP web application security testing
* PostgreSQL security database
* SQL security analytics
* Python security automation

The objective of this project is to gain hands-on experience with security operations, vulnerability management, threat detection, security analytics, incident response, and digital forensics while practicing skills aligned with CompTIA CySA+ CS0-004.

---

## Environment

| Component         | Purpose                                  |
| ----------------- | ---------------------------------------- |
| VirtualBox        | Virtualization platform                  |
| OPNsense          | Firewall, routing, NAT, and segmentation |
| Suricata          | Network IDS/IPS                          |
| Wazuh             | SIEM/XDR and centralized monitoring      |
| Windows 11        | Windows security endpoint                |
| Sysmon            | Windows endpoint telemetry               |
| Ubuntu Linux      | Linux security endpoint                  |
| auditd            | Linux security auditing                  |
| osquery           | Endpoint visibility and querying         |
| Greenbone/OpenVAS | Vulnerability management                 |
| Nmap              | Network and service discovery            |
| Wireshark         | Packet capture and analysis              |
| MISP              | Threat intelligence and IOC management   |
| DFIR-IRIS         | Incident response and case management    |
| YARA              | File and malware detection               |
| Volatility 3      | Memory forensics                         |
| Autopsy           | Disk and file forensics                  |
| OWASP ZAP         | Web application security testing         |
| PostgreSQL        | Security operations database             |
| Python            | Security automation                      |

---

## Network Topology

The lab uses multiple VirtualBox network segments to simulate an enterprise environment.

### Security LAN

| Setting  | Value         |
| -------- | ------------- |
| Network  | 10.50.10.0/24 |
| Gateway  | 10.50.10.1    |
| Firewall | OPNsense      |
| IDS/IPS  | Suricata      |

### DMZ

| Setting  | Value                                            |
| -------- | ------------------------------------------------ |
| Network  | 10.50.20.0/24                                    |
| Gateway  | 10.50.20.1                                       |
| Purpose  | Isolated security testing and vulnerable systems |
| Firewall | OPNsense                                         |

### Architecture

```text
                         INTERNET
                            |
                     OPNsense Firewall
                            |
                         Suricata
                         IDS / IPS
                            |
              +-------------+-------------+
              |                           |
        SECURITY LAN                     DMZ
       10.50.10.0/24               10.50.20.0/24
              |                           |
     +--------+--------+             Vulnerable
     |        |        |             Web Server
 Windows   Ubuntu    Security
 Endpoint  Endpoint  Services
     |        |        |
     +--------+--------+
              |
            Wazuh
              |
       SecurityOpsDB
        PostgreSQL
              |
            Python
         Automation
```

---

## Project Objectives

* Build an enterprise-style cybersecurity lab using VirtualBox
* Configure network segmentation
* Deploy an enterprise firewall
* Implement IDS/IPS monitoring
* Deploy centralized SIEM monitoring
* Monitor Windows and Linux endpoints
* Perform network discovery
* Analyze network packets
* Perform vulnerability assessments
* Prioritize vulnerabilities using risk and severity
* Manage threat intelligence
* Investigate Indicators of Compromise
* Perform incident response
* Conduct memory and disk forensics
* Create YARA detection rules
* Perform web application security testing
* Build a security operations SQL database
* Analyze security information using SQL
* Automate security operations using Python
* Simulate security incidents
* Document detection and response activities

---

# Phase 1: VirtualBox Enterprise Environment

## Build the Virtual Lab

VirtualBox is used to create an isolated enterprise cybersecurity environment.

### Tasks

* Install VirtualBox
* Create Security LAN
* Create DMZ
* Configure virtual network adapters
* Create project virtual machines
* Configure NAT connectivity
* Verify network isolation

### Virtual Machines

| VM                  | Purpose                          |
| ------------------- | -------------------------------- |
| OPNsense            | Firewall and network security    |
| Windows 11          | Windows endpoint                 |
| Ubuntu              | Linux endpoint                   |
| Wazuh               | SIEM/XDR                         |
| OpenVAS             | Vulnerability scanner            |
| Security Server     | PostgreSQL and security services |
| Analyst Workstation | Security analysis tools          |
| Vulnerable Server   | Controlled security testing      |

### Snapshot 1 — VirtualBox Virtual Machines

![VirtualBox Virtual Machines](images/phase1-vms.png)

### Snapshot 2 — VirtualBox Network

![VirtualBox Network](images/phase1-network.png)

### Outcome

The virtual enterprise environment was created with isolated network segments for security monitoring and controlled testing.

---

# Phase 2: OPNsense Firewall

## Configure Network Security

OPNsense is deployed as the primary firewall and gateway.

### Tasks

* Configure WAN
* Configure Security LAN
* Configure DMZ
* Configure NAT
* Configure DHCP
* Create firewall rules
* Configure network segmentation
* Enable firewall logging

### Snapshot 1 — OPNsense Dashboard

![OPNsense Dashboard](images/phase2-dashboard.png)

### Snapshot 2 — Network Interfaces

![OPNsense Interfaces](images/phase2-interfaces.png)

### Snapshot 3 — Firewall Rules

![Firewall Rules](images/phase2-firewall-rules.png)

### Outcome

OPNsense provides routing, network segmentation, firewall protection, and centralized network logging.

---

# Phase 3: Windows and Linux Endpoint Monitoring

## Windows 11 Endpoint

The Windows 11 endpoint represents a standard enterprise workstation.

### Tools

* Sysmon
* Wazuh Agent
* Windows Event Logs
* PowerShell logging

### Snapshot 1 — Windows Endpoint

![Windows Endpoint](images/phase3-windows.png)

### Snapshot 2 — Sysmon

![Sysmon Events](images/phase3-sysmon.png)

### Snapshot 3 — Windows Wazuh Agent

![Windows Wazuh Agent](images/phase3-windows-wazuh.png)

## Linux Endpoint

Ubuntu is used as the Linux enterprise endpoint.

### Tools

* auditd
* osquery
* Wazuh Agent
* Linux system logs

### Snapshot 4 — Linux Endpoint

![Linux Endpoint](images/phase3-linux.png)

### Snapshot 5 — Linux Security Monitoring

![Linux Monitoring](images/phase3-linux-monitoring.png)

### Outcome

Windows and Linux endpoint telemetry is generated for security monitoring and investigation.

---

# Phase 4: Wazuh SIEM/XDR

## Centralized Security Monitoring

Wazuh provides centralized security monitoring and alerting.

### Data Sources

* Windows Event Logs
* Sysmon
* Linux logs
* auditd
* osquery
* OPNsense
* Suricata

### Monitoring

* Authentication events
* Process activity
* File integrity
* Security alerts
* Endpoint telemetry
* Network alerts
* Vulnerability information

### Snapshot 1 — Wazuh Dashboard

![Wazuh Dashboard](images/phase4-dashboard.png)

### Snapshot 2 — Wazuh Agents

![Wazuh Agents](images/phase4-agents.png)

### Snapshot 3 — Security Alerts

![Wazuh Alerts](images/phase4-alerts.png)

### Outcome

Security information from multiple systems is collected and analyzed from a centralized SIEM platform.

---

# Phase 5: Suricata IDS/IPS

## Network Threat Detection

Suricata provides intrusion detection and prevention capabilities.

### Detection

* Port scans
* Network reconnaissance
* Suspicious connections
* Protocol anomalies
* Known malicious patterns
* IDS signatures

### Snapshot 1 — Suricata Configuration

![Suricata Configuration](images/phase5-config.png)

### Snapshot 2 — Suricata Alert

![Suricata Alert](images/phase5-alert.png)

### Snapshot 3 — Wazuh Suricata Alert

![Wazuh Suricata Integration](images/phase5-wazuh.png)

### Outcome

Network security events detected by Suricata are forwarded to Wazuh for centralized investigation.

---

# Phase 6: Nmap and Wireshark

## Network Discovery

Nmap is used to discover hosts, ports, services, and network exposure.

```bash
nmap -sV 10.50.10.0/24
```

### Snapshot 1 — Nmap Discovery

![Nmap Scan](images/phase6-nmap.png)

## Packet Analysis

Wireshark is used to capture and investigate network communications.

### Analysis

* TCP/IP
* DNS
* HTTP/HTTPS metadata
* Network connections
* Suspicious traffic
* Protocol behavior

### Snapshot 2 — Wireshark Capture

![Wireshark Capture](images/phase6-wireshark.png)

### Snapshot 3 — Packet Investigation

![Packet Investigation](images/phase6-packet-analysis.png)

### Outcome

Network discovery and packet analysis provide additional evidence for security investigations.

---

# Phase 7: Vulnerability Management

## Greenbone/OpenVAS

Greenbone/OpenVAS Community Edition is used to identify vulnerabilities.

### Workflow

1. Discover assets
2. Scan systems
3. Identify vulnerabilities
4. Analyze CVSS scores
5. Prioritize findings
6. Remediate
7. Rescan
8. Validate remediation

### Snapshot 1 — Vulnerability Scan

![OpenVAS Scan](images/phase7-scan.png)

### Snapshot 2 — Vulnerability Results

![OpenVAS Results](images/phase7-results.png)

### Snapshot 3 — Vulnerability Detail

![Vulnerability Detail](images/phase7-detail.png)

### Snapshot 4 — Remediation Rescan

![OpenVAS Rescan](images/phase7-rescan.png)

### Outcome

The complete vulnerability management lifecycle is demonstrated from discovery through remediation validation.

---

# Phase 8: Security Operations SQL Database

## PostgreSQL SecurityOpsDB

A PostgreSQL database is created to store and analyze security information.

### Database Name

```text
SecurityOpsDB
```

### Database Tables

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

### SQL Skills

* CREATE TABLE
* INSERT
* UPDATE
* DELETE
* SELECT
* WHERE
* JOIN
* GROUP BY
* ORDER BY
* COUNT
* SUM
* AVG
* Date functions
* Views
* Triggers
* Functions
* Audit tables

### Example Query

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

### Snapshot 1 — SecurityOpsDB

![SecurityOpsDB](images/phase8-database.png)

### Snapshot 2 — Database Tables

![Database Tables](images/phase8-tables.png)

### Snapshot 3 — SQL JOIN

![SQL JOIN](images/phase8-join.png)

### Snapshot 4 — Security Analytics

![SQL Security Analytics](images/phase8-analytics.png)

### Snapshot 5 — SQL Trigger and Audit Table

![SQL Audit](images/phase8-audit.png)

### Outcome

SQL is used to store, correlate, and analyze security information produced by the enterprise lab.

---

# Phase 9: MISP Threat Intelligence

## Indicator of Compromise Management

MISP is used to manage threat intelligence.

### Indicators

* IP addresses
* Domains
* URLs
* File hashes
* Malware indicators

### Workflow

```text
Threat Intelligence
        |
       MISP
        |
       IOC
        |
  Security Logs
        |
     Analysis
```

### Snapshot 1 — MISP Dashboard

![MISP Dashboard](images/phase9-dashboard.png)

### Snapshot 2 — IOC

![MISP IOC](images/phase9-ioc.png)

### Snapshot 3 — IOC Investigation

![IOC Investigation](images/phase9-investigation.png)

### Outcome

Threat intelligence is correlated with network and endpoint security information.

---

# Phase 10: DFIR-IRIS Incident Response

## Security Case Management

DFIR-IRIS is used to document and manage security investigations.

### Case Information

* Incident description
* Severity
* Affected assets
* Indicators of Compromise
* Evidence
* Investigation notes
* Timeline
* Containment actions
* Remediation
* Resolution

### Incident Response Lifecycle

```text
Detection
   |
Analysis
   |
Investigation
   |
Containment
   |
Eradication
   |
Recovery
   |
Lessons Learned
```

### Snapshot 1 — DFIR-IRIS Dashboard

![DFIR IRIS Dashboard](images/phase10-dashboard.png)

### Snapshot 2 — Incident Case

![Incident Case](images/phase10-case.png)

### Snapshot 3 — Incident Timeline

![Incident Timeline](images/phase10-timeline.png)

### Outcome

Security alerts are transformed into documented incident-response investigations.

---

# Phase 11: Digital Forensics

## Autopsy

Autopsy is used for disk and file system forensics.

### Analysis

* Disk examination
* File system analysis
* Deleted files
* Metadata
* Evidence collection
* Timeline analysis

### Snapshot 1 — Autopsy

![Autopsy](images/phase11-autopsy.png)

## Volatility 3

Volatility 3 is used for memory forensics.

### Analysis

* Running processes
* Network connections
* Memory artifacts
* Suspicious processes

### Snapshot 2 — Volatility Processes

![Volatility Processes](images/phase11-volatility.png)

### Snapshot 3 — Memory Investigation

![Memory Investigation](images/phase11-memory.png)

### Outcome

Memory and disk evidence is examined during simulated security investigations.

---

# Phase 12: YARA Detection

## File Analysis and Detection Rules

YARA rules are created to identify suspicious files.

### Tasks

* Create detection rules
* Scan files
* Identify matches
* Investigate findings
* Document results

### Snapshot 1 — YARA Rule

![YARA Rule](images/phase12-rule.png)

### Snapshot 2 — YARA Detection

![YARA Detection](images/phase12-detection.png)

### Outcome

Custom detection rules provide additional file and malware identification capabilities.

---

# Phase 13: Web Application Security

## OWASP ZAP

OWASP ZAP is used against an intentionally vulnerable web application located inside the isolated DMZ.

### Testing

* Web application discovery
* Passive scanning
* Controlled active scanning
* HTTP analysis
* Security header analysis
* Vulnerability identification

All security testing is performed only against systems created specifically for this lab.

### Snapshot 1 — Vulnerable Web Application

![Vulnerable Web Application](images/phase13-webapp.png)

### Snapshot 2 — OWASP ZAP

![OWASP ZAP](images/phase13-zap.png)

### Snapshot 3 — ZAP Findings

![ZAP Findings](images/phase13-findings.png)

### Outcome

Web application vulnerabilities are identified and documented within the isolated security environment.

---

# Phase 14: Python Security Automation

## Automate Security Operations

Python is used to automate repetitive SOC and security analysis tasks.

### Automation

* Parse security logs
* Process JSON data
* Process CSV data
* Import vulnerabilities into PostgreSQL
* Import security events
* Search for IOCs
* Query SecurityOpsDB
* Generate reports

### Workflow

```text
Security Tools
      |
      v
JSON / CSV / Logs
      |
      v
    Python
      |
      v
Parse / Normalize
      |
      v
 PostgreSQL
      |
      v
SQL Analysis
      |
      v
Security Report
```

### Snapshot 1 — Python Script

![Python Script](images/phase14-script.png)

### Snapshot 2 — Script Execution

![Python Execution](images/phase14-execution.png)

### Snapshot 3 — PostgreSQL Import

![SQL Import](images/phase14-import.png)

### Outcome

Python connects multiple security technologies and automates security data processing and analysis.

---

# Phase 15: Enterprise SOC Investigation

## Simulated Security Incidents

Controlled security events are generated against systems owned and isolated inside the VirtualBox environment.

### Scenarios

* Failed login attempts
* Network reconnaissance
* Port scanning
* Suspicious PowerShell activity
* Unauthorized network connections
* File integrity changes
* IOC matches
* Suspicious files
* Vulnerability findings
* Web application security alerts

### Investigation Workflow

```text
Security Event
      |
      v
Endpoint / Network Telemetry
      |
      v
Suricata + Wazuh
      |
      v
SOC Alert
      |
      v
Investigation
      |
      v
Nmap / Wireshark / YARA / Forensics
      |
      v
SQL Analysis
      |
      v
MISP IOC Correlation
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

![Security Event](images/phase15-event.png)

### Snapshot 2 — Wazuh Alert

![Wazuh Alert](images/phase15-wazuh.png)

### Snapshot 3 — Suricata Detection

![Suricata Detection](images/phase15-suricata.png)

### Snapshot 4 — SOC Investigation

![SOC Investigation](images/phase15-investigation.png)

### Snapshot 5 — SQL Analysis

![SQL Analysis](images/phase15-sql.png)

### Snapshot 6 — MISP Correlation

![MISP Correlation](images/phase15-misp.png)

### Snapshot 7 — DFIR-IRIS Incident

![DFIR IRIS Incident](images/phase15-dfir.png)

### Snapshot 8 — Remediation

![Remediation](images/phase15-remediation.png)

### Snapshot 9 — Validation Rescan

![Validation Rescan](images/phase15-rescan.png)

### Outcome

The final investigation demonstrates how multiple security technologies work together to detect, investigate, contain, remediate, validate, and document an enterprise security incident.

---

# CySA+ CS0-004 Skills Demonstrated

## Security Operations

* SIEM monitoring
* Endpoint monitoring
* Network monitoring
* Log analysis
* IDS/IPS analysis
* Firewall analysis
* Threat intelligence
* IOC analysis
* Security automation

## Vulnerability Management

* Asset discovery
* Vulnerability scanning
* CVSS analysis
* Risk prioritization
* Remediation
* Rescanning
* Validation

## Incident Response

* Detection
* Analysis
* Investigation
* Containment
* Eradication
* Recovery
* Evidence preservation
* Documentation
* Lessons learned

## Security Analysis

* Packet analysis
* Endpoint telemetry
* Log correlation
* Network analysis
* SQL analytics
* Threat intelligence correlation
* File analysis
* Memory analysis
* Disk forensics

---

# Technology Stack

```text
VirtualBox
|
+-- OPNsense
|   +-- Suricata
|
+-- Windows 11
|   +-- Sysmon
|   +-- Wazuh Agent
|
+-- Ubuntu Linux
|   +-- auditd
|   +-- osquery
|   +-- Wazuh Agent
|
+-- Wazuh SIEM/XDR
|
+-- Greenbone/OpenVAS
|
+-- MISP
|
+-- DFIR-IRIS
|
+-- PostgreSQL
|
+-- Analyst Workstation
|   +-- Nmap
|   +-- Wireshark
|   +-- OWASP ZAP
|   +-- YARA
|   +-- Volatility 3
|   +-- Autopsy
|
+-- Vulnerable Web Application
|
+-- Python Automation
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
|   +-- phase1-vms.png
|   +-- phase1-network.png
|   +-- phase2-dashboard.png
|   +-- phase2-interfaces.png
|   +-- phase2-firewall-rules.png
|   +-- phase3-windows.png
|   +-- phase3-sysmon.png
|   +-- phase3-windows-wazuh.png
|   +-- phase3-linux.png
|   +-- phase3-linux-monitoring.png
|   +-- phase4-dashboard.png
|   +-- phase4-agents.png
|   +-- phase4-alerts.png
|   +-- phase5-config.png
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
|   +-- phase9-dashboard.png
|   +-- phase9-ioc.png
|   +-- phase9-investigation.png
|   +-- phase10-dashboard.png
|   +-- phase10-case.png
|   +-- phase10-timeline.png
|   +-- phase11-autopsy.png
|   +-- phase11-volatility.png
|   +-- phase11-memory.png
|   +-- phase12-rule.png
|   +-- phase12-detection.png
|   +-- phase13-webapp.png
|   +-- phase13-zap.png
|   +-- phase13-findings.png
|   +-- phase14-script.png
|   +-- phase14-execution.png
|   +-- phase14-import.png
|   +-- phase15-event.png
|   +-- phase15-wazuh.png
|   +-- phase15-suricata.png
|   +-- phase15-investigation.png
|   +-- phase15-sql.png
|   +-- phase15-misp.png
|   +-- phase15-dfir.png
|   +-- phase15-remediation.png
|   +-- phase15-rescan.png
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

This project provides practical experience building and operating an enterprise-style cybersecurity environment from the ground up.

The lab integrates network security, endpoint monitoring, vulnerability management, threat intelligence, incident response, digital forensics, SQL security analytics, and Python automation into one environment.

The project demonstrates how security analysts collect telemetry, identify suspicious activity, investigate alerts, correlate security information, document incidents, remediate vulnerabilities, and validate that security issues have been resolved.

SQL and Python are used directly within the security operations workflow for security data analysis, automation, reporting, and incident investigation.

---

# Disclaimer

This project is intended for educational and defensive cybersecurity training purposes only.

All scanning, testing, traffic generation, and security analysis documented in this repository is performed against systems owned and isolated within the VirtualBox lab environment.

---

# Final Outcome

**Enterprise Security Operations Lab**

**VirtualBox + OPNsense + Suricata + Wazuh + Greenbone/OpenVAS + Nmap + Wireshark + MISP + DFIR-IRIS + YARA + Volatility 3 + Autopsy + OWASP ZAP + PostgreSQL + Python**

**Detect → Analyze → Investigate → Respond → Remediate → Validate → Report**
