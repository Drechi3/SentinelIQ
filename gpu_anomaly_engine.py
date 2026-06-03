import random
import math

# -------------------------
# LEVEL 10 GPU-BASED ANOMALY SCORER (SIMULATED)
# -------------------------

def compute_embedding(event):
    """
    Simulated GPU embedding generator
    (replace with real model later: sentence-transformers / LLM / ONNX / CUDA)
    """

    base = len(event.user_id) * 0.1
    ip_factor = sum(int(x) for x in event.ip_address.split(".") if x.isdigit()) % 50
    event_factor = len(event.event_type) * 2

    return [base, ip_factor, event_factor]


def anomaly_score(embedding):
    """
    Simulated GPU cosine-like anomaly score
    """

    score = math.sqrt(sum(x ** 2 for x in embedding))

    # normalize into 0–100 risk scale
    return min(100, round(score * random.uniform(0.8, 1.3), 2))