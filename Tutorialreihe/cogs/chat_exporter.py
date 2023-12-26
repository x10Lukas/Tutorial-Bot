import discord
from discord.ext import commands
from discord import app_commands
import chat_exporter
import io

class Chat_Exporter(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command()
    async def export(self, interaction: discord.Interaction, anzahl: int):
        transcript = await chat_exporter.export(
            interaction.channel,
            limit=anzahl,
            bot=self.bot,
            tz_info="Europe/berlin"
        )

        file = discord.File(io.BytesIO(transcript.encode()), filename="transcript.html")

        msg = await interaction.channel.send(file=file)
        link = await chat_exporter.link(msg)

        embed = discord.Embed(description=f"Hier ist der Link zum [Transcript]({link})",
                              color=discord.Color.blue())
        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(Chat_Exporter(bot))
