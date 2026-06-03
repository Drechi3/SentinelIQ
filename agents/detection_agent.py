class DetectionAgent:
    def analyze(self, event, ueba, threat):
        signals = []

        if event["event_type"] == "LOGIN_FAILURE":
            signals.append("BRUTE_FORCE_SIGNAL")

        if threat.get("malicious"):
            signals.append("KNOWN_BAD_IP")

        if ueba.get("risk_score", 0) > 50:
            signals.append("HIGH_RISK_USER")

        return {
            "signals": signals,
            "confidence": len(signals) * 35
        }