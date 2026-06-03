# 🛡️ SentinelIQ — Autonomous SOC Intelligence Engine

SentinelIQ is a real-time **Security Operations Center (SOC) simulation system** that detects, analyzes, and responds to cyber threats using AI-driven correlation, UEBA (User and Entity Behavior Analytics), and an evolving attack graph.

It simulates how modern SOC platforms like Splunk + SentinelOne + CrowdStrike behave — but in a fully autonomous, lightweight Python architecture.

---

## 🔥 Key Features

### 🧠 AI-Powered Threat Detection
- UEBA-based risk scoring system
- Login anomaly detection
- Failed login pattern recognition
- IP reputation enrichment

### 🕸 Attack Graph Engine
- Real-time node creation (users + IPs)
- Weighted edge relationships (attack paths)
- Attack chain reconstruction
- Graph summary analytics

### ⚡ Correlation Engine
- MITRE ATT&CK mapping (e.g., T1110 Brute Force)
- Behavioral pattern classification
- Attack escalation detection

### 🚨 Autonomous Response System
- Auto-block suspicious IPs
- User quarantine simulation
- Escalation decisions (IGNORE → ESCALATE → AUTO_BLOCK)

### 📊 Live SOC Dashboard
- Real-time streaming UI
- Attack graph visualization
- Node/edge updates every event
- SOC-style monitoring interface

---

## 🧪 Example Event Flow

```json
{
  "user_id": "admin",
  "event_type": "LOGIN_FAILURE",
  "ip_address": "8.8.8.8"
}
