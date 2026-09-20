# 🖥️ Phase 01 — VirtualBox Enterprise Environment

> **Objective:** Build and validate the five-VM virtual infrastructure and networking foundation for the Enterprise Security Operations Lab.

[🏠 Main Project](../README.md) | [Next: Phase 02 →](phase-02-network-segmentation.md)

---

## 📑 Table of Contents

- [Phase Summary](#-phase-summary)
- [Overview](#-overview)
- [Lab Architecture](#️-lab-architecture)
- [Virtual Machine Roles](#-virtual-machine-roles)
- [Network Architecture](#-network-architecture)
- [Phase Objectives](#-phase-objectives)
- [Implementation](#️-implementation)
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
| **Platform** | Oracle VirtualBox |
| **Primary Systems** | OPNsense, Windows 11, Ubuntu, Wazuh, Kali Linux |
| **Security LAN** | `10.10.10.0/24` |
| **DMZ** | `10.50.20.0/24` |
| **Gateway** | `10.10.10.1` |
| **Focus** | Virtualization & Network Infrastructure |
| **Next Phase** | OPNsense Firewall & Network Segmentation |

---

# 📋 Overview

Phase 1 established the virtualization and networking foundation for the **Enterprise Security Operations Lab**.

The environment was designed around five primary virtual machines representing the major components of a small enterprise Security Operations Center.

The purpose of this phase was to ensure that the underlying infrastructure was operational before security monitoring, detection, automation, and incident-response technologies were introduced.

---

# 🏗️ Lab Architecture

The lab was designed around five primary virtual machines:

```text
                         INTERNET
                            │
                            ▼
                     ┌─────────────┐
                     │ SOC-OPNsense│
                     │ Firewall    │
                     │ NAT/Routing │
                     └──────┬──────┘
                            │
              ┌─────────────┴─────────────┐
              │                           │
              ▼                           ▼
           SOC-LAN                      SOC-DMZ
         10.10.10.0/24               10.50.20.0/24
              │                           │
       ┌──────┼─────────┐                 │
       │      │         │                 │
       ▼      ▼         ▼                 ▼
   Windows   Kali     Wazuh             Ubuntu
   Endpoint  Analyst  SIEM/XDR          Endpoint
```

This architecture created the foundation for later phases involving:

- Firewall segmentation
- Endpoint monitoring
- Wazuh SIEM/XDR
- Suricata IDS/IPS
- Vulnerability assessment
- Threat hunting
- Security automation
- Centralized logging
- Incident response
- Web application security testing

---

# 💻 Virtual Machine Roles

## 🛡️ SOC-OPNsense

**Primary Role:** Firewall and network security gateway

Responsibilities:

- Firewall enforcement
- Routing
- NAT
- Network segmentation
- DHCP
- Suricata IDS/IPS

---

## 🪟 SOC-Windows11

**Primary Role:** Windows enterprise endpoint

Security capabilities used throughout the project include:

- Windows Event Logs
- Sysmon
- PowerShell logging
- Wazuh Agent
- Endpoint monitoring

---

## 🐧 SOC-Ubuntu

**Primary Role:** Linux endpoint and controlled security-testing target

Security capabilities include:

- auditd
- osquery
- Wazuh Agent
- Apache
- Controlled vulnerable web applications

---

## 📊 SOC-Wazuh

**Primary Role:** Centralized security monitoring server

The system later provides:

- Wazuh SIEM/XDR
- Security event collection
- Detection and correlation
- PostgreSQL
- SecurityOpsDB
- Python security automation

---

## 🐉 SOC-Kali

**Primary Role:** SOC analyst and controlled security-testing workstation

Tools used throughout the project include:

- Nmap
- Wireshark
- OWASP ZAP
- Nikto
- YARA
- Volatility 3
- Python
- DFIR-IRIS

---

# 🌐 Network Architecture

## Security LAN

```text
Network: 10.10.10.0/24
Gateway: 10.10.10.1
Purpose: Internal SOC systems
```

The Security LAN provides internal connectivity for systems such as:

- SOC-Windows11
- SOC-Kali
- SOC-Wazuh

---

## DMZ

```text
Network: 10.50.20.0/24
Purpose: Isolated monitored services and security-testing targets
```

SOC-Ubuntu operates within the DMZ.

This design allows controlled security activity to be generated from the Security LAN toward an isolated target while monitoring traffic through the security stack.

---

## WAN

OPNsense uses VirtualBox NAT for external connectivity.

```text
WAN
 │
 ▼
OPNsense
 │
 ├── SOC-LAN
 │
 └── SOC-DMZ
```

---

# 🎯 Phase Objectives

- [x] Install and configure VirtualBox
- [x] Create five primary virtual machines
- [x] Deploy OPNsense
- [x] Create the Security LAN
- [x] Establish the DMZ architecture
- [x] Configure VirtualBox network adapters
- [x] Configure internet connectivity
- [x] Validate DHCP
- [x] Validate gateway connectivity
- [x] Validate internet connectivity
- [x] Validate DNS resolution
- [x] Establish the infrastructure required for later security phases

---

# ⚙️ Implementation

## 1. VirtualBox Environment

Five primary virtual machines were created to represent the major systems required by the enterprise SOC environment.

```text
┌───────────────────────────────┐
│        VirtualBox Host        │
├───────────────────────────────┤
│ SOC-OPNsense                  │
│ SOC-Windows11                 │
│ SOC-Ubuntu                    │
│ SOC-Wazuh                     │
│ SOC-Kali                      │
└───────────────────────────────┘
```

Separating the systems into individual virtual machines provides a realistic security environment while keeping the lab resource-efficient enough to operate on a single physical host.

### 📸 Evidence — Virtual Machine Inventory

![VirtualBox VM Inventory](../images/phase1-vm-inventory.png)

---

## 2. Virtual Network Configuration

VirtualBox networking was configured so that traffic could flow through OPNsense instead of allowing every system to operate independently.

This was important because later security phases depend on traffic being visible to the firewall and monitoring infrastructure.

```text
Endpoint
   │
   ▼
VirtualBox Network
   │
   ▼
OPNsense
   │
   ├── Firewall Rules
   ├── Routing
   ├── NAT
   └── IDS/IPS
```

### 📸 Evidence — Kali Network Configuration

![VirtualBox Network Configuration](../images/phase1-network-kali.png)

---

## 3. OPNsense Firewall

OPNsense was deployed as the central network security gateway.

The firewall provides the foundation for:

- Internal routing
- NAT
- DHCP
- Network segmentation
- Firewall policy enforcement
- IDS/IPS monitoring

### 📸 Evidence — OPNsense Dashboard

![OPNsense Dashboard](../images/phase1-opnsense-dashboard.png)

---

## 4. Windows 11 Network Configuration

SOC-Windows11 was connected to the internal Security LAN.

The endpoint successfully received network configuration through the OPNsense environment and used OPNsense as its gateway.

```text
SOC-Windows11
      │
      ▼
10.10.10.0/24
      │
      ▼
10.10.10.1
      │
      ▼
SOC-OPNsense
```

The address shown in the original Phase 1 evidence represents the Windows endpoint during this stage of the project.

Addressing evolved during later phases as the lab architecture was expanded and refined.

### 📸 Evidence — Windows Network Configuration

![Windows Network Configuration](../images/windows11-opnsense-network-config.png)

---

## 5. Network Connectivity Testing

After the endpoint network configuration was established, connectivity was tested at multiple layers.

```text
DHCP
  │
  ▼
Local IP Configuration
  │
  ▼
Default Gateway
  │
  ▼
OPNsense
  │
  ▼
Internet
  │
  ▼
DNS
```

Testing each layer independently verified that the virtual networking environment was functioning correctly before deploying security applications.

### 📸 Evidence — Network Validation

![Windows Network Validation](../images/windows11-network-validation.png)

---

# 🧪 Validation

## DHCP Validation

The Windows endpoint successfully received network configuration on the Security LAN.

This demonstrated that the endpoint could communicate with the network infrastructure and obtain the required addressing information.

---

## Gateway Validation

Connectivity to the OPNsense Security LAN gateway was tested:

```text
10.10.10.1
```

Successful communication demonstrated that the endpoint could reach the firewall.

---

## Internet Connectivity

External connectivity was validated using an external IP address.

Example:

```text
8.8.8.8
```

Testing an IP address independently from a hostname helped separate routing problems from DNS problems.

---

## DNS Validation

DNS resolution was validated using a hostname such as:

```text
google.com
```

Successful resolution demonstrated that both internet connectivity and DNS functionality were operational.

---

## ✅ Validation Result

The completed tests demonstrated a working path:

```text
Virtual Machine
      │
      ▼
VirtualBox Adapter
      │
      ▼
Security LAN
      │
      ▼
OPNsense Gateway
      │
      ▼
Internet
      │
      ▼
DNS Resolution

   ✅ VALIDATED
```

---

# 🔧 Troubleshooting

Troubleshooting was an important part of building the initial environment.

Rather than immediately installing security applications, the underlying infrastructure was validated first.

This reduced the chance of incorrectly blaming applications such as Wazuh or Suricata for problems caused by networking.

---

## OPNsense Initial Configuration

During the initial OPNsense deployment, LAN and DHCP configuration required correction before the internal network operated as intended.

The firewall configuration was reviewed before continuing with the deployment of additional systems.

### Key Lesson

A configuration problem involving:

- Interface assignments
- Subnets
- Gateways
- DHCP
- NAT
- Routing

can affect every connected virtual machine.

The firewall and network layer should therefore be validated before troubleshooting higher-level security applications.

---

## VirtualBox Network Adapters

Each virtual machine required the correct VirtualBox network adapter configuration.

An incorrectly assigned adapter could prevent the VM from reaching:

- OPNsense
- Other internal systems
- The internet
- Security monitoring infrastructure

This reinforced the importance of checking the virtualization layer before troubleshooting the operating system or application layer.

---

## Connectivity Troubleshooting

Connectivity was validated one layer at a time:

```text
VM Running?
    │
    ▼
Adapter Correct?
    │
    ▼
IP Address Correct?
    │
    ▼
Gateway Reachable?
    │
    ▼
OPNsense Working?
    │
    ▼
Internet Reachable?
    │
    ▼
DNS Working?
```

This approach became a recurring troubleshooting methodology throughout the Enterprise Security Operations Lab.

---

# 💡 Lessons Learned

### 1. Validate Infrastructure Before Applications

A security application cannot function correctly if the underlying network is broken.

Before troubleshooting Wazuh, Suricata, agents, or other security tools:

```text
VM → Adapter → IP → Gateway → Routing → Service
```

---

### 2. Test Connectivity in Layers

Testing each network layer independently provides better information than testing everything at once.

```text
Ping Gateway
     ↓
Test External IP
     ↓
Test DNS Name
```

---

### 3. Firewall Configuration Affects the Entire Lab

OPNsense became a central component of the project.

Incorrect firewall or interface configuration can affect:

- DHCP
- Routing
- NAT
- Segmentation
- IDS/IPS
- Endpoint communication
- SIEM communication

---

### 4. Build the Lab in Layers

The lab was intentionally developed incrementally.

```text
Virtualization
      ↓
Networking
      ↓
Segmentation
      ↓
Endpoint Monitoring
      ↓
SIEM/XDR
      ↓
IDS/IPS
      ↓
Detection
      ↓
Automation
      ↓
Incident Response
```

This approach made troubleshooting easier and provided clear evidence for each completed capability.

---

# 🧠 Skills Demonstrated

| Skill | Application |
|---|---|
| **Virtualization** | Created and managed multiple VirtualBox VMs |
| **Network Architecture** | Designed Security LAN, DMZ, and WAN connectivity |
| **IPv4 Networking** | Configured and validated private IPv4 networks |
| **Subnetting** | Used separate internal network segments |
| **DHCP** | Validated dynamic endpoint configuration |
| **Routing** | Routed endpoint traffic through OPNsense |
| **NAT** | Provided external connectivity through the firewall |
| **DNS** | Validated hostname resolution |
| **Firewall Architecture** | Positioned OPNsense as the central security gateway |
| **Troubleshooting** | Used layered network validation |
| **Documentation** | Recorded implementation and validation evidence |

---

# 📸 Evidence Summary

| Evidence | Existing File |
|---|---|
| VirtualBox VM Inventory | `phase1-vm-inventory.png` |
| Kali VirtualBox Network | `phase1-network-kali.png` |
| OPNsense Dashboard | `phase1-opnsense-dashboard.png` |
| Windows Network Configuration | `windows11-opnsense-network-config.png` |
| Windows Network Validation | `windows11-network-validation.png` |

All screenshots are reused from the original project documentation.

---

# 🏁 Phase Outcome

## ✅ Phase 1 Complete

Phase 1 successfully established the virtualization and networking foundation for the **Enterprise Security Operations Lab**.

```text
                    INTERNET
                       │
                       ▼
                  SOC-OPNsense
                       │
              ┌────────┴────────┐
              │                 │
              ▼                 ▼
           SOC-LAN            SOC-DMZ
              │                 │
       ┌──────┼──────┐          │
       │      │      │          │
       ▼      ▼      ▼          ▼
    Windows  Kali   Wazuh     Ubuntu
```

With the underlying infrastructure operational, the project was ready to move into firewall policies and network segmentation.

---

# ➡️ Next Phase

**Phase 02 — OPNsense Firewall & Network Segmentation**

The next phase introduces firewall policy enforcement and segmentation between the internal Security LAN and DMZ.

---

[🏠 Back to Main Project](../README.md) | [Next: Phase 02 →](phase-02-network-segmentation.md)

---

### Enterprise Security Operations Lab

**SOC Operations • Detection Engineering • Network Security • Security Automation • Incident Response**
