import discord
from discord.ext import commands
from discord import app_commands

class Select(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command()
    async def select_type(self, interaction: discord.Interaction):
        await interaction.response.send_message(view=TutorialView())

    @app_commands.command()
    async def select_type2(self, interaction: discord.Interaction):
        await interaction.response.send_message(view=TutorialView2())

class TutorialView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.values = None

    @discord.ui.select(cls=discord.ui.RoleSelect, placeholder="Wähle eine Rolle aus", max_values=1)
    async def select_role(self, interaction: discord.Interaction, select):
        self.values = select.values
        await interaction.response.send_message(f"Du hast folgende Rollen ausgewählt: {self.values[0].mention}")

    @discord.ui.select(cls=discord.ui.UserSelect, placeholder="Wähle einen Benutzer aus", max_values=1)
    async def select_user(self, interaction: discord.Interaction, select):
        self.values = select.values
        await interaction.response.send_message(f"Du hast folgende Benutzer ausgewählt: {self.values[0].mention}")

    @discord.ui.select(cls=discord.ui.ChannelSelect, channel_types=[discord.ChannelType.text], placeholder="Wähle einen Channel aus", max_values=1)
    async def select_channel(self, interaction: discord.Interaction, select):
        self.values = select.values
        await interaction.response.send_message(f"Du hast folgende Channel ausgewählt: {self.values[0].mention}")

class TutorialView2(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(RoleSelectMenu())
        self.add_item(UserSelectMenu())
        self.add_item(ChannelSelectMenu())

class RoleSelectMenu(discord.ui.RoleSelect):
    def __init__(self):
        super().__init__(placeholder="Wähle eine Rolle aus", max_values=1)

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"Du hast folgende Rollen ausgewählt: {self.values[0].mention}")

class UserSelectMenu(discord.ui.UserSelect):
    def __init__(self):
        super().__init__(placeholder="Wähle einen Benutzer aus", max_values=1)

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"Du hast folgende Benutzer ausgewählt: {self.values[0].mention}")

class ChannelSelectMenu(discord.ui.ChannelSelect):
    def __init__(self):
        super().__init__(placeholder="Wähle einen Channel aus", channel_types=[discord.ChannelType.text], max_values=1)

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"Du hast folgende Channel ausgewählt: {self.values[0].mention}")

async def setup(bot):
    await bot.add_cog(Select(bot))
