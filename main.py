'''
Copyright (©) 2020 Kiet Pham <kiet.riley2005@gmail.com>
This software/program has a copyright license, more information is in the 'LICENSE' file
IF YOU WANT TO USE/COPY/MODIFY/REPRODUCE/RE-DISTRIBUTE THIS PROGRAM, YOU MUST INCLUDE A COPY OF THE LICENSE

Author Name: Kiet Pham
Author Contact: kiet.riley2005@gmail.com
Discord: CaptainVietnam6#0001
Discord Server: https://discord.gg/3z76p8H5yj
GitHub: https://github.com/CaptainVietnam6
Instagram: @itz_kietttttttttt
Program Status: ACTIVE, FINALISED
'''

#imports related to discord or discord packages
import discord
from discord.ext import commands
from discord.utils import get
from discord.ext.commands import cooldown
from discord.ext.commands import BucketType
from discord import FFmpegPCMAudio

#other important imports for system
import os
from os import system
import random
from random import randint
import time
import youtube_dl
import shutil
import asyncio

#imports from other files
from keep_alive import keep_alive
from BOT_TOKEN import BOT_TOKEN


'''REFER TO NOTES TO UNDERSTAND CODE BETTER AND USE IT AS A INDEX TO SEE WHERE CERTAIN COMMAND CLASSES ARE'''


'''START OF IMPORTANT STUFF, DEALS WITH BOT AND INTERNAL COMMANDS'''


#INTENTS
intents = discord.Intents(messages=True, guilds=True, reactions=True, members=True)

#PREFIX THE BOT USES
bot_prefixes = ["/", "."]
client = commands.Bot(command_prefix = bot_prefixes)
bot = commands.Bot(command_prefix = "/", intents = intents)


#REMOVES DEFAULT HELP COMMAND
client.remove_command("help")


#AUTO ROLE, GIVES TEMP MEMBER TO NEW MEMBERS
#AUTOROLE AND MEMBER JOIN WELCOME
@client.event
async def on_member_join(member):
    role = discord.utils.get(member.guild.roles, name = "Playground Member")
    await asyncio.sleep(1)
    await member.add_roles(role)
    print("AutoRole: added a role to member")


#LOAD cog
@client.command()
async def load(ctx, extension):
    client.load_extension(f"cogs.{extension}")


#UNLOAD cog
@client.command()
async def unload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")


#RELOAD COG
@client.command()
async def reload(ctx, extension):
    client.reload_extension(f"cogs.{extension}")


#CONNECTS COGS FILE 
for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")


#ALERTS WHEN MONARCHBOT IS READY
@client.event
async def on_ready():
    await client.change_presence(status = discord.Status.online, activity = discord.Game("Programmed by CaptainVietnam6#0001 in Python 3.8.2"))
    await asyncio.sleep(3)
    print("MonarchBot is ready")

    #notifs for Monarch SMP Server
    channel = client.get_channel(767474825538437120)
    await channel.send("MonarchBot is online")
    #notifs for CV6's Playground server
    channel = client.get_channel(816179144961818634)
    await channel.send("MonarchBot is online")
    #notifs for CV6's Bots server
    channel = client.get_channel(812974446801059860)
    await channel.send("MonarchBot is online")

    #joins vc on ready
    channel = client.get_channel(815933179378270208)
    await channel.connect()


#RETURNS BOT'S PING IN MILLISECONDS
@client.command()
async def ping(ctx):
    await ctx.send(f"Pong motherfucker {client.latency * 1000}ms")


'''END OF IMPORTANT STUFF, DEALS WITH BOT AND INTERNAL COMMANDS'''

'''START OF MODERATION COMMANDS'''


#chat purge command cleared out as suspicion of passing rate limit
'''
#CHAT PURGE COMMAND
@client.command(aliases = ["clear", "Clear", "Purge", "purge"])
@commands.has_any_role("Admin", "Co-admin", "Moderator", "Staff", "staff-in-training")
@cooldown(1, 180, BucketType.default)
async def _chat_clear(ctx, amount = 100):
    await ctx.channel.purge(limit = amount + 1)
    await asyncio.sleep(float(1.5))
    await ctx.send (f"cleared {amount} messages from chat")
    await asyncio.sleep(float(0.5))
    await ctx.send("Please wait 3 minutes before using this command again :)")
'''


#SEND BOT INVITE LINK COMMAND
@client.command(aliases = ["botinvite", "BotInvite", "Botinvite", "MBlink", "mblink"])
@cooldown(1, 60, BucketType.default)
async def _sendbotinvite(ctx):
    print("Someone requested bot invite link\n")
    await ctx.send("Sending bot's invite link!")
    await asyncio.sleep(float(0.5))
    await ctx.send("https://discord.com/api/oauth2/authorize?client_id=749200957937549332&permissions=0&scope=bot")


#SENDS MONARCH'S SEED
@client.command(aliases = ["seed", "Seed"])
async def _monarchseed(ctx):
    embed = discord.Embed(
        title = "The seed for Monarch SMP is -1385471052",
        color = 0x00ff44
    )
    await ctx.send(embed = embed)


#HELP COMMAND
@client.group(invoke_without_command = True, aliases = ["help", "Help"])
async def _help(ctx):
    author_name = ctx.author.display_name
    embed = discord.Embed(
        title = "**Help command categories**",
        description = "**These are the commands you can run to see the list of commands in each category. There is also a command list in <#767323639384113153>**\n\nFun commands: **/help fun**\nMusic commands: **/help music**\nSoundboard commands: **/help sb**\nGame commands: **/help game**\nEmoji commands: **/help emoji**\nModeration commands: **/help mod**\n",
        color = 0x00ff44
    )
    embed.set_footer(text = f"Requested by {author_name}")
    await ctx.send(embed = embed)

#HELP - FUN COMMANDS
@_help.command(aliases = ["fun", "Fun"])
async def _help_fun(ctx):
    author_name = ctx.author.display_name
    embed = discord.Embed(
        title = "**Fun/responses related commands list**",
        description = "**These are commands that relate to fun or responses features of MonarchBot**\n\n8ball command: **/8ball {question}**\nDice command: **/dice**\nFranklin roast meme: **/loc**\nMeme command: **/meme**\nHow-to-use-google: **/google**\nServer daddy: **/daddy**\nServer mommy: **/mommy**\nBenice to staff: **/benice**\nSend thigh pics: **/thighpics**\nZeroTwo GIF: **/zerotwo**\nDictionary: **/dictionary {word}**\nRepeat after user: **/repeat**\nWhat-a-legend: **/legend**\nCapt Twitch link: **/twitch**\nEw lightmode: **/lightmode**\nReply spam: **/spam {word}**\nPrint fancy text: **/print {word}**\nSpeedrun profile: **/speedrun {user name}**\nShut up GIF: **/shut**\nDweam: **/dweam**\nSends nothing: **/nothing**\nDiscordmod meme: **/discordmod**\nCusswords: **/cusswords**\nFunny Pinged: **/pinged**\nFair: **fair**\nPog: **pog**",
        color = 0x00ff44
    )
    embed.set_footer(text = f"Requested by {author_name}")
    await ctx.send(embed = embed)

#HELP - MUSIC COMMANDS
@_help.command(aliases = ["music", "Music"])
async def _help_music(ctx):
    author_name = ctx.author.display_name
    embed = discord.Embed(
        title = "**Music related commands list**",
        description = "**These are commands that relate to music features of MonarchBot**\n\nJoin VC: **/join**\nLeave VC: **/leave**\nPlay song: **/play (youtube url)**\nQueue song: **/queue (youtube url)**\nPause music: **/pause**\nResume music: **/resume**\nStop music: **/stop**\n",
        color = 0x00ff44
    )
    embed.set_footer(text = f"Requested by {author_name}")
    await ctx.send(embed = embed)

