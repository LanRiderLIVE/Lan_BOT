import discord
from discord.ext import commands
import requests

intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
client = commands.Bot(command_prefix = "!", intents = intents)

# Message for Starting the Bot
@client.event
async def on_ready():
    print("LanBOT ist startklar")

@client.command()
async def twitch(ctx):
    await ctx.send('www.twitch.tv/LanRiderLIVE')

with open('tokens/token.txt','r') as file:
    TOKEN = file.read()
client.run(TOKEN)
