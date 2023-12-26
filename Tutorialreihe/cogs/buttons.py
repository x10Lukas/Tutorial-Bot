import discord
from discord.ext import commands
from discord import app_commands, Interaction

class Buttons(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command()
    async def button1(self, interaction: discord.Interaction):
        await interaction.response.send_message("Klicke hier", view=TutorialView())

    @app_commands.command()
    async def button2(self, interaction: discord.Interaction):
        button = TutorialButton("Python ist cool")
        view = discord.ui.View()
        view.add_item(button)
        await interaction.response.send_message("Klicke hier", view=view)

    @app_commands.command()
    async def url_button(self, interaction: discord.Interaction):
        button = discord.ui.Button(label="GitHub", url="https://github.com/")
        view = discord.ui.View()
        view.add_item(button)
        await interaction.response.send_message("Klicke hier", view=view)

class TutorialView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.channel_url = f"https://github.com/"
        self.add_item(discord.ui.Button(label="GitHub", url=self.channel_url))

    @discord.ui.button(label="Klicke hier", style=discord.ButtonStyle.primary, emoji="😊", custom_id="button1")
    async def button1(self, interaction: discord.Interaction, button: discord.Button):
        await interaction.response.send_message("Hey!", ephemeral=True)

    @discord.ui.button(label="Klicke hier", style=discord.ButtonStyle.primary, emoji="😊", custom_id="button2")
    async def button2(self, interaction: discord.Interaction, button: discord.Button):
        button.disabled = True
        await interaction.response.edit_message(view=self)

class TutorialButton(discord.ui.Button):
    def __init__(self, label):
        super().__init__(label=label, style=discord.ButtonStyle.green)

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_message("Hey!", ephemeral=True)

async def setup(bot):
    await bot.add_cog(Buttons(bot))
    bot.add_view(TutorialView())