#HELP - SOUNDBOARD COMMANDS
@_help.command(aliases = ["sb", "Sb", "SB", "soundboard", "SoundBoard", "Soundboard"])
async def _help_soundboard(ctx):
    author_name = ctx.author.display_name
    embed = discord.Embed(
        title = "**Soundboard related commands list**",
        description = "**These are commands that relate to voice channel soundboard features of MonarchBot**\n\nJoin VC: **/join**\nLeave VC: **/leave**\nAirhorn: **/sb airhorn**\nAli-a intro: **/sb alia**\nBegone thot: **/sb begonethot**\nDamn son where'd you find this: **/sb damnson**\nDankstorm: **/sb dankstorm**\nDeez nuts: **/sb deeznuts**\nDeja Vu: **/sb dejavu**\nLook at this dude: **/sb dis_dude**\nAnother fag left the chat: **/sb fleft**\nFart: **/sb fart**\nHah gaaayyy: **/sb hahgay**\nIt's called hentai and it's art: **/sb henart**\nIlluminati song: **/sb illuminati**\nBitch Lasagna: **/sb lasagna**\nLoser: **/sb loser**\nNoob: **/sb noob**\nOof sound: **/sb oof**\nPickle Rick: **/sb picklerick**\nNice: **/sb nice**\nWhy don't we just relax and turn on the radio: **/sb radio**\nRick roll: **/sb rickroll**\nThis is sparta: **/sb sparta**\nTitanic flute fail: **/sb titanic**\nGTA V Wasted: **/sb wasted**\nWubba lubba dub dub: **/sb wubba**\n",
        color = 0x00ff44
    )
    embed.set_footer(text = f"Requested by {author_name}")
    await ctx.send(embed = embed)

#HELP - GAME COMMANDS
@_help.command(aliases = ["game", "Game"])
async def _help_game(ctx):
    author_name = ctx.author.display_name
    embed = discord.Embed(
        title = "**Game related commands list**",
        description = "**These are commands that relate to game features of MonarchBot**\n\n8ball command: **/8ball (your question)**\nDice command, returns 1-6: **/dice**\nFranklin roast meme: **/loc**\nRock Paper Scissors: **/rps (rock, paper, or scissors)**\nMeme command: **/meme**\nHentai command: **/hentai**\n",
        color = 0x00ff44
    )
    embed.set_footer(text = f"Requested by {author_name}")
    await ctx.send(embed = embed)

#HELP - EMOJI COMMANDS
@_help.command(aliases = ["emoji", "Emoji"])
async def _help_emoji(ctx):
    author_name = ctx.author.display_name
    embed = discord.Embed(
        title = "**Emoji related commadns list**",
        description = "**The commands with an $ have an auto detection feature to detect a certain keyword in your message**\n\nSo fake$: **/fake**\nX to doubt$: **/doubt**\nStonks$: **/stonks**\nSimp pill$: **/simp**\nUwU*: **/uwu**\nWat: **/wat**\nAdmin abooz: **/abooz**\n60s Timer$: **/timer**\nThats racist$: **/racist**\nPolice$: **/police**\nF-spam emoji: **/fpsam**\nClap emoji: **/clap**\nYou tried: **/youtried**\nPython logo: **/python**\nPepe pog: **/pepepog**\nGay flag$: **/gay**\nBisexual flag$: **/bisexual**\nTrans flag$: **/trans**",
        color = 0x00ff44
    )
    embed.set_footer(text = f"Requested by {author_name}")
    await ctx.send(embed = embed)

#HELP - MODERATION COMMANDS
@_help.command(aliases = ["mod", "Mod", "moderation", "Moderation"])
async def _help_moderation(ctx):
    author_name = ctx.author.display_name
    embed = discord.Embed(
        title = "**Moderation related commands list**",
        description = "**These are commands that relate to moderation features of MonarchBot, most require administrative powers**\n\nKick command: **/kick (tag member, reason)**\nBan command: **/ban (tag member, reason)**\nPurge/clear chat: **/clear (number of messages)**\nBot invite link: **/botinvite**\nMonarchSMP Seed: **/seed**\nHelp directory: **/help**\n",
        color = 0x00ff44
    )
    embed.set_footer(text = f"Requested by {author_name}")
    await ctx.send(embed = embed)


#ANTI-SLUR & SLUR DETECTION COMMAND


'''END OF MODERATION COMMANDS'''

'''START OF TEST-BED COMMANDS OR COMMANDS FOR TESTING'''


#TEST COMMAND
@client.command(aliases = ["ban", "Ban", "kick", "Kick"])
async def _repeat(ctx):
    await ctx.send("shut up.")


#TEST COMMAND 2
@client.command(aliases = ["website", "Website"])
async def _captswebsite(ctx):
    await asyncio.sleep(float(0.1))
    await ctx.send("Sending website...")
    await asyncio.sleep(float(1.5))
    await ctx.send("https://Basic-Website-1.itzkiettttt.repl.co")


'''END OF TEST-BED COMMANDS OR COMMANDS FOR TESTING'''

'''START OF MUSIC AND VOICE CHANNEL RELATED COMMANDS'''


#VOICE CHANNEL JOIN
@client.command(pass_context = True, aliases = ["Join", "join", "j", "J", "connect", "Connect"])
async def _join(ctx):
    global voice
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild = ctx.guild)

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
        await ctx.send("I joined your voice channel :D")
        print("MonarchBot joined a voice channel")


#VOICE CHANNEL LEAVE
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


#VOICE CHANNEL PLAY YOUTUBE URL
@client.command(pass_context = True, aliases = ["play", "Play", "p", "P"])
async def _play(ctx, url: str):
    def check_queue():
        Queue_infile = os.path.isdir("./Queue")
        if Queue_infile is True:
            DIR = os.path.abspath(os.path.realpath("Queue"))
            length = len(os.listdir(DIR))
            still_queue = length - 1 #outprints how many are left in queue after new song is played
            try:
                first_file = os.listdir(DIR)[0] #first file inside directory
            except:
                print("No more songs in queue\n")
                queues.clear
                return
            main_location = os.path.dirname(os.path.realpath(__file__))
            song_path = os.path.abspath(os.path.realpath("Queue") + "//" + first_file)
            
            if length != 0:
                print("Sone finished playing, loading next song\n")
                print(f"Songs still in queue: {still_queue}")
                is_song_there = os.path.isfile("song.mp3")
                if is_song_there: 
                    os.remove("song.mp3")
                shutil.move(song_path, main_location) #moves queued song to main directory
                for file in os.listdir("./"):
                    if file.endswith(".mp3"):
                        os.rename(file, "song.mp3")
                vcvoice.play(discord.FFmpegPCMAudio("song.mp3"), after = lambda e: check_queue()) #plays the song
                vcvoice.source = discord.PCMVolumeTransformer(vcvoice.source)
                vcvoice.source.value = 0.05
            
            else: #if queues = 0, clearns it
                queues.clear()
                return

        else: #is there is no queue folder
            queues.clear()
            print("No songs queued after last song\n")

    #end of queue section thingy for play command
    is_song_there = os.path.isfile("song.mp3")
    try: #code will try to remove song, if it's playing then no remove
        if is_song_there:
            os.remove("song.mp3")
            queues.clear()
            print("Removed an old song file")
    except PermissionError:
        print("Failed to remove song file, song file in use")
        ctx.send("Error: song file cannot be removed because it's playing idiot")
        return

    #this section is here to remove the old queue folder
    Queue_infile = os.path.isdir("./Queue")
    try:
        Queue_folder = "./Queue"
        if Queue_infile is True:   #if there is an old queue file, it will try to remove it
            print("Removed old queue folder")
            shutil.rmtree(Queue_folder)
    except:
        print("No old queue folder")

    #rest of play command to play songs
    await ctx.send("Getting everything ready :D (this may take a bit to load)")
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    ydl_opts = {
        "format": "bestaudio/best",
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "256",
        }], #code above to specify options in ydl
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        print("Downloaded audio file\n")
        ydl.download([url])
    #renames file name 
    for file in os.listdir("./"): #./ for current directory
        if file.endswith(".mp3"):
            audio_file_name = file
            print(f"Renamed File {file}\n")
            os.rename(file, "song.mp3")
    #checks to see if audio has finished playing, after then it will print
    vcvoice.play(discord.FFmpegPCMAudio("song.mp3"), after = lambda e: check_queue())
    vcvoice.source = discord.PCMVolumeTransformer(vcvoice.source)
    vcvoice.source.value = 0.05
    new_name = audio_file_name.rsplit("-", 2)
    await ctx.send(f"Playing {new_name}")
    print("playing\n")


