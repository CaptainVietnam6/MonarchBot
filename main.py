import discord
from discord.ext import commands
from discord.utils import get
from keep_alive import keep_alive
import os
import random
from random import randint
import time
import youtube_dl


#intents
intents = discord.Intents(messages=True, guilds=True, reactions=True, members=True)

#prefix the bot uses for it's commands
client = commands.Bot(command_prefix=".")

#load cog command
@client.command()
async def load(ctx, extension):
    client.load_extension(f"cogs.{extension}")


#unload cog command
@client.command()
async def unload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")


#reload cog command
@client.command()
async def reload(ctx, extension):
    client.reload_extension(f"cogs.{extension}")


#connects the cog file with main
for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")


#says MonarchBot is ready once it's ready
@client.event
async def on_ready():
    await client.change_presence(status = discord.Status.online, activity = 
    discord.Game("Actively being programmed in Python 3.8.2"))
    time.sleep(3)
    print("MonarchBot is ready")


'''start of voice & music commands'''
#voice channel join
@client.command(pass_context = True, aliases = ["Join", "join", "j", "J", "connect", "Connect"])
async def _join(ctx):
    global voice
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild = ctx.guild)

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
        await ctx.send(f"I joined your voice channel :D")
        print("MonarchBot joined a voice channel")

#voice channel leave
@client.command(pass_context = True, aliases = ["Leave", "leave", "L", "l", "Disconnect", "disconnect"])
async def _leave(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild = ctx.guild)

    if voice and voice.is_connected():
        await voice.disconnect()
        print(f"MonarchBot is disconnected from {channel} voice channel")
        await ctx.send(f"I left the '{channel}' voice channel :(")
    else:
        print("command given to leave voice channel but bot wasn't in a voice channel")
        await ctx.send("Invalid command: bot wasn't in any voice channels retard")

#voice channel play youtube
@client.command(pass_context = True, aliases = ["play", "Play", "p", "P"])
async def _play(ctx, url: str):
    is_song_there = os.path.isfile("song.mp3")
    try: #code will try to remove song, if it's playing then no remove
        if is_song_there:
            os.remove("song.mp3")
            print("Removed an old song file")
    except PermissionError:
        print("Failed to remove song file, song file in use")
        ctx.send("Error: song file cannot be removed because it's playing idiot")
        return

    await ctx.send(f"Getting everything ready :D (this may take a bit to load)")
    voice = get(client.voice_clients, guild = ctx.guild)
    ydl_opts = {
        "format": "bestaudio/best",
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }], #code above to specify options in ydl
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        print("Downloaded audio file\n")
        ydl.download([url])
    #renames file name 
    for file in os.list.dir("./"): #./ for current directory
        if file.endswith(".mp3"):
            audio_file_name = file
            print(f"Renamed File {file}\n")
            os.rename(file, "song.mp3")
    #checks to see if audio has finished playing, after then it will print
    voice.play(discord.FFmpegPCMAudio("song.mp3"), after = lambda e: print(f"{audio_file_name} has finished playing"))
    voice.source = discord.PCMVolumeTransformer(voice.source)
    voice.source.value = 0.07
    new_name = audio_file_name.rsplit("-", 2)
    await ctx.send(f"Playing {new_name}")
    print("playing\n")

'''end of voice & music commands'''

#8ball command
@client.command(aliases=["8ball", "eightball"])
async def _8ball(ctx, *, user_question):
    responses = [
        "As I see it, yes.",
        "Ask again later.",
        "Better not tell you now.",
        "Cannot predict now.",
        "Concentrate and ask again.",
        "Don’t count on it.",
        "It is certain.",
        "It is decidedly so.",
        "Most likely.",
        "My reply is no.",
        "My sources say no.",
        "Outlook not so good.",
        "Outlook good.",
        "Reply hazy, try again.",
        "Signs point to yes.",
        "Very doubtful.",
        "Without a doubt.",
        "Yes.",
        "Yes – definitely.",
        "You may rely on it.",
        "No it'll never happen give up.",
        "It might happen but ehhhhhhh.",
        "stfu i aint god."]
    await ctx.send(
        f"Question: {user_question}\nAnswer: {random.choice(responses)}")
    print("8ball command was executed")


#dice command, standard 1-6 numbers
@client.command()
async def dice(ctx):
    dice_number = randint(1,6)
    await ctx.send(dice_number)


#returns bot's ping/delay in milliseconds
@client.command()
async def ping(ctx):
    await ctx.send(f"Pong motherfucker {client.latency * 1000}ms")


#clear/purge command
@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)
    #anyone can use this command, change to only people with manage permissons only later


#send thigh pics lmao
@client.command(aliases = ["thighpics", "thigh_pics", "thighpic", "thigh_pic"])
async def _thighpics(ctx):
    await ctx.send("send thigh pics uwu")


#MonarchBot counts
@client.command(aliases = ["count", "Count"])
async def _count(ctx):
    MB_count = 0
    while MB_count != 86400:
        time.sleep(1)
        await ctx.send(MB_count)
        MB_count = MB_count + 1
    

#spam ping
@client.command(aliases = ["spam_ping", "Spam_ping", "spamping"])
async def _spam_ping(ctx):
    ping_count = 0
    while ping_count != 69420:
        time.sleep(1)
        await ctx.send(f"<@467451098735837186>")
        ping_count = ping_count + 1


#zero two gif
@client.command(aliases = ["zerotwo", "02", "ZeroTwo", "zero two", "Zero Two", "Zero two", "Zerotwo", "simp"])
async def _zerotwo(ctx):
    await ctx.send("https://tenor.com/view/darling-in-the-franxx-zero-two-dance-gif-14732606")
    print("someone's being a simp")


#keep alive command for webserver
keep_alive()


#bot token to connect it to discord's API
client.run('NzQ5MjAwOTU3OTM3NTQ5MzMy.X0ohww.CV5csOWU_tkOnN7yVAJ6P2esvCU')
