import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

intents = discord.Intents.all()

bot = commands.Bot(command_prefix="!", intents=intents)
bot.remove_command('help')

@bot.event
async def on_ready():
    print(f"{bot.user} ist ready!")
    for filename in os.listdir("cogs"):
        if filename.endswith(".py"):
            cog_name = filename[:-3]
            await bot.load_extension(f"cogs.{cog_name}")
            print(f"cogs.{cog_name}")

    await bot.tree.sync()

if __name__ == "__main__":
    load_dotenv()
    bot.run(os.getenv("TOKEN"))