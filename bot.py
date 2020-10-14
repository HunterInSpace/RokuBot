import discord
from discord.ext import commands
from roku import Roku

roku = Roku(Roku_IP)

bot = commands.Bot(command_prefix = '$')

@bot.command()
async def home(ctx):
	await ctx.send('***Command has been sent!***')
	roku.home()

@bot.command()
async def stop(ctx):
	await ctx.send('*Stopping* :wave:')
	await bot.logout()

@bot.command()
async def down(ctx):
	await ctx.send('***Command has been sent!***')
	roku.down()

@bot.command()
async def up(ctx):
	await ctx.send('***Command has been sent!***')
	roku.up()

@bot.command()
async def left(ctx):
	await ctx.send('***Command has been sent!***')
	roku.left()

@bot.command()
async def right(ctx):
	await ctx.send('***Command has been sent!***')
	roku.right()

@bot.command()
async def select(ctx):
	await ctx.send('***Command has been sent!***')
	roku.select()

@bot.command()
async def back(ctx):
	await ctx.send('***Command has been sent!***')
	roku.back()

@bot.command()
async def type(ctx, arg):
	await ctx.send(f'***String {arg} has been sent!***')
	roku.literal(arg)

@bot.command()
async def backspace(ctx):
	await ctx.send('***Command has been sent!***')
	roku.backspace()

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('With Roku!'))
    print('Bot is online!')

bot.run(Bot_Token)
