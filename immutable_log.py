import json
from datetime import datetime

FILE = "security_log.json"

def store_event(event):
    record = {
        "time": datetime.utcnow().isoformat(),
        "data": event
    }

    try:
        with open(FILE, "r") as f:
            logs = json.load(f)
    except:
        logs = []

    logs.append(record)

    with open(FILE, "w") as f:
        json.dump(logs, f, indent=2)

    return record