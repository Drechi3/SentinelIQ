from datetime import datetime
from collections import defaultdict

class Node:
    def __init__(self, node_id):
        self.id = node_id
        self.label = node_id
        self.first_seen = datetime.utcnow().isoformat()
        self.event_count = 0
        self.risk_accumulator = 0


class Edge:
    def __init__(self, s, t):
        self.id = f"{s}->{t}"
        self.source = s
        self.target = t
        self.weight = 0
        self.events = []
        self.last_updated = None


class AttackGraph:
    def __init__(self):
        self.nodes = {}
        self.edges = {}
        self.chains = defaultdict(list)

    def add_node(self, node_id):
        if node_id not in self.nodes:
            self.nodes[node_id] = Node(node_id)
        self.nodes[node_id].event_count += 1

    def add_edge(self, s, t, risk, event):
        key = f"{s}->{t}"

        if key not in self.edges:
            self.edges[key] = Edge(s, t)

        e = self.edges[key]
        e.weight += risk
        e.last_updated = datetime.utcnow().isoformat()
        e.events.append({
            "type": event,
            "risk": risk,
            "time": datetime.utcnow().isoformat()
        })

    def add_attack_event(self, u, ip, event, risk):
        self.chains[u].append({
            "event": event,
            "ip": ip,
            "risk": risk,
            "time": datetime.utcnow().isoformat()
        })

    def export(self):
        return {
            "nodes": [n.__dict__ for n in self.nodes.values()],
            "edges": [e.__dict__ for e in self.edges.values()],
            "attack_chains": dict(self.chains),
            "summary": {
                "total_nodes": len(self.nodes),
                "total_edges": len(self.edges)
            }
        }