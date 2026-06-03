USER_STATE = {}

def analyze_user_behavior(event):
    user = event["user_id"]

    state = USER_STATE.get(user, {
        "failed_logins": 0,
        "suspicious": 0,
        "last_ip": None
    })

    if event["event_type"] == "LOGIN_FAILURE":
        state["failed_logins"] += 1

    if state["failed_logins"] >= 3:
        state["suspicious"] += 2

    state["last_ip"] = event["ip_address"]

    risk = state["failed_logins"] * 20 + state["suspicious"] * 25

    USER_STATE[user] = state

    return {
        "user": user,
        "risk_score": risk,
        "failed_logins": state["failed_logins"],
        "last_seen": event
    }