import random

def gpu_risk_inference(features):
    base = features.get("failed_logins", 0) * 0.25
    ip_risk = 1.0 if features.get("malicious_ip") else 0.3
    anomaly = random.uniform(0.5, 1.5)

    score = (base + ip_risk + anomaly) * 35
    return round(min(score, 100), 2)