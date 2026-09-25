def parse_user_record(data: str) -> dict:
    """Parses a comma-separated record: name, age, email"""
    parts = data.split(",")
    name = parts[0]
    age = int(parts[1])
    email = parts[2]
    return {"name": name, "age": age, "email": email}