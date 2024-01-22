from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Message
from responses import get_response, get_random_quote, get_random_challenge, add_new_challenge, list_all_challenges
from discord.ext import commands

load_dotenv()
TOKEN: Final[str] = os.getenv("DISCORD_TOKEN")
API_KEY: Final[str] = os.getenv("API_KEY")
PATH_TO_JSON: Final[str] = os.getenv("PATH_TO_JSON")

intents: Intents = Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix = '!', intents=intents)

@client.event
async def on_ready() -> None:
    print(f'{client.user} has connected to Discord!')  

@client.command(name='quote')
async def quote(ctx):
    await ctx.send(get_random_quote(API_KEY))

@client.command(name='challenge')
async def challenge(ctx):
    await ctx.send(get_random_challenge(PATH_TO_JSON))

@client.command(name='add')
async def add(ctx, url: str):
    await ctx.send(add_new_challenge(PATH_TO_JSON, url))

@client.command(name='list')
async def list(ctx):
    await ctx.send(list_all_challenges(PATH_TO_JSON))

@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return
    
    if message.content.startswith('!'):
        await client.process_commands(message)
        return

    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)
    print(f'{username} sent "{user_message}" in {channel}')
    await send_message(message, user_message, username)

async def send_message(message: Message, user_message: str, username: str) -> None:
    #  If the message starts with a question mark, it is a private message
    if is_private := user_message[0] == '?':
        user_message = user_message[1:]
    
    try:
        response: str = get_response(user_message, username)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

def main() -> None:
    client.run(token=TOKEN)

if __name__ == "__main__":
    main()