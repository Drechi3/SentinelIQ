def correlate_event(event, ueba, intel):

    risk = ueba["risk_score"]
    malicious = intel["malicious"]

    if malicious and risk >= 60:
        return "CONFIRMED_ATTACK (T1110 Brute Force)"

    if malicious and risk >= 30:
        return "SUSPICIOUS_ACTIVITY (T1110 Brute Force)"

    return "NORMAL (T1110 Brute Force)"