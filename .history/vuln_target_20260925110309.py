def parse_user_record(data: str) -> dict:
    """Parses a comma-separated record: name, age, email"""
    parts = data.split(",")

    if len(parts) != 3:
        raise ValueError("Record must have exactly 3 comma separate fields: name,age,email")

    name, age_str, email = parts
    if not age_str.strip().lstrip("-").isdigit():
        raise ValueError(f"Age must be a valid integer, got: {age_str!r}")

    return {"name": name, "age": age_str, "email": email}