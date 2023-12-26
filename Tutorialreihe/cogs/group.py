import discord
from discord.ext import commands
from discord import app_commands

class Group(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    goenrgy = app_commands.Group(name="gönrgy", description="Kauf dir ein Gönrgy")

    @goenrgy.command()
    async def blueberry(self, interaction: discord.Interaction):
        await interaction.response.send_message("Du hast dir ein Gönrgy mit Blueberry geschmack gegönnt.")

    @goenrgy.command()
    async def tropical_exotic(self, interaction: discord.Interaction):
        await interaction.response.send_message("Du hast dir ein Gönrgy mit Tropical Exotic geschmack gegönnt.")

    @goenrgy.command()
    async def raspberry(self, interaction: discord.Interaction):
        await interaction.response.send_message("Du hast dir ein Gönrgy mit Raspberry geschmack gegönnt.")

async def setup(bot):
    await bot.add_cog(Group(bot))
