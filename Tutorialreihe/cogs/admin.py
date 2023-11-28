import discord
from discord.ext import commands
from discord import app_commands

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        bot.tree.on_error = self.on_app_command_error

    @app_commands.command(description="Kicke einen Member")
    @app_commands.default_permissions(administrator=True, kick_members=True)
    @app_commands.guild_only()
    async def kick(self, interaction: discord.Interaction, member: discord.Member):
        try:
            await member.kick()
        except (discord.Forbidden, discord.HTTPException) as e:
            await interaction.response.send_message("Ich habe keine Berechtigung, um diesen Member zu kicken.")
            return
        await interaction.response.send_message(f"{member.mention} wurde gekickt!")

    @app_commands.command()
    @app_commands.checks.has_permissions(administrator=True)
    async def hallo(self, interaction: discord.Interaction):
        await interaction.response.send_message("Hey")

    async def on_app_command_error(self, interaction: discord.Interaction, error: app_commands.AppCommandError):
        if isinstance(error, app_commands.CheckFailure):
            await interaction.response.send_message(f"Für diesen Befehl musst du Admin sein.", ephemeral=True)
            return
        await interaction.response.send_message(f"Es ist ein Fehler aufgetreten: ```{error}```")

async def setup(bot):
    await bot.add_cog(Admin(bot))