#VOICE CHANNEL MUSIC PAUSE COMMAND
@client.command(pass_context = True, aliases = ["pause", "Pause"])
async def _pause(ctx):
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    
    if vcvoice and voice.is_playing():
        vcvoice.pause()
        print("Music paused")
        await ctx.send("Music paused")
    else:
        print("Music wasn't playing but there was a request to pause music")
        await ctx.send("Music wasn't playing so i can't pause it retard")


#VOICE CHANNEL MUSIC RESUME COMMAND
@client.command(pass_context = True, aliases = ["resume", "Resume"])
async def _resume(ctx):
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    
    if vcvoice and voice.is_paused():
        vcvoice.resume()
        print("Music resumed")
        await ctx.send("Music has been resumed pogs")
    else:
        print("Music was not paused but a request was sent for music pause")
        await ctx.send("Music can't be resumed if it wasn't paused dumbass smh")


#VOICE CHANNEL MUSIC STOP COMMAND
@client.command(pass_context = True, aliases = ["stop", "Stop"])
async def _stop(ctx):
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)

    queues.clear() #clears queue when stop command ran

    if vcvoice and voice.is_playing():
        vcvoice.stop()
        print("Music stopped")
        await ctx.send("Music stopped")
    else:
        print("Music could not be stopped")
        await ctx.send("Music can't be stopped if there aint music playing")


#VOICE CHANNEL MUSIC queue
#this command is for music to be queued up if you use the ".play" multiple times while music is still playing
queues = {}

@client.command(pass_context = True, aliases = ["Queue", "queue", "Q", "q"])
async def _queue(ctx, url: str):
    Queue_infile = os.path.isdir("./Queue")
    if Queue_infile is False:
        os.mkdir("Queue")      #sees if there is any song files in queue, if there is any then it counts them
    DIR = os.path.abspath(os.path.realpath("Queue"))
    queue_num = len(os.listdir(DIR)) #gets/counts ammount of files in the queue
    queue_num += 1 #adds another to queue
    add_queue = True
    while add_queue:
        if queue_num in queues:
            queue_num += 1
        else:
            add_queue = False
            queues[queue_num] = queue_num

    queue_path = os.path.abspath(os.path.realpath("Queue") + f"//song{queue_num}.%(ext)s")
    #takes the real path of song in queue and number of it
    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl" : queue_path,
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "1024",
        }], #code above to specify options in ydl
    }
    #downloads song and puts into queue path above ^
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        print("Downloaded audio file\n")
        ydl.download([url])
    await ctx.send("Adding song " + str(queue_num) + " to the queue")
    print("added a song to queue\n")


'''END OF MUSIC AND VOICE CHANNEL RELATED COMMANDS'''

'''START OF VOICE CHANNEL SOUNDBOARD COMMANDS'''


#old soundboard command, this is a singular command and doesn't rely on groups and subcommands
'''
@client.command(pass_context = True, aliases = ["airhorn", "Airhorn"])
async def _soundboard_airhorn(ctx):
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    vcvoice.play(discord.FFmpegPCMAudio("soundboard/airhorn.mp3"))
    vcvoice.source = discord.PCMVolumeTransformer(vcvoice.source)
    vcvoice.source.value = 0.05
'''

#soundboard command format; copy for future use, switch out airhorn with whatever, 2nd one already has that done
'''
@_soundboard.command(aliases = ["airhorn", "Airhorn"])
async def _soundboard_airhorn(ctx):
    await ctx.send("Playing **airhorn** sound effect from soundboard")
    print("\nPlayed airhorn sound effect\n")
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    vcvoice.play(discord.FFmpegPCMAudio("soundboard/airhorn.mp3"))
    vcvoice.source = discord.PCMVolumeTransformer(vcvoice.source)
    vcvoice.source.value = 0.05

@_soundboard.command(aliases = [""])
async def _soundboard_(ctx):
    await ctx.send("Playing **** sound effect from soundboard")
    print("\nPlayed  sound effect\n")
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    vcvoice.play(discord.FFmpegPCMAudio("soundboard/"))
    vcvoice.source = discord.PCMVolumeTransformer(vcvoice.source)
    vcvoice.source.value = 0.05
'''


#SOUNDBOARD COMMAND GROUP & HELP
@client.group(invoke_without_command = True, aliases = ["sb", "SB", "soundboard", "Soundboard", "SoundBoard"])
async def _soundboard(ctx):
    await ctx.send("**Soundboard Commands List**\n")

#SB AIRHORN 
@_soundboard.command(aliases = ["airhorn", "Airhorn"])
async def _soundboard_airhorn(ctx):
    await ctx.send("Playing **airhorn** sound effect from soundboard")
    print("\nPlayed airhorn sound effect\n")
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    vcvoice.play(discord.FFmpegPCMAudio("soundboard/airhorn.mp3"))
    vcvoice.source = discord.PCMVolumeTransformer(vcvoice.source)
    vcvoice.source.value = 0.05

#SB ALI-A SOUNDTRACK
@_soundboard.command(aliases = ["ali_a", "alia", "Ali-a", "Alia"])
async def _soundboard_ali_a(ctx):
    await ctx.send("Playing **ali_a** sound effect from soundboard")
    print("\nPlayed ali_a sound effect\n")
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    vcvoice.play(discord.FFmpegPCMAudio("soundboard/ali_a.mp3"))
    vcvoice.source = discord.PCMVolumeTransformer(vcvoice.source)
    vcvoice.source.value = 0.05

#SB BEGONE THOT
@_soundboard.command(aliases = ["begone_thot", "begonethot", "Begone_thot", "Begonethot"])
async def _soundboard_begone_thot(ctx):
    await ctx.send("Playing **begone_thot** sound effect from soundboard")
    print("\nPlayed begone_thot sound effect\n")
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    vcvoice.play(discord.FFmpegPCMAudio("soundboard/begone_thot.mp3"))
    vcvoice.source = discord.PCMVolumeTransformer(vcvoice.source)
    vcvoice.source.value = 0.05

#SB DAMN SON WHERE'D U FIND THIS
@_soundboard.command(aliases = ["damn_son", "Damn_son", "damnson", "Damnson"])
async def _soundboard_damn_son(ctx):
    await ctx.send("Playing **damn_son** sound effect from soundboard")
    print("\nPlayed damn_son sound effect\n")
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    vcvoice.play(discord.FFmpegPCMAudio("soundboard/damn_son.mp3"))
    vcvoice.source = discord.PCMVolumeTransformer(vcvoice.source)
    vcvoice.source.value = 0.05

#SB DANKSTORM
@_soundboard.command(aliases = ["dankstorm", "Dankstorm"])
async def _soundboard_dankstorm(ctx):
    await ctx.send("Playing **dankstorm** sound effect from soundboard")
    print("\nPlayed dankstorm sound effect\n")
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    vcvoice.play(discord.FFmpegPCMAudio("soundboard/dankstorm.mp3"))
    vcvoice.source = discord.PCMVolumeTransformer(vcvoice.source)
    vcvoice.source.value = 0.05

#SB DEEZNUTS
@_soundboard.command(aliases = ["deez_nuts", "deeznuts", "Deez_nuts", "Deeznuts"])
async def _soundboard_deez_nuts(ctx):
    await ctx.send("Playing **deez_nuts** sound effect from soundboard")
    print("\nPlayed deez_nuts sound effect\n")
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    vcvoice.play(discord.FFmpegPCMAudio("soundboard/deez_nuts.mp3"))
    vcvoice.source = discord.PCMVolumeTransformer(vcvoice.source)
    vcvoice.source.value = 0.05

#SB DEJA VU
@_soundboard.command(aliases = ["deja_vu", "dejavu", "Deja_vu", "Dejavu"])
async def _soundboard_deja_vu(ctx):
    await ctx.send("Playing **deja_vu** sound effect from soundboard")
    print("\nPlayed deja_vu sound effect\n")
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    vcvoice.play(discord.FFmpegPCMAudio("soundboard/deja_vu.mp3"))
    vcvoice.source = discord.PCMVolumeTransformer(vcvoice.source)
    vcvoice.source.value = 0.05

#SB LOOK AT THIS DUDE
@_soundboard.command(aliases = ["dis_dude", "this_dude", "disdude", "thisdude", "Dis_dude", "This_dude", "Disdude", "Thisdude" ])
async def _soundboard_this_dude(ctx):
    await ctx.send("Playing **dis_dude** sound effect from soundboard")
    print("\nPlayed dis_dude sound effect\n")
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    vcvoice.play(discord.FFmpegPCMAudio("soundboard/dis_dude.mp3"))
    vcvoice.source = discord.PCMVolumeTransformer(vcvoice.source)
    vcvoice.source.value = 0.05

