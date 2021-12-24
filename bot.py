import os

import discord
from discord.ext import commands

import numpy as np

token = <Fill discord token here>

BOT_PREFIX = "$"

# client = commands.Bot(command_prefix = BOT_PREFIX, help_command=None)
bot = commands.Bot(command_prefix = BOT_PREFIX, help_command=None)

# @client.event
@bot.event
async def on_ready():
    print('Bot is online.')

@bot.group(invoke_with_command=True)
async def help(ctx):
    em = discord.Embed(title = "Help", 
    description = "Gunakan $help <perintah> Untuk mendapatkan informasi tambahan terkait suatu perintah.")

    em.add_field(name = "register", value = "Registrasi peserta")
    
    await ctx.send(embed = em)
    
@help.command()
async def register(ctx):
    um = discord.Embed(title = "register", 
    description = 'Perintah untuk registrasi peserta workshop. Gunakan nama yang digunakan pada saat pendaftaran dan dibatasi dengan tanda (").')

    um.add_field(name = "***Syntax***", value = '$register "Gunawan Sutoyo"')
    
    await ctx.send(embed = um)

@bot.command()
async def register(ctx, *args):
    args = np.asarray(args)

    tes_user = [
        "Irfan Imaduddin",
        "John Doe"
        ]

    tes_user = np.asarray(tes_user)

    if args.size == 0:
        pass
    else:
        if args in tes_user:
            user = ctx.message.author
            role = discord.utils.get(ctx.guild.roles, name="Participants")

            response = "Welcome"
            
            for arg in args:
                response = response + " " + arg

            await user.add_roles(role)

            print("{} was added to {}".format(user, role))

            await ctx.channel.send(response)
        else:
            response = "Wrong name"

            await ctx.channel.send(response)


bot.run(token)
