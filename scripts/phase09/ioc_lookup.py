from pathlib import Path
import sys
import psycopg2

IOC_FILE = Path("malicious_ips.txt")

with IOC_FILE.open("r") as file:
    malicious_ips = {line.strip() for line in file if line.strip()}


if len(sys.argv) != 2:
    print("Usage: python3 ioc_lookup.py <ip_ADDRESS>")
    sys.exit(1)


test_ip = sys.argv[1]

conn = psycopg2.connect(
    dbname="securityops",
    user="postgres"
)

cursor = conn.cursor()

if test_ip in malicious_ips:
    print(f"[ALERT] Malicious IOC detected: {test_ip}")

    cursor.execute(
        """
        INSERT INTO incident
        (incident_type, source_ip, severity, incident_status, detected_by, description)
        VALUES (%s, %s, %s, %s, %s, %s)
        """,
        (
            "Malicious IOC",
            test_ip,
            "High",
            "Open",
            "IPSum Threat Intelligence",
            "IP address matched the IPSum malicious IP threat intelligence feed"
        )
    )

    conn.commit()
    print("[DB] Incident recorded in SecurityOpsDB")
else:
    print(f"[OK] IOC not found: {test_ip}")
