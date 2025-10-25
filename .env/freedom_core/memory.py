import json
from datetime import datetime
import os

LOG_FILE = os.path.join(os.path.dirname(__file__), "memory_log.json")


def _load_memory():
    """Load existing memory log or start fresh."""
    if not os.path.exists(LOG_FILE):
        return []
    try:
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []


def _save_memory(data):
    """Save updated memory log to file."""
    with open(LOG_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def log_interaction(user, text, reply, meta=None):
    """
    Store a single interaction (like a journal entry).
    Each entry includes timestamp, user input, AI reply, and metadata.
    """
    log = _load_memory()
    entry = {
        "timestamp": datetime.now().isoformat(),
        "user": user,
        "input": text,
        "reply": reply,
        "meta": meta or {},
    }
    log.append(entry)
    _save_memory(log)
    print(f"[memory] Logged interaction for {user} at {entry['timestamp']}")
    return entry


def recall_recent(n=5):
    """Return the last n memory entries."""
    log = _load_memory()
    return log[-n:]


def clear_memory(confirm=False):
    """Wipe the memory log clean (use carefully)."""
    if confirm:
        _save_memory([])
        print("[memory] All memories cleared.")
    else:
        print("[memory] Clear not confirmed — nothing deleted.")
