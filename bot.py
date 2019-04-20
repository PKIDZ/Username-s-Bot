import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from discord import Game


Client = discord.client
client = commands.Bot(command_prefix = "$", status=discord.Status.online, activity=discord.Game(name="Booting.."))
Clientdiscord = discord.Client()
    
@client.event
async def on_ready():
    print("Ready to go!")
    print(f"Server: {len(client.guilds)} guilds.")
    await client.change_presence(status=discord.Status.online, activity=discord.Game(name="[ $ ]user,clear,BC,ban,ping. BC and user is broken so don't use it."))


@client.command(pass_context=True)
async def BC(ctx, *, message):
    await ctx.message.delete()
    for user in ctx.guild.members:
        try:
            await user.send(message)
            print(f"{user.name} has recieved the message.")
        except:
            print(f"{user.name} has NOT recieved the message.")
    print("Action Completed")

@client.command()
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit=amount)

@client.command()
async def user(ctx, member:discord.User = None):
    if member == None:
        member = ctx.message.author
        pronoun = "Your"
    else:
        pronoun = "Their"
    name = f"{member.name}#{member.discriminator}"
    status = member.status
    joined = member.joinedat
    role = member.toprole
    await ctx.channel.send(f"{pronoun} name is {name}. {pronoun} status is {status}. They joined at {joined}. {pronoun} rank is {role}.")

@client.command()
async def ban(ctx, member:discord.User = None, reason = None):
    if member == None or member == ctx.message.author:
        await ctx.channel.send("Why would you do that? :thinking:")
        return
    if reason == None:
        reason = "No reason at all!"
    message = f"You have been banned from {ctx.guild.name} for {reason}!"
    await member.send(message)
    await ctx.guild.ban(member)
    await ctx.channel.send(f"{member} is banned!")

@client.command()
async def ping(ctx):
    ping = client.latency
    ping = round(ping * 1000)
    await ctx.channel.send(f"My ping is {ping}ms")
    
client.run('NTY2OTYwNTg5NTgzNDE3MzQ0.XLtPpQ.mj52XOJCIl8x9NZPfmpqtoCT2Ns')    
