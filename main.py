print("I am alive master")
import discum
from unittest import async_case
import ffmpeg
from discord import Member
import requests
from requests.structures import CaseInsensitiveDict

import requests

def handler(pd: "pipedream"):
  r = requests.get('https://pokeapi.co/api/v2/pokemon/charizard')
  # Export the data for use in future steps
  return r.json()
  
def handler(pd: "pipedream"):
  # Reference data from previous steps
  print(pd.steps["trigger"]["context"]["id"])
  # Return data for use in future steps
  return {"foo": {"test":True}}


def handler(pd: "pipedream"):
  headers = {"Authorization": f'Bot {pd.inputs["discord_bot"]["$auth"]["bot_token"]}'}
  r = requests.get('https://discord.com/api/users/@me', headers=headers)
  # Export the data for use in future steps
  return r.json()


from discord.ext.commands import has_permissions
from async_timeout import timeout
import pytz
from datetime import datetime
import hikari
import os
import DiscordEconomy
import time 
import tracemalloc


from discord.ext import commands
from unittest import async_case
import ffmpeg
from discord import Member
from discord.ext.commands import has_permissions
from async_timeout import timeout
import pytz
import hikari
import os
import DiscordEconomy

import tracemalloc
import discord
from discord.ext import commands

import discord
from discord.ext import commands
from random import randint
from discord import FFmpegPCMAudio
import discord
from random import randint
from discord import FFmpegPCMAudio


from youtube_search import YoutubeSearch




import discord


{"intents": [
        {"tag": "greeting",
         "patterns": ["Hi", "How are you", "Is anyone there?", "Hello", "Hey","Good day", "Whats up"],
         "responses": ["Hello!", "Good to see you again!", "Hi there, how can I help?"],
         "context_set": ""
        },
        {"tag": "goodbye",
         "patterns": ["cya", "See you later", "Goodbye", "I am Leaving", "Have a Good day","bye"],
         "responses": ["Sad to see you go..", "Talk to you later", "Goodbye!"],
         "context_set": ""
        }
         
   ]
}
import aiohttp
from youtube_dl import YoutubeDL
import os



import discord
from discord.ext import tasks, commands
import random
import json
from discord import FFmpegPCMAudio


import youtube_dl

import requests

def handler(pd: "pipedream"):
  headers = {"Authorization": f'Bot {pd.inputs["discord_bot"]["$auth"]["bot_token"]}'}
  r = requests.get('https://discord.com/api/users/@me', headers=headers)
  # Export the data for use in future steps
  return r.json()

def handler(pd: "pipedream"):
  # Reference data from previous steps
  print(pd.steps["trigger"]["context"]["id"])
  # Return data for use in future steps
  return {"foo": {"test":True}}

def handler(pd: "pipedream"):
  # Reference data from previous steps
  print(pd.steps["trigger"]["context"]["id"])
  # Return data for use in future steps
  return {"foo": {"test":True}}







               
import asyncio
#import DiscordUtils




intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
intents=discord.Intents.all()
intents = discord.Intents.default()
intents.message_content = True
from pretty_help import PrettyHelp


intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True


token = os.environ['token']


# Import the command handler

# Run the bot
# Note that this is blocking meaning no code after this line will run
# until the bot is shut off
  
client = commands.Bot(command_prefix=',',intents=intents)

import functools
import typing
import asyncio


_afk = []  

bot_fox = commands.Bot(command_prefix=',', intents = intents,help_command=PrettyHelp( no_category = 'test commands', description = "i am learning code with some of these commands"))




@bot_fox.command()
async def test(ctx):
   embed=discord.Embed(title="Incense Ping", description="Recive ping when we launch a incense in <#1054884994910265385>  ")
   embed.set_image(url="https://c4.wallpaperflare.com/wallpaper/927/247/737/pokemon-nature-pikachu-charmander-wallpaper-preview.jpg")
  
   await ctx.send(embed=embed)
  
@bot_fox.command()
async def s(ctx,red:str):
    embed = discord.Embed()

    async with aiohttp.ClientSession() as cs:
        async with cs.get(f'https://www.reddit.com/r/{red}/new.json?sort=hot') as r:
            res = await r.json()
            t = res['data']['children'][random.randint(0, 25)]['data']['url']
            embed.set_image(url=t)
            await ctx.send(embed=embed, delete_after=35)
            print(t)

async def run(ctx, arg1):
  ctx.send(os.system(arg1))


queue = []

YDL_OPTIONS = {
            "format" : "bestaudio",
            "postprocessors" : [{
                "key" : "FFmpegExtractAudio",
                "preferredcodec" : "mp3",
                "preferredquality" : "192",
            }], "noplaylist" : "True"
        }

FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}



@bot_fox.event
async def on_message_edit(before, after):
    if before.content != after.content:
      await bot_fox.process_commands(after)



