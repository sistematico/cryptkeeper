from discord.ext import commands

class Util(commands.Cog):
    def __init__(self, bot, config):
        self.bot = bot
        self.bot.add_listener(self.on_message, "on_message")

    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        if message.content == '@clear all':
            if message.author.permissions_in(message.channel).manage_messages:
                deleted = await message.channel.purge(limit=100, check=lambda msg: not msg.pinned)
                await message.channel.send('100 mensagens foram apagadas.'.format(deleted))
            elif not message.author.permissions_in(message.channel).manage_messages:
                await message.channel.send("{0.author} você precisa de permissões para apagar as mensagens em massa.".format(message))
            
            return

        await self.bot.process_commands(message)