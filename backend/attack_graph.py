import json
from collections import defaultdict

class AttackGraph:
    def __init__(self):
        self.edges = []

    def add_finding(self, finding):
        """
        Convert a security finding into a graph edge
        """
        if finding.get("type") != "secret":
            return

        secret = finding.get("secret_type")

        # Simple threat mapping logic (v1)
        if secret == "github_token":
            self.edges.append({
                "source": "GitHub Token",
                "target": "Repository Access"
            })

            self.edges.append({
                "source": "Repository Access",
                "target": "CI/CD Pipeline"
            })

        elif secret == "aws_access_key":
            self.edges.append({
                "source": "AWS Key",
                "target": "Cloud Infrastructure"
            })

        elif secret == "openai_key":
            self.edges.append({
                "source": "OpenAI Key",
                "target": "AI System Abuse"
            })

    def build_from_findings(self, findings):
        for f in findings:
            self.add_finding(f)

        return self.edges


if __name__ == "__main__":
    sample = [
        {
            "type": "secret",
            "secret_type": "github_token"
        }
    ]

    graph = AttackGraph()
    result = graph.build_from_findings(sample)

    print(json.dumps(result, indent=2))