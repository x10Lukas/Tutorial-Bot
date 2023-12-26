import discord
from discord.ext import commands
from discord import app_commands

class Context(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

class ContextMessage(app_commands.ContextMenu):
    def __init__(self):
        super().__init__(callback=self.getMessageAuthor, name="Zeige die ID")

    async def getMessageAuthor(self, interaction: discord.Interaction, message: discord.Message):
        await interaction.response.send_message(f"Die ID der nachricht ist {message.id}")


class ContextMember(app_commands.ContextMenu):
    def __init__(self):
        super().__init__(callback=self.getMessageAuthor, name="Stups")

    async def getMessageAuthor(self, interaction: discord.Interaction, member: discord.Member):
        await interaction.response.send_message(f"{interaction.user.mention} hat {member.mention} angestupst")

async def setup(bot):
    await bot.add_cog(Context(bot))
    bot.tree.add_command(ContextMessage())
    bot.tree.add_command(ContextMember())