#SB ANOTHER FAG LEFT THE CHAT
@_soundboard.command(aliases = ["f_left", "fleft", "F_left", "Fleft"])
async def _soundboard_f_left(ctx):
    await ctx.send("Playing **f_left** sound effect from soundboard")
    print("\nPlayed f_left sound effect\n")
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    vcvoice.play(discord.FFmpegPCMAudio("soundboard/f_left.mp3"))
    vcvoice.source = discord.PCMVolumeTransformer(vcvoice.source)
    vcvoice.source.value = 0.05

#SB FART
@_soundboard.command(aliases = ["fart", "Fart"])
async def _soundboard_fart(ctx):
    await ctx.send("Playing **fart** sound effect from soundboard")
    print("\nPlayed fart sound effect\n")
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    vcvoice.play(discord.FFmpegPCMAudio("soundboard/fart.mp3"))
    vcvoice.source = discord.PCMVolumeTransformer(vcvoice.source)
    vcvoice.source.value = 0.05

#SB HAH GAAAYY
@_soundboard.command(aliases = ["hah_gay", "hahgay", "Hah_gay", "Hahgay"])
async def _soundboard_hah_gay(ctx):
    await ctx.send("Playing **hah_gay** sound effect from soundboard")
    print("\nPlayed hah_gay sound effect\n")
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    vcvoice.play(discord.FFmpegPCMAudio("soundboard/hah_gay.mp3"))
    vcvoice.source = discord.PCMVolumeTransformer(vcvoice.source)
    vcvoice.source.value = 0.05

#SB IT'S CALLED HENTAI, AND IT'S ART
@_soundboard.command(aliases = ["hen_art", "henart", "Hen_art", "Henart"])
async def _soundboard_hentai_art(ctx):
    await ctx.send("Playing **henart (hentai art)** sound effect from soundboard")
    print("\nPlayed henart sound effect\n")
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    vcvoice.play(discord.FFmpegPCMAudio("soundboard/hen_art.mp3"))
    vcvoice.source = discord.PCMVolumeTransformer(vcvoice.source)
    vcvoice.source.value = 0.05

#SB ILLUMINATI X-FILES SOUNDTRACK
@_soundboard.command(aliases = ["illuminati", "Illuminati"])
async def _soundboard_illuminati(ctx):
    await ctx.send("Playing **illuminati** sound effect from soundboard")
    print("\nPlayed illuminati sound effect\n")
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    vcvoice.play(discord.FFmpegPCMAudio("soundboard/illuminati.mp3"))
    vcvoice.source = discord.PCMVolumeTransformer(vcvoice.source)
    vcvoice.source.value = 0.05

#SB BITCH LASAGNA
@_soundboard.command(aliases = ["lasagna", "Lasagna", "bitch_lasagna", "Bitch_lasagna"])
async def _soundboard_bitch_lasagna(ctx):
    await ctx.send("Playing **bitch_lasagna** sound effect from soundboard")
    print("\nPlayed bitch_lasagna sound effect\n")
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    vcvoice.play(discord.FFmpegPCMAudio("soundboard/lasagna.mp3"))
    vcvoice.source = discord.PCMVolumeTransformer(vcvoice.source)
    vcvoice.source.value = 0.05

#SB LOOSER
@_soundboard.command(aliases = ["looser", "Looser", "loser", "Loser"])
async def _soundboard_loser(ctx):
    await ctx.send("Playing **loser** sound effect from soundboard")
    print("\nPlayed loser sound effect\n")
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    vcvoice.play(discord.FFmpegPCMAudio("soundboard/loser.mp3"))
    vcvoice.source = discord.PCMVolumeTransformer(vcvoice.source)
    vcvoice.source.value = 0.05

#SB NOOB 
@_soundboard.command(aliases = ["noob", "Noob"])
async def _soundboard_noob(ctx):
    await ctx.send("Playing **noob** sound effect from soundboard")
    print("\nPlayed noob sound effect\n")
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    vcvoice.play(discord.FFmpegPCMAudio("soundboard/noob.mp3"))
    vcvoice.source = discord.PCMVolumeTransformer(vcvoice.source)
    vcvoice.source.value = 0.05

#SB OOF SOUND
@_soundboard.command(aliases = ["oof", "Oof"])
async def _soundboard_oof(ctx):
    await ctx.send("Playing **oof** sound effect from soundboard")
    print("\nPlayed oof sound effect\n")
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    vcvoice.play(discord.FFmpegPCMAudio("soundboard/oof.mp3"))
    vcvoice.source = discord.PCMVolumeTransformer(vcvoice.source)
    vcvoice.source.value = 0.05

#SB I'M PICKLE RICKKKK
@_soundboard.command(aliases = ["pickle_rick", "Pickle_rick", "picklerick", "Picklerick"])
async def _soundboard_pickcle_rick(ctx):
    await ctx.send("Playing **pickle_rick** sound effect from soundboard")
    print("\nPlayed pickle_rick sound effect\n")
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    vcvoice.play(discord.FFmpegPCMAudio("soundboard/pickle_rick.mp3"))
    vcvoice.source = discord.PCMVolumeTransformer(vcvoice.source)
    vcvoice.source.value = 0.05

#SB *POP* NICE  
@_soundboard.command(aliases = ["nice", "Nice"])
async def _soundboard_nice(ctx):
    await ctx.send("Playing **nice** sound effect from soundboard")
    print("\nPlayed nice sound effect\n")
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    vcvoice.play(discord.FFmpegPCMAudio("soundboard/nice.mp3"))
    vcvoice.source = discord.PCMVolumeTransformer(vcvoice.source)
    vcvoice.source.value = 0.05

#SB WHY DON'T WE JUST RELAX, TURN ON THE RADIO, WOULD YOU LIKE AM OR FM
@_soundboard.command(aliases = ["radio", "Radio"])
async def _soundboard_radio(ctx):
    await ctx.send("Playing **radio** sound effect from soundboard")
    print("\nPlayed radio sound effect\n")
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    vcvoice.play(discord.FFmpegPCMAudio("soundboard/radio.mp3"))
    vcvoice.source = discord.PCMVolumeTransformer(vcvoice.source)
    vcvoice.source.value = 0.05

#SB RICKROLL
@_soundboard.command(aliases = ["rick_roll", "Rick_roll", "rickroll", "Rickroll"])
async def _soundboard_rick_roll(ctx):
    await ctx.send("Playing **rick_roll** sound effect from soundboard")
    print("\nPlayed rick_roll sound effect\n")
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    vcvoice.play(discord.FFmpegPCMAudio("soundboard/rick_roll.mp3"))
    vcvoice.source = discord.PCMVolumeTransformer(vcvoice.source)
    vcvoice.source.value = 0.05

#SB SPARTA
@_soundboard.command(aliases = ["sparta", "Sparta"])
async def _soundboard_sparta(ctx):
    await ctx.send("Playing **sparta** sound effect from soundboard")
    print("\nPlayed sparta sound effect\n")
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    vcvoice.play(discord.FFmpegPCMAudio("soundboard/sparta.mp3"))
    vcvoice.source = discord.PCMVolumeTransformer(vcvoice.source)
    vcvoice.source.value = 0.05

#SB TITANIC FLUTE MEME
@_soundboard.command(aliases = ["titanic", "Titanic"])
async def _soundboard_titanic(ctx):
    await ctx.send("Playing **titanic** sound effect from soundboard")
    print("\nPlayed titanic sound effect\n")
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    vcvoice.play(discord.FFmpegPCMAudio("soundboard/titanic.mp3"))
    vcvoice.source = discord.PCMVolumeTransformer(vcvoice.source)
    vcvoice.source.value = 0.05

#SB GTAV WASTED SOUND
@_soundboard.command(aliases = ["wasted", "Wasted"])
async def _soundboard_wasted(ctx):
    await ctx.send("Playing **wasted** sound effect from soundboard")
    print("\nPlayed wasted sound effect\n")
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    vcvoice.play(discord.FFmpegPCMAudio("soundboard/wasted.mp3"))
    vcvoice.source = discord.PCMVolumeTransformer(vcvoice.source)
    vcvoice.source.value = 0.05

