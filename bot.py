import discord
from discord.ext import commands
from roku import Roku

roku = Roku("Roku_IP")

bot = commands.Bot(command_prefix = '$', status=discord.Status.online, activity=discord.Game('With Roku!'))

@bot.command()
async def home(ctx):
	roku.home()
	await ctx.send('***Command has been sent!***')

@bot.command()
async def stop(ctx):
	await ctx.send('*Stopping* :wave:')
	await bot.logout()

@bot.command()
async def down(ctx):
	roku.down()
	await ctx.send('***Command has been sent!***')

@bot.command()
async def up(ctx):
	roku.up()
	await ctx.send('***Command has been sent!***')

@bot.command()
async def left(ctx):
	roku.left()
	await ctx.send('***Command has been sent!***')

@bot.command()
async def right(ctx):
	roku.right()
	await ctx.send('***Command has been sent!***')

@bot.command()
async def select(ctx):
	roku.select()
	await ctx.send('***Command has been sent!***')

@bot.command()
async def back(ctx):
	roku.back()
	await ctx.send('***Command has been sent!***')

@bot.command()
async def type(ctx, arg):
	await ctx.send(f'***String {arg} has been sent!***')
	roku.literal(arg)

@bot.command()
async def backspace(ctx):
	roku.backspace()
	await ctx.send('***Command has been sent!***')

@bot.event
async def on_ready():
    print('Bot is online!')

bot.run("Roku_IP")