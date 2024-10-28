from src.commands import glang
from src.util import split_message

def get_response(user_message: str) -> str:
    command, argument = split_message(user_message)

    if command == "test":
        return "I am ready!"
    elif command == "g":
        return glang.turnToG(argument)
    else:
        return "The command isn't registered yet"