#SB RICK & MORTY WUBBA LUBBA DUB DUB
@_soundboard.command(aliases = ["wubba", "Wubba"])
async def _soundboard_wubba(ctx):
    await ctx.send("Playing **wubba** sound effect from soundboard")
    print("\nPlayed wubba sound effect\n")
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    vcvoice.play(discord.FFmpegPCMAudio("soundboard/wubba.mp3"))
    vcvoice.source = discord.PCMVolumeTransformer(vcvoice.source)
    vcvoice.source.value = 0.05


'''END OF VOICE CHANNEL SOUNDBOARD COMMANDS'''

'''START OF GAME RELATED COMMANDS'''


#8BALL COMMAND
@client.command(aliases=["8ball", "eightball"])
async def _8ball(ctx, *, user_question):
    author_name = ctx.author.display_name
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
    final_response = random.choice(responses)
    embed = discord.Embed(
        title = "8ball command",
        description = f"Question: **{user_question}**\nAnswer: **{final_response}**",
        color = 0x00ff44
    )
    embed.set_footer(text = f"Requested by {author_name}")
    await ctx.send(embed = embed)


#DICE COMMAND; 1-6
@client.command()
async def dice(ctx):
    dice_number = randint(1,6)
    await ctx.send(dice_number)


'''
#GTA V ROAST MEME FRANKLIN SIDE
@client.command(aliases = ["loc", "Loc", "LOC", "crib", "Crib", "gtavroast", "GTAVroast"])
async def _locfranklin(ctx):
    await asyncio.sleep(float(1.4))
    await ctx.send("Man, fuck you.")
    await asyncio.sleep(float(0.6))
    await ctx.send("I'll see you at work.")
    await asyncio.sleep(float(6.5))
    await ctx.send("What?!?")
    await asyncio.sleep(float(0.5))
    await ctx.send("Argh, motherfucker.")
'''


#GTA V ROAST MEME LAMAR SIDE
#blanked out since it's hosted on Neko's bot
#GTA V roast meme LAMAR SIDE
@client.command(aliases = ["loc", "Loc", "LOC", "crib", "Crib", "gtavroast", "GTAVroast"])
async def _loclamar(ctx):
    await asyncio.sleep(float(0))
    await ctx.send(f"Wassup, can a loc come up in your crib?\n")
    await asyncio.sleep(float(2.5))
    await ctx.send("Ah, n-word, don't hate me 'cause I'm beautiful, n-word.")
    await asyncio.sleep(float(0.5))
    await ctx.send("Maybe if you got rid of that old yee-yee ass haircut you got")
    await asyncio.sleep(float(0.5))
    await ctx.send("you'd get some bitches on your dick.")
    await asyncio.sleep(float(0.5))
    await ctx.send("Oh, better yet,")
    await asyncio.sleep(float(0.25))
    await ctx.send("maybe Tanisha'll call your dog-ass")
    await asyncio.sleep(float(0.50))
    await ctx.send("if she ever stop fucking with that brain surgeon or lawyer she fucking with")
    await asyncio.sleep(float(0.75))
    await ctx.send("N-word")


'''
@client.command(aliases = ["rps", "RPS", "Rps", "rockpaperscissors", "Rockpaperscissors", "RockPaperScissors", "rockpaperscissor", "Rockpaperscissor", "RockPaperScissor"])
@cooldown(5, 10, BucketType.default)
async def _rpsgame(ctx, user_rps_input):
    print("someone used the rps command")
    bot_rps_list = ["rock", "paper", "scissors"]
    bots_rps_choice = random.choice(bot_rps_list)
    print(f"bot chose {bots_rps_choice} in rps game")

    if user_rps_input == "rock" or "Rock" or "ROCK" or "paper" or "Paper" or "PAPER" or "scissors" or "Scissors" or "SCISSORS" or "scissor" or "Scissor" or "SCISSOR":
        if user_rps_input == bots_rps_choice:
            print("Tied")
            await ctx.send(f"Tie! Your picked {user_rps_input} and I picked {bots_rps_choice} which results in a tie")
        else:
            if user_rps_input == "rock" or "Rock" or "ROCK":
                if bots_rps_choice != "paper":
                    print("Bot lost")
                    await ctx.send(f"You win! You picked {user_rps_input} and I picked {bots_rps_choice}")
                else:
                    print("Bot won")
                    await ctx.send(f"I win! You picked {user_rps_input} and I picked {bots_rps_choice}")

            elif user_rps_input == "paper" or "Paper" or "PAPER":
                if bots_rps_choice != "scissors":
                    print("Bot lost")
                    await ctx.send(f"You win! You picked {user_rps_input} and I picked {bots_rps_choice}")
                else:
                    print("Bot won")
                    await ctx.send(f"I win! You picked {user_rps_input} and I picked {bots_rps_choice}")

            elif user_rps_input == "scissors" or "Scissors" or "SCISSORS" or "scissor" or "Scissor" or "SCISSOR":
                if bots_rps_choice != "paper":
                    print("Bot lost")
                    await ctx.send(f"You win! You picked {user_rps_input} and I picked {bots_rps_choice}")
                else:
                    print("Bot won")
                    await ctx.send(f"I win! You picked {user_rps_input} and I picked {bots_rps_choice}")
    else:
        await ctx.send("Please use a valid syntax! e.g '/rps rock'")
'''


#MEME COMMAND
@client.command(aliases = ["meme", "Meme"])
async def _sendsmeme(ctx):
    random_meme_number = randint(1,5000)
    embed = discord.Embed(
        color = 0x00ff44
    )
    embed.set_image(url = f"https://ctk-api.herokuapp.com/meme/{random_meme_number}")
    await ctx.send(embed = embed)


'''END OF GAME RELATED COMMANDS'''

'''START OF RESPONSES OR RELATED COMMANDS'''


#WELCOME
@client.command(aliases = ["welcome", "Welcome"])
async def _welcomecommand(ctx):
    embed = discord.Embed(
        title = "Welcome!",
        description = "Welcome to the Monarch minecraft server! This is a pre-written message from the server owner, @CaptainVietnam6, Please take a look at #rules and read all of it! We look forward to having you on this server and would love if you were to be active 😀",
        color = 0x00ff44
    )
    await ctx.send(embed = embed)


#DESCRIPTION
@client.command(aliases = ["description", "Description"])
async def _descriptioncommand(ctx):
    embed = discord.Embed(
        title = "Server description",
        description = "This is a Pure Survival Server started on 4/16/20 by @CaptainVietnam6 and has since evolved from a simple small world to a small community filled with great Survival players, builders, and even some speedrunners with world records! Our goal here is to host a small minecraft community for all ages and skill levels! Don't worry if you're not that good at the game, feel free to DM or @ our admins and co-admins for help. Cheats have never been turned on in the server so it's a great way to get achievements! Some of our members have even obtained all the achievements in the game! (That's alot of work and dedication). Anyways if you have any more questions, ping @admin, @co-admin, or @moderator",
        color = 0x00ff44
    )
    await ctx.send(embed = embed)


#BOT DESCRIPTION COMMAND 
@client.command(aliases = ["BotDesc", "botdesc", "BotDescription", "Botdescription", "botdescription"])
async def _botdescription(ctx):
    await ctx.send("Hi! I am a bot known as MonarchBot. I have been programmed by CaptainVietnam6 in Python, JavaScript, and DBscript. My task is to watch over the server!")


#/GOOGLE COMMAND  
@client.command(aliases = ["google", "Google", "GOOGLE"])
async def _googlelinklmao(ctx):
    await ctx.send("<https://searchengineland.com/guide/how-to-use-google-to-search>")


#/DADDY PINGS CAPTAIN
# <a:emoji_name:emoji_id> for animated
@client.command(aliases = ["daddy", "Daddy", "DADDY"])
async def _pingcaptdaddy(ctx):
    await ctx.send("<@467451098735837186> <:capt:803781820234989568>")


#/MOMMY PING ELYSE
@client.command(aliases = ["mommy", "Mommy", "MOMMY"])
async def _pingelysemommy(ctx):
    await ctx.send("<@770836334247018518> <:elyse:803791622139412541>")


#/BENICE SEND FUNNY 'BE NICE TO SERVER STAFF'
@client.command(aliases = ["benice", "Benice", "BeNice"])
async def _benicetoserverstaff(ctx):
    await ctx.send("https://media.discordapp.net/attachments/709672550707363931/721226547817873519/tenor.gif")


