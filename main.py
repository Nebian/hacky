import discord
from discord.ext import commands, tasks
from discord import app_commands
import random
from random import choice
from typing import Literal
import json


with open("config.json") as file:
    cfg = json.load(file)

with open("Data/roles.json") as file:
    roles_clase = json.load(file)


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
            discord.SelectOption(label="Gamer", emoji="🎮",
                                 description="This role allows you to see the gamer channel."),
            discord.SelectOption(label="Otaku", emoji="🚿",
                                 description="This role allows you to see the anime channel."),
            discord.SelectOption(label="Birras", emoji="🍻",
                                 description="This role will allow other users to mention you."),
            discord.SelectOption(label="Furro", emoji="<furro:1054413958687228027>",
                                 description="This role will allow you to see the Furros channel.")
            ]
        super().__init__(placeholder="Roles", max_values=4, min_values=1, options=options)

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

    await bot.process_commands(message)


@bot.tree.command(name="ping", description="Prints the ping between discord and bot server")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message(f"**Pong!** Latency {round(bot.latency * 1000)}ms", ephemeral=True)


@bot.tree.command(name="schedule", description="Shows the schedule of your class")
@app_commands.describe(schedule="Class schedule you would want to see")
async def show_schedule(interaction: discord.Interaction, schedule: str = None):
    if schedule is None:
        roles = interaction.user.roles
        for role in roles:
            if str(role) in roles_clase['roles']:
                print(role)
                await interaction.response.send_message(file=discord.File(f'Media/schedules/schedule{role}.png'))
                break
    else:
        await interaction.response.send_message(file=discord.File(f'Media/schedules/schedule{schedule}.png'))


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