@bot_fox.command()
async def r(ctx,*,searchTerm:  str=("cute ")):  
    apikey = "AIzaSyBkfUt38tc34U7-mIDAr88j6Iwxn3k7lig"
    ckey = "AIzaSyBkfUt38tc34U7-mIDAr88j6Iwxn3k7lig"
    lmt= 1
    
    r = requests.get("https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" % (searchTerm, apikey, ckey,  lmt))

    if r.status_code == 200:
     

     top_8gifs = json.loads(r.content)["results"][0]['url']
        
 
     await ctx.channel.purge(limit=1)
     embed = discord.Embed(color=0xffffff)
     print(top_8gifs)


     embed.set_image(url=top_8gifs)
     await  asyncio.sleep(0.4)
     await ctx.send(top_8gifs, delete_after=60)

     search_term = "excited"
     apikey2 = "AIzaSyD4V5U_VVOQ9pOMsDYODmtQUERpgDneNp0"

     r2 = requests.get(
    "https://g.tenor.com/v1/random?q=%s&key=%s&limit=%s" % (search_term, apikey2, lmt))

     if r.status_code == 200:
        gifs = json.loads(r2.content)
        print(gifs)
     else:
        print(gifs)

        gifs = None


import aiohttp

@bot_fox.command(pass_context=True)
async def gg(ctx, *, search):
    embed = discord.Embed(colour=discord.Colour.blue())
    session = aiohttp.ClientSession()

    if search == '':
        response = await session.get('https://api.giphy.com/v1/gifs/random?api_key=ICQxdYi29ul8p8uKkIFjrLzj17fr1zBx')
        data = json.loads(await response.text())
        embed.set_image(url=data['data']['images']['original']['url'])
    else:
        search.replace(' ', '+')
        response = await session.get('http://api.giphy.com/v1/gifs/search?q=' + search + '&api_key=ICQxdYi29ul8p8uKkIFjrLzj17fr1zBx&limit=10')
        data = json.loads(await response.text())
        gif_choice = random.randint(0, 9)
        x =str(data['data'][gif_choice]['images']['original']['url'])
        embed.set_image(url=x)

    await session.close()

    await ctx.send(x)
    await bot_fox.send_message(embed=embed)
    


@bot_fox.command(description="Pokemon research")
async def rp(ctx,ranpoke=None):

  url = "https://pokeapi.co/api/v2/pokemon/"
  x= url
  if ranpoke == None:
    ranpoke = randint(1,905)

  r = requests.get(f'{x}{ranpoke}')


  packages_json = r.json()
  packages_json.keys

  napo = packages_json["name"]
  napo3 = packages_json["id"]

  #e =requests.get(f'https://pokeapi.co/api/v2/characteristic/{napo3}/')
  #_json = r.json()
  #_json.keys

  
  napo4 = packages_json["types"][0]["type"]
  napo2 =  packages_json["moves"][0]["move"]

  

  embed = discord.Embed()
  embed.set_thumbnail(url = f"https://play.pokemonshowdown.com/sprites/ani/{napo}.gif")
  embed.add_field(name="Pokemon: ",   value = f" {napo.capitalize()} (#{napo3})"   , inline=False)
  embed.add_field(name="Pokemon Type: ", value=napo4   , inline=True)
  embed.add_field(name="Moves: ", value=napo2   , inline=False)

  await ctx.send(embed = embed)


@bot_fox.command()
@commands.has_permissions(manage_roles=True)
async def ar(ctx, *,role):
   guild = ctx.guild
   await ctx.send(f"Alright {ctx.message.author} I just created a role called **{role}** For you")
   await guild.create_role(name=role)


@ar.error

async def ar_error(ctx, error):
    if isinstance(error, MissingPermissions):
        text = "Sorry {}, you do not have permissions to add roles ".format(ctx.message.author)
        await ctx.send(text)


import typing
import discord


@bot_fox.command()
@commands.has_permissions(manage_channels=True)
async def lock(ctx, channel : discord.TextChannel=None):
    channel = channel or ctx.channel
    overwrite = channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = False
    await ctx.send(f'{ctx.author.mention} has locked {channel.mention}, {channel.mention} is now :lock: ')
    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)

@bot_fox.command()
@commands.has_permissions(manage_channels=True)
async def unlock(ctx, channel : discord.TextChannel=None):
    channel = channel or ctx.channel
    overwrite = channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = True
    await ctx.send(f'{ctx.author.mention} has unlocked {channel.mention}, {channel.mention} is now :unlock:')
    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)

@lock.error
async def lock_error(ctx, error):
    if isinstance(error, MissingPermissions):
        text = "Sorry {}, you do not have permissions to lock channels".format(ctx.message.author)
        await ctx.send(text)
      




import discord
from discord.ext import commands

