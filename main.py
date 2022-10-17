import enum

import discord
from discord.app_commands import Choice
from discord.ext import commands, tasks
from discord import app_commands
import os
import asyncio
import random
from random import choice
import json


with open("config.json") as json_data_file:
    cfg = json.load(json_data_file)

bot = commands.Bot(command_prefix='$', owner_id=295498594604154890, intents=discord.Intents.all())

status = ['Hackeando el ITB']


@bot.event
async def on_ready():
    change_status.start()
    print('Captain Teemo on duty! {0.user}'.format(bot))


@bot.command()
async def resync(ctx):
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)


@tasks.loop(seconds=20)
async def change_status():
    await bot.change_presence(activity=discord.Game(choice(status)))


@bot.event
async def on_raw_reaction_add(payload):
    channel_id = 1021129934749585459
    message_id = 1021469640502825020

    if channel_id == payload.channel_id and message_id == payload.message_id:

        guild = bot.get_guild(int(payload.guild_id))

        # get role
        if payload.emoji == discord.PartialEmoji.from_str('🇦'):
            role = discord.utils.get(guild.roles, name="ASIX-1A")
            print(role)
            await payload.member.add_roles(role, reason="self-role reaction")
        elif payload.emoji == discord.PartialEmoji.from_str('🇧'):
            role = discord.utils.get(guild.roles, name="ASIX-1B")
            print(role)
            await payload.member.add_roles(role, reason="self-role reaction")
        elif payload.emoji == discord.PartialEmoji.from_str('🇨'):
            role = discord.utils.get(guild.roles, name="ASIX-1C")
            print(role)
            await payload.member.add_roles(role, reason="self-role reaction")
        elif payload.emoji == discord.PartialEmoji.from_str('🅰️'):
            role = discord.utils.get(guild.roles, name="ASIX-2A")
            print(role)
            await payload.member.add_roles(role, reason="self-role reaction")
        elif payload.emoji == discord.PartialEmoji.from_str('🅱️'):
            role = discord.utils.get(guild.roles, name="ASIX-2B")
            print(role)
            await payload.member.add_roles(role, reason="self-role reaction")
        elif payload.emoji == discord.PartialEmoji.from_str("<:itb:1020051101044723722>"):
            role = discord.utils.get(guild.roles, name="Profesor")
            print(role)
            await payload.member.add_roles(role, reason="self-role reaction")


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if random.randint(1, 200) == 69:
        await message.channel.send('Tu argumento no tiene sentido.', reference=message, mention_author=False)

    await bot.process_commands(message)


@bot.tree.command(name="ping")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message(f"**Pong!** Latency {round(bot.latency * 1000)}ms", ephemeral=True)


class Ciclos(enum.Enum):
    ASIXA = 1
    ASIXB = 2
    ASIXC = 3


@bot.tree.command(name="horario")
@app_commands.describe(horarios='Horarios disponibles')
async def horario(interaction: discord.Interaction, horarios: Ciclos):
    await interaction.response.send_message(file=discord.File(f'Media/horario{horarios.name}.png'))

"""
@bot.tree.command(name="horario")
@app_commands.describe(ciclos='Horarios disponibles')
@app_commands.choices(ciclos=[
    Choice(name='ASIXA', value=1),
    Choice(name='ASIXB', value=1),
    Choice(name='ASIXC', value=1),
])
async def horario(interaction: discord.Interaction, ciclos: Choice[int]):
    await interaction.response.send_message(file=discord.File(f'Media/horario{ciclos.name}.png'))
"""

@bot.command()
async def horarioB(ctx):
    await ctx.send(file=discord.File('Media/horarioASIXB.png'))


@bot.command()
async def horarioC(ctx):
    await ctx.send(file=discord.File('Media/horarioASIXC.png'))


@bot.command()
async def mimir(ctx):
    await ctx.send(file=discord.File('Media/sleepy-sleeping.gif'))


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
