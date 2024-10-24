
def command_type(user_message: str):

    if user_message[0] == '?':
        user_message = user_message[1:]
        return (True, False, False, user_message)
        
    if user_message[0] == '!':
        user_message = user_message[1:]

        if user_message[0] == '!':
            user_message = user_message[1:]
            return (False, True, True, user_message)
        return (False, True, False, user_message)

    return (False, False, False, user_message)