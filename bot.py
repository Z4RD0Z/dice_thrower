import os

import discord
from dotenv import load_dotenv
from dice_throwers import DiceThrowerFactory

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

dice_thrower = DiceThrowerFactory.create_thrower('Savage')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if  "roll" in message.content :
        print("ok")
        dice_value = message.content.split("roll")
        print(dice_value)
        response = dice_thrower.parse_dice_string(dice_value[1])
        await message.channel.send(response)


client.run(TOKEN)