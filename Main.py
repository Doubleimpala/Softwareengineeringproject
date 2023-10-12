
# Stability-SDK:0.8.4
# discord.py:2.3.2

import os 
import warnings
import io

from fileinput import filename
from PIL import Image

import discord
from discord.ext import commands

from dotenv import load_dotenv
from stability_sdk import client
import stability_sdk.interfaces.gooseai.generation.generation_pb2 as generation

load_dotenv()

stability_api = client.StabilityInference(
    key=os.environ['DIFFUSION_KEY'], verbose=True)

TOKEN = os.getenv('DISCORD_TOKEN')
SERVER = os.getenv('DISCORD_SERVER')

intents = discord.Intents.all()
client = commands.Bot(command_prefix = "?", intents = intents)


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
    ans = stability_api.generate(prompt=prompt)
    
    for resp in ans:
        for artifact in resp.artifacts:
            # Check if prompt violates safety filters
            if artifact.finish_reason == generation.FILTER:
                warnings.warn("Your prompt has triggered the safety filter, please edit prompt and try again.")
            # Generate image prompt
            if artifact.type == generation.ARTIFACT_IMAGE:
                img = Image.open(io.BytesIO(artifact.binary))
                art = io.BytesIO(artifact.binary)
                img.save(art, format='PNG')
                art.seek(0) #Sets the file handle for the file
                file = discord.File(art, filename='art.png')
                await ctx.send(file)
                
client.run(TOKEN)
