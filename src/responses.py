from src.utils.calculate import calculate

def get_response(user_message: str) -> str:
    lowered: str = user_message.lower().split()
    command: str = lowered[0]
    param1: str = lowered[1] if len(lowered) >= 2 else None
    param2: str = lowered[2] if len(lowered) >= 3 else None
    

    if command == "test":
        return "I am ready!"
    elif command == "calculate":
        return calculate(param1)
    else:
        return "The command isn't registered yet"