@bot_fox.command()
async def help_fox(ctx, args=None):
    help_embed = discord.Embed(title="My Bot's Help!")
    command_names_list = [x.name for x in bot_fox.commands]

    help_embed.set_thumbnail(url=bot_fox.user.avatar.url)

    # If there are no arguments, just list the commands:
    if not args:
        help_embed.add_field(
            name="List of supported commands:",
            value="\n".join([str(i+1)+". "+x.name for i,x in enumerate(bot_fox.commands)]),
            inline=False
        )
        help_embed.add_field(
            name="Details",
            value="Type `,help <command name>` for more details about each command.",
            inline=False
        )

    # If the argument is a command, get the help text from that command:
    elif args in command_names_list:
        help_embed.add_field(
            name=args,
            value=bot_fox.get_command(args).help
        )

    # If someone is just trolling:
    else:
        help_embed.add_field(
            name="Nope.",
            value="Don't think I got that command, boss!"
        )

    await ctx.send(embed=help_embed)



          
import discord
from discord.ext import commands


tracemalloc.start()

import tracemalloc

tracemalloc.start()
@bot_fox.command()
@commands.cooldown(1, 1, commands.BucketType.user)

async def hug(ctx, *, user: discord.Member = None):
    with open("hug.txt", "r") as file:
        allText = file.read()
        words = list(map(str, allText.split()))   
        x = random.choice(words)

    if user == bot_fox.user: 
       msg =  await ctx.send(f'Aww, "Thank You!"  {ctx.author.mention}')
       emoji='😄'      
       await ctx.message.add_reaction(msg,emoji)  #:pokelove:1055822955084513303


    elif user:
       embed = discord.Embed(title=f"Hugs {user}",description=f" {user} You've just been hugged by {ctx.author}", color=0xffffff)

       embed.set_image(url=x)
       await ctx.send(embed=embed)




  

    else:
        await ctx.send("if you wanna hug anyone just do:`,hug <@mention.user>`")






@bot_fox.command()
async def kill(ctx, *, member: discord.Member = None):
    with open("kill.txt", "r") as file:
        allText = file.read()
        words = list(map(str, allText.split()))   
        x = random.choice(words)

    if member == bot_fox.user:
                 await ctx.reply("..." , delete_after=40)

  
    elif member:

      embed = discord.Embed(title=f"Kills {member}",color=0xffffff)

      embed.set_image(url=x)
      await ctx.send(embed=embed)

    else:
        await ctx.send("command is missing. ,kill `[@mention_member]`")













@bot_fox.command()
async def info(ctx,*, member: discord.Member = None):
  embed=discord.Embed()

  if member == None:
       
          

          
         author = ctx.author # we get the member object
         top_role = author.roles[-1] 
         color = author.color
         
         joined = ctx.author.joined_at.strftime("%b %d, %Y, %I:%M %p")
         registered =  ctx.author.created_at.strftime("%b %d, %Y, %I:%M %p")

      
         embed.set_image(url=str(ctx.author.display_avatar.url))

         embed.set_author(name=ctx.author, icon_url=ctx.author.avatar.url)    

         embed.add_field(name="    Your Information    ", value="",  inline=False)
         embed.add_field(name="`_Registered_`", value= f"||{registered}||", inline=False)
         embed.add_field(name="`_Joined_`", value=f"||{joined}||", inline=False)

         embed.add_field(name="__User Status__", value="", inline=False)
    
         embed.add_field(name=f"`_Roles_ [{len([role.mention for role in ctx.author.roles [1:]])}]`",value=f"{' '+' , '.join ([role.mention for role in ctx.author.roles [1:]])}",inline=False)
         embed.add_field(name="`_Top Role_`:", value=f"||{top_role.mention} ||")
    


    
  elif member:
     
         if member.status == discord.Status.online :
             x = "Online :online:"
         if member.status == discord.Status.idle :
             x = "Idle :idle: "
         if member.status == discord.Status.dnd :
             x = "Do Not Disturb :dnd: "
          
         author = member # we get the member object
         top_role = member.roles[-1] 
         color = author.color
         perms_string = "      "
         for perm, true_false in top_role.permissions:
            if true_false is True:
                perms_string += f"[{perm.capitalize().replace('_', ' ').capitalize()}]   "

         
         joined = member.joined_at.strftime("%b %d, %Y, %I:%M %p")
         registered =  member.created_at.strftime("%b %d, %Y, %I:%M %p")
    
         embed.set_image(url=str(member.display_avatar.url))

         embed.set_author(name=ctx.author, icon_url=ctx.author.avatar.url)    

         embed.add_field(name=f" {member.name}'s Information    ", value="",  inline=False)
    

         embed.add_field(name="`_Registered_`", value= f"||{registered}||", inline=False)
         embed.add_field(name="`_Joined_`", value=f"||{joined}||", inline=False)

         embed.add_field(name="__User Status__", value="", inline=False)
         
        
         embed.add_field(name=f"`Roles [{len([role.mention for role in member.roles [1:]])}]`",value=f"{' '+', '.join ([role.mention for role in member.roles [1:]])}",inline=False)
    
         embed.add_field(name="`_Top Role_`:", value=f"||{top_role.mention} ||")

         embed.add_field(name="__Key Permissions__",value =f"{perms_string}" , inline=False)

  elif member == bot_fox.user:
         author = member # we get the member object
         top_role = member.roles[-1] 
         perms_string = "      "
         for perm, true_false in top_role.permissions:
            if true_false is True:
                perms_string += f"[{perm.capitalize().replace('_', ' ').capitalize()}] "

         
         joined = member.joined_at.strftime("%b %d, %Y, %I:%M %p")
         registered =  member.created_at.strftime("%b %d, %Y, %I:%M %p")
    
         embed.set_image(url=str(member.display_avatar.url))

         embed.set_author(name=ctx.author, icon_url=ctx.author.avatar.url)    

         embed.add_field(name="My Information", value="",  inline=False)
    

         embed.add_field(name="`_Registered_`", value= f"||{registered}||", inline=False)
         embed.add_field(name="`_Joined_`", value=f"||{joined}||", inline=False)

         embed.add_field(name="__User Status__", value="", inline=False)
         embed.add_field(name=f"`Roles [{len([role.mention for role in member.roles [1:]])}]`",value=f"{' '+', '.join ([role.mention for role in member.roles [1:]])}",inline=False)
    
         embed.add_field(name="`_Top Role_`:", value=f"||{top_role.mention} ||")

         embed.add_field(name="__Key Permissions__",value =f"{perms_string}" , inline=False)

  

    



  
  await ctx.send(embed=embed, delete_after=90)

