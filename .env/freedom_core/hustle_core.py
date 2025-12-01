# freedom_core/hustle_core.py
import random

def hustle_response(user, text):
    """
    Generates a motivational or strategic response.
    Keeps the vibe grounded and action-driven.
    """
    vibes = [
        f"{user}, we stay grindin’. Small moves stack up big.",
        f"{user}, hustle’s not noise — it’s precision in motion.",
        f"{user}, lock in. You’ve got more gears than they’ve ever seen.",
        f"Keep it rollin’, {user}. Every sunrise’s another shot.",
        f"{user}, execution over excuses. Always.",
        f"Steady hands, focused heart — that’s how legends move, {user}.",
    ]

    reply = random.choice(vibes)
    print(f"[hustle_core] Generated response: {reply}")
    return reply


# --- Self-Test ---
if __name__ == "__main__":
    print("⚙️ Hustle Core Test Running...")
    test_user = "Chief"
    test_text = "Let’s keep building the Freedom Core."
    result = hustle_response(test_user, test_text)
    print("✅ Test complete:", result)
