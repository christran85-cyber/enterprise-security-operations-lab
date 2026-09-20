# 🛡️ Phase 02 — OPNsense Firewall & Network Segmentation

> **Objective:** Configure OPNsense as the central firewall, router, and security gateway while enforcing segmentation between the Security LAN and DMZ.

[← Phase 01](phase-01-virtualbox-environment.md) | [🏠 Main Project](../README.md) | [Phase 03 →](phase-03-endpoint-monitoring.md)

---

## 📑 Table of Contents

- [Phase Summary](#-phase-summary)
- [Overview](#-overview)
- [Network Architecture](#️-network-architecture)
- [Security Zones](#-security-zones)
- [Phase Objectives](#-phase-objectives)
- [OPNsense Configuration](#️-opnsense-configuration)
- [Firewall Policy](#-firewall-policy)
- [DMZ Segmentation Validation](#-dmz-segmentation-validation)
- [Firewall Logging](#-firewall-logging)
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
| **Firewall** | OPNsense |
| **WAN** | `10.0.2.15/24` |
| **Security LAN** | `10.10.10.0/24` |
| **LAN Gateway** | `10.10.10.1` |
| **DMZ** | `10.50.20.0/24` |
| **DMZ Gateway** | `10.50.20.1` |
| **Primary Control** | Firewall-based network segmentation |
| **Validation** | DMZ → Security LAN traffic blocked and logged |
| **Focus** | Segmentation, firewall policy, NAT, DHCP & logging |
| **Next Phase** | Endpoint Security Monitoring |

---

# 📋 Overview

Phase 2 transformed the VirtualBox environment created in Phase 1 into a segmented enterprise-style network.

OPNsense functions as the primary:

- Firewall
- Router
- Gateway
- NAT device
- DHCP provider
- Network segmentation control
- Security logging point

The primary security objective was to isolate the **DMZ** from the protected **Security LAN** while continuing to allow required network connectivity.

Instead of creating unrestricted communication between systems, firewall policies were designed around the principle:

```text
Allow Required Traffic
        +
Block Unauthorized Traffic
        +
Log Security Decisions
```

This created the network-security foundation used by the monitoring, IDS/IPS, SIEM, automation, and incident-response phases later in the project.

---

# 🏗️ Network Architecture

```text
                         INTERNET
                            │
                            ▼
                    ┌──────────────┐
                    │ SOC-OPNsense │
                    │   Firewall   │
                    │ NAT / Router │
                    └──────┬───────┘
                           │
             ┌─────────────┴─────────────┐
             │                           │
             ▼                           ▼
      SECURITY LAN                     DMZ
      10.10.10.0/24               10.50.20.0/24
             │                           │
             │                           │
     Protected Systems              SOC-Ubuntu
             │                     10.50.20.100
             │                           │
             └──────── OPNsense ─────────┘
                     Firewall Policy
```

OPNsense controls communication between the two security zones.

---

# 🌐 Security Zones

## Security LAN

```text
Network:  10.10.10.0/24
Gateway:  10.10.10.1
Zone:     Protected Internal Network
```

The Security LAN contains internal SOC systems such as:

- Windows endpoint
- Wazuh security server
- Kali analyst workstation

---

## DMZ

```text
Network:  10.50.20.0/24
Gateway:  10.50.20.1
Zone:     Isolated Security Testing Network
```

The Ubuntu endpoint was placed in the DMZ:

```text
SOC-Ubuntu
10.50.20.100
```

This provided an isolated target for controlled security testing while protecting internal SOC systems.

---

## WAN

The OPNsense WAN interface provides external connectivity through VirtualBox NAT.

```text
WAN: 10.0.2.15/24
```

The resulting traffic path is:

```text
Internal VM
    │
    ▼
OPNsense
    │
    ▼
VirtualBox NAT
    │
    ▼
Internet
```

---

# 🎯 Phase Objectives

- [x] Configure OPNsense WAN
- [x] Configure Security LAN
- [x] Configure DMZ
- [x] Configure NAT
- [x] Configure DHCP
- [x] Create firewall rules
- [x] Restrict inter-network traffic
- [x] Enable firewall logging
- [x] Validate permitted traffic
- [x] Validate blocked traffic
- [x] Verify DMZ segmentation
- [x] Preserve required internet connectivity

---

# ⚙️ OPNsense Configuration

## 1. OPNsense Dashboard

OPNsense was configured as the central network-security device for the lab.

The dashboard confirmed that the firewall and required interfaces were operational.

Configured interfaces included:

```text
WAN
10.0.2.15/24

SECURITY LAN
10.10.10.1/24

DMZ
10.50.20.1/24
```

The firewall therefore became the routing and policy-enforcement point between the different network zones.

### 📸 Evidence — OPNsense Dashboard

![OPNsense Dashboard](../images/phase1-opnsense-dashboard.png)

This is the **same OPNsense dashboard screenshot used in the original project documentation**.

---

## 2. Network Interfaces

The OPNsense interfaces were configured to separate internal systems from the isolated DMZ.

```text
                     OPNsense
                        │
             ┌──────────┴──────────┐
             │                     │
             ▼                     ▼
         SOC-LAN                  DMZ
      10.10.10.1/24          10.50.20.1/24
```

Each network uses a separate IP range and firewall interface.

This allows security policy to be applied between zones rather than treating all virtual machines as part of one unrestricted network.

### 📸 Evidence — OPNsense Interfaces

![OPNsense Interfaces](../images/phase2-interfaces.png)

---

# 🔥 Firewall Policy

OPNsense firewall rules were created to control communication between the Security LAN and DMZ.

The primary segmentation requirement was:

```text
DMZ
 │
 │ Unauthorized Access
 ▼
Security LAN

❌ BLOCK
```

while still allowing traffic required for normal operation.

The security model was therefore not:

```text
Block Everything
```

or:

```text
Allow Everything
```

Instead:

```text
Required Traffic
      │
      ▼
   ALLOWED

Unauthorized Inter-Zone Traffic
      │
      ▼
   BLOCKED
```

### 📸 Evidence — Firewall Rules

![Firewall Rules](../images/phase2-firewall-rules.png)

The configured rules provide the policy foundation for later security phases.

---

# 🧪 DMZ Segmentation Validation

Segmentation was validated using the Ubuntu endpoint located in the DMZ.

At the time of this Phase 2 validation:

```text
Source:
SOC-Ubuntu
10.50.20.100

Destination:
Windows Endpoint
10.10.10.123

Protocol:
ICMP
```

The attempted communication from the DMZ toward the protected Security LAN was blocked.

The firewall log identified:

```text
Source:      10.50.20.100
Destination: 10.10.10.123
Protocol:    ICMP
Action:      BLOCK
Rule:        Block DMZ to Security LAN
```

The Ubuntu endpoint retained required network connectivity while direct communication to the protected Security LAN was denied.

### 📸 Evidence — DMZ Segmentation Validation

![DMZ Segmentation Validation](../images/phase2-segmentation-validation.png)

This provided direct evidence that segmentation was being enforced by the firewall rather than simply relying on network design assumptions.

---

# 📜 Firewall Logging

Firewall logging was used to validate **why** communication was denied.

The logs provided evidence showing:

| Field | Purpose |
|---|---|
| **Source IP** | System initiating communication |
| **Destination IP** | Intended target |
| **Protocol** | Network protocol involved |
| **Action** | Allow or block decision |
| **Firewall Rule** | Policy responsible for the decision |

This distinction is important during troubleshooting.

A failed connection does not automatically mean:

```text
Network Failure
```

It may instead mean:

```text
Network Working
      +
Firewall Policy Working
      =
Connection Intentionally Blocked
```

Reviewing the firewall logs confirmed that the segmentation policy—not a broken network—caused the failed DMZ-to-LAN communication.

---

# 🔧 Troubleshooting

Phase 2 demonstrated that firewall troubleshooting requires validating both **allowed** and **blocked** traffic.

---

## DMZ Segmentation Validation

The Ubuntu endpoint was placed on the isolated DMZ while the Windows endpoint remained on the protected Security LAN.

Testing confirmed two important behaviors:

```text
Ubuntu DMZ
    │
    ├──── Required Connectivity ────► ✅ Available
    │
    └──── Security LAN Access ─────► ❌ Blocked
```

This showed that segmentation did not simply disconnect the DMZ.

Instead, OPNsense enforced selective network access.

---

## Firewall Logging

When communication failed, the OPNsense logs were reviewed rather than immediately changing network settings.

This helped distinguish between:

```text
Routing Failure
Firewall Block
Incorrect IP
Service Failure
Network Adapter Problem
```

The logs confirmed that the failed connection was an intentional firewall action.

---

## Allowed vs. Blocked Traffic

A properly segmented network should be tested in both directions.

The validation process followed:

```text
DMZ Endpoint
     │
     ├──── Required Traffic ──────► Allowed
     │
     └──── Security LAN Access ───► Blocked
                                      │
                                      ▼
                                OPNsense Log
                                      │
                                      ▼
                                  Verified
```

Testing only blocked traffic would not prove that required connectivity remained operational.

Testing only permitted traffic would not prove that segmentation was actually enforced.

Both behaviors needed validation.

---

## Firewall Rule Ordering

OPNsense evaluates firewall policies according to their configured rule order.

Specific permitted traffic must be defined narrowly while broader segmentation rules continue to protect the internal network.

This became especially important later when SOC-Ubuntu required communication with the Wazuh manager.

The required connection was:

```text
SOC-Ubuntu
10.50.20.100
     │
     │ TCP 1514
     ▼
SOC-Wazuh
10.10.10.102
```

A narrow firewall exception could permit this required security telemetry without allowing unrestricted DMZ-to-Security-LAN communication.

Conceptually:

```text
DMZ
 │
 ├── Ubuntu → Wazuh TCP 1514 ─────► ALLOW
 │
 └── Other Security LAN Traffic ──► BLOCK
```

The specific allow rule must be evaluated before the broader blocking policy.

---

# 💡 Lessons Learned

### 1. A Failed Connection Does Not Always Mean the Network Is Broken

Firewall policy may intentionally prevent communication.

Always review firewall logs before changing network configuration.

---

### 2. Segmentation Must Be Tested

Creating different subnets alone does not prove that network isolation is working.

The policy should be actively tested:

```text
Traffic That Should Pass
        ↓
      PASS

Traffic That Should Fail
        ↓
      FAIL

Firewall Logs
        ↓
    CONFIRM WHY
```

---

### 3. Security Should Permit Required Services

Effective segmentation does not mean blocking every connection.

Security controls should permit legitimate services while reducing unnecessary access.

This principle later allowed the Ubuntu Wazuh Agent to communicate with the Wazuh manager over TCP `1514` without removing the broader DMZ isolation policy.

---

### 4. Firewall Rule Order Matters

A correctly written rule may still fail if it is evaluated after a broader blocking rule.

Rule order therefore becomes part of firewall troubleshooting.

---

### 5. Logs Are Security Evidence

OPNsense logs were not used only for troubleshooting.

They also provided evidence that the firewall security policy was operating as intended.

This same principle becomes important later in the project when network, endpoint, IDS, and SIEM logs are correlated during SOC investigations.

---

# 🧠 Skills Demonstrated

| Skill | Application |
|---|---|
| **Firewall Administration** | Configured OPNsense as the central security gateway |
| **Network Segmentation** | Separated Security LAN and DMZ |
| **IPv4 Networking** | Managed multiple private network ranges |
| **Routing** | Routed traffic through OPNsense |
| **NAT** | Maintained external connectivity |
| **DHCP** | Supported dynamic network configuration |
| **Firewall Rules** | Controlled communication between security zones |
| **Access Control** | Restricted unauthorized DMZ-to-LAN traffic |
| **Security Logging** | Used firewall logs to verify policy enforcement |
| **Troubleshooting** | Distinguished policy blocks from network failures |
| **Rule Ordering** | Applied narrow exceptions before broad blocking policies |
| **Validation** | Tested both permitted and denied traffic |

---

# 📸 Evidence Summary

The original Phase 2 evidence is reused in this reorganized documentation.

| Evidence | Existing Screenshot |
|---|---|
| OPNsense Dashboard | `phase1-opnsense-dashboard.png` |
| OPNsense Interfaces | `phase2-interfaces.png` |
| Firewall Rules | `phase2-firewall-rules.png` |
| DMZ Segmentation Validation | `phase2-segmentation-validation.png` |

No duplicate screenshots are required.

---

# 🏁 Phase Outcome

## ✅ Phase 2 Complete

Phase 2 successfully implemented firewall-based segmentation between the internal Security LAN and isolated DMZ.

The completed security model was:

```text
                         INTERNET
                            │
                            ▼
                     SOC-OPNsense
                            │
               Firewall / NAT / Routing
                            │
             ┌──────────────┴──────────────┐
             │                             │
             ▼                             ▼
        SECURITY LAN                      DMZ
        10.10.10.0/24                10.50.20.0/24
             ▲                             │
             │                             │
             └──── Unauthorized ───────────┘
                    Traffic Blocked
                         ❌

              Required Traffic
                    Allowed
                      ✅
```

The phase demonstrated that network traffic could be:

- Segmented
- Controlled
- Permitted when required
- Blocked when unauthorized
- Logged
- Validated through firewall evidence

The segmented environment was now ready for endpoint security monitoring.

---

# ➡️ Next Phase

**Phase 03 — Endpoint Security Monitoring**

Phase 3 introduces security telemetry from Windows and Linux endpoints using:

- Windows Security Auditing
- Sysmon
- PowerShell logging
- auditd
- osquery
- Wazuh Agents

---

[← Phase 01](phase-01-virtualbox-environment.md) | [🏠 Back to Main Project](../README.md) | [Phase 03 →](phase-03-endpoint-monitoring.md)

---

### Enterprise Security Operations Lab

**SOC Operations • Detection Engineering • Network Security • Security Automation • Incident Response**
