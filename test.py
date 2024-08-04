import os
import random
import discord
from discord.ext import commands

from myserver import server_on

prefix = "!"
intents = discord.Intents.default()
intents.message_content = True



@bot.event
async def on_ready():
    print("The bot is ready!")

@bot.command()
async def randomnumber(ctx):
    random_number = random.randint(1, 100)  # สุ่มหมายเลขระหว่าง 1 ถึง 100
    embed = discord.Embed(title="Random Number", description=f"Your random number is {random_number}", color=0xF85252)
    await ctx.send(embed=embed)

list #NT Token
options_NT = ['★ Scarlet scale', '★ The Emerald shield', '★ The Lighting','★ Perdimirs bones','★ Dagger of Light','★ Lucky coin','★★ Blood stone','★★ Emerald scarub','★★ The Thunderbolt','★★ Perdimirs sting','★★ The Orb','เกลือ']

@bot.command(name='NT')
async def NT(ctx):
    choice = random.choice(options_NT)
    embed = discord.Embed(
        title="Drop",
        description=f"คุณได้รับ: {choice}",
        color=0xF85252
    )
    await ctx.send(embed=embed)

list #DT Token
options_DT = ['★★★ Phoenix tears', '★★★ Prometheus', '★★★ Prometheus','★★★ Vanisher','★★★ Bright stars','เกลือ']

@bot.command(name='DT')
async def DT(ctx):
    choice = random.choice(options_DT)
    embed = discord.Embed(
        title="Drop",
        description=f"คุณได้รับ: {choice}",
        color=0xF85252
    )
    await ctx.send(embed=embed)

server_on()

bot.run(os.getenv('token'))