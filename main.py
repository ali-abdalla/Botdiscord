import os
import discord
from dotenv import load_dotenv

load_dotenv(dotenv_path="config")
client = discord.Client()

@client.event
async def on_ready():
    print("Le bot est connecté.")
    
@client.event
async def on_message(message):
    word_list = ['merde', 'putain', 'pute']
    messageContent = message.content
    if len(messageContent) > 0:
        for word in word_list:
            if word in messageContent:
                error = await message.channel.send('Ne dite pas ça!')
                await message.delete(delay=2)
                authoreroor = await message.channel.send(message.author)
                await error.delete(delay=5)
                await authoreroor.delete(delay=5)    
                return
client.run(os.getenv('TOKEN'))