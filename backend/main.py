from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime
from collections import defaultdict

app = FastAPI(title="SentinelIQ SOC v4 ELITE")

# CORS FIX (VERY IMPORTANT)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ----------------------------
# GRAPH STORE
# ----------------------------
graph = {
    "nodes": {},
    "edges": {},
    "attack_chains": defaultdict(list)
}

# ----------------------------
# REQUEST MODEL
# ----------------------------
class ScanRequest(BaseModel):
    path: str


# ----------------------------
# SIMPLE SECRET DETECTOR
# ----------------------------
def detect_secrets(file_content: str):
    findings = []

    if "PRIVATE KEY" in file_content:
        findings.append(("private_key", "critical"))

    if "sk-" in file_content:
        findings.append(("api_key", "high"))

    if "ghp_" in file_content:
        findings.append(("github_token", "high"))

    return findings


# ----------------------------
# SCAN ENDPOINT
# ----------------------------
@app.post("/scan-code")
def scan_code(req: ScanRequest):

    import os

    findings = []
    attack_graph = []

    for root, _, files in os.walk(req.path):
        for file in files:
            if file.endswith((".py", ".js", ".env", ".txt")):
                full_path = os.path.join(root, file)

                try:
                    with open(full_path, "r", errors="ignore") as f:
                        content = f.read()

                    secrets = detect_secrets(content)

                    for secret_type, severity in secrets:

                        findings.append({
                            "type": "secret",
                            "secret_type": secret_type,
                            "file": full_path,
                            "line": 1,
                            "content": content[:80],
                            "severity": severity
                        })

                        attack_graph.append({
                            "source": secret_type,
                            "target": full_path,
                            "risk": 95 if severity == "critical" else 70
                        })

                except:
                    continue

    return {
        "findings": findings,
        "attack_graph": attack_graph,
        "summary": {
            "total_findings": len(findings),
            "total_edges": len(attack_graph)
        }
    }


# ----------------------------
# HEALTH CHECK
# ----------------------------
@app.get("/")
def home():
    return {
        "status": "running",
        "system": "SentinelIQ SOC v4 ELITE",
        "message": "Security Intelligence API active"
    }


# ----------------------------
# GRAPH ENDPOINT (OPTIONAL)
# ----------------------------
@app.get("/graph")
def get_graph():
    return {
        "nodes": list(graph["nodes"].values()),
        "edges": list(graph["edges"].values())
    }