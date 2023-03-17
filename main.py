import discord
from discord.ext import commands, tasks
from discord.utils import get
from discord import app_commands
from discord import FFmpegPCMAudio
import random
from random import choice
from typing import Literal
import json
import matplotlib.pyplot as plt
import os
from gtts import gTTS
import asyncio

with open("config.json") as file:
    cfg = json.load(file)

with open("Data/roles.json") as file:
    roles_json = json.load(file)

bot = commands.Bot(command_prefix='$', owner_id=295498594604154890, intents=discord.Intents.all())

status = ['Hackeando el ITB']
MANAGEMENT_CHANNEL = 1034529648857595914
GUILD = 1018310672058155160


@bot.event
async def on_ready():
    change_status.start()
    print("Captain Teemo on duty! {0.user}".format(bot))


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


class ClassSelectASIX(discord.ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(label="ASIX-1A"),
            discord.SelectOption(label="ASIX-1B"),
            discord.SelectOption(label="ASIX-1C"),
            discord.SelectOption(label="ASIX-2A"),
            discord.SelectOption(label="ASIX-2B")
        ]
        super().__init__(placeholder="ASIX", max_values=1, min_values=1, options=options)

    async def callback(self, interaction: discord.Interaction):
        guild = bot.get_guild(GUILD)
        role = discord.utils.get(guild.roles, name=self.values[0])
        await interaction.user.add_roles(role, reason="self-role selection")
        await interaction.response.send_message(f"You now have the role {self.values[0]}!\n"
                                                f"If you can't see the other channels, send a DM to @Nebian#2817",
                                                ephemeral=True)


class ClassSelectDAM(discord.ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(label="DAM-1A"),
            discord.SelectOption(label="DAM-2A"),
            discord.SelectOption(label="DAM-2B"),
            discord.SelectOption(label="DAMv-1A"),
            discord.SelectOption(label="DAMv-2A")
        ]
        super().__init__(placeholder="DAM", max_values=1, min_values=1, options=options)

    async def callback(self, interaction: discord.Interaction):
        guild = bot.get_guild(GUILD)
        role = discord.utils.get(guild.roles, name=self.values[0])
        await interaction.user.add_roles(role, reason="self-role selection")
        await interaction.response.send_message(f"You now have the role {self.values[0]}!\n"
                                                f"If you can't see the other channels, send a DM to @Nebian#2817",
                                                ephemeral=True)


class ClassSelectDAW(discord.ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(label="DAWe-1A"),
            discord.SelectOption(label="DAWe-2A")
        ]
        super().__init__(placeholder="DAW", max_values=1, min_values=1, options=options)

    async def callback(self, interaction: discord.Interaction):
        guild = bot.get_guild(GUILD)
        role = discord.utils.get(guild.roles, name=self.values[0])
        await interaction.user.add_roles(role, reason="self-role selection")
        await interaction.response.send_message(f"You now have the role {self.values[0]}!\n"
                                                f"If you can't see the other channels, send a DM to @Nebian#2817",
                                                ephemeral=True)


class ClassSelectA3D(discord.ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(label="A3D-1A"),
            discord.SelectOption(label="A3D-2A")
        ]
        super().__init__(placeholder="A3D", max_values=1, min_values=1, options=options)

    async def callback(self, interaction: discord.Interaction):
        guild = bot.get_guild(GUILD)
        role = discord.utils.get(guild.roles, name=self.values[0])
        await interaction.user.add_roles(role, reason="self-role selection")
        await interaction.response.send_message(f"You now have the role {self.values[0]}!\n"
                                                f"If you can't see the other channels, send a DM to @Nebian#2817",
                                                ephemeral=True)


class ClassSelectSMX(discord.ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(label="SMX-1A"),
            discord.SelectOption(label="SMX-1B"),
            discord.SelectOption(label="SMX-1C"),
            discord.SelectOption(label="SMX-1D"),
            discord.SelectOption(label="SMX-1E"),
            discord.SelectOption(label="SMX-1F"),
            discord.SelectOption(label="SMX-2A"),
            discord.SelectOption(label="SMX-2B"),
            discord.SelectOption(label="SMX-2C"),
            discord.SelectOption(label="SMX-2D"),
            discord.SelectOption(label="SMX-2E")
        ]
        super().__init__(placeholder="SMX", max_values=1, min_values=1, options=options)

    async def callback(self, interaction: discord.Interaction):
        guild = bot.get_guild(GUILD)
        role = discord.utils.get(guild.roles, name=self.values[0])
        await interaction.user.add_roles(role, reason="self-role selection")
        await interaction.response.send_message(f"You now have the role {self.values[0]}!\n"
                                                f"If you can't see the other channels, send a DM to @Nebian#2817",
                                                ephemeral=True)


