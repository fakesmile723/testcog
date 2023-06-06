from .cog import Cog


async def setup(bot):
    await bot.add_cog(Cog(bot))