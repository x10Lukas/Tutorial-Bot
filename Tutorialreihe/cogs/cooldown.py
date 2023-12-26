import discord
from discord.ext import commands
from discord import app_commands

class Cooldown(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        bot.tree.on_error = self.on_app_command_error

    @app_commands.command()
    @app_commands.checks.cooldown(1, 30 * 60, key=lambda i: (i.user.id))
    async def hey(self, interaction: discord.Interaction):
        await interaction.response.send_message("Hey")

    @staticmethod
    def convert_time(seconds):
        if seconds < 60:
            return f"{round(seconds)} Sekunden"

        minutes = seconds / 60
        if minutes < 60:
            return f"{round(minutes)} Minuten"

        hours = minutes / 60
        if hours < 60:
            return f"{round(hours)} Stunden"

    async def on_app_command_error(self, interaction: discord.Interaction, error: app_commands.CheckFailure):
        if isinstance(error, app_commands.CommandOnCooldown):
            seconds = error.retry_after
            final_time = self.convert_time(seconds)
            await interaction.response.send_message(f"Du musst noch {final_time} warten.", ephemeral=True)


async def setup(bot):
    await bot.add_cog(Cooldown(bot))