@info.error
async def info_error(ctx,error):
     await ctx.send(f"The user info command is `,info` or `,info <@mention.user>`. For example: ,info <@1029944463059075162>. || {error} ||")
    
  
@bot_fox.command(name="ping", help="see ping")
async def ping(ctx):
        message = await ctx.send("Pong!")
        embed = discord.Embed()
        embed.add_field(name=":ping_pong:", value=f"{(bot_fox.latency*1000).round}")
        await message.delete()
        await message.edit(content=embed)



@bot_fox.command()
async def stop_cd(ctx):
  while True:
    break

t=True
@bot_fox.command(pass_context=True, description=',cd [any number between 1-150]')
@commands.cooldown(1, 550, commands.BucketType.user)
async def cd(ctx, time: int):
    with open("cela.txt", "r") as file:
      allText = file.read()
      words = list(map(str, allText.split()))   
      x = random.choice(words)

      while time > 150:
        await ctx.send("https://media.discordapp.net/attachments/1048796812531728404/1049042029184831509/cute-fox-is-bored-illustration-vector_617647-8.png?width=120&height=100")
        await ctx.reply("Bruh [the limit is 150]")
        await asyncio.run(stop())
        break

        #error point
        while time < 100 and a ==1:
          async with ctx.typing():
            await ctx.send("Loading ...", delete_after=4.9)
            await asyncio.sleep(3)
            await ctx.send(f"Counting down from {time} ", delete_after=5.9)
        #end off error forever loop
      async with ctx.typing():
            embed = discord.Embed()
            embed.add_field(name="Time", value=time)

            await ctx.send(f"{ctx.author.mention} used ,cd",delete_after=4.9)
            await asyncio.sleep(3)

            await ctx.send(f"Counting down from {time} ")
      while time > 0:
        time-= 1        # Sleep for 1 second
        await asyncio.sleep(1)
        embed = discord.Embed()
        embed.add_field(name="Time:",value=time)
        message = await ctx.send(embed = embed)

        await message.edit(embed=embed, delete_after=time)

      await ctx.send(f"Countdown has completed")
      await ctx.reply(f"{x}")

  



def stop():
  pass


@bot_fox.event
async def on_command_error(ctx , error):

  if isinstance(error, commands.CommandOnCooldown):
          reactions = '⌛'
          await ctx.send(f"sorry please try again , after:  **`{round(error.retry_after)}`** seconds", delete_after=10)
          await ctx.message.add_reaction(reactions)



#delete if 


# Say hi Functoin
collection = []

# Say hi Functoin
collection = []

# python
import json

@bot_fox.command(name="hi",description='Yay you made it, this is for starters',aliases=['hello', 'hey','sup','hoi','yo'])
@commands.cooldown(3, 1, commands.BucketType.user)
async def hi(ctx,*,user: discord.Member = None):

  with open("hello.txt", "r") as file:
    allText = file.read()
    words = list(map(str, allText.split()))
    x = random.choice(words)


  if user == bot_fox.user: 
     
       await ctx.send("Hello to me  awww cute")

  elif user == ctx.message.author: 

       await ctx.send(f"...hello {ctx.message.author.mention}")


  
  elif user:
      await ctx.send(f"{ctx.message.author.mention} greets  || {user.mention} ||")
      embed = discord.Embed(title=f"Greets  || {user} || ")
      embed.set_author(name=f"{ctx.message.author}", icon_url=ctx.author.avatar.url)

      embed.set_image(url=x)
      await ctx.send(embed=embed)
  else:
      await ctx.send(f"Hello {ctx.message.author.mention}", )
      embed = discord.Embed(title=f"Hello {ctx.message.author} ")
      embed.set_author(name=f"{ctx.message.author}", icon_url=ctx.author.avatar.url)

      embed.set_image(url=x)
      
    

      await ctx.send(embed=embed)

      return
      pass





