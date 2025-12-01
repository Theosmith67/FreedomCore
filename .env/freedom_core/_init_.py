# freedom_core/__init__.py
# Initializes the Freedom Core package and runs quick diagnostics.

import os, sys

# --- Ensure project root is in path ---
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# --- Core Imports ---
from freedom_core.core import generate_response
from freedom_core.hustle_core import hustle_response
from freedom_core.mood_engine import analyze_mood
from freedom_core.weight_engine import calculate_weights
from freedom_core.memory import log_interaction
from freedom_core.persona_profile import load_persona, speak_like


# --- Self-Test (Run directly to verify connections) ---
if __name__ == "__main__":
    print("✅ Freedom Core initialized successfully.\n")

    user = "Chief"
    text = "Let's build and grind today, make something powerful."

    print("🧠 Mood Analysis:")
    print("   ", analyze_mood(text))

    print("\n⚖️ Weight Engine:")
    print("   ", calculate_weights(text))

    print("\n💬 Generated Response:")
    reply = generate_response(user, text)
    print("   ", reply)
    print("\n💼 Hustle Core:")
    print("   ", hustle_response(user, text))

    print("\n🧾 Logging Interaction:")
    log_interaction(user, text, reply)
    print("   Interaction logged successfully.")
