
# Stability-SDK:0.8.4
# discord.py:2.3.2

import os 
import warnings
import io
import GenerateImg as img

from fileinput import filename
from PIL import Image

import discord
from discord.ext import commands

from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
SERVER = os.getenv('DISCORD_SERVER')

intents = discord.Intents.all()
client = commands.Bot(command_prefix="?", intents=intents)


@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == SERVER:
            break
        
    print(f'{client.user} has connected to:\n' + 
            f'{guild.name}(id: {guild.id})')
    
    
@client.command()
async def makeimg(ctx, prompt):
    msg = await ctx.send(f"“{prompt}”\n> Generating...")
    

                
client.run(TOKEN)
