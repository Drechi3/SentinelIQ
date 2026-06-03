# alerts.py

def create_alert(event, ueba, correlation):

    return {
        "alert_id": f"ALERT-{event['user_id']}-{event['ip_address']}",
        "severity": "HIGH" if ueba["risk_score"] >= 70 else "MEDIUM",
        "user": event["user_id"],
        "ip": event["ip_address"],
        "event": event["event_type"],
        "correlation": correlation,
        "message": "Suspicious activity detected in SentinelIQ SOC pipeline"
    }