import discord
from discord.ext import commands
from discord import app_commands

class Bild(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command()
    async def bild(self, interaction: discord.Interaction):
        embed = discord.Embed(title="Christmas",
                              color=0xffffff)
        file = discord.File("img/christmas.png", filename="image.png")
        embed.set_image(url="attachment://image.png")
        await interaction.response.send_message(embed=embed, file=file)

async def setup(bot):
    await bot.add_cog(Bild(bot))
