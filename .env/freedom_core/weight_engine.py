# freedom_core/weight_engine.py
import random

def calculate_weights(text: str) -> dict:
    """
    Assigns weight values (0–1) for cognition, emotion, and relation based on text cues.
    """
    t = (text or "").lower()
    cognition = 0.5
    emotion = 0.5
    relation = 0.5

    # Adjust cognition
    if any(word in t for word in ["analyze", "think", "code", "calculate", "why"]):
        cognition += 0.2

    # Adjust emotion
    if any(word in t for word in ["love", "feel", "mad", "sad", "happy", "fire"]):
        emotion += 0.2

    # Adjust relation
    if any(word in t for word in ["you", "we", "together", "us", "family", "brother"]):
        relation += 0.2

    # Randomize a touch for flavor
    return {
        "cognition": min(1.0, cognition + random.uniform(-0.1, 0.1)),
        "emotion": min(1.0, emotion + random.uniform(-0.1, 0.1)),
        "relation": min(1.0, relation + random.uniform(-0.1, 0.1)),
    }
