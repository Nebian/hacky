import discord
from discord.app_commands import Choice
from discord.ext import commands, tasks
from discord import app_commands
import random
from random import choice
import json
import enum


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


@bot.tree.command(name="ping", description="Prints the ping between discord and bot server")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message(f"**Pong!** Latency {round(bot.latency * 1000)}ms", ephemeral=True)


class Ciclos(enum.Enum):
    ASIX1A = 1
    ASIX1B = 2
    ASIX1C = 3
    ASIX2A = 4
    ASIX2B = 5


@bot.tree.command(name="schedule", description="Shows the schedule of the selected class")
@app_commands.describe(schedules='Available schedules')
async def schedule(interaction: discord.Interaction, schedules: Ciclos):
    await interaction.response.send_message(file=discord.File(f'Media/horarios/horario{schedules.name}.png'))


@bot.tree.command(name="sleepy", description="Sends a sleepy Tom gif")
async def sleepy(interaction: discord.Interaction):
    await interaction.response.send_message(file=discord.File('Media/sleepy-sleeping.gif'))


@bot.tree.command(name="pepe", description="Sends a video that explains the history of pepe")
async def pepe(interaction: discord.Interaction):
    await interaction.response.send_message('https://www.youtube.com/watch?v=mxpbwpU9HAo&ab_channel=theScoreesports')


@bot.tree.command(name="rolldice", description="Roll a dice")
@app_commands.describe(dices="Available dices")
@app_commands.choices(dices=[
    Choice(name='4', value=1),
    Choice(name='6', value=2),
    Choice(name='8', value=3),
    Choice(name='10', value=4),
    Choice(name='12', value=5),
    Choice(name='20', value=6),
])
async def rolldice(interaction: discord.Interaction, dices: Choice[int]):
    await interaction.response.send_message(f'**{random.randint(1, int({dices.name}))}**')


bot.run(cfg['token'])
