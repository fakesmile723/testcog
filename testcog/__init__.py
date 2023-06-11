from .cog import Pupu


async def setup(bot):
    await bot.add_cog(Pupu(bot))
