import discord
from discord.ext import commands
import os

intents = discord.Intents.all()

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} ist ready!")
    await bot.load_extension("cogs.activity")
    await bot.load_extension("cogs.admin")
    await bot.load_extension("cogs.buttons")
    await bot.load_extension("cogs.cooldown")
    await bot.tree.sync()

bot.run("MTE3ODA4NTU2ODQ4ODQxNTI3Mg.GpInVk.Zu5tF6Hmlh7ygNA31Xb1rkgNWcbLlf3m-X1KQw")