import os

import discord
from dotenv import load_dotenv
from dice_throwers import DiceThrowerFactory
from utils import help_message

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

dice_thrower = DiceThrowerFactory.create_thrower('Savage')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if "roll" in message.content:
        print("ok")
        dice_value = message.content.split("roll")
        print(dice_value)
        response = dice_thrower.parse_dice_string(dice_value[1])
        await message.channel.send(response)

    if "help" in message.content:
        response = help_message
        await message.channel.send(response)

    if "e1m1" in message.content:
        response = "!play https://www.youtube.com/watch?v=qsjHbxVI3EI"
        await message.channel.send(response)

    if "change_game" in message.content:
        pass


client.run(TOKEN)