from discord.ext import commands
import random

# made Reply subclass commands.Cog
class Reply(commands.Cog):
    # Cogs must take the Bot and a config dict as arguments,
    # based on the way I have set things up in bot.py
    def __init__(self, bot, config):
        # keep a reference to the Bot object
        self.bot = bot
        # register the on_message function as a listener for the
        # `on_message` event.
        self.bot.add_listener(self.on_message, "on_message")

    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        
        if len(message.attachments) > 0:
            return

        if message.content.startswith('!'):
            return

        if any(x in message.content.lower() for x in ['frase do dia']):
            await ctx.send(f"hello, {ctx.author.name}")
            frase_do_dia = random.choice(list(open('txt/confucio.txt','r')))
            await message.channel.send("{0.author.name} {frase_do_dia}".format(message, frase_do_dia))
            return

        if any(x in message.content.lower() for x in ['oie', 'olá','e aí']):
            saudacao = random.choice(['Olá!', 'Oi, tudo bom?', 'E aí! Blza?'])
            await message.channel.send("{0.author.name} {0.mention} {0.user.name} {saudacao}".format(message))
            return

        # if 'olá' in message.content.lower():
        # if message.content.startswith('hello'):

        # use self.bot instead of self.client
        await self.bot.process_commands(message)