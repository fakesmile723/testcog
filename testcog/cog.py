from redbot.core import commands
from redbot.core.bot import Red
import discord

class View(discord.ui.View):
    def __init__(self) -> None:
        super().__init__(timeout=180)  # seconds
        self._message: discord.Message = None

    async def on_timeout(self) -> None:
        if self._message is not None:
            self.click_here_button.disabled = True
            try:
                await self._message.edit(view=self)
            except discord.HTTPException:
                pass

    @discord.ui.button(label="Click here.", style=discord.ButtonStyle.success)
    async def click_here_button(self, interaction: discord.Interaction, button: discord.ui.Button) -> None:
        await interaction.response.send_message("You clicked on the button.", ephemeral=True)

class Cog(commands.Cog):
    def __init__(self, bot: Red) -> None:
        self.bot = bot

    @commands.command()
    async def sendbutton(self, ctx: commands.Context) -> None:
        embed: discord.Embed = discord.Embed(title="Click on the button below.", color=await ctx.embed_color())
        view = View()
        view._message = await ctx.send(embed=embed, view=view)
