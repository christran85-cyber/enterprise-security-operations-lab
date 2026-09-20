# Phase 01 — VirtualBox Enterprise Environment

[← Back to Main Project](../README.md)

---

## Overview

Phase 1 established the virtualization and network foundation for the Enterprise Security Operations Lab.

VirtualBox provides the virtualization platform for the project, with five primary virtual machines representing the firewall, Windows endpoint, Linux endpoint, centralized security server, and SOC analyst workstation.

The objective of this phase was to build and validate the base infrastructure before deploying the security monitoring and incident-response technologies used in later phases.

---

## Five-VM Architecture

### VM 1 — SOC-OPNsense

Primary role:

- Firewall
- Routing
- NAT
- Network segmentation
- Suricata IDS/IPS

### VM 2 — SOC-Windows11

Primary role:

- Windows enterprise endpoint
- Sysmon
- Wazuh Agent
- Windows Event Logs
- PowerShell logging

### VM 3 — SOC-Ubuntu

Primary role:

- Linux endpoint
- auditd
- osquery
- Wazuh Agent
- Controlled vulnerable web application

### VM 4 — SOC-Wazuh

Primary role:

- Wazuh SIEM/XDR
- PostgreSQL
- SecurityOpsDB
- Python security automation

### VM 5 — SOC-Kali

Primary role:

- SOC analyst workstation
- Nmap
- Wireshark
- OWASP ZAP
- YARA
- Volatility 3

---

## Network Architecture

The lab was designed around multiple VirtualBox network segments controlled by OPNsense.

### Security LAN

```text
Network: 10.10.10.0/24
Gateway: 10.10.10.1
VirtualBox Network: SOC-LAN
```

### DMZ

```text
Network: 10.50.20.0/24
Gateway: 10.50.20.1
```

The DMZ provides an isolated network for controlled security testing and monitored services.

### WAN

OPNsense uses VirtualBox NAT for external connectivity.

```text
WAN: VirtualBox NAT
OPNsense WAN: 10.0.2.15/24
```

---

## Architecture

```text
                         INTERNET
                            |
                            v
                     SOC-OPNsense
                 Firewall / NAT / Routing
                            |
              +-------------+-------------+
              |                           |
              v                           v
         SECURITY LAN                    DMZ
         10.10.10.0/24              10.50.20.0/24
              |                           |
       +------+------+                    |
       |             |                    |
       v             v                    v
 SOC-Windows11   SOC-Kali            SOC-Ubuntu
   Endpoint      Analyst              Endpoint
       |             |                    |
       +-------------+--------------------+
                     |
                     v
                 SOC-Wazuh
                 SIEM / XDR
```

---

## Phase Objectives

The primary objectives for Phase 1 were:

- [x] Install VirtualBox
- [x] Create five primary virtual machines
- [x] Create the Security LAN
- [x] Create the DMZ
- [x] Configure VirtualBox network adapters
- [x] Configure internet connectivity
- [x] Verify internal communication
- [x] Verify gateway connectivity
- [x] Verify DNS resolution
- [x] Establish the infrastructure required for later network segmentation

---

# Implementation

## 1. VirtualBox Environment

Five primary virtual machines were created to represent the major systems required by the SOC environment.

The architecture intentionally separates major security functions while remaining resource-efficient enough to operate on a single physical host.

The five systems provide dedicated roles for:

```text
Firewall / Network Security
           |
Windows Endpoint
           |
Linux Endpoint
           |
Centralized Security Monitoring
           |
SOC Analyst Workstation
```

---

## 2. VirtualBox VM Inventory

The completed VirtualBox inventory confirmed that the primary systems required for the lab were successfully created.

### Evidence

![VirtualBox VM Inventory](../images/phase1-vm-inventory.png)

The five-primary-VM architecture provides the foundation for all later security phases.

---

## 3. VirtualBox Network Configuration

VirtualBox networking was configured so systems could communicate through the OPNsense security gateway rather than operating as isolated standalone virtual machines.

This design allows later phases to implement:

- Firewall policies
- Network segmentation
- IDS/IPS monitoring
- Security logging
- Controlled attack simulation
- Centralized SIEM monitoring

### Evidence

![VirtualBox Network Configuration](../images/phase1-network-kali.png)

---

## 4. Windows 11 Network Configuration

The Windows 11 SOC endpoint was connected to the internal Security LAN.

At this stage of the build, the endpoint successfully received network configuration from the OPNsense DHCP service.

Observed configuration:

```text
IPv4 Address:    10.10.10.123
Subnet Mask:     255.255.255.0
Default Gateway: 10.10.10.1
```

The address shown here represents the Windows endpoint during this stage of the project. Addressing changed during later phases as the lab evolved.

### Evidence

![Windows 11 Network Configuration](../images/windows11-opnsense-network-config.png)

---

## 5. Windows Network Validation

Connectivity testing was performed from the Windows endpoint to verify the basic network path.

Validation confirmed:

```text
OPNsense Gateway
10.10.10.1
     |
     | Reachable
     v

Internet
8.8.8.8
     |
     | Reachable
     v

DNS Resolution
google.com
     |
     | Successful
     v

Packet Loss
0%
```

These tests demonstrated that the Windows endpoint could successfully communicate through the OPNsense security gateway.

### Evidence

![Windows 11 Network Validation](../images/windows11-network-validation.png)

---

# Validation

Phase 1 validation focused on confirming each layer of the basic network environment before installing security applications.

The validation process included:

### DHCP

The Windows endpoint successfully received an IP address on the Security LAN.

### Gateway

The endpoint successfully communicated with:

```text
10.10.10.1
```

which is the OPNsense Security LAN gateway.

### Internet Connectivity

External IP connectivity was successfully validated using:

```text
8.8.8.8
```

### DNS

DNS resolution was validated using:

```text
google.com
```

### Result

The completed validation demonstrated:

```text
Virtual Machine
      |
      v
VirtualBox Network Adapter
      |
      v
Security LAN
      |
      v
OPNsense Gateway
      |
      v
Internet
      |
      v
DNS Resolution
```

The base networking environment was therefore operational.

---

# Troubleshooting and Lessons Learned

Several configuration and validation issues were encountered while building the initial VirtualBox environment.

Documenting these issues was important because troubleshooting became a major part of the later SOC phases.

---

## OPNsense Initial Configuration

During the initial OPNsense installation, the LAN and DHCP configuration required correction before the internal network operated as intended.

The configuration was reviewed and corrected before continuing with deployment of the remaining virtual machines.

### Lesson

Firewall interface assignments and IP addressing should be validated before additional systems are deployed.

An incorrect gateway, subnet, interface assignment, or DHCP configuration at the firewall layer can create connectivity problems across the entire environment.

---

## VirtualBox Network Configuration

The virtual machines required the correct VirtualBox network adapters to communicate through OPNsense.

Network configuration was validated before security tools were installed.

This was important because later connectivity failures could otherwise be incorrectly attributed to:

- Wazuh
- Suricata
- Endpoint agents
- Firewall rules
- Security applications

when the underlying problem might actually be the virtual network configuration.

---

## Windows Network Validation

After SOC-Windows11 was connected to the Security LAN, multiple connectivity layers were tested independently.

Validation included:

1. DHCP address assignment
2. IP configuration
3. Default gateway connectivity
4. Internet connectivity
5. DNS resolution

The endpoint successfully received an address on the Security LAN and used OPNsense as its default gateway.

---

## Layered Troubleshooting Methodology

One of the most important lessons from Phase 1 was to validate network connectivity in layers.

```text
Virtual Machine
      |
      v
VirtualBox Adapter
      |
      v
IP Configuration
      |
      v
Default Gateway
      |
      v
OPNsense
      |
      v
Internet Connectivity
      |
      v
DNS Resolution
```

If a connection fails, each layer should be validated individually.

This makes it easier to determine whether the problem exists at the:

- Virtual machine
- VirtualBox adapter
- IP configuration
- Gateway
- Firewall
- Routing layer
- Internet connection
- DNS layer

This troubleshooting methodology was reused throughout later phases of the project.

---

# Skills Demonstrated

Phase 1 provided hands-on experience with:

- VirtualBox virtualization
- Virtual machine deployment
- Virtual networking
- Network architecture
- IPv4 addressing
- Subnetting
- DHCP
- Default gateways
- NAT
- DNS validation
- Firewall-based network design
- Connectivity testing
- Layered troubleshooting
- Infrastructure documentation

---

# Phase 1 Outcome

Phase 1 successfully established the virtual infrastructure required for the Enterprise Security Operations Lab.

The completed environment included:

```text
SOC-OPNsense
      |
      +---- SOC-LAN
      |
      +---- DMZ
      |
      +---- Internet / NAT

SOC-Windows11
SOC-Ubuntu
SOC-Wazuh
SOC-Kali
```

The environment provided a functional base for implementing firewall segmentation, endpoint security monitoring, centralized SIEM/XDR, IDS/IPS, incident response, security automation, and the other capabilities introduced throughout the project.

---

# Evidence Summary

| Evidence | Description |
|---|---|
| `phase1-vm-inventory.png` | Five-primary-VM VirtualBox inventory |
| `phase1-network-kali.png` | VirtualBox network configuration |
| `windows11-opnsense-network-config.png` | Windows Security LAN configuration |
| `windows11-network-validation.png` | Gateway, internet, and DNS validation |

---

# Phase 1 Status

## ✅ COMPLETE

The VirtualBox enterprise environment was successfully built and validated.

The lab was ready to proceed to **Phase 2 — OPNsense Firewall and Network Segmentation**.

---

## Navigation

[← Back to Main Project](../README.md)

**Next:** [Phase 02 — OPNsense Firewall & Network Segmentation](phase-02-network-segmentation.md)