class SelectViewClass(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(ClassSelectASIX())
        self.add_item(ClassSelectDAM())
        self.add_item(ClassSelectDAW())
        self.add_item(ClassSelectA3D())
        self.add_item(ClassSelectSMX())


@bot.tree.command(name="autoroles_class", description="Select the role of your class")
async def autoroles_class(interaction: discord.Interaction):
    await interaction.response.send_message(f'Autoroles de Clase', view=SelectViewClass(), ephemeral=True)


class ThematicRoles(discord.ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(label="Minecraft", emoji="<minecraft:1079053853829365860>",
                                 description="This role allows you to receive notifications about minecraft."),
            discord.SelectOption(label="Birras", emoji="🍻",
                                 description="This role allows other users to mention you."),
            discord.SelectOption(label="Gamer", emoji="🎮",
                                 description="This role allows you to see the gamer channel."),
            discord.SelectOption(label="Otaku", emoji="🚿",
                                 description="This role allows you to see the anime channel."),
            discord.SelectOption(label="Furro", emoji="<furro:1054413958687228027>",
                                 description="This role allows you to see the Furros channel."),
            discord.SelectOption(label="Maricón", emoji="🏳️‍🌈",
                                 description="This role proclaims that you are Maricón.")
        ]
        super().__init__(placeholder="Roles", max_values=6, min_values=1, options=options)

    async def callback(self, interaction: discord.Interaction):
        guild = bot.get_guild(GUILD)
        for i, value in enumerate(self.values):
            role = discord.utils.get(guild.roles, name=self.values[i])
            await interaction.user.add_roles(role, reason="self-role selection")
        await interaction.response.send_message(f"You now have the role(s) {self.values}.", ephemeral=True)


class SelectViewThematic(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(ThematicRoles())


@bot.tree.command(name="autoroles_thematic", description="Select the thematic roles you want to have.")
async def autoroles_thematic(interaction: discord.Interaction):
    await interaction.response.send_message(f'Autoroles Temáticos', view=SelectViewThematic(), ephemeral=True)


@bot.tree.command(name="embed_autoroles_class", description="Send an embed explaining the autoroles_class usage")
@app_commands.default_permissions(administrator=True)
@app_commands.describe(ch="Channel to send")
async def embed_autoroles_class(interaction: discord.Interaction, ch: str):
    title = "Escoger un rol de clase"
    description = "Para escoger un rol tienes que introducir </autoroles_class:1034611158050684998> " \
                  "o hacer click en el comando. El bot te enviará un mensaje con menús desplegables " \
                  "donde podrás seleccionar el rol de tu clase.\n\n " \
                  "Atención: Escoge el rol de tu clase a la primera porque sólo se puede escoger una vez. " \
                  "Para cambiarlo tendrás que solicitárselo a un moderador o administrador."
    tutorial_gif = discord.File("Media/tutorials/autoroles.gif", filename="autoroles.gif")
    class_embed = discord.Embed(title=title, description=description, color=0x00ff00)
    class_embed.add_field(name="Tutorial", value="A continuación un gif con una demostración:")
    class_embed.set_image(url="attachment://autoroles.gif")
    channel = bot.get_channel(int(ch))
    await channel.send(file=tutorial_gif, embed=class_embed)
    await interaction.response.send_message("Embed sent", ephemeral=True)


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if random.randint(1, 200) == 69:
        await message.channel.send("Tu argumento no tiene sentido.", reference=message, mention_author=False)
    elif random.randint(1, 300) == 69:
        await message.channel.send("Puta Renfe.", mention_author=False)
    elif random.randint(1, 400) == 69:
        with open("Media/ascii/train.txt", "r") as renfe:
            rodalies = renfe.read()
        await message.channel.send(rodalies)
    elif random.randint(1, 1000) == 69:
        await message.channel.send("Doxing user...", reference=message, mention_author=False)

    await bot.process_commands(message)


def get_salute_audio(user):
    audio_path = os.path.join(".", "Media/audio")
    text = f"Hola {user}, te estoy vigilando, cuidado con lo que haces o te doxeo."
    tts = gTTS(text, lang="de")
    audio_file = os.path.join(audio_path, f"saludo.mp3")
    tts.save(audio_file)
    return audio_file

@bot.event
async def on_voice_state_update(member, before, after):
    if not before.channel and after.channel:  # User joined a channel
        channel = after.channel
        voice_client = get(bot.voice_clients, guild=member.guild)
        if voice_client and not voice_client.is_connected():
            if voice_client.channel != channel:
                await voice_client.move_to(channel)
        else:
            voice_client = await channel.connect()
        audio_file = get_salute_audio(member.name)
        if os.path.exists(audio_file):
            audio_source = FFmpegPCMAudio(audio_file, executable="ffmpeg")
            voice_client.play(audio_source)
            while voice_client.is_playing():
                await asyncio.sleep(0.1)
            await asyncio.sleep(1)
            await voice_client.disconnect(force=False)
        else:
            print(f"Error: audio file not found for {member.nick}.")


@bot.tree.command(name="ping", description="Prints the ping between discord and bot server")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message(f"**Pong!** Latency {round(bot.latency * 1000)}ms", ephemeral=True)


@bot.tree.command(name="schedule", description="Shows the schedule of your class")
@app_commands.describe(schedule="Class schedule you would want to see")
async def show_schedule(interaction: discord.Interaction, schedule: str = None):
    if schedule is None:
        roles = interaction.user.roles
        for role in roles:
            for grade in roles_json:
                if grade in role.name and len(grade) == len(role.name) - 3:
                    await interaction.response.send_message(file=discord.File(f'Media/schedules/schedule{role}.jpg'))
                    break
    else:
        await interaction.response.send_message(file=discord.File(f'Media/schedules/schedule{schedule}.png'))


def count_role_members():
    role_counts = {}
    guild = bot.get_guild(GUILD)
    roles = guild.roles

    for role in roles:
        member_count = len(role.members)
        role_counts[role.name] = member_count

    grades = {'ASIX': 0, 'DAM': 0, 'DAMv': 0, 'DAWe': 0, 'A3D': 0, 'SMX': 0}
    role_counts.update(grades)

    for role in role_counts:
        for grade in roles_json:
            if grade in role and len(role) == len(grade) + 3:
                role_counts[grade] += role_counts[role]

    return role_counts


@bot.tree.command(name="users_stats", description="Shows the number of members of each class")
@app_commands.describe(graph="Type of graph to show the statistics on")
async def users_stats(interaction: discord.Interaction, graph: Literal['Bars'] = None,
                      rol: Literal['Otaku', 'Furro'] = None,
                      grade: Literal['ASIX', 'DAM', 'DAMv', 'DAWe', 'A3D', 'SMX'] = None):
    guild = bot.get_guild(GUILD)
    role_counts = count_role_members()
    if graph is None and rol is None and grade is None:

        title = "Estadísticas del servidor"
        description = f"**Total** - **{role_counts['@everyone']}**"
        embed_counts = discord.Embed(title=title, description=description, color=0x004ffc)

        for ciclo, roles in roles_json.items():
            field_value = ""
            for role in roles:
                role_obj = discord.utils.get(guild.roles, name=role)
                field_value += f"{role_obj.mention} - {role_counts[role]}\n"
            embed_counts.add_field(name=f"**{ciclo}** - {role_counts[ciclo]}", value=field_value, inline=True)

        logo = discord.File("Media/embeds/itb_logo_no_background.png", filename="itb_logo_no_background.png")
        embed_counts.set_thumbnail(url="attachment://itb_logo_no_background.png")
        await interaction.response.send_message(file=logo, embed=embed_counts)

    elif rol is None and grade is None:
        fig, ax = plt.subplots()

        grades = []
        counts = []
        colors = []

        for ciclo, role in roles_json.items():
            grades.append(ciclo)
            counts.append(role_counts[ciclo])
            role_obj = discord.utils.get(guild.roles, name=role[0])
            c = str(role_obj.color)
            colors.append(c)

        ax.bar(grades, counts, label=grades, color=colors)
        ax.set_ylabel('num')
        ax.set_title('Miembros de cada ciclo')
        ax.legend(title='Ciclos')
        plt.savefig('Media/plots/plot.png')

        await interaction.response.send_message(file=discord.File(f'Media/plots/plot.png'))

    else:
        await interaction.response.send_message(f"Aún no está implementado, te esperas.")


@bot.tree.command(name="sleepy", description="Sends a sleepy Tom gif")
async def sleepy(interaction: discord.Interaction):
    await interaction.response.send_message(file=discord.File('Media/sleepy-sleeping.gif'))


@bot.tree.command(name="pepe", description="Sends a video that explains the history of pepe")
async def pepe(interaction: discord.Interaction):
    await interaction.response.send_message("https://www.youtube.com/watch?v=mxpbwpU9HAo&ab_channel=theScoreesports")


@bot.tree.command(name="rolldice", description="Roll a dice")
@app_commands.describe(dices="Available dices")
async def rolldice(interaction: discord.Interaction, dices: Literal['4', '6', '8', '10', '12', '20']):
    await interaction.response.send_message(f"It\'s a **{random.randint(1, int(dices))}**!")


bot.run(cfg['token'])
