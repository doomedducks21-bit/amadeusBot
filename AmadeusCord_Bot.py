
from random import Random
import discord
from discord.ext import commands
import discord.permissions
import dotenv
from dotenv import load_dotenv
import logging
import os
import math
import random
from discord import AllowedMentions, Color, Embed
import webserver
webserver.keep_alive()

load_dotenv()
token = os.getenv("DISCORD_TOKEN")
intent = discord.Intents.all()
bot = commands.Bot(command_prefix=";",intents=intent)

@bot.event
async def on_ready():
    await bot.tree.sync()

@bot.hybrid_command(name="ban",description="ban a user")

async def banuser(ctx,user : discord.User):
    await discord.Member.ban(user)
    await ctx.send(f"{user} has been banned from AmadeusCord. One less person for Niven to rape🙄")
@commands.cooldown(1,900,commands.BucketType.user)
@bot.hybrid_command(name="rape",description="Rape a user")
async def rapeuser(ctx,user : discord.Member,):
    rurls = ["https://cdn.discordapp.com/attachments/1468324270525649087/1497758693519917136/image.png?ex=69eeaffb&is=69ed5e7b&hm=b2a8c2d8c653d4b538fdd5daf16a76446613e84bec3fd0710a1737280ee81467&",
             "https://cdn.discordapp.com/attachments/1468324270525649087/1497758718107062393/image.png?ex=69eeb001&is=69ed5e81&hm=8c6c1bd271ce251a8f781ea92c0652bad733d95f14b156093e7a124146e60de1&",
             "https://media.discordapp.net/attachments/1494361267341623346/1497764194655932457/2063441.JPG?ex=69eeb51b&is=69ed639b&hm=127dfd047a166ee76c807e477fd91232124ffcea706021dbdc614a9219ed3b33&=&format=webp&width=1503&height=845",
             "https://cdn.discordapp.com/attachments/1494361267341623346/1497766000362258492/image.png?ex=69eeb6c9&is=69ed6549&hm=d39bcfff0c8cb4af88430db789f8bbc6431948feab835dc16667402fcd107ef4&",
             "https://cdn.discordapp.com/attachments/1494361267341623346/1497766132319260763/image.png?ex=69eeb6e9&is=69ed6569&hm=ed211cfd3d862848357dd67b02a2b10c26101a547edf811d805304e0f05151dc&",
             "https://cdn.discordapp.com/attachments/1468324270525649087/1497769482414985417/Steins3BGate.1024.648722.png?ex=69eeba07&is=69ed6887&hm=64e31ef931e34bed79e06e7ade873801fd408b69ce9c6cc3320745477f019961&"
             "https://cdn.discordapp.com/attachments/1468324270525649087/1497769559715877024/images.png?ex=69eeba1a&is=69ed689a&hm=d9962dad1979faa43691f59b393e9ff4c2a3537576c85e90d997c08379cc5bd7&",
             "https://cdn.discordapp.com/attachments/1468324270525649087/1497770128086138993/9aec868844b6750b2a465f7ab19ea1af.png?ex=69eebaa1&is=69ed6921&hm=36cda024d3414b310eac09305a87c18bf4f6bf3e9c918f0cc624576625af5343&",
             "https://media.discordapp.net/attachments/1494361267341623346/1497767668252409876/20A8F41.JPG?ex=69eeb857&is=69ed66d7&hm=18215beefafefd0febabf66b083e29aee1170c6df0461fd5450495522e6c1a0d&=&format=webp&width=1503&height=845",
             "https://cdn.discordapp.com/attachments/1494361267341623346/1497767735898144809/image.png?ex=69eeb867&is=69ed66e7&hm=146698342fef44431397ba20354e784adc082bae5027bdbb36e0c1e1a9c22204&",
             "https://cdn.discordapp.com/attachments/1468324270525649087/1497770218569728060/sample_b093fdd1c557f53de1b9333f67e036dd.png?ex=69eebab7&is=69ed6937&hm=1be5be4693cf5c9dd9efdd6f068019483d2612d0622f293ecaad10e10e5d1c3d&",
             "https://cdn.discordapp.com/attachments/1468324270525649087/1497770320843767918/sample_d7227183bb6a812571c427d51e6e9d8a.png?ex=69eebacf&is=69ed694f&hm=1700056314349448e414dfb601c699724cbb881b50a2ab69250272df1f292aa7&"
             ]
    embed1 = discord.Embed(title=f"Ring the cuck alarm for Akiho and Niven!!!!",description=f"{ctx.author.mention} RAPED AND ASSAULTED {user.mention}")
    url2 = random.choice(rurls)
    embed1.set_image(url=url2)
    await ctx.send(f"",embed=embed1)
@bot.event
async def on_command_error(ctx,error):
    if isinstance(error,commands.CommandOnCooldown):
        em = Embed(title="plz wait b4 raping again pl0x",description=f"try again in {error.retry_after:.2f}s duhuhu", color=Color.red())
        await ctx.send(embed=em)


bot.run(token=token)
