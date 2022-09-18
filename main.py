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
async def on_raw_reaction_add(payload):
    channel_id = 1021129934749585459
    message_id = 1021169218252722346

    if channel_id == payload.channel_id and message_id == payload.message_id:

        guild = bot.get_guild(int(payload.guild_id))

        # get role
        if payload.emoji == discord.PartialEmoji.from_str('🇦'):
            role = discord.utils.get(guild.roles, name="ASIX-A")
            print(role)
            await payload.member.add_roles(role, reason="self-role reaction")
        elif payload.emoji == discord.PartialEmoji.from_str('🇧'):
            role = discord.utils.get(guild.roles, name="ASIX-B")
            print(role)
            await payload.member.add_roles(role, reason="self-role reaction")
        elif payload.emoji == discord.PartialEmoji.from_str('🇨'):
            role = discord.utils.get(guild.roles, name="ASIX-C")
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

    if 'hola' in message.content.lower():
        await message.channel.send('¡Pa ti mi cola!', reference=message, mention_author=False)

    await bot.process_commands(message)


@bot.command()
async def ping(ctx):
    await ctx.send(f'**Pong!** Latency {round(bot.latency * 1000)}ms')

"""
@bot.event
async def on_member_join(member):
    message = "Este mensaje debería llegar al DM"
    await member.send(message)
    
@bot.command()
async def embed(ctx):
    emessage = discord.Embed(title="Sample Embed", url="https://realdrewdata.medium.com/", description="This is an embed that will show how to build an embed and the different components", color=0xFF5733)
    await ctx.send(embed=emessage)

@bot.command()
async def reactmessagerol(ctx):
    emessage = discord.Embed(title="Reacciona con la letra correspondiente a tu clase.",
                             description="Atención: Escoge el rol de tu clase a la primera porque sólo lo podrás escoger una vez. Para "
                                         "cambiarlo tendrás que solicitárselo a un moderador/administrador.\n\nASIX-A    🇦\nASIX-B   🇧\nASIX-C   "
                                         "🇨\nProfesor  <:itb:1020051101044723722>", color=0x332C9C)
    await ctx.send(embed=emessage)
"""


@bot.command()
async def horarioA(ctx):
    await ctx.send(file=discord.File('Media/horarioA.png'))


@bot.command()
async def horarioB(ctx):
    await ctx.send(file=discord.File('Media/horarioB.png'))


@bot.command()
async def horarioC(ctx):
    await ctx.send(file=discord.File('Media/horarioC.png'))


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