#but if you want to make the bot change status every 5 minutes try this :



status1=[
  discord.Status.dnd,
  discord.Status.idle,
  discord.Status.online
]



@bot_fox.event
async def on_ready():
  with open("online.txt", "r") as file:
        allText = file.read()
        words = list(map(str, allText.splitlines()))   
        e = random.choice(words)
        y=random.choice(status1)
  print("---------------------------------------------")
  print(f"Discord bot : {bot_fox.user}")
  print("Has successfully logged in = True")
  print(f"Current status: discord.status.{y}")
  print("---------------------------------------------")

  print(f"Welcome : {bot_fox.user}")
  print("---------------------------------------------")
  time.sleep(2)

  print("-------------------------")

  with open("alive.txt", "r") as file:
    allText = file.read()
    words = list(map(str, allText.splitlines()))   
    x = random.choice(words)
  with open("bot_status.txt", "r") as file:
    allText = file.read()
    words = list(map(str, allText.splitlines()))   
    s = random.choice(words)
    for guild in bot_fox.guilds:
        for channel in guild.text_channels :
            if str(channel) == "002-🦊test":
                await channel.purge()#deletes all messages
             
        print("=============")

        print('Active in {}\n Member Count {}'.format(guild.name,guild.member_count))

        time.sleep(0.5)

    my_time =  pytz.timezone("America/Indiana/Indianapolis")
    currentDateAndTime = datetime.now(my_time)
  

    currentTime = currentDateAndTime.strftime("%I:%M")

    
  await bot_fox.change_presence(status=y)
  await bot_fox.change_presence(status=y,activity=discord.Activity(type=discord.ActivityType.watching, name =f'{s} {" since"} {currentTime}'))
  print("-------------------------")
  print("Enjoy coding")
  print("-------------------------")

  print("--------------- -> INFO <- ------------------")
  print(f"Discord bot : {bot_fox.user}")
  print("Has successfully logged in = True")
  print(f"Current status: discord.status.{y}")
  print("---------------------------------------------")

  print(f"Welcome : {bot_fox.user}")
  print("---------------------------------------------")

  
  if y == discord.Status.idle:
    print("idle status updated")
    
    await bot_fox.change_presence(status=y,activity=discord.Activity(type=discord.ActivityType.listening, name =",help"))
  else:
      print("idle status is not true")
      for guild in bot_fox.guilds:
         
       await bot_fox.change_presence(status=y,activity=discord.Activity(type=discord.ActivityType.watching, name =f"over {len(bot_fox.guilds)} servers."))

@tasks.loop(seconds = 10) # repeat after every 10 seconds
async def change():
      info=[
        discord.ActivityType.playing,
        discord.ActiviyType.watching,
        discord.ActivityType.listening
      ]
      name=[
         "Foxy games"
         f"over {len(bot_fox.guilds)} servers."
         ",help :fox:"
       ]

      k = random.choice(info)
      if x == discord.ActivityType.playing:
         await bot_fox.change_presence(status=y,activity=discord.Activiy(type=k,name= "Foxy games"))


# import the time module
import time




@bot_fox.command()
@commands.cooldown(1, 45, commands.BucketType.user)

async def now(ctx):
   user_timezone = ()

   timezone = pytz.timezone(user_timezone)

   user_time = datetime.now(timezone)

   currentDateAndTime = datetime.now(user_time)
   currentTime = currentDateAndTime.strftime("%I:%M %p")
   embed = discord.Embed(title=f"Time in Indiana: {currentTime}")
   with open("time.txt", "r") as file:
    allText = file.read()
    words = list(map(str, allText.splitlines()))   
    t = random.choice(words)
   with open("time-am.txt", "r") as file:
    allText = file.read()
    words = list(map(str, allText.splitlines()))   
    g = random.choice(words)
  

   if currentDateAndTime.strftime("%p") == str("PM"):
     embed.set_image(url=t)


   else:
     embed.set_image(url=g)


   await ctx.reply(embed=embed, delete_after=40)

import os

#db = sqlite3.connect('poke2auto.db')
#cur = db.cursor()
import discord
from discord.ext import commands
from discord.ext import tasks

token = os.environ['token']





global x
x = "[AFK] "

#AFK

import yt_dlp

#say
import tracemalloc

tracemalloc.start()



print("music file is activated")


@bot_fox.event
async def on_message(message):
    if " " in message.content:
       message.replace(" ", '_')

      



