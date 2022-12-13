import discord
import os
import random

intents = discord.Intents.all()

client = discord.Client(intents=intents)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    intro = "Salut c'est Hugo et comme chaque jour on est parti pour un nouveau résumé de l'actualité en moins de 10 minutes. \n"

    ville = [
        "Roubaix",
        "Limoges",
        "Nantes",
        "Orleans",
        "Angers",
        "Paris",
        "Marseille",
        "Toulouse",
        "Tourcoing",
        "Saint-Nazaire",
        "Clermont-ferrand",
        "San Francisco",
        "New York",
        "Londres",
        "Tokyo",
        "Sydney",
        "Los Angeles",
        "Rio de janeiro",
    ]

    personnalite = [
        "Emmanuel Macron",
        "Valerie Pecresse",
        "Jean Castex",
        "Antoine Daniel",
        "Le maire de " + random.choice(ville),
        "Zinedine Zidane",
    ]

    actu = [
        "j'ai chier dans mon benne.",
        "Ayant perdu sa seule raison d'exister, la ville de " + random.choice(ville) + " sera rasé.",
    ]

    phrase = intro + "premiére actualité : \n" + random.choice(actu)

    if message.content == '!actu':
        response = phrase
        await message.channel.send(response)

client.run('MTA1MTI2NDk2ODk4MjUzMjEzNg.GLTLsy.4pWfu5cMIgrGc1_-os2DOFBtGo4YUlNG0T4Ee8')

