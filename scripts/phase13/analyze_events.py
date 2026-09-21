import json
from collections import Counter

# Load security events
with open("security_events.json", "r") as file:
    events = json.load(file)

print("=== PHASE 13 SECURITY EVENT ANALYSIS ===")
print(f"Total Events: {len(events)}")
print()

# Count events by source
sources = Counter(event["source"] for event in events)

print("Events by Source:")
for source, count in sources.items():
    print(f"    {source}: {count}")

print()

# Count events by severity
severities = Counter(event["severity"] for event in events)

print("Events by Severity:")
for severity, count in severities.items():
    print(f"    {severity}: {count}")

print()

# Display each security event
print("Security Events:")

for event in events:
    print(
        event.get("timestamp", "N/A"),
        "|", event.get("source", "N/A"),
        "|", event.get("severity", "N/A"),
        "|", event.get("event_type", "N/A"),
        "|", event.get("source_ip", "N/A"),
        "->", event.get("destination_ip", "N/A")
    )

# Generate alerts for medium-severity events
print()
print("Security Alerts:")

for event in events:
    if event.get("severity") == "Medium":
        print(
            "ALERT:",
            event.get("event_type", "Unknown Event"),
            "| Source:", event.get("source", "Unknown"),
            "|", event.get("source_ip", "N/A"),
            "->", event.get("destination_ip", "N/A")
        )
