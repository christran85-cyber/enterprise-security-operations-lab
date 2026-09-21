import psycopg2
from datetime import datetime

conn = psycopg2.connect(
    dbname="securityops",
    user="postgres"
)

cursor = conn.cursor()

cursor.execute("""
    SELECT incident_id, incident_type, severity, incident_status, detected_by
    FROM incident
    WHERE incident_status = 'Investigated'
    ORDER BY incident_id;
""")

incidents = cursor.fetchall()

for incident in incidents:
    incident_id = incident[0]
    incident_type = incident[1]
    severity = incident[2]
    status = incident[3]
    detected_by = incident[4]

    print(f"[+] Processing incident {incident_id}: {incident_type}")

    if severity == "High":
        priority = "IMMEDIATE REVIEW"
        new_status = "Escalated"
    elif severity == "Medium":
        priority = "STANDARD REVIEW"
        new_status = "Reviewed"
    else:
        priority = "LOW PRIORITY"
        new_status = "Reviewed"

    print(f"    Severity: {severity}")
    print(f"    Action: {priority}")
    print(f"    Detected By: {detected_by}")

    cursor.execute(
        """
        UPDATE incident
        SET incident_status = %s
        WHERE incident_id = %s
        """,
        (new_status, incident_id)
    )

    cursor.execute(
        """
        INSERT INTO automation_log
            (incident_id, previous_status, new_status, action_taken)
        VALUES (%s, %s, %s, %s)
        """,
        (incident_id, status, new_status, priority)
    )

conn.commit()

cursor.close()
conn.close()
