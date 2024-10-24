def get_response(user_message: str) -> str:
    lowered: str = user_message.lower()

    if lowered == "test":
        return "I am ready!"
    else:
        return "The command isn't registered yet"