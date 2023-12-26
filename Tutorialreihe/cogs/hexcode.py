import discord
from discord.ext import commands
from discord import app_commands

class HexCode(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command()
    async def hexcode(self, interaction: discord.Interaction, hexcode: str):
        hex_string = f"0x{hexcode}"
        color = int(hex_string, 16)

        embed = discord.Embed(description="Dies sit ein sehr cooler Text"
                                          "\n\n🎁 Bald ist Weihnachten",
                              color=color)
        embed.set_thumbnail(url=f"{interaction.user.display_avatar}")
        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(HexCode(bot))