youtube_dl.utils.bug_reports_message = lambda: ''

yt_dlp_opts = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0',  # bind to ipv4 since ipv6 addresses cause issues sometimes
}

ffmpeg_options = {
    'options': '-vn',
}
import discord
from discord.ext import commands
import random
import asyncio
import sys
import youtube_dl
from youtube_dl import YoutubeDL

# Suppress noise about console usage from errors
youtube_dl.utils.bug_reports_message = lambda: ''

ytdlopts = {
    'format': 'bestaudio/best',
    'outtmpl': 'downloads/%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0' , # ipv6 addresses cause issues sometimes
    
}

ffmpegopts = {
    'before_options': '-nostdin',
    'options': '-vn'
}

ytdl = YoutubeDL(ytdlopts)


class VoiceConnectionError(commands.CommandError):
    """Custom Exception class for connection errors."""


class InvalidVoiceChannel(VoiceConnectionError):
    """Exception for cases of invalid Voice Channels."""


class YTDLSource(discord.PCMVolumeTransformer):

    def __init__(self, source, *, data, requester):
        super().__init__(source)
        self.requester = requester

        self.title = data.get('title')
        self.web_url = data.get('webpage_url')
        self.duration = data.get('duration')

        # YTDL info dicts (data) have other useful information you might want
        # https://github.com/rg3/youtube-dl/blob/master/README.md

    def __getitem__(self, item: str):
        """Allows us to access attributes similar to a dict.
        This is only useful when you are NOT downloading.
        """
        return self.__getattribute__(item)

    @classmethod
    async def create_source(cls, ctx, search: str, *, loop, download=False):
        loop = loop or asyncio.get_event_loop()

        to_run = partial(ytdl.extract_info, url=search, download=download)
        data = await loop.run_in_executor(None, to_run)

        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]

        embed = discord.Embed(title="", description=f"Queued [{data['title']}]({data['webpage_url']}) [{ctx.author.mention}]", color=discord.Color.green())
        await ctx.send(embed=embed)

        if download:
            source = ytdl.prepare_filename(data)
        else:
            return {'webpage_url': data['webpage_url'], 'requester': ctx.author, 'title': data['title']}

        return cls(discord.FFmpegPCMAudio(source), data=data, requester=ctx.author)

    @classmethod
    async def regather_stream(cls, data, *, loop):
        """Used for preparing a stream, instead of downloading.
        Since Youtube Streaming links expire."""
        loop = loop or asyncio.get_event_loop()
        requester = data['requester']

        to_run = partial(ytdl.extract_info, url=data['webpage_url'], download=False)
        data = await loop.run_in_executor(None, to_run)

        return cls(discord.FFmpegPCMAudio(data['url']), data=data, requester=requester)


import discord
import youtube_dl

from discord.ext import commands


#=============== MUSIC









@bot_fox.command()
@has_permissions(administrator=True, ban_members=True)

async def c(ctx):
  await ctx.channel.purge()#deletes all messages



@c.error
async def ar_error(ctx, error):
    if isinstance(error, MissingPermissions):
        text = "Sorry {}, you do not have permissions to purge ".format(ctx.message.author)
        await ctx.send(text)
      
print(f"{bot_fox.user} is attempting to get online" )



@bot_fox.event  
async def on_message(msg):
    await bot_fox.process_commands(msg)

from discord.ext import commands

from discord.ext.commands import has_permissions, MissingPermissions




youtube_dl.utils.bug_reports_message = lambda: ''
ytdl_format_options = {
    'format': 'bestaudio/best',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0' # bind to ipv4 since ipv6 addresses cause issues sometimes
}
ffmpeg_options = {
    'options': '-vn'
}
ytdl = youtube_dl.YoutubeDL(ytdl_format_options)
class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)
        self.data = data
        self.title = data.get('title')
        self.url = ""

import discord
from discord.ext import commands
import youtube_dl
import asyncio
import discord
from discord.ext import commands
import youtube_dl




class music(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def join(self,ctx):
        if ctx.author.voice is None:
            await ctx.send("You're not in a voice channel!")
        voice_channel = ctx.author.voice.channel
        if ctx.voice_client is None:
            await voice_channel.connect()
        else:
            await voice_channel.connect()

            await ctx.voice_client.move_to(voice_channel)

    @commands.command()
    async def disconnect(self,ctx):
        await ctx.voice_client.disconnect()

    @commands.command()
    async def play(self,ctx,url):
        ctx.voice_client.stop()
        FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
        YDL_OPTIONS = {'format':"bestaudio"}
        vc = ctx.voice_client

        with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydlp:
          
            info = YoutubeSearch.extract_info(url, download=False)
            url2 = info['formats'][0]['url']
            source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
            if not vc:
                      await ctx.invoke(self.connect_)

                      player = self.get_player(ctx)


            source = await YTDLSource.create_source(ctx, url, loop=self.bot_fox.loop, download=False)

            await vc.play(source, after=lambda _: ctx.send('Done'))
            await ctx.reply(f"Now playing {url}") 
    
    @commands.command()
    async def pause(self,ctx):
        await ctx.voice_client.pause()
        await ctx.channel.send("Paused ⏸")
    
    @commands.command()
    async def resume(self,ctx):
        await ctx.voice_client.resume()
        await ctx.channel.send("resume ⏯")




class special(commands.Cog):
  def __init__(self, bot_fox):
        self.bot_fox = bot_fox

  @commands.has_permissions(manage_channels=True)
  async def lock(ctx, channel : discord.TextChannel=None):
    channel = channel or ctx.channel
    overwrite = channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = False
    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    await ctx.send('Channel locked.')



from discord import FFmpegOpusAudio
import youtube_dl
from discord import FFmpegPCMAudio

from discord.ext import commands

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}   


