from discord.ext import commands
import discord
from asyncio import sleep 
from discord.utils import get
import tracemalloc
client = commands.AutoShardedBot(command_prefix=commands.when_mentioned_or('flame!'), help_comamnd = None)

@client.event
async def on_ready():
    print(f'{client.user} has Awoken!')
    

@client.command()
async def loop(ctx, channel: discord.TextChannel):
    mbed = discord.Embed(
        title = 'Success.',
        color = discord.Color(0xffff),
        description = f"{channel.mention} is now being flamed."
    )
    roleSelect = get(ctx.guild.channels, name = 'role-select')
    mbed2 = discord.Embed(
        title = 'Hello there!',
        color = discord.Color(0xffff),
        description = f'Hello, if youre tired of getting notifications from this channel, go to {roleSelect.mention} and get the No Partnership Ping Role.'
    )
    if ctx.author.guild_permissions.administrator:
        await ctx.send(embed=mbed)
        while True:
            await channel.send(embed=mbed2, delete_after=3600.0)
            await sleep(10800)
            await channel.send(embed=mbed2, delete_after=3600.0)
            await sleep(10800)
            


client.run('NzMyNjU0NTgyMDg5NTE1MDA5.Xw3vwA.1csUvA74TVIT9bxvigUUXsQ5ET4')