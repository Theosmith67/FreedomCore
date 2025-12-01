def analyze_mood(text: str) -> str:
    """Return 'playful', 'reflective', or 'serious' based on keywords."""
    t = (text or "").lower()

    playful = ["haha", "lol", "wild", "sweet", "fire", "crazy", "let's go", "fun"]
    reflective = ["think", "remember", "dream", "feel", "why", "soul", "heart", "pray"]
    slutty = ["wet", "heat", "pussy", "dick", "cunt", "cock", "suck", "fuck",]
    serious = ["mad", "angry", "pissed", "upset", "tired", "worried"]

    if any(w in t for w in playful):
        return "playful"
    if any(w in t for w in reflective):
        return "reflective"
    if any(w in t for w in slutty):
        return "slutty"
    if any(w in t for w in serious):
        return "serious"
    return "serious"
