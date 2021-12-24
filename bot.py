import os

import discord
from discord.ext import commands

import numpy as np

token = "ODU2NDUyNTE5MDA2MTc1MjUz.YNBPkA.nIzChxTbXfXe9JGjqMUA7HCw9HY"

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
        "Tiara",
        "Rezky",
        "Eston Anin",
        "Agus TPJ",
        "Muhammad Akbarul Human",
        "Ayu Lestari",
        "Mahirah Ulfah Abdi",
        "Mulyadi",
        "Lynatu Khoirinnisa",
        "Putri Rahmawati",
        "Ruslandi",
        "Fransiska Yoefi",
        "Farahhati Mumtahana",
        "Ryan Sudrajat P. Putra",
        "Bagas Adicita Rabbani",
        "Baskoro Adi Pratomo",
        "Raihan Mohammad Fikri",
        "Maya Hermawati",
        "Nurlaila, S.Si",
        "Venny Christiani Wahyudi",
        "Siti Sarah",
        "O. Rocky Fernandes",
        "Arkha Ridho",
        "Nauralitha Zayn Aqnia",
        "Hayuning Azaniarti",
        "Tiara Dewi Imas Mahardika",
        "dr. Erda Purnamasari",
        "Salma Dilsani Sabita",
        "Alfina Asha Putri Ramadhani",
        "Asyian Zanil",
        "Atma Dewita",
        "Almira Sifak Fauziah Narariya",
        "Rifqi Rizmanda Abidin",
        "Nanda Ayu Windasari",
        "Reza Nur Wibisono",
        "Kresna Darmawan",
        "Adinda Wulan Anjarwati",
        "Novita Hudyaningtyas",
        "Niken Ayu Febrianti Ratnasari",
        "Majedah Ulfa",
        "Adila Widya Utami",
        "Ira Sidik ",
        "Fenny Nur Handayani",
        "Martinus Luther Langga Gado",
        "Eka Oktowani",
        "Nur Hikmah",
        "Andreas C.H. Louk",
        "Felix K. A. Durto"
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