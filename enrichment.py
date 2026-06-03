def enrich_event(event):
    event["geo"] = "UNKNOWN"
    event["device"] = "UNKNOWN"
    return event