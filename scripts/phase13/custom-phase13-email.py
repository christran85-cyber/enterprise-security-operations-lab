#!/opt/phase13-email-venv/bin/python3.14

import sys
import json
import os
import base64

from datetime import datetime, timezone
from email.message import EmailMessage

from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build


SCOPE = ["https://www.googleapis.com/auth/gmail.send"]
TOKEN_FILE = "/var/ossec/integrations/phase13-email/token.json"
HEALTH_LOG = "/tmp/phase13-email-health.log"


def log_health(status, message):
    timestamp = datetime.now(timezone.utc).isoformat()

    with open(HEALTH_LOG, "a") as log:
        log.write(f"{timestamp} | {status} | {message}\n")


def authenticate_gmail():
    creds = None

    if os.path.exists(TOKEN_FILE):
        creds = Credentials.from_authorized_user_file(
            TOKEN_FILE,
            SCOPE
        )

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())

        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json",
                SCOPE
            )

            creds = flow.run_local_server(port=0)

        with open(TOKEN_FILE, "w") as token:
            token.write(creds.to_json())

    return build("gmail", "v1", credentials=creds)


def send_security_alert(alert):
    rule = alert.get("rule", {})

    severity = rule.get("level", "N/A")
    event = rule.get("description", "Unknown Wazuh alert")

    data = alert.get("data", {})

    source_ip = data.get("srcip", "N/A")
    destination_ip = data.get("dstip", "N/A")

    service = authenticate_gmail()

    message = EmailMessage()

    # Portfolio-safe placeholder addresses.
    # Real SOC email addresses are intentionally excluded.
    message["To"] = "soc-analyst@example.com"
    message["From"] = "soc-alerts@example.com"
    message["Subject"] = "SOC Security Alert - Phase 13"

    message.set_content(
        f"""SECURITY OPERATIONS CENTER ALERT

Severity: {severity}
Source: Suricata
Event: {event}
Source IP: {source_ip}
Destination IP: {destination_ip}

Phase 13 - Python Security Automation
"""
    )

    encoded_message = base64.urlsafe_b64encode(
        message.as_bytes()
    ).decode()

    try:
        result = service.users().messages().send(
            userId="me",
            body={"raw": encoded_message}
        ).execute()

        log_health(
            "SUCCESS",
            "Gmail alert delivered - Message ID " + result["id"]
        )

        print("Email security alert sent successfully.")
        print("Gmail Message ID:", result["id"])

    except Exception as error:
        log_health(
            "FAILURE",
            f"Gmail alert delivery failed - "
            f"{type(error).__name__}: {error}"
        )

        raise


if __name__ == "__main__":
    alert_file = sys.argv[1]

    with open(alert_file, "r") as file:
        alert = json.load(file)

    send_security_alert(alert)