#REPLIES SEND THIGH PICS
@client.command(aliases = ["thighpics", "thigh_pics", "thighpic", "thigh_pic"])
async def _thighpics(ctx):
    await ctx.send("send thigh pics uwu")


#MONARCHBOT COUNTS FOR 24 HOURS
@client.command(aliases = ["count", "Count"])
@cooldown(1, 86400, BucketType.default)
async def _count(ctx):
    MB_count = 0
    print("someone activated the count feature")
    while MB_count != 86400:
        await asyncio.sleep(1)
        await ctx.send(MB_count)
        MB_count = MB_count + 1


#SPAM PINGS
@client.command(aliases = ["spam_ping", "Spam_ping", "spamping"])
@cooldown(1, 86400, BucketType.default)
async def _spam_ping(ctx):
    ping_count = 0
    while ping_count != 69415:
        await asyncio.sleep(float(0.1))
        await ctx.send("<@467451098735837186>")
        ping_count = ping_count + 1


#ZERO TWO GIF
@client.command(aliases = ["zerotwo", "02", "ZeroTwo", "zero two", "Zero Two", "Zero two", "Zerotwo"])
async def _zerotwo(ctx):
    await ctx.send("bruh-")
    await asyncio.sleep(float(0.5))
    await ctx.send("https://tenor.com/view/darling-in-the-franxx-zero-two-dance-gif-14732606")
    print("someone's being a simp")
    await asyncio.sleep(float(1.5))
    await ctx.send("fuckin simp....")


#PINGS LANCE
@client.command(aliases = ["lanty", "lance", "lantypanty", "lant"])
async def _lant(ctx):
    await ctx.send("<@499048848165961759>")


#TO DO LIST FOR MONARCHBOT
@client.command(aliases = ["todolist", "tdl", "to do list", "to_do_list", "to.do.list", "TDL"])
async def _tdl(ctx):
    await ctx.send(
        "Your to do list is:\n 1. Create a slur detection and warning system with variables in each word.\n 2. Create a active permanent server for MonarchBot's beta/development phase.\n 3. Create a funny voice chat soundboard for MonarchBot.")


#DICTIONARY COMMAND, GIVES YOU A DICTIONARY LINK TO THE WORD YOU MENTIONED
@client.command(aliases = ["Dictionary", "dictionary", "Dict", "dict"])
@cooldown(3, 30, BucketType.default)
async def _dictionarylink(ctx, user_dictionary_request):
    print(f"Someone used the dictionary command for the word {user_dictionary_request}")
    await ctx.send(f"Getting you the dictionary link for the word {user_dictionary_request}")
    await asyncio.sleep(float(0.5))
    await ctx.send(f"Here you go!\nhttps://www.dictionary.com/browse/{user_dictionary_request}?s=t")


#REPEAT COMMAND; BOT REPEATS AFTER USER
@client.command(aliases = ["repeat", "Repeat", "say", "Say"])
@cooldown(5, 60, BucketType.default)
async def _repeat_after_user(ctx, *, user_repeat_input):
    if "@everyone" in user_repeat_input:
        await ctx.send("Cannot repeat mass ping")
    else:
        if "@here" in user_repeat_input:
            await ctx.send("Cannot repeat mass ping")
        else:
            await ctx.send(f"{user_repeat_input}")


#LEGEND REPLY COMMAND THINGY
@client.command(aliases = ["Legend", "legend"])
async def _legendlol(ctx):
    await ctx.send("WHAT AN ABSOLUTE LEGEND. WHAT A GOD. HOLY SHIT PRAISE THIS MAN HE'S THE GOD OF EVERYTHING HOLY SHIT WOW THAT WAS SO AMAZING EVEN I'M SHOCKED WOW. EVERYONE ON THE EARTH SHOULD PRAISE THIS MAN WOW THAT WAS DAMN GODLY\n")


#TWITCH LINK COMMAND
@client.command(aliases = ["twitch", "Twitch"])
async def _twitchlink(ctx):
    await ctx.send("https://twitch.tv/captainvietnam6")


#EW LIGHTMODE BADDDDDD
@client.command(aliases = ["lightmode", "Lightmode", "discordlightmode", "Discordlightmode"])
@cooldown(1, 5, BucketType.default)
async def _ewlightmode(ctx):
    await ctx.send("eW liGht mOdE bAd DarK MOdE GOoD")


#REPLY SPAM COMMAND
#spams what you type after "/spam" 5 times
@client.command(aliases = ["spam", "Spam"])
@cooldown(1, 60, BucketType.default)
async def _replyspam(ctx, *, user_spam_input):
    print("Someone activated the reply spam command")
    if "@everyone" in user_spam_input:
        await ctx.send("Cannot spam mass ping")
    else:
        if "@here" in user_spam_input:
            await ctx.send("Cannot spam mass ping")
        else:
            for i in range(5):
                await ctx.send(f"{user_spam_input}")
                await asyncio.sleep(float(0.1))
            await asyncio.sleep(float(0.25))
            print("Reply spam command ended")
            await ctx.send("Please wait 60 seconds to use this command again.")


#PRINT COMMAND; SENDS A FANCY EMBED IMAGE WITH AUTHOR'S MESSAGE
@client.command(aliases = ["print", "Print"])
@cooldown(1, 15, BucketType.default)
async def _printmessage(ctx, *, user_print_message):
    embed = discord.Embed(
        color = 0x00ff44
    )
    embed.set_image(url = f"https://flamingtext.com/net-fu/proxy_form.cgi?script=crafts-logo&text={user_print_message}+&_loc=generate&imageoutput=true")
    await ctx.send(embed = embed)


#SENDS SPEEDRUN.COM PROFILE OF USER
@client.command(aliases = ["speedrun", "Speedrun"])
async def _speedrunprofile(ctx, user_speedrun_input):
    await ctx.send(f"Sending {user_speedrun_input}'s profile...")
    await asyncio.sleep(float(1.5))
    await ctx.send(f"https://speedrun.com/user/{user_speedrun_input}")


#DWEAM COMMAND LOL
@client.command(aliases = ["dweam", "Dweam"])
async def _dweamlolcommand(ctx):
    await ctx.send("In this video, me and my friends coded it so that we're all anime cat girls, this was INSANE! To make it harder, we decided to give ourselves nicknames, so in the video we will be calling ourselves Dweam, Gogy and Sapcat. Can we beat Minecraft? You're about to find out. Also only a small percentage of people that watch my videos are actually subscribed so if you end up liking this video consider subscribing, it's free and you can always change your mind in the future, we are getting so close to 69420 million subscribers. Enjoy the video!")


#SEND NOTHING COMMAND
@client.command(aliases = ["nothing"])
async def _sendnothinglol(ctx):
    await ctx.send("⠀⠀⠀⠀⠀")


#DISCORDMOD FUNNY
@client.command(aliases = ["discordmod", "Discordmod"])
async def _funnydiscordmod(ctx):
    await ctx.send("https://i.kym-cdn.com/entries/icons/original/000/035/767/cover4.jpg")


#CUSSWORDS FUNNY
@client.command(aliases = ["cusswords", "cussword", "Cusswords", "Cussword"])
async def _funnycusswords(ctx):
    await ctx.send("no more saying cuss words! it. is. not. good. i'm putting a video on youtube about no more saying cuss words. no more saying cuss words, guys! it's inappropriate, and violent! if you say a cuss word then you're like.... going to jail and you're.. like... when you go to jail.. if u- when you go to jail if you say.. if you say a cuss word you go to jail and when you go to jail, you said a cuss word.. then you're only gonna eat broccoli and other vegetables for your whole life. you don't wanna eat vegetables sometimes people like eating sweets but... i eat broccoli.. so, i'm okay with broccoli but i do not wanna go to jail.")


#FUNNY PINGED
@client.command(aliases = ["pinged", "Pinged"])
async def _funnygotpinged(ctx):
    await ctx.send("I GOT PINGED FUCK SHIT SHIT SHIT MY PC IS GONNA EXPLODE IM GONNA DIE IM GONNA BE HOMLESS NOW WHY DID YOU DO THIS TO ME MY PC MADE A SMALL DING NOISE AHHHHHHHHHHHHHHHHHHHHHHHHHH WHY WHY WHY WHY IM SO SAD YOU BESTOWED THIS ANCIENT FORM OF TORTURE UPON ME YOU SHOULD BE UNMODDED AND BANNED IMMDIATELY WHYYYYYYYYYYYYYYYY")


