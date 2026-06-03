from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime
from collections import defaultdict

app = FastAPI()

# Allow frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ----------------------------
# MEMORY STORE (GRAPH)
# ----------------------------
graph = {
    "nodes": {},
    "edges": {},
    "attack_chains": defaultdict(list)
}

# ----------------------------
# EVENT MODEL
# ----------------------------
class Event(BaseModel):
    user_id: str
    event_type: str
    ip_address: str


# ----------------------------
# RISK ENGINE
# ----------------------------
def calculate_risk(event_type, failed_logins=1, malicious_ip=False):
    base = failed_logins * 15
    ip_risk = 50 if malicious_ip else 10

    if event_type == "LOGIN_FAILURE":
        return base + ip_risk
    return 10


# ----------------------------
# CORRELATION ENGINE
# ----------------------------
def correlate(risk_score):
    if risk_score >= 60:
        return "CONFIRMED_ATTACK (T1110 - Brute Force)"
    elif risk_score >= 30:
        return "SUSPICIOUS_IP_ACTIVITY"
    return "NORMAL"


# ----------------------------
# EVENT ENDPOINT
# ----------------------------
@app.post("/event")
def ingest_event(event: Event):

    user = event.user_id
    ip = event.ip_address

    risk = calculate_risk(event.event_type, failed_logins=1, malicious_ip=True)
    correlation = correlate(risk)

    # ---------------- NODE UPDATE ----------------
    for entity in [user, ip]:
        if entity not in graph["nodes"]:
            graph["nodes"][entity] = {
                "id": entity,
                "label": entity,
                "first_seen": datetime.utcnow().isoformat(),
                "event_count": 0,
                "risk_accumulator": 0
            }

        graph["nodes"][entity]["event_count"] += 1
        graph["nodes"][entity]["risk_accumulator"] += risk

    # ---------------- EDGE UPDATE ----------------
    edge_id = f"{user}->{ip}"

    if edge_id not in graph["edges"]:
        graph["edges"][edge_id] = {
            "id": edge_id,
            "source": user,
            "target": ip,
            "weight": 0,
            "events": [],
            "last_updated": datetime.utcnow().isoformat()
        }

    graph["edges"][edge_id]["weight"] += risk
    graph["edges"][edge_id]["events"].append({
        "type": event.event_type,
        "risk": risk,
        "time": datetime.utcnow().isoformat()
    })

    # ---------------- ATTACK CHAIN ----------------
    graph["attack_chains"][user].append({
        "event": event.event_type,
        "ip": ip,
        "risk": risk,
        "time": datetime.utcnow().isoformat()
    })

    return {
        "event": event,
        "risk": risk,
        "correlation": correlation,
        "graph": graph
    }


# ----------------------------
# GRAPH ENDPOINT (FRONTEND USES THIS)
# ----------------------------
@app.get("/graph")
def get_graph():

    return {
        "nodes": list(graph["nodes"].values()),
        "edges": list(graph["edges"].values()),
        "attack_chains": dict(graph["attack_chains"]),
        "summary": {
            "total_nodes": len(graph["nodes"]),
            "total_edges": len(graph["edges"])
        }
    }