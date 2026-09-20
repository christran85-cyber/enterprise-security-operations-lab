# 📡 Phase 10 — Centralized Network Security Logging & Correlation

> **Objective:** Centralize OPNsense firewall telemetry in Wazuh, validate the remote syslog pipeline, generate controlled network activity, and correlate firewall, IDS, and SIEM telemetry during a security investigation.

[← Phase 09](phase-09-threat-intelligence.md) | [🏠 Main Project](../README.md) | [Phase 11 →](phase-11-incident-response.md)

---

## 📑 Table of Contents

- [Phase Summary](#-phase-summary)
- [Overview](#-overview)
- [Environment](#️-environment)
- [Centralized Logging Architecture](#️-centralized-logging-architecture)
- [Phase Objectives](#-phase-objectives)
- [Wazuh Remote Syslog Configuration](#-wazuh-remote-syslog-configuration)
- [Wazuh Syslog Listener Validation](#-wazuh-syslog-listener-validation)
- [OPNsense Remote Syslog](#-opnsense-remote-syslog)
- [Packet-Level Syslog Validation](#-packet-level-syslog-validation)
- [Wazuh Archive Validation](#-wazuh-archive-validation)
- [Controlled Reconnaissance](#-controlled-reconnaissance)
- [Suricata Telemetry](#-suricata-telemetry)
- [Multi-Source Correlation](#-multi-source-correlation)
- [Commands Used](#-commands-used)
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
| **Firewall IP** | `10.10.10.1` |
| **SIEM** | Wazuh |
| **Wazuh IP** | `10.10.10.102` |
| **Analyst System** | SOC-Kali `10.10.10.103` |
| **DMZ Target** | SOC-Ubuntu `10.50.20.100` |
| **IDS** | Suricata |
| **Logging Protocol** | Syslog |
| **Transport** | UDP |
| **Port** | `514` |
| **Firewall Decoder** | `pf` |
| **Wazuh Archive** | `archives.json` |
| **Suricata Telemetry** | EVE JSON |
| **Primary Skill** | Centralized Logging & Correlation |
| **Workflow** | Generate → Forward → Collect → Store → Search → Correlate |

---

# 📋 Overview

Phase 10 extended the Enterprise Security Operations Lab by centralizing **network security telemetry from OPNsense into Wazuh**.

Earlier phases provided:

- Endpoint telemetry
- Wazuh SIEM/XDR
- Suricata IDS
- Security-event correlation
- Vulnerability management
- Python automation
- Threat-intelligence integration

Phase 10 connected the firewall layer directly to the centralized SIEM.

The goal was not simply to generate security events.

The goal was to validate the entire telemetry pipeline:

```text
Network Activity
      │
      ▼
OPNsense Firewall
      │
      ├──────────────► Suricata IDS
      │
      │
      ▼
Remote Syslog
UDP/514
      │
      ▼
Wazuh
      │
      ▼
archives.json
      │
      ▼
Centralized Search
      │
      ▼
Security Correlation
```

This allowed activity originating from SOC-Kali and targeting SOC-Ubuntu to be traced across multiple security layers.

---

# 🖥️ Environment

| System | Role | IP Address |
|---|---|---|
| **SOC-OPNsense** | Firewall / Suricata IDS / Syslog Source | `10.10.10.1` |
| **SOC-Wazuh** | SIEM / Centralized Log Collection | `10.10.10.102` |
| **SOC-Kali** | Analyst / Controlled Traffic Generator | `10.10.10.103` |
| **SOC-Ubuntu** | DMZ Target | `10.50.20.100` |

The investigated traffic path was:

```text
SOC-Kali
10.10.10.103
     │
     │ Controlled Reconnaissance
     ▼
SOC-OPNsense
Firewall + Suricata
     │
     ├────────► Suricata Detection
     │
     │ Remote Syslog
     │ UDP/514
     ▼
SOC-Wazuh
10.10.10.102
     │
     ▼
Centralized Security Analysis
```

---

# 🏗️ Centralized Logging Architecture

The completed Phase 10 architecture was:

```text
                 SOC-Kali
              10.10.10.103
                    │
                    │
          Controlled Reconnaissance
                    │
                    ▼
                OPNsense
              10.10.10.1
           Firewall + Suricata
                    │
           ┌────────┴────────┐
           │                 │
           ▼                 ▼
    Firewall Telemetry   Suricata IDS
           │                 │
           │                 ▼
           │              EVE JSON
           │                 │
           ▼                 │
       Syslog UDP/514        │
           │                 │
           ▼                 │
          Wazuh              │
       10.10.10.102          │
           │                 │
           ▼                 │
      archives.json          │
           │                 │
           └────────┬────────┘
                    │
                    ▼
          Security Investigation
                    │
                    ▼
             Event Correlation
```

This architecture combined three different perspectives:

**OPNsense**
- Network connection telemetry
- Firewall decisions
- Source/destination information

**Suricata**
- IDS detection
- Reconnaissance identification
- Security context

**Wazuh**
- Centralized storage
- Search
- Investigation
- Correlation

---

# 🎯 Phase Objectives

- [x] Configure Wazuh to accept remote syslog
- [x] Restrict the permitted syslog source to OPNsense
- [x] Use UDP port `514`
- [x] Validate Wazuh configuration
- [x] Restart Wazuh safely
- [x] Verify the UDP/514 listener
- [x] Configure OPNsense remote syslog
- [x] Validate packets reaching SOC-Wazuh
- [x] Verify firewall events in Wazuh archives
- [x] Generate controlled Kali reconnaissance
- [x] Trace Kali-to-Ubuntu activity
- [x] Investigate Suricata EVE JSON
- [x] Validate Suricata reconnaissance detection
- [x] Correlate firewall and IDS telemetry
- [x] Document troubleshooting methodology
- [x] Preserve investigation evidence

---

# ⚙️ Wazuh Remote Syslog Configuration

Wazuh was configured to accept remote syslog messages from OPNsense.

The Wazuh configuration contained a remote listener similar to:

```xml
<remote>
  <connection>syslog</connection>
  <port>514</port>
  <protocol>udp</protocol>
  <allowed-ips>10.10.10.1</allowed-ips>
</remote>
```

The important security control was:

```xml
<allowed-ips>10.10.10.1</allowed-ips>
```

This restricted the permitted remote syslog source to the OPNsense firewall.

The resulting path was:

```text
OPNsense
10.10.10.1
     │
     │ UDP/514
     ▼
SOC-Wazuh
10.10.10.102
```

---

## Validate Wazuh Configuration

Before restarting the manager, the configuration was tested:

```bash
sudo /var/ossec/bin/wazuh-analysisd -t
```

This reduced the risk of restarting Wazuh with an invalid configuration.

Wazuh was then restarted:

```bash
sudo systemctl restart wazuh-manager
```

The same principle used during Apache hardening applied here:

```text
Configuration Change
        │
        ▼
Syntax Validation
        │
        ▼
Service Restart
        │
        ▼
Operational Validation
```

**Result:** ✅ Wazuh configured for remote OPNsense syslog collection.

---

# 👂 Wazuh Syslog Listener Validation

After restarting Wazuh, the next step was to verify that the system was actually listening on UDP port `514`.

The listener was checked using:

```bash
sudo ss -lunp | grep ':514'
```

This validated the receiving side of the pipeline.

```text
Wazuh Configuration
        │
        ▼
Wazuh Manager
        │
        ▼
UDP/514 Listener
        │
        ▼
Ready for OPNsense
```

## 📸 Evidence — Wazuh Syslog Listener

![Wazuh Syslog Listener](../images/phase10-wazuh-syslog-listener.png)

The evidence confirms that Wazuh was prepared to receive remote syslog telemetry.

**Result:** ✅ UDP/514 listener validated.

---

# 🔥 OPNsense Remote Syslog

OPNsense was configured to forward firewall telemetry to:

```text
SOC-Wazuh
10.10.10.102
```

using:

```text
UDP/514
```

The resulting logging path was:

```text
OPNsense Firewall Event
          │
          ▼
       Syslog
          │
          ▼
      UDP/514
          │
          ▼
     SOC-Wazuh
```

At this point, configuration alone was not considered sufficient proof.

The next step was to verify that packets actually reached the Wazuh server.

---

# 📦 Packet-Level Syslog Validation

Packet capture was used on SOC-Wazuh to verify that OPNsense was transmitting syslog traffic.

```bash
sudo tcpdump -ni any udp port 514
```

The packet capture confirmed traffic following the path:

```text
10.10.10.1 → 10.10.10.102:514
```

This proved that:

- OPNsense was sending traffic
- Network connectivity existed
- UDP/514 packets reached Wazuh

The validation layers now looked like:

```text
Wazuh Listening
      │
      ▼
OPNsense Sending
      │
      ▼
Packets Reach Wazuh
      │
      ▼
Next: Verify Storage
```

**Result:** ✅ OPNsense syslog packets reached SOC-Wazuh.

---

# 🗃️ Wazuh Archive Validation

Receiving packets does not automatically prove that the SIEM stored or processed them.

The Wazuh archive was therefore investigated.

The relevant archive was:

```text
/var/ossec/logs/archives/archives.json
```

A search for OPNsense telemetry used:

```bash
sudo grep '10.10.10.1' /var/ossec/logs/archives/archives.json | tail -5
```

The returned events contained structured firewall telemetry.

Important fields included:

```text
hostname: OPNsense.internal
program_name: filterlog
decoder: pf
action: pass
```

This established:

```text
OPNsense
    │
    ▼
Syslog UDP/514
    │
    ▼
Wazuh
    │
    ▼
pf Decoder
    │
    ▼
Structured Firewall Event
```

## 📸 Evidence — OPNsense Telemetry in Wazuh

![OPNsense Syslog to Wazuh](../images/phase10-opnsense-syslog-to-wazuh.png)

This evidence demonstrates that OPNsense telemetry was not only transmitted—it was also available inside the centralized Wazuh environment.

**Result:** ✅ OPNsense firewall telemetry stored and searchable in Wazuh.

---

# 🔍 Controlled Reconnaissance

SOC-Kali was used to generate authorized reconnaissance against SOC-Ubuntu.

```text
Source:
SOC-Kali
10.10.10.103

Target:
SOC-Ubuntu
10.50.20.100
```

This created traffic that could be investigated across:

- OPNsense
- Suricata
- Wazuh

The investigation path was:

```text
SOC-Kali
    │
    ▼
Reconnaissance
    │
    ▼
OPNsense
    │
    ├────────► Firewall Telemetry
    │
    └────────► Suricata Inspection
```

The purpose was not simply to generate an IDS alert.

The goal was to determine whether the same activity could be identified across multiple telemetry sources.

---

# 🛡️ Suricata Telemetry

Suricata provided IDS visibility into the controlled Kali-to-Ubuntu activity.

Suricata's EVE JSON telemetry was investigated as part of the correlation process.

## EVE JSON Location

The raw Suricata EVE JSON log location was verified.

## 📸 Evidence — Suricata EVE JSON Location

![Suricata EVE Log Location](../images/phase10-suricata-eve-log-location.png)

This established the raw IDS telemetry source used during investigation.

---

## Raw IDS Telemetry

Raw EVE JSON was reviewed for security events associated with the controlled activity.

## 📸 Evidence — Suricata EVE JSON Alert

![Suricata EVE JSON Alert](../images/phase10-suricata-eve-json-alert.png)

The raw telemetry provided IDS-level evidence associated with the Kali-to-Ubuntu traffic.

---

## Reconnaissance Detection

Suricata successfully identified controlled reconnaissance activity.

## 📸 Evidence — Suricata Nmap Detection

![Suricata Nmap Detection](../images/phase10-suricata-nmap-detection.png)

This provided security context that firewall logs alone could not provide.

```text
Firewall:
"Network connection occurred"

Suricata:
"Reconnaissance activity detected"
```

**Result:** ✅ Controlled reconnaissance detected by Suricata.

---

# 🔗 Multi-Source Correlation

The central goal of Phase 10 was to correlate activity across multiple security layers.

The analyst could compare:

```text
SOC-Kali
10.10.10.103
      │
      ▼
SOC-Ubuntu
10.50.20.100
```

across both firewall and IDS telemetry.

The correlation workflow was:

```text
Kali Reconnaissance
        │
        ▼
OPNsense Firewall
        │
        ├─────────────────┐
        │                 │
        ▼                 ▼
Firewall Telemetry    Suricata IDS
        │                 │
        ▼                 ▼
Wazuh Archive       IDS Detection
        │                 │
        └────────┬────────┘
                 │
                 ▼
        Compare Source IP
                 │
                 ▼
      Compare Destination IP
                 │
                 ▼
         Compare Activity
                 │
                 ▼
       Security Correlation
```

The firewall telemetry established that network activity occurred.

Suricata provided detection context indicating reconnaissance.

Wazuh provided centralized storage and investigation capability.

Together, the telemetry provided a stronger security picture than any individual source.

---

## 📸 Supporting Correlation Evidence

![OPNsense Wazuh Kali Ubuntu Correlation](../images/phase9-opnsense-wazuh-kali-ubuntu-correlation.png)

This supporting cross-phase evidence demonstrates the broader OPNsense, Wazuh, Kali, and Ubuntu correlation workflow.

---

# 💻 Commands Used

## Validate Wazuh Configuration

```bash
sudo /var/ossec/bin/wazuh-analysisd -t
```

Purpose:

```text
Validate Wazuh configuration before restarting
the manager.
```

---

## Restart Wazuh

```bash
sudo systemctl restart wazuh-manager
```

Purpose:

```text
Apply the remote syslog configuration.
```

---

## Verify UDP/514 Listener

```bash
sudo ss -lunp | grep ':514'
```

Purpose:

```text
Confirm that Wazuh is listening for remote
syslog traffic on UDP port 514.
```

---

## Capture Syslog Traffic

```bash
sudo tcpdump -ni any udp port 514
```

Purpose:

```text
Verify that OPNsense syslog packets actually
reach SOC-Wazuh.
```

Expected network path:

```text
10.10.10.1 → 10.10.10.102:514
```

---

## Search Wazuh Archive

```bash
sudo grep '10.10.10.1' /var/ossec/logs/archives/archives.json | tail -5
```

Purpose:

```text
Confirm that OPNsense firewall telemetry
is stored inside Wazuh.
```

---

## Relevant Wazuh Archive

```text
/var/ossec/logs/archives/archives.json
```

---

# 🔧 Troubleshooting

Phase 10 reinforced a layered troubleshooting methodology.

A logging pipeline can fail at several different points.

```text
Source
  │
  ▼
Network
  │
  ▼
Listener
  │
  ▼
Collection
  │
  ▼
Storage
  │
  ▼
Search
  │
  ▼
Correlation
```

Instead of treating the logging pipeline as one component, each layer was tested independently.

---

## 1. Is the Service Listening?

The first question was whether Wazuh was actually listening on the configured port.

```bash
sudo ss -lunp | grep ':514'
```

If there is no listener, packet forwarding alone cannot solve the problem.

---

## 2. Are Packets Reaching the Server?

The next layer was tested using:

```bash
sudo tcpdump -ni any udp port 514
```

This separated:

```text
Network / Forwarding Problem
```

from:

```text
Wazuh Processing Problem
```

If packets are visible in `tcpdump`, then the source and network path are functioning.

---

## 3. Are Events Being Stored?

After packet delivery was confirmed, Wazuh storage was checked.

```bash
sudo grep '10.10.10.1' /var/ossec/logs/archives/archives.json | tail -5
```

This verified that packet receipt translated into stored security telemetry.

---

## 4. Can the Event Be Searched?

Stored data must also be retrievable by the analyst.

Searching the Wazuh archive demonstrated that OPNsense events could be located during an investigation.

---

## 5. Did the IDS Detect the Activity?

Suricata EVE JSON was investigated separately.

This was important because:

```text
Firewall Log ≠ IDS Alert
```

The two telemetry sources provide different information.

---

## 6. Can the Analyst Correlate the Sources?

The final step was to compare:

- Source IP
- Destination IP
- Network activity
- IDS detection
- Firewall telemetry

The full troubleshooting methodology became:

```text
1. Is the service listening?
            │
            ▼
2. Are packets reaching the server?
            │
            ▼
3. Are events being stored?
            │
            ▼
4. Can the event be searched?
            │
            ▼
5. Did the IDS detect the activity?
            │
            ▼
6. Can the analyst correlate the sources?
```

---

# 💡 Lessons Learned

## 1. Configuration Does Not Prove Operation

Adding a syslog configuration does not prove that logs are actually flowing.

Operational validation is required.

---

## 2. A Listening Port Is Only One Layer

Seeing UDP/514 listening proves the receiving service is ready.

It does not prove that OPNsense is sending packets.

---

## 3. Packet Capture Provides Network-Level Proof

Using:

```bash
sudo tcpdump -ni any udp port 514
```

proved that syslog traffic actually reached SOC-Wazuh.

---

## 4. Packet Receipt Does Not Prove Storage

Even when packets reach the server, the SIEM must still successfully ingest and store them.

This required checking:

```text
archives.json
```

---

## 5. Firewall and IDS Telemetry Are Different

OPNsense firewall logs answer questions such as:

```text
Did this connection occur?
Was it passed or blocked?
What were the source and destination?
```

Suricata answers different questions:

```text
Was the activity suspicious?
Did it match a detection rule?
Was reconnaissance identified?
```

---

## 6. Multiple Telemetry Sources Improve Investigation

A single log source provides only part of the picture.

Combining:

```text
Firewall
   +
IDS
   +
SIEM
```

provides stronger investigative context.

---

## 7. Source and Destination IPs Are Key Correlation Fields

The same:

```text
10.10.10.103 → 10.50.20.100
```

activity could be compared across security systems.

---

## 8. Raw Logs Are Valuable During Troubleshooting

Dashboards are useful for investigations, but raw telemetry can provide direct evidence when determining whether a logging pipeline is functioning.

---

## 9. Validate Each Layer Independently

The strongest troubleshooting approach was:

```text
Listener
   ↓
Packets
   ↓
Storage
   ↓
Search
   ↓
Detection
   ↓
Correlation
```

---

## 10. Centralized Logging Improves SOC Visibility

Without centralized logging, an analyst would need to investigate systems individually.

Wazuh provided a central location for network-security telemetry.

---

## 11. IDS Alerts Require Supporting Context

An IDS alert becomes more useful when it can be compared with firewall activity and endpoint information.

---

## 12. Correlation Requires Evidence

Events occurring around the same time should not automatically be assumed to be related.

Correlation should be based on common fields and observable activity.

---

# 🧠 Skills Demonstrated

| Skill | Application |
|---|---|
| **Centralized Logging** | Forwarded OPNsense telemetry into Wazuh |
| **Syslog** | Implemented remote firewall logging |
| **Wazuh** | Collected and investigated network telemetry |
| **OPNsense** | Configured firewall log forwarding |
| **UDP/514** | Validated remote syslog transport |
| **Linux Networking** | Verified listening sockets |
| **tcpdump** | Confirmed packet delivery |
| **Log Analysis** | Investigated `archives.json` |
| **Suricata** | Analyzed IDS telemetry |
| **EVE JSON** | Reviewed raw Suricata security events |
| **Network Security Monitoring** | Traced activity across network controls |
| **Event Correlation** | Compared firewall and IDS telemetry |
| **Troubleshooting** | Isolated failures by pipeline layer |
| **SOC Investigation** | Reconstructed controlled activity |
| **Security Documentation** | Preserved investigation evidence |

---

# 📸 Evidence Summary

Phase 10 includes the following original evidence from the centralized logging and correlation workflow. :contentReference[oaicite:1]{index=1}

| # | Evidence | Screenshot |
|---|---|---|
| 1 | Wazuh Syslog Listener | `phase10-wazuh-syslog-listener.png` |
| 2 | OPNsense Telemetry in Wazuh | `phase10-opnsense-syslog-to-wazuh.png` |
| 3 | Suricata EVE JSON Location | `phase10-suricata-eve-log-location.png` |
| 4 | Raw Suricata IDS Telemetry | `phase10-suricata-eve-json-alert.png` |
| 5 | Suricata Reconnaissance Detection | `phase10-suricata-nmap-detection.png` |
| 6 | Supporting Cross-Phase Correlation Evidence | `phase9-opnsense-wazuh-kali-ubuntu-correlation.png` |

Because this document is located inside:

```text
/docs/
```

the correct screenshot path is:

```text
../images/<filename>
```

The existing evidence files do not need to be renamed.

---

# 🏁 Phase Outcome

## ✅ Phase 10 Complete

Phase 10 successfully established centralized network security logging between OPNsense and Wazuh.

The logging pipeline was validated at multiple layers:

```text
OPNsense
10.10.10.1
     │
     │ Syslog UDP/514
     ▼
SOC-Wazuh
10.10.10.102
     │
     ▼
UDP Listener
     │
     ▼
Packet Capture
     │
     ▼
Wazuh Archive
     │
     ▼
Searchable Firewall Telemetry

     ✅
```

Controlled reconnaissance then demonstrated the broader investigation workflow:

```text
SOC-Kali
10.10.10.103
     │
     │ Reconnaissance
     ▼
SOC-Ubuntu
10.50.20.100
     │
     ▼
OPNsense Firewall
     │
     ├──────────────┐
     │              │
     ▼              ▼
Firewall Logs   Suricata IDS
     │              │
     ▼              ▼
Wazuh Archive   EVE JSON Alert
     │              │
     └───────┬──────┘
             │
             ▼
       SOC Correlation

             ✅
```

The phase demonstrated that:

- Wazuh was listening on UDP/514
- OPNsense transmitted firewall telemetry
- Packets reached SOC-Wazuh
- Wazuh stored the events
- Firewall telemetry was searchable
- Suricata detected controlled reconnaissance
- Raw EVE JSON could be investigated
- Source and destination information could be correlated
- Multiple telemetry sources provided stronger investigative context

The completed workflow was:

```text
Generate → Forward → Collect → Store → Search → Detect → Correlate
```

Phase 10 therefore connected:

**Network Activity → OPNsense Firewall → Remote Syslog → Wazuh SIEM → Suricata IDS → Multi-Source SOC Investigation**

---

# ➡️ Next Phase

## Phase 11 — Incident Response & Case Management

Phase 11 moves from detection and correlation into formal incident-response case management using **DFIR-IRIS**.

The next phase includes:

- DFIR-IRIS deployment
- Incident creation
- SOC case identification
- Asset documentation
- IOC documentation
- Incident timeline development
- Suricata evidence
- OPNsense/Wazuh correlation
- Investigation findings
- Response tasks
- Containment and remediation assessment
- Case closure

---

[← Phase 09](phase-09-threat-intelligence.md) | [🏠 Back to Main Project](../README.md) | [Phase 11 →](phase-11-incident-response.md)

---

### Enterprise Security Operations Lab

**Centralized Logging • OPNsense • Wazuh • Syslog • Suricata • Network Monitoring • Event Correlation**