#SHUT UP COMMAND
@client.command(aliases = ["shut", "Shut"])
async def _shutupcommand(ctx):
    await ctx.send("https://tenor.com/view/meryl-streep-shut-up-yell-gif-15386483")


#LOCATE USER COMMAND
@client.group(aliases = ["locate", "Locate"])
async def _locate(ctx):
    await ctx.send("Do '/locate (user_name)' to locate a server member")

#LOCATE CAPTAINVIETNAM6
@_locate.command(aliases = ["captain", "capt", "Captain", "Capt", "CaptainVietnam6", "captainvietnam6"])
async def _locate_captainvietnam6(ctx):
    await ctx.send("CaptainVietnam6 located in [Hawaii, United States]")

#LOCATE CHICKEN
@_locate.command(aliases = ["chicken", "Chicken", "Chicken01011", "chicken01011"])
async def _locate_chicken(ctx):
    await ctx.send("Chicken01011 located in [Georgia, United States]")

#LOCATE BLUEISH
@_locate.command(aliases = ["blueish", "Blueish"])
async def _locate_blueish(ctx):
    await ctx.send("Blueish located in [Florida, United States]")

#LOCATE CALEB
@_locate.command(aliases = ["caleb", "Caleb", "calabadoodle", "Calabadoodle"])
async def _locate_caleb(ctx):
    await ctx.send("Calabadoodle located in [Hawaii, United States]")

#LOCATE BOLER
@_locate.command(aliases = ["boler", "Boler", "daniel"])
async def _locate_boler(ctx):
    await ctx.send("Boler located in [Hawaii, United States]")

#LOCATE KACTUS
@_locate.command(aliases = ["kactus", "Kactus", "ColdKactus9471", "coldkactus9471"])
async def _locate_kactus(ctx):
    await ctx.send("Kactus located in [Auckland, New Zealand]")

#LOCATE ELYSE
@_locate.command(aliases = ["elyse", "Elyse", "Elyse05"])
async def _locate_elyse(ctx):
    await ctx.send("Elyse located in [Hawaii, United States]")

#LOCATE LANT
@_locate.command(aliases = ["lant", "Lant", "lance", "Lance"])
async def _locate_lance(ctx):
    await ctx.send("Lance located in [Hawaii, United States]")

#LOCATE GARCIA
@_locate.command(aliases = ["garcia", "Garcia", "OGarcia263"])
async def _locate_garcia(ctx):
    await ctx.send("Garica located in [Mississippi, United States]")

#LOCATE NEKO
@_locate.command(aliases = ["neko", "Neko", "NekoGamerGirl03", "nekogamergirl03"])
async def _locate_nekogamergirl(ctx):
    await ctx.send("NekoGamerGirl03 located in [STATE, COUNTRY]")

#LOCATE NEPTUNE
@_locate.command(aliases = ["neptune", "Neptune", "POGGERtune"])
async def _locate_neptune(ctx):
    await ctx.send("Neptune located in [Victoria, Australia]")

#LOCATE BEAR
@_locate.command(aliases = ["bear", "Bear", "Bear4996", "bear4996"])
async def _locate_bear4996(ctx):
    await ctx.send("Bear4996 located in [Hawaii, United States]")


'''
#MINUTEPASSES
@client.command(aliases = ["minutepasses", "minutecount"])
async def _minutepasses(ctx):
    await asyncio.sleep(float(0))
    for i in range(420):
        await asyncio.sleep(float(60))
        await ctx.send("Every 60 seconds, a minute passes...")
'''


#FAIR
@client.listen("on_message")
async def replyping(message):
    if message.author.bot:   #ends command if "fair" is detected from a bot, this stops spam loops
        return
    if "fair" in message.content:   #if "fair" is in a message the member sends, it replies with "fair"
        await message.channel.send("fair")


#POG REPLY
@client.listen("on_message")
async def replypog(message):
    pog_responses = ["pog", "poggers", "pogsss", "pogs", "pogs?"]

    if message.author.bot:
        return
    if "pog" in message.content:
        await message.channel.send(random.choice(pog_responses))
    if "POG" in message.content:
        await message.channel.send(random.choice(pog_responses))
    if "Pog" in message.content:
        await message.channel.send(random.choice(pog_responses))


'''
#CAPT GET PINGED ANGR
@client.listen("on_message")
async def captgetpinged(message):
    if message.author.bot:
        return
    #mobile varient
    if "<@467451098735837186>" in message.content:
        await message.channel.send("<:captgetpinged:805046045472981013><a:WHY_PING:776540275455557652>")
    #PC varient
    if "<@!467451098735837186>" in message.content:
        await message.channel.send("<:captgetpinged:805046045472981013><a:WHY_PING:776540275455557652>")
'''


#ELYSE GET PINGED ANGR
@client.listen("on_message")
async def elysegetpinged(message):
    if message.author.bot:
        return
    #mobile varient
    if "<@770836334247018518>" in message.content:
        await message.channel.send("<:elysegetpinged:805046260310474772><a:WHY_PING:776540275455557652>")
    #PC varient
    if "<@!770836334247018518>" in message.content:
        await message.channel.send("<:elysegetpinged:805046260310474772><a:WHY_PING:776540275455557652>")


#MONARCHBOT GETS PINGED ANGR
@client.listen("on_message")
async def mbgetpiged(message):
    if message.author.bot:
        return
    #mobile varient
    if "<@749200957937549332>" in message.content:
        await message.channel.send("<a:WHY_PING:776540275455557652>")
        await asyncio.sleep(float(0.5))
        await message.channel.send("fuck off why ping")
    #PC varient
    if "<@!749200957937549332>" in message.content:
        await message.channel.send("<a:WHY_PING:776540275455557652>")
        await asyncio.sleep(float(0.5))
        await message.channel.send("fuck off why ping")


'''
#REPLY GOODNIGHT IF SOMEONE SAYS GOODNIGHT OR SIMILAR
@client.listen("on_message")
async def _replygoodnight(message):
    if message.author.bot:
        return
    if "goodnight" in message.content:
        await message.channel.send("goodnight! <:CHONK:802126491927314462>")
    if "Goodnight" in message.content:
        await message.channel.send("goodnight! <:CHONK:802126491927314462>")
    if "gn " in message.content:
        await message.channel.send("goodnight! <:CHONK:802126491927314462>")
    if "Gn" in message.content:
        await message.channel.send("goodnight! <:CHONK:802126491927314462>")
    if "GN" in message.content:
        await message.channel.send("goodnight! <:CHONK:802126491927314462>")
'''


'''
#DETECTS CODE
@client.listen("on_message")
async def _detects_code(message):
    if message.author.bot:
        return
    if "```py" in message.content:
        await message.channel.send("wow python code")
    if "```java" in message.content:
        await message.channel.send("wow java code")
    if "```js" in message.content:
        await message.channel.send("wow JavaScript code")
    if "```javascript" in message.content:
        await message.channel.send("wow JavaScript code")
    if "```ruby" in message.content:
        await message.channel.send("wow ruby code")
    if "```cpp" in message.content:
        await message.channel.send("wow C++ code")
    if "```c++" in message.content:
        await message.channel.send("wow C++ code")
    if "```c" in message.content:
        await message.channel.send("wow C code")
    if "```kotlin" in message.content:
        await message.channel.send("wow kotlin code")
    if "```go" in message.content:
        await message.channel.send("wow go code")
    if "```swift" in message.content:
        await message.channel.send("wow swift code")
    if "```rust" in message.content:
        await message.channel.send("wow rust code")
@client.listen("on_message")
async def _detects_code2(message):
    if message.author.bot:
        return
    if "```html" in message.content:
        await message.channel.send("wow HTML code")
    if "```css" in message.content:
        await message.channel.send("wow CSS code")
'''


'''END OF RESPONSES OR RELATED COMMANDS'''

'''START OF EMOJI RESPONSES COMMANDS'''

#SAMPLE ON MESSAGE CODE
'''
@client.listen("on_message")
async def _(message):
    if message.author.bot:
        return
    if "" in message.content:
        await message.channel.send("")
    if "" in message.content:
        await message.channel.send("")
'''

