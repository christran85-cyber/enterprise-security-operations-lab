# 🌐 Phase 12 — Web Application Security Assessment

> **Objective:** Deploy a deliberately vulnerable web application in the DMZ and perform an authorized web application security assessment using service discovery, technology fingerprinting, vulnerability enumeration, troubleshooting, recovery, and post-recovery validation.

[← Phase 11](phase-11-incident-response.md) | [🏠 Main Project](../README.md) | [Phase 13 →](phase-13-email-automation.md)

---

## 📑 Table of Contents

- [Phase Summary](#-phase-summary)
- [Overview](#-overview)
- [Assessment Architecture](#️-assessment-architecture)
- [Phase Objectives](#-phase-objectives)
- [OWASP Juice Shop Deployment](#-owasp-juice-shop-deployment)
- [Initial Service Discovery](#-initial-service-discovery)
- [HTTP Service Validation](#-http-service-validation)
- [Technology Fingerprinting](#-technology-fingerprinting)
- [Nikto Vulnerability Enumeration](#-nikto-vulnerability-enumeration)
- [Security Findings](#-security-findings)
- [Application Availability Issue](#️-application-availability-issue)
- [Docker Troubleshooting](#-docker-troubleshooting)
- [Service Recovery](#-service-recovery)
- [Post-Recovery Validation](#-post-recovery-validation)
- [Commands Used](#-commands-used)
- [Assessment Workflow](#-assessment-workflow)
- [Lessons Learned](#-lessons-learned)
- [Skills Demonstrated](#-skills-demonstrated)
- [Evidence Summary](#-evidence-summary)
- [VirtualBox Snapshot](#-virtualbox-snapshot)
- [Phase Outcome](#-phase-outcome)

---

# 📊 Phase Summary

| Category | Details |
|---|---|
| **Status** | ✅ Complete |
| **Analyst System** | SOC-Kali |
| **Analyst IP** | `10.10.10.103` |
| **Target System** | SOC-Ubuntu |
| **Target IP** | `10.50.20.100` |
| **Target Zone** | DMZ |
| **Web Server** | Apache |
| **Web Server Port** | TCP/80 |
| **Vulnerable Application** | OWASP Juice Shop |
| **Deployment** | Docker |
| **Application Port** | TCP/3000 |
| **Discovery Tool** | Nmap |
| **Fingerprinting Tool** | WhatWeb |
| **Vulnerability Tool** | Nikto |
| **HTTP Validation** | curl |
| **Primary Skill** | Web Application Security Assessment |
| **Workflow** | Discovery → Fingerprinting → Vulnerability Enumeration → Analysis → Troubleshooting → Recovery → Validation → Documentation |

---

# 📋 Overview

Phase 12 expanded the Enterprise Security Operations Lab into **web application security assessment**.

OWASP Juice Shop was deployed on SOC-Ubuntu as a deliberately vulnerable application for controlled security testing.

The assessment was performed from:

```text
SOC-Kali
10.10.10.103
```

against:

```text
SOC-Ubuntu
10.50.20.100
```

The target environment provided two web-service components:

```text
SOC-Ubuntu
10.50.20.100
      │
      ├── Apache
      │     └── TCP/80
      │
      └── Docker
            └── OWASP Juice Shop
                  └── TCP/3000
```

The assessment combined multiple tools rather than relying on a single scanner.

```text
Nmap
  +
WhatWeb
  +
Nikto
  +
curl
  +
Docker
  │
  ▼
Web Application Assessment
```

An unexpected Juice Shop container failure also created a realistic troubleshooting scenario requiring service diagnosis, recovery, and validation before testing could continue.

---

# 🏗️ Assessment Architecture

The Phase 12 architecture was:

```text
                    SOC-Kali
                  10.10.10.103
                       │
          ┌────────────┼────────────┐
          │            │            │
          ▼            ▼            ▼
        Nmap        WhatWeb        Nikto
          │            │            │
          └────────────┼────────────┘
                       │
                       ▼
                  SOC-Ubuntu
                 10.50.20.100
                       │
             ┌─────────┴─────────┐
             │                   │
             ▼                   ▼
         Apache :80           Docker
                                  │
                                  ▼
                         OWASP Juice Shop
                              TCP/3000
```

The security assessment followed:

```text
Discovery
   │
   ▼
Service Enumeration
   │
   ▼
Application Fingerprinting
   │
   ▼
Vulnerability Enumeration
   │
   ▼
Finding Analysis
   │
   ▼
Troubleshooting
   │
   ▼
Service Recovery
   │
   ▼
Validation
   │
   ▼
Documentation
```

---

# 🎯 Phase Objectives

- [x] Deploy OWASP Juice Shop on SOC-Ubuntu
- [x] Host the vulnerable application using Docker
- [x] Validate Juice Shop availability on TCP/3000
- [x] Perform Nmap service discovery
- [x] Identify exposed web services
- [x] Validate HTTP connectivity
- [x] Fingerprint web technologies with WhatWeb
- [x] Perform vulnerability enumeration with Nikto
- [x] Review HTTP security headers
- [x] Identify potential sensitive paths
- [x] Distinguish scanner findings from confirmed vulnerabilities
- [x] Troubleshoot unexpected application downtime
- [x] Inspect Docker container state
- [x] Recover the Juice Shop container
- [x] Revalidate TCP/3000
- [x] Continue the assessment after recovery
- [x] Document security findings
- [x] Preserve the completed lab state

---

# 🧃 OWASP Juice Shop Deployment

OWASP Juice Shop was deployed on SOC-Ubuntu as the deliberately vulnerable web application used during Phase 12.

The application ran inside Docker and was exposed through:

```text
TCP/3000
```

The application path was therefore:

```text
SOC-Kali
    │
    ▼
OPNsense
    │
    ▼
SOC-Ubuntu
10.50.20.100
    │
    ▼
Docker
    │
    ▼
OWASP Juice Shop
TCP/3000
```

Juice Shop provided a safe, intentionally vulnerable target for practicing web application assessment techniques inside the isolated lab.

## 📸 Evidence — OWASP Juice Shop

![OWASP Juice Shop](../images/phase12-juice-shop.png)

**Result:** ✅ OWASP Juice Shop deployed as the controlled web-security target.

---

# 🔍 Initial Service Discovery

Nmap was used from SOC-Kali to identify the network services exposed by SOC-Ubuntu.

The purpose was to establish the target's visible attack surface before deeper web assessment.

The discovery process was:

```text
SOC-Kali
    │
    ▼
Nmap
    │
    ▼
10.50.20.100
    │
    ▼
Identify Open Ports
    │
    ▼
Identify Services
```

The assessment identified web services associated with the Ubuntu target, including Apache and the Juice Shop application environment.

## 📸 Evidence — Nmap Service Enumeration

![Phase 12 Nmap Service Enumeration](../images/phase12-nmap-service-enumeration.png)

**Result:** ✅ Target services successfully enumerated.

---

# 🌍 HTTP Service Validation

Before running additional web assessment tools, HTTP connectivity was validated.

This step helped distinguish:

```text
Application Problem
```

from:

```text
Network Connectivity Problem
```

The service chain being tested was:

```text
SOC-Kali
   │
   ▼
Network
   │
   ▼
SOC-Ubuntu
   │
   ▼
TCP Port
   │
   ▼
Web Service
   │
   ▼
Application
```

`curl` was used as part of the HTTP validation process.

This provided a direct method for reviewing HTTP responses and confirming whether the target service was responding.

---

# 🔬 Technology Fingerprinting

After confirming web-service availability, **WhatWeb** was used to fingerprint the target.

WhatWeb provided additional context about the technologies exposed by the application.

The workflow was:

```text
Target Web Service
       │
       ▼
     WhatWeb
       │
       ▼
HTTP Response Analysis
       │
       ▼
Technology Identification
```

Fingerprinting helps an analyst understand what technologies are present before deeper testing.

## 📸 Evidence — WhatWeb Fingerprinting

![Phase 12 WhatWeb Fingerprinting](../images/phase12-whatweb-fingerprinting.png)

**Result:** ✅ Web technologies successfully fingerprinted.

---

# 🛡️ Nikto Vulnerability Enumeration

Nikto was used to perform automated web-server and application vulnerability enumeration.

The purpose was to identify:

- Potential security misconfigurations
- Missing security headers
- Potential sensitive paths
- Web-server configuration issues
- Findings requiring manual validation

The process followed:

```text
Web Target
    │
    ▼
  Nikto
    │
    ▼
Automated Enumeration
    │
    ▼
Potential Findings
    │
    ▼
Manual Analysis Required
```

A critical principle during this phase was:

> Automated scanner output was treated as a source of potential findings, not automatic proof of a confirmed vulnerability.

## 📸 Evidence — Nikto Vulnerability Scan

![Phase 12 Nikto Vulnerability Scan](../images/phase12-nikto-vulnerability-scan.png)

**Result:** ✅ Automated vulnerability enumeration completed.

---

# 🚨 Security Findings

The assessment identified several findings and security-hardening opportunities.

| Finding | Assessment |
|---|---|
| Content-Security-Policy missing | Security hardening opportunity |
| Referrer-Policy missing | Security hardening opportunity |
| Permissions-Policy missing | Security hardening opportunity |
| Strict-Transport-Security missing | Relevant when HTTPS is deployed |
| `/ftp/` identified | Requires manual review |
| `/public/` identified | Requires manual review |
| Potential sensitive paths | Scanner finding requiring validation |
| `Access-Control-Allow-Origin: *` | Configuration should be reviewed based on application requirements |
| Juice Shop container exited | Operational/application availability issue |

The findings were intentionally separated into:

```text
Confirmed Observation
        │
        ▼
Document
```

versus:

```text
Scanner Finding
      │
      ▼
Manual Validation
      │
      ▼
Determine Security Impact
```

This avoided overstating automated scan results.

## 📸 Evidence — Assessment Findings

![Phase 12 Web Assessment Findings](../images/phase12-web-assessment-findings.png)

---

# ⚠️ Application Availability Issue

During the assessment, OWASP Juice Shop unexpectedly became unavailable.

At first, this could have represented several possible problems:

```text
SOC-Kali
   │
   ▼
Network Problem?
   │
   ▼
Port Problem?
   │
   ▼
Ubuntu Problem?
   │
   ▼
Docker Problem?
   │
   ▼
Application Problem?
```

Rather than immediately rebuilding the application, the service chain was investigated.

The troubleshooting process established that the Juice Shop Docker container had stopped.

This turned an unexpected availability issue into an additional operational troubleshooting exercise.

---

# 🐳 Docker Troubleshooting

Docker status information was used to determine the state of the Juice Shop container.

The investigation followed:

```text
Application Unavailable
        │
        ▼
Check Target Host
        │
        ▼
Check Network
        │
        ▼
Check TCP/3000
        │
        ▼
Check Docker
        │
        ▼
Identify Stopped Container
```

The existing container was identified instead of unnecessarily creating a replacement.

## 📸 Evidence — Docker Troubleshooting

![Phase 12 Docker Troubleshooting](../images/phase12-docker-troubleshooting.png)

**Finding:** Juice Shop container had exited.

---

# ♻️ Service Recovery

After identifying the stopped Juice Shop container, the existing container was restarted.

The recovery process followed:

```text
Stopped Container
       │
       ▼
Identify Existing Container
       │
       ▼
Restart Container
       │
       ▼
Check Container State
       │
       ▼
Validate TCP/3000
       │
       ▼
Continue Assessment
```

This preserved the existing application deployment and allowed testing to continue.

## 📸 Evidence — Juice Shop Recovery

![Phase 12 Juice Shop Recovery](../images/phase12-juice-shop-recovery.png)

**Result:** ✅ Existing Juice Shop container successfully recovered.

---

# ✅ Post-Recovery Validation

After restarting Juice Shop, application availability was validated before continuing security testing.

The validation included confirming:

```text
SOC-Ubuntu
10.50.20.100
      │
      ▼
TCP/3000
      │
      ▼
OWASP Juice Shop
      │
      ▼
Reachable
```

This demonstrated that recovery should not be considered successful simply because a container starts.

The application itself must also be validated.

## 📸 Evidence — TCP/3000 Validation

![Phase 12 TCP 3000 Validation](../images/phase12-tcp3000-validation.png)

**Result:** ✅ Juice Shop availability restored and validated.

---

# 💻 Commands Used

Phase 12 used several tools for discovery, validation, fingerprinting, vulnerability enumeration, and troubleshooting.

## Nmap

Nmap was used for service enumeration against:

```text
10.50.20.100
```

The assessment used Nmap to determine which network services were exposed by the Ubuntu target.

---

## WhatWeb

WhatWeb was used against the web target to identify exposed application technologies.

The output provided additional application context before vulnerability enumeration.

---

## Nikto

Nikto was used to enumerate potential web-server and application security weaknesses.

The results were analyzed as **potential findings requiring validation**, not automatically as confirmed vulnerabilities.

---

## curl

`curl` was used to validate HTTP service behavior and inspect responses.

This helped determine whether problems occurred at the network, service, or application layer.

---

## Docker

Docker was used to:

- Host OWASP Juice Shop
- Inspect container state
- Identify the stopped application container
- Restart the existing container
- Validate application recovery

> The original Phase 12 documentation confirms the tools and operations above but does not preserve every exact command-line argument used during each test. Exact command lines that were not preserved are intentionally not reconstructed here.

---

# 🔄 Assessment Workflow

The completed Phase 12 assessment followed:

```text
                    SOC-Kali
                       │
          ┌────────────┼────────────┐
          │            │            │
        Nmap        WhatWeb        Nikto
          │            │            │
          └────────────┼────────────┘
                       │
                       ▼
                  SOC-Ubuntu
                 10.50.20.100
                       │
             ┌─────────┴─────────┐
             │                   │
             ▼                   ▼
         Apache :80           Docker
                                  │
                                  ▼
                         OWASP Juice Shop
                              TCP/3000
```

The operational workflow was:

```text
Discovery
   │
   ▼
Service Enumeration
   │
   ▼
Application Fingerprinting
   │
   ▼
Vulnerability Enumeration
   │
   ▼
Finding Analysis
   │
   ▼
Troubleshooting
   │
   ▼
Service Recovery
   │
   ▼
Validation
   │
   ▼
Documentation
```

---

# 🔧 Troubleshooting Methodology

The Juice Shop availability issue reinforced a layered troubleshooting approach.

```text
Application Unavailable
        │
        ▼
Is the Host Reachable?
        │
        ▼
Is the Network Path Working?
        │
        ▼
Is TCP/3000 Available?
        │
        ▼
Is Docker Running?
        │
        ▼
Is the Container Running?
        │
        ▼
Is Juice Shop Responding?
```

This approach prevented unnecessary changes.

Instead of rebuilding the application immediately, the failed layer was identified first.

The problem was ultimately traced to the application container.

After the existing container was restarted, TCP/3000 and application availability were validated again.

---

# 💡 Lessons Learned

## 1. Automated Scanners Require Validation

Nikto can identify potential vulnerabilities and configuration weaknesses, but scanner output should not automatically be treated as a confirmed vulnerability.

Analysts must review findings and understand their context.

---

## 2. Multiple Tools Provide Better Context

Nmap, WhatWeb, curl, Docker, and Nikto provided different perspectives on the same target.

```text
Nmap
  │
  └── What services are exposed?

WhatWeb
  │
  └── What technologies are present?

Nikto
  │
  └── What potential weaknesses exist?

curl
  │
  └── How is the HTTP service responding?

Docker
  │
  └── Is the application container operational?
```

Together, these tools produced a more complete assessment.

---

## 3. Application Availability Matters

When Juice Shop became unavailable, the issue initially appeared to be a connectivity problem.

Checking Docker showed that the application container itself had stopped.

The complete service chain should therefore be validated:

```text
Host
  ↓
Network
  ↓
Port
  ↓
Process / Container
  ↓
Application
```

---

## 4. Troubleshooting Is Part of Security Operations

Unexpected service failures are part of real security work.

The container failure required:

```text
Identify
   ↓
Diagnose
   ↓
Recover
   ↓
Validate
   ↓
Continue
```

---

## 5. Do Not Rebuild Before Diagnosing

The existing Juice Shop container was recovered instead of creating a new deployment.

This preserved the environment and reduced unnecessary changes.

---

## 6. A Running Container Does Not Automatically Prove Application Health

After restarting the container, TCP/3000 and application accessibility still had to be verified.

```text
Container Running
       ≠
Application Validated
```

---

## 7. Security Headers Provide Defensive Context

The assessment identified missing HTTP security headers as hardening opportunities.

Their absence was documented without automatically treating each one as a directly exploitable vulnerability.

---

## 8. Sensitive Paths Require Manual Review

Paths such as:

```text
/ftp/
/public/
```

require additional investigation to determine whether they expose sensitive or unintended content.

Discovery alone does not prove impact.

---

## 9. CORS Configuration Requires Application Context

The observed:

```text
Access-Control-Allow-Origin: *
```

configuration should be evaluated based on the application's intended access model.

Its presence alone does not establish exploitation.

---

## 10. Findings Should Be Described Accurately

A professional assessment should distinguish:

```text
Observation
Potential Finding
Confirmed Vulnerability
Operational Issue
```

This avoids overstating risk.

---

# 🧠 Skills Demonstrated

| Skill | Application |
|---|---|
| **Web Application Security** | Assessed a deliberately vulnerable application |
| **Nmap** | Performed service enumeration |
| **HTTP Analysis** | Validated web-service behavior |
| **WhatWeb** | Fingerprinted web technologies |
| **Nikto** | Performed vulnerability enumeration |
| **Security Headers** | Reviewed HTTP hardening opportunities |
| **Docker** | Hosted and managed Juice Shop |
| **Docker Troubleshooting** | Diagnosed stopped container |
| **Service Recovery** | Restored the existing application |
| **Linux Administration** | Validated target services |
| **curl** | Tested HTTP behavior |
| **Apache** | Assessed exposed web service |
| **OWASP Juice Shop** | Provided controlled vulnerable target |
| **Finding Analysis** | Distinguished findings from confirmed vulnerabilities |
| **Troubleshooting** | Diagnosed availability failure by layer |
| **Security Documentation** | Documented findings and recovery |

---

# 📸 Evidence Summary

Phase 12 documentation preserves evidence for the web application assessment, including:

| Evidence | Screenshot |
|---|---|
| OWASP Juice Shop | `phase12-juice-shop.png` |
| Nmap Service Enumeration | `phase12-nmap-service-enumeration.png` |
| WhatWeb Fingerprinting | `phase12-whatweb-fingerprinting.png` |
| Nikto Vulnerability Scan | `phase12-nikto-vulnerability-scan.png` |
| Web Assessment Findings | `phase12-web-assessment-findings.png` |
| Docker Troubleshooting | `phase12-docker-troubleshooting.png` |
| Juice Shop Recovery | `phase12-juice-shop-recovery.png` |
| TCP/3000 Validation | `phase12-tcp3000-validation.png` |

Because this document is stored under:

```text
/docs/
```

image references use:

```text
../images/<filename>
```

---

# 💾 VirtualBox Snapshot

After completing the web application security assessment and validating the recovered environment, a VirtualBox snapshot was created.

## Snapshot Name

```text
Phase 12 - Web Application Security Assessment Complete
```

## Snapshot Description

```text
Completed Phase 12 web application security assessment.

Deployed OWASP Juice Shop on SOC-Ubuntu and performed
Nmap service enumeration, WhatWeb fingerprinting, and
Nikto vulnerability enumeration from SOC-Kali.

Validated TCP/3000 connectivity and recovered the Juice
Shop Docker container after an unexpected exit.

Documented assessment findings, troubleshooting actions,
and lessons learned.
```

The snapshot preserved the completed Phase 12 environment before moving into security automation.

---

# 🏁 Phase Outcome

## ✅ Phase 12 Complete

Phase 12 successfully expanded the Enterprise Security Operations Lab into **web application security assessment**.

The completed assessment combined:

```text
SOC-Kali
10.10.10.103
     │
     ├──── Nmap
     ├──── WhatWeb
     ├──── Nikto
     └──── curl
     │
     ▼
SOC-Ubuntu
10.50.20.100
     │
     ├──── Apache :80
     │
     └──── Docker
              │
              ▼
       OWASP Juice Shop
           TCP/3000
```

The workflow demonstrated:

```text
Discovery
    │
    ▼
Fingerprinting
    │
    ▼
Vulnerability Enumeration
    │
    ▼
Finding Analysis
    │
    ▼
Unexpected Application Failure
    │
    ▼
Docker Troubleshooting
    │
    ▼
Service Recovery
    │
    ▼
Post-Recovery Validation
    │
    ▼
Documentation

    ✅
```

Nmap identified exposed services, WhatWeb fingerprinted the application, and Nikto identified potential security weaknesses and configuration issues.

The unexpected Juice Shop container failure added practical troubleshooting experience. Docker status information was used to identify the stopped container, recover the service, verify TCP/3000 availability, and continue the assessment.

Phase 12 demonstrated that effective web security assessment involves more than running scanners.

An analyst must:

- Understand the target
- Correlate multiple tools
- Validate scanner findings
- Troubleshoot service availability
- Recover affected services
- Verify recovery
- Accurately document findings

The completed workflow was:

**Discovery → Fingerprinting → Vulnerability Enumeration → Analysis → Troubleshooting → Recovery → Validation → Documentation**

---

# ➡️ Next Phase

## Phase 13 — Python Security Automation & Automated SOC Email Alerting

Phase 13 extends the SOC environment with Python-based automation and automated security notifications.

The next phase includes:

- JSON security-event processing
- Python event analysis
- Severity classification
- Security reporting
- CSV export
- Gmail API integration
- OAuth 2.0
- Wazuh custom integration
- Automated SOC email alerts
- End-to-end alert validation

---

[← Phase 11](phase-11-incident-response.md) | [🏠 Back to Main Project](../README.md) | [Phase 13 →](phase-13-email-automation.md)

---

### Enterprise Security Operations Lab

**Web Application Security • OWASP Juice Shop • Nmap • WhatWeb • Nikto • Docker • HTTP Analysis • Troubleshooting**
