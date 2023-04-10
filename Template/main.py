import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

bot = commands.Bot(command_prefix="!", case_intensive=True, intents=discord.Intents.all())
bot.remove_command('help')

@bot.event
async def on_ready():
    print(f'{bot.user.name}')
    print(f'{bot.user.id}')
    print("Online")
    print("-------------")
    await bot.load_extension("cogs.base")

load_dotenv()
bot.run(os.getenv("TOKEN"))