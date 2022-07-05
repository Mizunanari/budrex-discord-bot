import discord
import env
from moves import get_moves, isMoveSuccess

intents = discord.Intents.all()
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"{client.user}がログインしました")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    move = get_moves(message.content)

    if move[0]:
        if isMoveSuccess(move[1]["priority"], move[1]["damage_class"]):
            await message.channel.send("バドレックスはたおれた")
        else:
            await message.channel.send("しかしうまくきまらなかった")


client.run(env.BOT_TOKEN)
