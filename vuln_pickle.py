import json

def load_user_preferences(data: bytes):
    """Loads a user's saved preferences from serialized data"""
    preferences = json.loads(data)
    return preferences

if __name__ == "__main__":
    # Simulate a normal, legitimate use case first
    normal_prefs = {"theme": "dark", "font_size": 14}
    serialized = json.dumps(normal_prefs)

    loaded = load_user_preferences(serialized)
    print(f"Loaded preferences: {loaded}")