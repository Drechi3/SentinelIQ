from transformers import pipeline

print("Loading AI model... (first run may download files)")

classifier = pipeline(
    "zero-shot-classification",
    model="valhalla/distilbart-mnli-12-1"
)

def analyze_security_event(event_text):

    labels = [
        "Brute Force Attack",
        "Credential Stuffing",
        "Account Takeover",
        "Suspicious Login Activity",
        "Normal Activity"
    ]

    result = classifier(
        event_text,
        candidate_labels=labels
    )

    return {
        "classification": result["labels"][0],
        "confidence": round(result["scores"][0], 4)
    }


if __name__ == "__main__":

    sample_event = """
    User admin generated 15 LOGIN_FAILURE events
    from IP 8.8.8.8 within 60 seconds.
    """

    analysis = analyze_security_event(sample_event)

    print("\n=== SentinelIQ AI Analysis ===")
    print(f"Classification: {analysis['classification']}")
    print(f"Confidence: {analysis['confidence']}")