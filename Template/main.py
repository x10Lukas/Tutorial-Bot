import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

intents = discord.Intents.default()

bot = commands.Bot(intents=intents, debug_guilds=[123456789])
bot.remove_command("help")

if __name__ == "__main__":
    for filename in os.listdir(""):
        if filename.endswith(".py"):
            bot.load_extension(f"cogs.{filename[:-3]}")

    load_dotenv()
    bot.run(os.getenv("TOKEN"))