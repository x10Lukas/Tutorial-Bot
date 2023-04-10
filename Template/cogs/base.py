import discord
from discord.ext import commands
from discord import app_commands

class Base(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(description="hello")
    async def hello(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"Hey {interaction.user.mention}")

async def setup(bot):
    await bot.add_cog(Base(bot))
    print("cogs.Base")