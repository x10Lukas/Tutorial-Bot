import discord
from discord.ext import commands
from discord import app_commands

options = [
        discord.SelectOption(label="Python", description="Python Beschreibung", emoji="<:Python:1183380630302629908>"),
        discord.SelectOption(label="Java", description="Java Beschreibung", emoji="<:Java:1183381146126520430>"),
        discord.SelectOption(label="JavaScript", description="JavaScript Beschreibung", emoji="<:JavaScript:1183381161783873636>"),
    ]

class Dropdown(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command()
    async def select1(self, interaction: discord.Interaction):
        await interaction.response.send_message("Wähle eine Programmiersprache aus", view=TutorialView())

    @app_commands.command()
    async def select2(self, interaction: discord.Interaction):
        select = TutorialSelect()
        view = discord.ui.View(timeout=None)
        view.add_item(select)

        await interaction.response.send_message(view=view)

class TutorialView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.select(placeholder="Triff eine Auswahl", min_values=1, max_values=2, options=options)
    async def select_callback(self, interaction: discord.Interaction, select):
        selected_values = select.values
        user = interaction.user

        selected_options = [f"- {option.label}\n" for option in select.options if option.value in selected_values]

        await interaction.response.send_message(f"Du hast folgendes ausgewählt:\n{''.join(selected_options)}")

class TutorialSelect(discord.ui.Select):
    def __init__(self):
        super().__init__(placeholder="Triff eine Auswahl", min_values=1, max_values=1, options=options)

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"Du hast {self.values[0]} ausgewählt")

async def setup(bot):
    await bot.add_cog(Dropdown(bot))
