KNOWN_BAD_IPS = ["10.0.0.99", "185.220.101.1"]

def check_threat_intel(ip):
    return {
        "ip": ip,
        "malicious": ip in KNOWN_BAD_IPS
    }