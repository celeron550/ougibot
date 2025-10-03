import discord
import random
from random import choice
import time
from discord.ext import commands
from discord.ext.commands import has_permissions
from discord.ext.commands import Cog
import aiohttp
from typing import Optional
import os
from dotenv import load_dotenv
import asyncio
import youtube_dl
import datetime as dt
import re
import enum
import wavelink
import typing as t
from enum import Enum
from anilist import anime as anilist_anime
from anilist import manga as anilist_manga
from anilist import user_profile

load_dotenv()
TOKEN = os.getenv("TOKEN")

intents = discord.Intents.all()
client = commands.Bot(command_prefix='%', intents=intents)

bot_version = '2025.6.16'
danca = False
nyaa = False
psy = False
queue = []




#bot_start
@client.event
async def on_ready():
	await client.change_presence(activity=discord.Activity(
	    type=discord.ActivityType.listening, name="you"))
	print('Hello, World!')
	print(client.user.name)
	

@client.event
async def on_member_join(member : discord.Member):
	await member.send(f"{member.name} https://i.imgur.com/9jzk2Fu.jpeg")

#bot_commands
@client.command()
@commands.has_permissions(manage_messages=True)
async def clean(ctx, qntd):
	await ctx.message.delete()
	await ctx.channel.purge(limit=int(qntd))
	await ctx.send(f"{ctx.author.mention} {qntd} messages has been cleaned")



@client.command()
@commands.has_permissions(manage_channels=True)
async def say(ctx, *, msg):
	await ctx.message.delete()
	await ctx.send(str(msg))


@client.command()
async def esquizo(ctx):
	await ctx.send('https://imgur.com/a/zZe73BY')


@client.command()
async def version(ctx):
	embed = discord.Embed(title=f'my current version is {bot_version}',
	                      color=000000)
	await ctx.send(embed=embed)


@client.command('ougi')
async def ougi(ctx):
	await ctx.send("https://media.discordapp.net/attachments/748731688074346599/822162459971289149/FB_IMG_1616078049740.jpg")


@client.command()
async def run(ctx):
	await ctx.message.delete()
	await ctx.send("<a:PepeRun:754911301259624498>")


@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason="no reason"):
	await ctx.send(member.name +
	               f" has been banned from this server by {ctx.author.mention}"
	               )
	await member.ban(reason=reason)


@client.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, member):
	banned_users = await ctx.guild.bans()
	member_name, member_disc = member.split('#')
	for banned_entry in banned_users:
		user = banned_entry.user
		if (user.name, user.discriminator) == (member_name, member_disc):
			await ctx.guild.unbar(user)
			await ctx.send(member_name + "has been unbanned")
			return
	await ctx.send(member + "wasn't found")


@client.command()
@commands.has_permissions(kick_members=True)
async def mute(ctx, member: discord.Member):
	muted_role = discord.utils.get(ctx.guild.roles, name='mute' or 'muted')
	guild = ctx.guild
	if not muted_role:
		await ctx.send('No mute role has been found. Creating a role...')
		muted_role = await guild.create_role(name='mute')
		for channel in guild.channels:
			await channel.set_permissions(muted_role,
			                              speak=False,
			                              send_messages=False,
			                              read_message_history=True,
			                              read_messages=True)
			await member.add_roles(muted_role)
	await member.add_roles(muted_role)
	await ctx.send(member.mention + " has been muted")


@client.command()
@commands.has_permissions(kick_members=True)
async def unmute(ctx, member: discord.Member):
	muted_role = discord.utils.get(ctx.guild.roles, name='mute')

	await member.remove_roles(muted_role)
	await ctx.send(member.mention + " has been unmuted")


@client.command()
@commands.has_permissions(manage_channels=True)
async def spank(ctx, member: discord.Member):
	muted_role = discord.utils.get(ctx.guild.roles, name='mute')
	await member.add_roles(muted_role)
	await ctx.send(member.mention + " has been spanked!")
	await asyncio.sleep(60)
	await member.remove_roles(muted_role)


@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason="No reason"):
	await member.kick(reason=reason)
	await ctx.send(member.mention +
	               f" has been kicked by {ctx.author.mention}")


@client.command()
async def roll(ctx, s = int()):
	dice = random.randint(1,s+1)
	em = discord.Embed(title='the dice shows:',
	                   description=f'{dice}',
	                   color=ctx.author.color)	
	await ctx.send(embed=em)


