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

    try:
        damage_class, priority = get_moves(message.content)
    except ValueError:
        pass
    else:
        if isMoveSuccess(priority, damage_class):
            await message.channel.send(message.author.name + "はたおれた")
        else:
            await message.channel.send("しかしうまくきまらなかった")


client.run(env.BOT_TOKEN)
