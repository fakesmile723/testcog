from redbot.core import commands
from redbot.core.bot import Red
import discord

class VerifyView(discord.ui.View):
    def __init__(self, role_id: int, invoker_id: int) -> None:
        super().__init__()
        self.role_id = role_id
        self.invoker_id = invoker_id

    @discord.ui.button(label="Add Role", style=discord.ButtonStyle.success)
    async def add_role_button(self, button: discord.ui.Button, interaction: discord.Interaction) -> None:
        member = interaction.user
        role = interaction.guild.get_role(self.role_id)
        if role and role not in member.roles:
            await member.add_roles(role)
            await interaction.response.send_message("Role added!", ephemeral=True)
        else:
            await interaction.response.send_message("You already have the role.", ephemeral=True)

    @discord.ui.button(label="Try Again", style=discord.ButtonStyle.secondary)
    async def try_again_button(self, button: discord.ui.Button, interaction: discord.Interaction) -> None:
        await interaction.response.send_message("Please try again.", ephemeral=True)

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        return interaction.user.id == self.invoker_id

class Cog(commands.Cog):
    def __init__(self, bot: Red) -> None:
        self.bot = bot

    @commands.command()
    async def sendbutton(self, ctx: commands.Context) -> None:
        role_id = 959146966858752006  # Modify this with the desired role ID
        invoker_id = ctx.author.id
        embed = discord.Embed(title="Verify using Discord", color=await ctx.embed_color())
        view = VerifyView(role_id, invoker_id)
        view.add_item(discord.ui.Button(style=discord.ButtonStyle.success, label="Verify"))
        await ctx.send(embed=embed, view=view)