@client.command()  #currently not showing previews very well beacause mangadex changed their url
async def manga(ctx, *,name):
	await anilist_manga(ctx,name)

@client.command()
@commands.has_permissions(manage_messages=True)
async def gozei(ctx):
	member=discord.Member
	victim = choice(ctx.guild.members)
	guild = ctx.guild
	gala_role = discord.utils.get(ctx.guild.roles, name='gozado')
	while victim.bot == True:
		victim = choice(ctx.guild.members)
	if not gala_role:
		await ctx.send('Creating a role...')
		gala_role = await guild.create_role(name='gozado', colour=0xFFFFFF)
		for channel in guild.channels:
			await member.add_roles(gala_role)
	await member.add_roles(gala_role)
	if victim.bot == False:
		await ctx.send(f"gozei no {victim.mention}")
		await victim.add_roles(gala_role)
	
@client.command()
@commands.has_permissions(manage_messages=True)
async def limpagala(ctx):
	role = discord.utils.get(ctx.guild.roles, name='gozado')
	membros = list()
	for m in role.members:
		membros.append(m)		
	if len(membros) == 0:
		await ctx.send('Não tem ninguém melado.')
	
	else:
		for m in role.members:
			await m.remove_roles(role)
		await ctx.send('Todo mundo limpinho.')


@client.command()
@commands.has_permissions(kick_members=True)
async def roulette(ctx):
    victim = choice(ctx.guild.members)
    muted_role = discord.utils.get(ctx.guild.roles, name='mute' or 'muted')
    while victim.bot == True:
        victim = choice(ctx.guild.members)
    if victim.bot == False:
        await ctx.send(victim.mention + " the gun shoots at you")
        await victim.add_roles(muted_role)
        await asyncio.sleep(60)  # Aguarda 60 segundos
        await victim.remove_roles(muted_role)


@client.command()
@commands.has_permissions(manage_messages=True)
async def dansa(ctx):
	gif = str(
	    'https://cdn.discordapp.com/attachments/748731688074346599/881543838873845810/emoji.gif'
	)
	msg = str('DANSA GATINHO, DANSA')
	global danca
	danca = True
	await ctx.message.delete()
	while danca == True:
		await ctx.send(msg)
		await ctx.send(gif)



@client.command()
@commands.has_permissions(manage_messages=True)
async def sleep(ctx):
	global nyaa
	global danca
	global psy
	nyaa= False
	danca = False
	psy = False


@client.command()
async def remindme(ctx, task, *, time):
	def convert(time):
		pos = ["s", "m", "h", "d"]

		time_dict = {"s": 1, "m": 60, "h": 3600, "d": 3600 * 24}

		unit = time[-1]

		if unit not in pos:
			return -1
		try:
			val = int(time[:-1])
		except:
			return -2

		return val * time_dict[unit]

	converted_time = convert(time)

	if converted_time == -1:
		await ctx.send("You dind't answer the time correctly")
		return

	if converted_time == -2:
		await ctx.send('The time must be an integer')
		return

	await ctx.send(
	    f'okay, **{ctx.author}**. I will remind you for **{task}** in **{time}**'
	)

	await asyncio.sleep(converted_time)

	await ctx.author.send(
	    f'{ctx.author.mention} your reminder **{task}** has been finished!')


@client.command()
async def comeram(ctx, count=0):
	await ctx.message.delete()
	while count < 11:
		await ctx.send(
		    'https://cdn.discordapp.com/attachments/748731688074346599/833496594992857149/COMERAM_O_CU_DO_EDUARDO480P.mp4'
		)
		count += 1


@client.command()
async def spoiler(ctx):
	file = ctx.message.attachments[0]
	file.filename = f"SPOILER_{file.filename}"
	spoiler = await file.to_file()
	file = spoiler
	await ctx.message.delete()
	await ctx.send(f'sent by {ctx.author.mention}, message content: "||{ctx.message.content}||"')
	await ctx.send(file=spoiler)


@client.command()
async def matsu(ctx):
	links = ('https://imgur.com/SrIOSwO', 'https://imgur.com/cJOrRNm',
	         'https://imgur.com/WJuw5fX', 'https://imgur.com/wMgyxqR',
	         'https://imgur.com/wMgyxqR', 'https://imgur.com/9smC2z6',
	         'https://imgur.com/d2IQoQ8')
	escolha = random.choice(links)
	await ctx.send(escolha)


