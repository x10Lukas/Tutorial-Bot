import discord
from discord.ext import commands

from easy_pil import Editor, Font, load_image_async

class Welcome(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        background = Editor("img/welcome.png").resize((1920, 790))

        avatar = await load_image_async(member.display_avatar.url)
        circle_avatar = Editor(avatar).resize((568, 568)).circle_image()

        background.paste(circle_avatar, (76, 107))

        big_text = Font.poppins(size=120, variant="bold")

        background.text((813, 390), f"{member.display_name}", color="white", font=big_text, align="left")

        embed = discord.Embed(title=f"**Welcome to** `{member.guild.name}`",
                              description=f"Hey, {member.mention} | {member.display_name},\n"
                                          f"Welcome to the **{member.guild.name}** Discord Server!")
        embed.set_thumbnail(url=f"{member.display_avatar}")
        file = discord.File(fp=background.image_bytes, filename="image.png")
        embed.set_image(url="attachment://image.png")
        channel = self.bot.get_channel(1178082128915861589)
        await channel.send(embed=embed, file=file)

async def setup(bot):
    await bot.add_cog(Welcome(bot))
