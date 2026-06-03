from gpu_anomaly_engine import compute_embedding, anomaly_score
from decentralized_memory import store_incident

# -------------------------
# LEVEL 10 SOC AGENT ORCHESTRATOR
# -------------------------

def run_soc_agents(event, ueba, threat, correlation):

    embedding = compute_embedding(event)
    gpu_risk = anomaly_score(embedding)

    decision = "MONITOR"

    if gpu_risk >= 70 or "CONFIRMED" in correlation:
        decision = "AUTO_BLOCK"

    elif gpu_risk >= 40:
        decision = "STEP_UP_AUTH"

    # -------------------------
    # STORE IN DECENTRALIZED MEMORY
    # -------------------------
    store_incident({
        "user": event.user_id,
        "ip": event.ip_address,
        "gpu_risk": gpu_risk,
        "ueba_risk": ueba["risk_score"],
        "correlation": correlation,
        "decision": decision
    })

    return {
        "gpu_embedding": embedding,
        "gpu_risk": gpu_risk,
        "decision": decision
    }