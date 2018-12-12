import discord
from discord.ext.commands import bot
from discord.ext import commands
import asyncio
import time

Client = discord.Client()
client = commands.Bot(command_prefix="!")

#admin checker
#chat_filter = [""]
#bypass_list = [""]

@client.event
async def on_ready():
    print("Bot is ready !!:)")


#to make it non case sensitive you whats below using the .upper


#Say commands
@client.event
async def on_message(message):
    if message.content.upper().startswith('!SAY'):
        if "" in [role.id for role in message.author.roles]: #for the role do \@ the role and copy paste the ID
            args = message.content.split(" ")
            await client.send_message(message.channel, "%s" % (" ".join(args[1:])))
        else:
            await client.send_message(message.channel, "You do not have permission to access this command")
    if message.content.upper().startswith('!AMIADMIN'):
        if "" in [role.id for role in message.author.roles]: #for the role do \@ the role and copy paste the ID
            await client.send_message(message.channel, "You are an admin")
        else:
            await client.send_message(message.channel, "You are not an admin")


#chat filter
#@client.event
#async def on_message(message):
    #contents = message.content.split(" ")
    #for word in contents:
        #if word.upper() in chat_filter:
            #if not message.author.id in bypass_list:
                #try:
                    #await client.delete_message(message)
                    #await client.send_message(message.channel, " Hey!! Don't say that here!")
                #except discord.errors.NotFound:
                    #return