@client.command()
@commands.has_permissions(manage_channels=True)
async def nya(ctx):
	global nyaa
	nyaa = True
	while nyaa == True:
		await ctx.send('@everyone')
		await ctx.send(
		    'https://cdn.discordapp.com/attachments/748763024449470564/880987922059382844/necoposting_https___t.co_syOtjMgmx9__SQ_.mp4'
		)



@client.command()
async def gabriel(ctx):
	await ctx.message.delete()
	await ctx.send("https://cdn.discordapp.com/attachments/748731688074346599/885133017931202580/vai_tomar_no_CU_Gabriel_que_nome_feio_da_pohA_shitpost480P.mp4")

@client.command()
async def kongroo(ctx):
	global psy
	psy = True
	await ctx.message.delete()
	while psy == True:
		await ctx.send('https://tenor.com/view/steins-gate0-last-game-okabe-rintar%C5%8D-mad-scientist-gif-20999759')

@client.command()
@commands.has_permissions(manage_channels= True)
async def ping(ctx, member: discord.Member):
	global psy
	psy = True
	await ctx.message.delete()
	while psy == True:
		await ctx.send(member.mention)

@client.command()
@commands.has_permissions(manage_channels = True)
async def selerom(ctx):
	global psy
	psy = True
	await ctx.message.delete()
	while psy == True:
		await ctx.send("https://media.discordapp.net/attachments/754906273497088141/889274937435643904/emoji.png")

@client.command()
async def anime(ctx, *, name):
	await anilist_anime(ctx, name)

@client.command()
async def profile(ctx, *, username):
    await user_profile(ctx, username)


#------------------------music_commands (they're very poor commands)-------------------


@client.command()
async def join(ctx):
		if ctx.author.voice is None:
			await ctx.send('You must be in a voice channel!')
		voice_channel = ctx.author.voice.channel
		if ctx.voice_client is None:
			await voice_channel.connect()
		else:
			await ctx.voice_client.move_to(voice_channel)

@client.command()
async def dc(ctx):
	if ctx.voice_client is None:
		await ctx.send("i'm not in a voice channel!")
	else:	
		await ctx.send('successfully discontected!')
		await ctx.voice_client.disconnect()

@client.command()
async def play(ctx, url):
	global queue
	FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
	YDL_OPTIONS = {'format':"bestaudio"}
	vc =  ctx.voice_client
	queue.append(url)
	
	with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
		
		info = ydl.extract_info(url, download = False)
		song_title = info.get('title')
		url2 = info['formats'][0]['url']
		source = await discord.FFmpegOpusAudio.from_probe(url2,
		**FFMPEG_OPTIONS)
		
		
		vc.play(source)
		await ctx.send(f"**Now playing:** {song_title}")
		del(queue[0])

@client.command()
async def search(ctx,*,song):
	global queue

	FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
	YDL_OPTIONS = {'format':"bestaudio"}
	link = (f"https://www.youtube.com/results?search_query={song}")
	await ctx.send(f"searching for {song}")
	vc =  ctx.voice_client
	queue.append(link)
	with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
		
		info = ydl.extract_info(link, download = False)
		song_title = info.get('title')
		url2 = info['formats'][0]['url']
		source = await discord.FFmpegOpusAudio.from_probe(url2,
		**FFMPEG_OPTIONS)
		
		
		vc.play(source)
		await ctx.send(f"**Now playing:** {song_title}")
		del(queue[0])
		

@client.command()
async def pause(ctx):
	await ctx.send('paused!')
	await ctx.voice_client.pause()

@client.command()
async def resume(ctx):
		await ctx.send('resuming!')
		await ctx.voice_client.resume()

@client.command()
async def stop(ctx):
	await ctx.send('stopped!')
	await ctx.voice_client.stop()

@client.command()
async def add(ctx, url):
	global queue
	queue.append(url)
	await ctx.send('added to queue!')
	

@client.command()
async def remove(ctx, number):
	global queue

	try:
		del(queue[int(number)])
		await ctx.send(f"Your queue is now{queue}")
	except:
		await ctx.send('Your queue is either **empty** or the index is **out of range**')

@client.command()
async def view(ctx):
	global queue
	await ctx.send(f'Your queue is {queue}')

@client.command()
async def skip(ctx):
	global queue
	vc = ctx.voice_client
	vc.stop()
	del(queue[0])
	await ctx.send('skipped!')
	vc.play(queue)

client.remove_command("help")
async def main():
	await client.load_extension("help")
	await client.start(TOKEN)

if __name__ == "__main__":
	asyncio.run(main())