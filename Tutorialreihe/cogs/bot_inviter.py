import discord
from discord.ext import commands

class Bot_Inviter(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        try:
            integrations = await guild.integrations()
        except discord.Forbidden:
            return

        for integration in integrations:
            if isinstance(integration, discord.BotIntegration):
                if integration.application.user == self.bot.user:
                    try:
                        await integration.user.send("Danke fürs Einladen!")
                    except discord.Forbidden:
                        return
                    break

async def setup(bot):
    await bot.add_cog(Bot_Inviter(bot))
