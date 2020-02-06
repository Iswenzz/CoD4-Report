from discord.ext import commands
import asyncio

class ReportCommands(commands.Cog):
    @commands.command()
    @commands.is_owner()
    async def stop(self, ctx):
        await ctx.send("Terminating Report BOT . . .", delete_after=2)
        await asyncio.sleep(3)
        exit(0)
