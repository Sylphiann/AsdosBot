from commands import glang

def get_response(user_message: str) -> str:
    lowered: str = user_message.lower()

    if lowered == "test":
        return "I am ready!"
    elif lowered == "g":
        return glang.turnToG(user_message)
    else:
        return "The command isn't registered yet"