
# Stability-SDK:0.8.4
# discord.py:2.3.2

import io
import os

import discord
from dotenv import load_dotenv

import GenerateImg as img
from discord.ext import commands


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
    image = img.test(prompt)
    
    arr = io.BytesIO()
    image.save(arr, format='PNG')
    arr.seek(0)
    file = discord.File(arr)
    await ctx.send(file = file)
    

                
client.run(TOKEN)
