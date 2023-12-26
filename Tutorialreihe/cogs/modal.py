import discord
from discord.ext import commands
from discord import app_commands, ui

class Modal(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command()
    async def modal(self, interaction: discord.Interaction):
        await interaction.response.send_modal(TutorialModal())

    @app_commands.command()
    async def button_modal(self, interaction: discord.Interaction):
        await interaction.response.send_message(view=TutorialView())

class TutorialModal(ui.Modal, title="Erzeuge ein Embed"):
    _titel = ui.TextInput(label="Embed Titel", placeholder="Placeholder", style=discord.TextStyle.short, custom_id="1")
    _beschreibung = ui.TextInput(label="Embed Beschreibung", placeholder="Placeholder", style=discord.TextStyle.long, custom_id="2")

    async def on_submit(self, interaction: discord.Interaction) -> None:
        embed = discord.Embed(title=f"{self._titel}", description=f"{self._beschreibung}", color=discord.Color.green())
        await interaction.response.send_message(embed=embed)

class TutorialView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Klicke hier", style=discord.ButtonStyle.grey, custom_id="1")
    async def button_callback(self, interaction: discord.Interaction, button: discord.Button):
        await interaction.response.send_modal(TutorialModal())

async def setup(bot):
    await bot.add_cog(Modal(bot))