youtube_dl.utils.bug_reports_message = lambda: ''
ytdl_format_options = {
    'format': 'bestaudio/best',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0' # bind to ipv4 since ipv6 addresses cause issues sometimes
}
ffmpeg_options = {
    'options': '-vn'
}
ytdl = youtube_dl.YoutubeDL(ytdl_format_options)
class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)
        self.data = data
        self.title = data.get('title')
        self.url = ""
      
    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))
        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]
        filename = data['title'] if stream else ytdl.prepare_filename(data)
        return filename

import pafy
from youtubesearchpython import SearchVideos
from yt_dlp import YoutubeDL

youtube_dl.utils.bug_reports_message = lambda: ''
ytdl_format_options = {
    'format': 'bestaudio/best',
    'restrictfilenames': True,
    'noplaylist': True,
    'extractor_retries': 'auto',
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0' # bind to ipv4 since ipv6 addresses cause issues sometimes
}
ffmpeg_options = {
    'options': '-vn'
}
ytdl = youtube_dl.YoutubeDL(ytdl_format_options)
class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)
        self.data = data
        self.title = data.get('title')
        self.url = ""
    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))
        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]
        filename = data['title'] if stream else ytdl.prepare_filename(data)
        return filename



class music(commands.Cog):
    def __init__(self, bot_fox):
        self.bot_fox = bot_fox




  
    @commands.command()
    async def play(self,ctx,*,url:str, loop=None, stream=False):
     
        await ctx.send("please wait")
      
        search = SearchVideos(url, offset = 1, mode = "json", max_results = 3)
        r = search.result()
        res = json.loads(r)
        res1 = res['search_result']
        res2 = res1[0]
        res_fin = res2['link']
        FFMPEG_OPTIONS = {
          'options': '-vn',
          "before_options": "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5"
}
        YDL_OPTIONS = {'format':"bestaudio"}
        vc = ctx.voice_client

        await ctx.reply(f"**Now Playing:** {res_fin} ")
        ctx.voice_client.stop()

        with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:

            info = ydl.extract_info(res_fin, download=False)
            url2 = info['format'][0]['url']
            source = await discord.FFmpegOpusAudio.from_probe(url2,**FFMPEG_OPTIONS),
        vc.play(source)
        await ctx.reply(f"**Now Playing:** {res_fin} ")
        video_list = []

        with youtube_dl.YoutubeDL() as ydl:
            playlist = ydl.extract_info(url=res_fin, download=False)['entries']
        for video in playlist:
           video_list.append(video['webpage_url'])
        vc.play(source)

    @play.error
    async def play_error(self, ctx, error):
     if ctx.voice_client == ctx.message.author:
       await ctx.send(f"Here is the problem: {error} ")



def is_connected(ctx):
    voice_client = get(ctx.bot.voice_clients, guild=ctx.guild)
    return voice_client and voice_client.is_connected()
   
    @commands.command()
    async def pause(self,ctx):
        await ctx.voice_client.pause()
        await ctx.channel.send("Paused ⏸")
    
    @commands.command()
    async def resume(self,ctx):
        await ctx.voice_client.resume()
        await ctx.channel.send("resume ⏯")




class afk(commands.Cog):
  def __init__(self,bot_fox):
    bot_fox.self = bot_fox
    self.data = []

  @commands.command()
  @commands.cooldown(1, 1, commands.BucketType.user)

  async def afk(self, ctx,*, msg : str = None ):
  

    self.data.append(ctx.author.id)
    self.data.append(msg)
    await ctx.send(f"{ctx.author.mention} **I set your AFK to** - AFK: {msg} ",delete_after=15)
    await asyncio.sleep(15)
    await ctx.channel.purge(limit=2)



  @commands.Cog.listener()
  async def on_typing(self,channel,user, when):
  
           if user.id in self.data:
              i = self.data.index(user.id)
              self.data.remove(self.data[i+1])
              self.data.remove(user.id)
              
              await channel.send(f"Welcome back {user.mention}, I removed your AFK!", delete_after=15)
      

    
  @commands.Cog.listener()
  async def on_message(ctx, message):
    for i in range(len(ctx.data)):
      if (f"<@{ctx.data[i]}>" in message.content) and (not message.author.bot):
        await message.channel.send(f"<@{ctx.data[i]}> is currently AFK, reason: {ctx.data[i+1]}",delete_after=15)
        return None
        break





