import discord
from discord.ext import commands
from discord import app_commands

class Activity(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="activity")
    @app_commands.checks.has_role(1179050492530278482)
    @app_commands.choices(activity=[
        discord.app_commands.Choice(name='game', value=1),
        discord.app_commands.Choice(name='stream', value=2)
    ])
    async def activity(self, interaction: discord.Interaction, activity: discord.app_commands.Choice[int], name: str):
        if activity == 1:
            act = discord.Game(name=name)
        else:
            act = discord.Streaming(name=name, url="https://www.twitch.tv/lukas9627")

        await self.bot.change_presence(activity=act, status=discord.Status.online)
        await interaction.response.send_message("Status wurde geändert!", ephemeral=True)

async def setup(bot):
    await bot.add_cog(Activity(bot))
