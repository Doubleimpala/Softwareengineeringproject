import os 
import discord

from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
SERVER = os.getenv('DISCORD_SERVER')

client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == SERVER:
            break
        
    print(f'{client.user} has connected to:\n'
            f'{guild.name}(id: {guild.id})')
    
client.run(TOKEN)

