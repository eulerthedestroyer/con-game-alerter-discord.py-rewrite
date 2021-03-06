from discord.ext import commands
##events
from events.error import command_error
from events.ready import ready
from events.command import command
from data.config import CONFIG
import sys 
import discord
sys.setrecursionlimit(10**6) 
intents = discord.Intents.default()
intents.members = True
def get_prefix(client, message):
    prefixes = [CONFIG.prefix]# sets the prefixes, u can keep it as an array of only 1 item if you need only one prefix
    return commands.when_mentioned_or(*prefixes)(client, message)    # Allow users to @mention the bot instead of using a prefix when using a command.
async def make_bot():
    bot = commands.Bot(        # Create a new bot                                     
        command_prefix=get_prefix,                              # Set the prefix
        description='A bot used for conflict of nations',                  # Set a description for the bot
        owner_id=464954455029317633,                            # Your unique User ID
        case_insensitive=True,
        intents=intents                                  # Make the commands case insensitive
    )
    def _print(self, message="oof"):
        if self.test:
            return
        print(message)
        if hasattr(self, 'log'):
            self.log+= f'{message}\n'
        else:
            self.log= f'{message}\n'
        self.log  =self.log[:1000]
    bot.test=False
    commands.Bot.print = _print
    # print("ready bot")
    await ready(bot)
    @bot.event
    async def on_command(ctx):
        await command(bot,ctx)
    @bot.event
    async def on_command_error(ctx,error):
        await command_error(bot, ctx, error)
    return bot