#SAMPLE RESPONSE COMMAND CODE
'''
@client.command(aliases = ["", ""])
async def _(ctx):
    await ctx.send("")
'''

#FULL SET
'''
@client.listen("on_message")
async def _(message):
    if message.author.bot:
        return
    if "" in message.content:
        await message.channel.send("")
    if "" in message.content:
        await message.channel.send("")

@client.command(aliases = ["", ""])
async def _(ctx):
    await ctx.send("")
'''

'''
#SO FAKE EMOJI
@client.listen("on_message")
async def _sofakeemoji(message):
    if message.author.bot:
        return
    if "fake" in message.content:
        await message.channel.send("<:cv6_so_fake:812995927605903400>")
    if "Fake" in message.content:
        await message.channel.send("<:cv6_so_fake:812995927605903400>")

@client.command(aliases = ["fake", "Fake"])
async def _sofakeemojisend(ctx):
    await ctx.send("<:cv6_so_fake:812995927605903400>")


#DOUBT EMOJI
@client.listen("on_message")
async def _doubtemoji(message):
    if message.author.bot:
        return
    if "Doubt" in message.content:
        await message.channel.send("<:cv6_X_doubt:812995858781438022>")
    if "doubt" in message.content:
        await message.channel.send("<:cv6_X_doubt:812995858781438022>")

@client.command(aliases = ["doubt", "Doubt"])
async def _doubtemojisend(ctx):
    await ctx.send("<:cv6_X_doubt:812995858781438022>")


#STONKS EMOJI
@client.listen("on_message")
async def _stonksemoji(message):
    if message.author.bot:
        return
    if "stonk" in message.content:
        await message.channel.send("<:cv6_stonks:812995837613309992>")
    if "Stonk" in message.content:
        await message.channel.send("<:cv6_stonks:812995837613309992>")

@client.command(aliases = ["stonks", "stonk", "Stonks", "Stonk"])
async def _stonksemojisend(ctx):
    await ctx.send("<:cv6_stonks:812995837613309992>")


#SIMP PILLS EMOJI
@client.listen("on_message")
async def _simppills(message):
    if message.author.bot:
        return
    if "simp" in message.content:
        await message.channel.send("<:cv6_simp_pills:812995814904561695>")
    if "Simp" in message.content:
        await message.channel.send("<:cv6_simp_pills:812995814904561695>")

@client.command(aliases = ["simp", "Simp"])
async def _simppillsemojisend(ctx):
    await ctx.send("<:cv6_simp_pills:812995814904561695>")


#UWU EMOJI
@client.listen("on_message")
async def _uwuemoji(message):
    if message.author.bot:
        return
    if "uwu" in message.content:
        await message.channel.send("uwu daddy smack me harder <:cv6_uwu:812995744247447563>")
    if "UwU" in message.content:
        await message.channel.send("uwu daddy smack me harder <:cv6_uwu:812995744247447563>")

@client.command(aliases = ["uwu", "UwU"])
async def _uwuemojisend(ctx):
    await ctx.send("uwu daddy smack me harder <:cv6_uwu:812995744247447563>")


#WAT EMOJI
@client.command(aliases = ["what", "What", "wat", "Wat"])
async def _watemojisend(ctx):
    await ctx.send("<:cv6_wat:812995793278468117>")


#ADMIN ABOOZ EMOJI
@client.command(aliases = ["abooz", "Abooz"])
async def _adminaboozemojisend(ctx):
    await ctx.send("<:cv6_abooz:812995683740418068>")


#60S TIMER EMOJI
@client.listen("on_message")
async def _timeremoji(message):
    if message.author.bot:
        return
    if "timer" in message.content:
        await message.channel.send("<a:cv6_60s_timer:812995903421022221>")
    if "Timer" in message.content:
        await message.channel.send("<a:cv6_60s_timer:812995903421022221>")

@client.command(aliases = ["timer", "Timer"])
async def _timeremojisend(ctx):
    await ctx.send("<a:cv6_60s_timer:812995903421022221>")


#RACIST EMOJI
@client.listen("on_message")
async def _racistemoji(message):
    if message.author.bot:
        return
    if "racist" in message.content:
        await message.channel.send("<:cv6_rascist:812995663817342986>")
    if "Racist" in message.content:
        await message.channel.send("<:cv6_rascist:812995663817342986>")

@client.command(aliases = ["racist", "Racist"])
async def _racistemojisend(ctx):
    await ctx.send("<:cv6_rascist:812995663817342986>")


#GAY EMOJI
@client.listen("on_message")
async def _gayemoji(message):
    if message.author.bot:
        return
    if "gay" in message.content:
        await message.channel.send("<:cv6_gay:812995646919147550>")
    if "Gay" in message.content:
        await message.channel.send("<:cv6_gay:812995646919147550>")

@client.command(aliases = ["gay", "Gay"])
async def _gayemojisend(ctx):
    await ctx.send("<:cv6_gay:812995646919147550>")


#BISEXUAL EMOJI
@client.listen("on_message")
async def _bisexualemoji(message):
    if message.author.bot:
        return
    if "bisexual" in message.content:
        await message.channel.send("<:cv6_bisexual:812995628950618112>")
    if "Bisexual" in message.content:
        await message.channel.send("<:cv6_bisexual:812995628950618112>")

@client.command(aliases = ["Bisexual", "bisexual", "bi", "Bi"])
async def _bisexualemojisend(ctx):
    await ctx.send("<:cv6_bisexual:812995628950618112>")


#TRANS EMOJI
@client.listen("on_message")
async def _transemoji(message):
    if message.author.bot:
        return
    if "transgender" in message.content:
        await message.channel.send("<:cv6_trans:812995611270840371>")
    if "Transgender" in message.content:
        await message.channel.send("<:cv6_trans:812995611270840371>")
    if "trans" in message.content:
        await message.channel.send("<:cv6_trans:812995611270840371>")
    if "Trans" in message.content:
        await message.channel.send("<:cv6_trans:812995611270840371>")

@client.command(aliases = ["transgender", "Transgender", "Trans", "trans"])
async def _transemojisend(ctx):
    await ctx.send("<:cv6_trans:812995611270840371>")


#POLICE EMOJI
@client.listen("on_message")
async def _policeemoji(message):
    if message.author.bot:
        return
    if "police" in message.content:
        await message.channel.send("<a:cv6_police:812995767639212032>")
    if "Police" in message.content:
        await message.channel.send("<a:cv6_police:812995767639212032>")

@client.command(aliases = ["police", "Police"])
async def _policeemojisend(ctx):
    await ctx.send("<a:cv6_police:812995767639212032>")


#Fspam EMOJI
@client.command(aliases = ["fspam", "Fspam"])
async def _fspamemojisend(ctx):
    await ctx.send("<a:cv6_Fspam:812995726710669342>")


#CLAP EMOJI
@client.command(aliases = ["clap", "Clap"])
async def _clapemojisend(ctx):
    await ctx.send("<a:cv6_clap:812995595613896714>")


#YOU TRIED EMOJI
@client.command(aliases = ["youtried", "Youtried"])
async def _uoutriedemojisend(ctx):
    await ctx.send("<a:cv6_youtried:812995570906038292>")


#PYTHON EMOJI SEND
@client.listen("on_message")
async def _pythonemoji(message):
    if message.author.bot:
        return
    if "python" in message.content:
        await message.channel.send("<a:cv6_python:812995549414162474>")
    if "Python" in message.content:
        await message.channel.send("<a:cv6_python:812995549414162474>")

@client.command(aliases = ["python", "Python"])
async def _pythonemojisend(ctx):
    await ctx.send("<a:cv6_python:812995549414162474>")


#PEPEfog emoji
@client.command(aliases = ["pepepog", "Pepepog"])
async def _pepefogemojisend(ctx):
    await ctx.send("<a:cv6_pepepog:812995528081276958>")
'''


'''END OF EMOJI RESPONSE COMMANDS'''

'''FINAL IMPORTANT FUNCTIONS AND IMPORTANT STUFF'''
#KEEP ALIVE COMMAND FOR WEBSERVER
keep_alive()

#BOT TOKEN TO CONNECT TO DISCORD'S API
client.run(BOT_TOKEN) #token can be found in the file 'BOT_TOKEN.py'
