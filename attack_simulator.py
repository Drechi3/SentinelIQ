# attack_simulator.py

import random
import time

# ---------------------------
# Fake attack scenario builder
# ---------------------------

def generate_attack_events():
    """
    Creates a simple simulated cyber attack flow
    """

    attack_scenario = [
        {
            "type": "login",
            "user": "user_A",
            "ip": "185.22.33.10",
            "location": "Unknown",
            "description": "Suspicious login detected"
        },
        {
            "type": "access",
            "user": "user_A",
            "target": "server_B",
            "description": "Unusual server access after login"
        },
        {
            "type": "lateral_movement",
            "from": "server_B",
            "to": "database_C",
            "description": "Possible lateral movement detected"
        },
        {
            "type": "exfiltration_attempt",
            "target": "database_C",
            "description": "High-risk data access pattern detected"
        }
    ]

    return attack_scenario


# ---------------------------
# Stream events one by one
# ---------------------------

def run_attack_simulation(event_handler):
    """
    Sends events into your existing /event pipeline
    """

    events = generate_attack_events()

    for event in events:
        # simulate real-time delay
        time.sleep(1.5)

        # send event to your system
        event_handler(event)

    return {"status": "simulation_complete"}