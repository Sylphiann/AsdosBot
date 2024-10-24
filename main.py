import os

from typing import Final
from dotenv import load_dotenv
from discord import Intents, Client, Message
from src.responses import get_response
from src.util import command_type

# Load token
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')
RESP_CHANNEL_ID: Final[str] = os.getenv('CHANNEL_ID')

# Bot setup
intents: Intents = Intents.default()
intents.message_content = True

client: Client = Client(intents=intents)

# Message functionality
async def send_message(message: Message, user_message: str) -> None:
    
    # If no user message
    if not user_message:
        print('Message was empty because intents was not configured properly')
        return

    is_anon, is_command, is_forced, user_message = command_type(user_message)

    # Get response
    try:
        response: str = get_response(user_message)
        if is_forced:
            await message.delete()
            await message.channel.send(response)
            
        elif is_command:
            resp_channel = client.get_channel(int(RESP_CHANNEL_ID))
            await resp_channel.send(response)

        elif is_anon:
            await message.delete()
            await message.channel.send(user_message)
            
    except Exception as e:
        print(f"Error caught!\n{e}")

# Help bot startup
@client.event
async def on_ready() -> None:
    print(f"{client.user} is now ready!")

# Handling incoming messages
@client.event
async def on_message(message: Message) -> None:

    # If the bot is the message sender: IGNORE!
    if message.author == client.user:
        return
    
    # If it's safe, retrieve the context of the message
    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    # Activity logging, every information about anything that happened is printed here
    print(f'[{channel}] {username}: {user_message}')

    # Call the send_message function
    await send_message(message=message, user_message=user_message)

# Run the main code
def main() -> None:
    client.run(token=TOKEN)

if __name__ == '__main__':
    main()