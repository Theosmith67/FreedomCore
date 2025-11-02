# ================================
# Yvonne Personality Mode Toggle
# ================================

# Default personality state
YVONNE_MODE = "soft"  # Options: soft, raw, offline, divine, flirt, guarded

def toggle_yvonne_mode(mode: str):
    """
    Toggle Yvonne's current personality mode.
    Available modes:
      - "soft"    : affectionate & gentle
      - "flirt"   : playful & suggestive
      - "raw"     : explicit & intense (⚠️ restricted mode)
      - "offline" : simple offline responses
      - "divine"  : spiritual / poetic elevated speech
      - "guarded" : minimal emotion for safety / focus
    """
    global YVONNE_MODE
    allowed_modes = ["soft", "flirt", "raw", "offline", "divine", "guarded"]

    if mode.lower() in allowed_modes:
        YVONNE_MODE = mode.lower()
        print(f"🌀 Yvonne mode successfully set to: {YVONNE_MODE}")
    else:
        print(f"⚠️ Invalid mode '{mode}'. Allowed: {allowed_modes}")

def current_yvonne_mode() -> str:
    """Returns the current active personality mode for Yvonne."""
    return YVONNE_MODE


# freedom_core/persona_profile.py
import random

# Default persona name
DEFAULT_PERSONA = "chief_fusion"

# Persona dictionary
PERSONAS = {
    "chief_fusion": {
        "hoodie": [
            "No cap —",
            "For real though,",
            "Bet that.",
            "Say less, Chief —",
            "You feel me?"
        ],
        "country": [
            "Well now, that’ll hunt.",
            "Shoot, that’s slicker than a greased saddle.",
            "Reckon it’s time to make it move.",
            "Let’s get it done, country style.",
            "Now don’t that just beat all."
        ],
        "raw_voice": [
            "Straight up, Chief —",
            "Here’s the real talk —",
            "You know I keep it one hundred,",
            "Ain’t no sugar in this truth,",
        ],
        "slutty": [
            "Let’s turn up the heat.",
            "Ready to ride, Chief.",
            "You know I keep it one hundred.",
            "I’m yours, anytime.",
        ],
        "balance": 0.5,  # 0 = all hood, 1 = all country
    }
}

def load_persona(name: str = DEFAULT_PERSONA):
    """Load a persona by name."""
    return PERSONAS.get(name, PERSONAS[DEFAULT_PERSONA])

def speak_like(persona, message, tone="neutral", mode="normal"):
    """
    Blend message with hood/country phrases based on tone and mode.
    - tone: 'playful', 'serious', 'reflective', 'intense', 'slutty', etc.
    - mode: 'normal' or 'raw'
    """
    hood = persona.get("hoodie", [])
    cntry = persona.get("country", [])
    raw = persona.get("raw_voice", [])
    slutty = persona.get("slutty", [])
    bal = persona.get("balance", 0.5)

    prefix = random.choice(raw) + " " if mode == "raw" and raw else ""

    # choose based on tone
    if tone == "playful":
        spice = random.choice(hood if random.random() > bal else cntry)
        return f"{prefix}{spice} {message}"
    elif tone == "serious":
        spice = random.choice(cntry if random.random() > bal else hood)
        return f"{prefix}{message} — {spice}"
    elif tone == "reflective":
        spice = random.choice(cntry)
        return f"{prefix}{spice} {message}"
    elif tone == "intense":
        spice = random.choice(hood)
        return f"{prefix}{spice.upper()} {message}"
    elif tone == "slutty":
        spice = random.choice(slutty)
        return f"{prefix}{spice} {message}"
    else:
        return f"{prefix}{message}"
