from datetime import datetime

# -------------------------
# LEVEL 9 AUTONOMOUS RESPONSE ENGINE
# -------------------------

BLOCKED_IPS = set()
QUARANTINED_USERS = set()
INCIDENT_MEMORY = []


def execute_response(user, ip, correlation, risk):
    actions = []

    # -------------------------
    # CONFIRMED ATTACK → HARD ACTIONS
    # -------------------------
    if "CONFIRMED_ATTACK" in correlation:
        BLOCKED_IPS.add(ip)
        QUARANTINED_USERS.add(user)

        actions.append({
            "action": "BLOCK_IP",
            "target": ip,
            "reason": "Confirmed attack detected"
        })

        actions.append({
            "action": "QUARANTINE_USER",
            "target": user,
            "reason": "High confidence compromise"
        })

    # -------------------------
    # SUSPICIOUS ACTIVITY → SOFT CONTROL
    # -------------------------
    elif "SUSPICIOUS" in correlation or risk >= 30:
        actions.append({
            "action": "RATE_LIMIT",
            "target": ip,
            "reason": "Suspicious behavior detected"
        })

    # -------------------------
    # NORMAL ACTIVITY → MONITOR ONLY
    # -------------------------
    else:
        actions.append({
            "action": "MONITOR",
            "target": user,
            "reason": "Normal baseline behavior"
        })

    # -------------------------
    # INCIDENT MEMORY (LEVEL 9 CORE)
    # -------------------------
    INCIDENT_MEMORY.append({
        "user": user,
        "ip": ip,
        "correlation": correlation,
        "risk": risk,
        "actions": actions,
        "time": datetime.utcnow().isoformat()
    })

    return {
        "actions": actions,
        "blocked_ips": list(BLOCKED_IPS),
        "quarantined_users": list(QUARANTINED_USERS)
    }