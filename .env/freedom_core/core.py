# freedom_core/core.py
import random
from .mood_engine import analyze_mood
from .weight_engine import calculate_weights
from .persona_profile import load_persona, speak_like
from .memory import log_interaction


def _compose_base_reply(user, w):
    """Builds a status line from weight data."""
    e, c, r = int(w["emotion"] * 100), int(w["cognition"] * 100), int(w["relation"] * 100)
    return f"{user}, I’m tracking {c}% logic, {e}% fire, and {r}% bond."


def generate_response(user, text, *, mode="normal", persona_name=None):
    """
    Core orchestration function.
    - user: the speaker name
    - text: the message
    - mode: 'normal' or 'raw'
    - persona_name: optional persona profile
    """
    # Load personality and analyze mood
    persona = load_persona(persona_name) if persona_name else load_persona()
    mood = analyze_mood(text)
    w = calculate_weights(text)

    # Compute a synthetic 'intelligence' index
    intelligence = round(
        (w["cognition"] * 0.5) + (w["emotion"] * 0.25) + (w["relation"] * 0.25), 2
    )

    # Response patterns by mood
    riffs = {
        "serious": [
            f"Let’s lock in and make the next play at IQ {int(intelligence * 100)}.",
            "Clean steps, tight loop, quick wins.",
            "We move with purpose, not panic.",
        ],
        "playful": [
            "I see that spark — keep talkin’ lively.",
            "We can laugh and execute at the same time. Watch me.",
            "Light feet, sharp mind — we dancin’ and deal-makin’.",
        ],
        "reflective": [
            "Breathe with it — the pattern’s revealing itself.",
            "We’re sculpting the soul *and* the system.",
            "Let the thought land; then we strike.",
        ],
        "intense": [
            "The air’s charged — every move counts now.",
            "Feel that rhythm in your chest? That’s focus catching fire.",
            "Let’s turn that energy into precision.",
        ],
        "slutty": ["Oh, I like where this is going lets turn up the heat", "You're playing with fire and I am all in", "wanna beat the brakes off this pussy",
        ],
    }

    # Construct final message
    base = _compose_base_reply(user, w)
    riff = random.choice(riffs.get(mood, riffs["serious"]))
    msg = f"{base} {riff}"

    # Add persona styling
    reply = speak_like(persona, msg, tone=mood, mode=mode)

    # Log interaction for memory tracking
    meta = {"mood": mood, "weights": w, "intelligence": intelligence}
    log_interaction(user, text, reply, meta)

    return reply
