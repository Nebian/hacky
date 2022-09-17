import discord
from discord.ext import commands, tasks
import os
import asyncio
import random
from random import choice
import json

with open("config.json") as json_data_file:
    cfg = json.load(json_data_file)

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='$', intents=intents)

status = ['Hackeando el ITB']


@bot.event
async def on_ready():
    change_status.start()
    print('Captain Teemo on duty! {0.user}'.format(bot))


@tasks.loop(seconds=20)
async def change_status():
    await bot.change_presence(activity=discord.Game(choice(status)))


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if random.randint(1, 100) == 22:
        await message.channel.send('Tu argumento no tiene sentido.', reference=message, mention_author=False)

    if 'hola' in message.content.lower():
        await message.channel.send('¡Pa ti mi cola!', reference=message, mention_author=False)

    await bot.process_commands(message)


@bot.command()
async def ping(ctx):
    await ctx.send(f'**Pong!** Latency {round(bot.latency * 1000)}ms')


@bot.command()
async def horario(ctx):
    await ctx.send(file=discord.File('Media/horario.png'))


@bot.command()
async def mimir(ctx):
    await ctx.send(file=discord.File('Media/sleepy-sleeping.gif'))


@bot.command()
async def spanglish(ctx):
    await ctx.send(file=discord.File('Media/relaxingcup.gif'))


@bot.command()
async def pepe(ctx):
    await ctx.send('https://www.youtube.com/watch?v=mxpbwpU9HAo&ab_channel=theScoreesports')


@bot.command()
async def rolldice(ctx):
    message = await ctx.send("Choose a number:\n**4**, **6**, **8**, **10**, **12**, **20** ")

    def check(m):
        return m.author == ctx.author

    try:
        message = await bot.wait_for("message", check=check, timeout=30.0)
        m = message.content

        if m != "4" and m != "6" and m != "8" and m != "10" and m != "12" and m != "20":
            await ctx.send("Sorry, invalid choice.")
            return

        coming = await ctx.send("Here it comes...")
        await asyncio.sleep(1)
        await coming.delete()
        await ctx.send(f"**{random.randint(1, int(m))}**")
    except asyncio.TimeoutError:
        await message.delete()
        await ctx.send("Procces has been canceled because you didn't respond in **30** seconds.")


bot.run(cfg['token'])