@bot_fox.event
async def on_voice_state_update(member, before, after):
    voice_state = member.guild.voice_client
    if voice_state is not None and len(voice_state.channel.members) == 1:
    # If the bot is connected to a channel and the bot is the only one in the channel
        await voice_state.disconnect() # Disconnect the bot from the channel

@bot_fox.command()
async def stop(context):
          await asyncio.run(stop(context))





@bot_fox.event
async def on_message(message):
      await bot_fox.process_commands(message)

      if "hey foxy" in message.content:
             
           await message.channel.send("hello")
        
           await bot_fox.process_commands(message)
      else:
           pass



@bot_fox.event
async def on_message(message):
       words = ['<@1030285330739363880>']
       user = discord.Member
       if message.author.bot:
        return None
        await bot_fox.process_commands(message)
       
       if message !=  any(map(message.content.__contains__, words)):
           pass
       if any(map(message.content.__contains__, words)):
          await message.channel.send("Master Ping =  <:sharkhug:1054917151892459610> , Dm them bro", delete_after= 30)
          await bot_fox.process_commands(message)

       elif message.author == message.author: 
         
         pass
         await bot_fox.process_commands(message)
         pass


          

@commands.has_role(1085723041222365255)
@bot_fox.command()
async def nick(ctx, member:discord.Member, nick):
           await member.edit(nick=nick)
           await ctx.send(f"Nickname changed to {nick}")


      






#host alive
from keep_alive import keep_alive #keep keep_alive and import toghther





keep_alive()
#---end---
import traceback
import sys
from discord.ext import commands


class CommandErrorHandler(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        """The event triggered when an error is raised while invoking a command.
        Parameters
        ------------
        ctx: commands.Context
            The context used for command invocation.
        error: commands.CommandError
            The Exception raised.
        """

        # This prevents any commands with local handlers being handled here in on_command_error.
        if hasattr(ctx.command, 'on_error'):
            return

        # This prevents any cogs with an overwritten cog_command_error being handled here.
        cog = ctx.cog
        if cog:
            if cog._get_overridden_method(cog.cog_command_error) is not None:
                return

        ignored = (commands.CommandNotFound, )

        # Allows us to check for original exceptions raised and sent to CommandInvokeError.
        # If nothing is found. We keep the exception passed to on_command_error.
        error = getattr(error, 'original', error)

        # Anything in ignored will return and prevent anything happening.
        if isinstance(error, ignored):
            return

        if isinstance(error, commands.DisabledCommand):
            await ctx.send(f'{ctx.command} has been disabled.')

        elif isinstance(error, commands.NoPrivateMessage):
            try:
                await ctx.author.send(f'{ctx.command} can not be used in Private Messages.')
            except discord.HTTPException:
                pass

        # For this error example we check to see where it came from...
        elif isinstance(error, commands.BadArgument):
            if ctx.command.qualified_name == 'tag list':  # Check if the command being invoked is 'tag list'
                await ctx.send('I could not find that member. Please try again.')

        else:
            # All other Errors not returned come here. And we can just print the default TraceBack.
            print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
            traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)

    """Below is an example of a Local Error Handler for our command do_repeat"""

    @commands.command(name='repeat', aliases=['mimic', 'copy'])
    async def do_repeat(self, ctx, *, inp: str):
        """A simple command which repeats your input!
        Parameters
        ------------
        inp: str
            The input you wish to repeat.
        """
        await ctx.send(inp)

    @do_repeat.error
    async def do_repeat_handler(self, ctx, error):
        """A local Error Handler for our command do_repeat.
        This will only listen for errors in do_repeat.
        The global on_command_error will still be invoked after.
        """

        # Check if our required argument inp is missing.
        if isinstance(error, commands.MissingRequiredArgument):
            if error.param.name == 'inp':
                await ctx.send("You forgot to give me input to repeat!")



def is_connected(ctx):
    voice_client = get(ctx.bot.voice_clients, guild=ctx.guild)
    return voice_client and voice_client.is_connected()

@bot_fox.event
async def setup(bot_fox):
   await bot_fox.add_cog(music(bot_fox))
  
   await bot_fox.add_cog(afk(bot_fox))



asyncio.get_event_loop().run_until_complete(setup(bot_fox))




if __name__ == '__main__':
  bot = discum.Client(token= os.environ['token'])
  bot_fox.run(token)
  
def __init__(self):
    loop = asyncio.get_event_loop()
    loop.create_task(self.main())
    loop.run_forever()
  

client.run(token)
#==----
 
