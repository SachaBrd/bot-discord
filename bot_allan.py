import discord
import os
import random

intents = discord.Intents.all()

client = discord.Client(intents=intents)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    phrase = [
        "OUIN OUIN",
        "J'ai envie d'un bon steak froid du RU miam",
        "seuuuukeuuu",
        "Je blaire mon mucus quotidiennement",
        "World of warcraft shadowlands",
        "WOOOOUUUUH WOUH WOUH FOUCO FOUCO FOUCO",
        "ALLAN"
    ]

    response = random.choice(phrase)

    if message.content.lower() == 'allan':
        await message.channel.send(response)

client.run('MTA1MjM2MTEyNjQxNzAwNjYyMg.Gbg0iF.fZHg4Df4Wh7xANEUCY6DTALEIG8yNl28LRkS3k')

