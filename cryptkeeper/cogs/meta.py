import sys
from discord.ext import commands
from datetime import datetime
# sys.path.append("..")
from .. import util

class Meta(commands.Cog):
    """Commands relating to the bot itself."""

    def __init__(self, bot, config):
        self.bot = bot
        self.start_time = datetime.now()
        self.config = config

    @commands.command()
    async def uptime(self, ctx):
        """Tells how long the bot has been running."""
        uptime_seconds = round(
            (datetime.now() - self.start_time).total_seconds())
        await ctx.send(f"Tempo online: {util.format_seconds(uptime_seconds)}")
