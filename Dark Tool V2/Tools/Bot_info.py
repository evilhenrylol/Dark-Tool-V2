import discord
from discord.ext import commands
import sys

TOKEN = input("Enter your bot token: ").strip()

intents = discord.Intents.default()
intents.guilds = True  
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    print("Servers the bot is in:")
    for guild in bot.guilds:
        print(f"- {guild.name} (ID: {guild.id})")
        invite_link = await get_invite_link(guild)
        if invite_link:
            print(f"Invite Link: {invite_link}")
        else:
            print("Could not generate an invite.")

async def get_invite_link(guild):
    """Tries to create an invite link for the first available channel."""
    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).create_instant_invite:
            invite = await channel.create_invite(max_age=0, max_uses=0)  
            return invite.url
    return None  

bot.run(TOKEN)
