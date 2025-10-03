import discord
from discord.ext import commands

class HelpCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group(invoke_without_command=True)
    async def help(self, ctx):
        em = discord.Embed(
            title='Help',
            description='use %help [command] for extended information on a command.',
            color=ctx.author.color)
        em.add_field(
            name="utils",
            value="say, mute, unmute, spank, clean, kick, ban, unban, remindme, spoiler"
        )
        em.add_field(
            name="Fun",
            value="ougi, roll, run, manga, version, roulette, anime, profile")
        em.add_field(
            name="music",
            value="join, play, pause, stop, resume, queue, view")
        await ctx.send(embed=em)

    @help.command()
    async def kick(self, ctx):
        em = discord.Embed(title='Description',
                           description="Kick a member from this server")
        em.add_field(name="***syntax***", value="%kick <member> [reason]")
        await ctx.send(embed=em)

    @help.command()
    async def mute(self, ctx):
        em = discord.Embed(title='Description',
                           description="mute a member from this server")
        em.add_field(name="***syntax***", value="%mute <member> [time] [reason]")
        await ctx.send(embed=em)

    @help.command()
    async def unmute(self, ctx):
        em = discord.Embed(title='Description',
                           description="unmute a member that has muted before")
        em.add_field(name="***syntax***", value="%unmute <member>")
        await ctx.send(embed=em)

    @help.command()
    async def roll(self, ctx):
        em = discord.Embed(title='Description', description="Rolls a dice")
        em.add_field(name="***syntax***", value="%roll <sides>")
        await ctx.send(embed=em)

    @help.command()
    async def say(self, ctx):
        em = discord.Embed(title='Description',
                           description="Makes the Ougi says anything")
        em.add_field(name="***syntax***", value="%say <message>")
        await ctx.send(embed=em)

    @help.command()
    async def clean(self, ctx):
        em = discord.Embed(
            title='Description',
            description="Delete an amount (x) of messages from this channel")
        em.add_field(name="***syntax***", value="%clean <amount>")
        await ctx.send(embed=em)

    @help.command()
    async def ougi(self, ctx):
        em = discord.Embed(title='Description',
                           description="pra ver se ela ta viva")
        em.add_field(name="***syntax***", value=" just type %ougi")
        await ctx.send(embed=em)

    @help.command()
    async def spank(self, ctx):
        em = discord.Embed(title='Description',
                           description="Mute a member for 1 minute")
        em.add_field(name="***syntax***", value="%spank <user> [reason]")
        await ctx.send(embed=em)

    @help.command()
    async def limpagala(self, ctx):
        em = discord.Embed(title='Description', description="Remove a tag 'gozado' de todos os membros.")
        em.add_field(name="***syntax***", value="%limpagala")
        await ctx.send(embed=em)

    @help.command()
    async def ban(self, ctx):
        em = discord.Embed(title='Description',
                           description="ban a member from this server")
        em.add_field(name="***syntax***", value="%ban <member> [reason]")
        await ctx.send(embed=em)

    @help.command()
    async def unban(self, ctx):
        em = discord.Embed(
            title='Description',
            description="unban a member that was banned from this server")
        em.add_field(name="***syntax***", value="%unban <member#tag>")
        await ctx.send(embed=em)

    @help.command()
    async def manga(self, ctx):
        em = discord.Embed(title='Description', description="Searches for a manga on anilist")
        em.add_field(name="***syntax***", value="%manga [title]")
        await ctx.send(embed=em)

    @help.command()
    async def anime(self, ctx):
        em = discord.Embed(title='Description', description="Searches for an anime on anilist")
        em.add_field(name="***syntax***", value="%anime [title]")
        await ctx.send(embed=em)

    @help.command()
    async def profile(self, ctx):
        em = discord.Embed(title='Description', description="Searches for an user profile on anilist")
        em.add_field(name="***syntax***", value="%profile [user]")
        await ctx.send(embed=em)

    @help.command()
    async def version(self, ctx):
        em = discord.Embed(title='Description',
                           description="Shows the current version of Ougi Bot")
        em.add_field(name="***syntax***", value="%version")
        await ctx.send(embed=em)

    @help.command()
    async def dansa(self, ctx):
        em = discord.Embed(title='Description', description="DANSA GATINHO DANSA")
        em.add_field(name="***syntax***", value='%dansa')
        await ctx.send(embed=em)

    @help.command()
    async def roulette(self, ctx):
        em = discord.Embed(title='Description', description="Mute a random member")
        em.add_field(name="***syntax***", value="%roulette")
        await ctx.send(embed=em)

    @help.command()
    async def remindme(self, ctx):
        em = discord.Embed(title='Description', description="Write a reminder")
        em.add_field(name="***syntax***", value="%remindme [task] [time]")
        await ctx.send(embed=em)

    @help.command()
    async def join(self, ctx):
        em = discord.Embed(title='Description', description="makes ougi joins in a voice channel")
        em.add_field(name="***syntax***", value="%join")
        await ctx.send(embed=em)

    @help.command()
    async def stop(self, ctx):
        em = discord.Embed(title='Description', description="stops playing the current song")
        em.add_field(name="***syntax***", value="%stop")
        await ctx.send(embed=em)

    @help.command()
    async def resume(self, ctx):
        em = discord.Embed(title='Description', description="resumes the current song")
        em.add_field(name="***syntax***", value="%resume")
        await ctx.send(embed=em)

    @help.command()
    async def pause(self, ctx):
        em = discord.Embed(title='Description', description="pauses the current song")
        em.add_field(name="***syntax***", value="%pause")
        await ctx.send(embed=em)

    @help.command()
    async def dc(self, ctx):
        em = discord.Embed(title='Description', description="disconnects ougi from a voice channel")
        em.add_field(name="***syntax***", value="%dc")
        await ctx.send(embed=em)

    @help.command()
    async def play(self, ctx):
        em = discord.Embed(title='Description', description="plays a song")
        em.add_field(name="***syntax***", value="%play [youtube_url]")
        await ctx.send(embed=em)

    @help.command()
    async def spoiler(self, ctx):
        em = discord.Embed(title='Description',
                           description="Sends a message as spoiler")
        em.add_field(name="***syntax***", value="%spoiler [file]")
        await ctx.send(embed=em)

async def setup(bot):
    await bot.add_cog(HelpCog(bot))