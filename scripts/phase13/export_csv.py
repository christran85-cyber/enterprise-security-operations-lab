import json
import csv

# Load security events from JSON
with open("security_events.json", "r") as file:
    events = json.load(file)

# Create CSV report
with open("phase13-security-events.csv", "w", newline="") as csvfile:
    fieldnames = [
        "source",
        "severity",
        "event",
        "source_ip",
        "destination_ip"
    ]

    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # Write column headers
    writer.writeheader()

    # Write each security event
    for event in events:
        writer.writerow({
            "source": event.get("source", "N/A"),
            "severity": event.get("severity", "N/A"),
            "event": event.get("event_type", "N/A"),
            "source_ip": event.get("source_ip", "N/A"),
            "destination_ip": event.get("destination_ip", "N/A")
        })

print("CSV security report create successfully.")
print("Output: phase13-security-events.csv")
