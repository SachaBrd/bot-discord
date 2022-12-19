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
        "Ayant perdu sa seule raison d'exister, la ville de " + random.choice(ville) + " sera rasé.",
        ""
    ]

    phrase = intro + "premiére actualité : \n" + random.choice(actu)

    if message.content == '!actu':
        response = phrase
        await message.channel.send(response)

    phrase = [
        "J'ai envie d'un bon steak froid du RU miam",
        "seuuuukeuuu",
        "Je blaire mon mucus quotidiennement",
        "WOOOOUUUUH WOUH WOUH FOUCOOOOOOOOOO",
        "ALLAN",
        "Gelano PA PM",
        "J'adore les cours de probabilité en amphi le vendredi matin !!!",
        "U E AAAAA U",
        "Salut " + str(message.author.name) + " comment ça va ? ^^",
        "Ah tu tombes à pique " + str(message.author.name) + " ! Je vais lancer World of warcraft shadowlands tu veux venir ?",
        "Ta gueule " + str(message.author.name)
    ]

    response = random.choice(phrase)

    if 'allan' in message.content.lower() :
        await message.channel.send(response)

client.run('MTA1MTI2NDk2ODk4MjUzMjEzNg.GZzToM.N5EFIAqvcnP0EXHg8DAk2Y8Mmhc_kQTdbctnKU')

