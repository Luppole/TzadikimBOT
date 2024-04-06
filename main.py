import discord
from discord.ext import commands
import base64
import urllib.parse
import re
import requests
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

import db
import functions

intents = discord.Intents.default()
intents.message_content = True
help_command = commands.DefaultHelpCommand(no_category='Commands')
bot = commands.Bot(command_prefix='!', intents=intents, help_command=None)

SUPERVISOR_ROLE_ID = 1148530335550804018

@bot.command(name='64enc', description="Encoding a text using Base64", category="Encoding", help_command=help_command)
async def encode64(ctx, *, text):
    encoded_text = functions.b64enc(text)
    await ctx.send(f"Original Text: {text}\nBase64 Encoded: {encoded_text}")


@bot.command(name='64dec')
async def decode64(ctx, *, text):
    encoded_text = functions.b64dec(text)
    await ctx.send(f"Original Text: {text}\nBase64 Decoded: {encoded_text}")


@bot.command(name='32enc')
async def encode64(ctx, *, text):
    encoded_text = functions.b32enc(text)
    await ctx.send(f"Original Text: {text}\nBase32 Encoded: {encoded_text}")


@bot.command(name='32dec')
async def decode64(ctx, *, text):
    encoded_text = functions.b32dec(text)
    await ctx.send(f"Original Text: {text}\nBase32 Decoded: {encoded_text}")


@bot.command(name='cyc')
async def cyclic_gen(ctx, *, num):
    text = functions.cyclic(int(num))
    await ctx.send(text)


@bot.command(name='cycfind')
async def cyclic_find(ctx, string: str, substring: str):
    text = functions.locate_cyclic(string, substring)
    await ctx.send(text)


@bot.command(name='urlenc')
async def url_enc(ctx, *, url):
    text = functions.encode_url(url)
    await ctx.send(text)


@bot.command(name='urldec')
async def url_dec(ctx, *, url):
    text = functions.decode_url(url)
    await ctx.send(text)


@bot.command(name='hextobin')
async def hex_to_bin(ctx, *, text):
    encoded_text = functions.hex_to_bin(text)
    await ctx.send(f"Original Text: {text}\nBinary Value: {encoded_text}")


@bot.command(name='bintohex')
async def bin_to_hex(ctx, *, text):
    encoded_text = functions.bin_to_hex(text)
    await ctx.send(f"Original Text: {text}\nHexadecimal Value: {encoded_text}")


@bot.command(name='hextodec')
async def hex_to_dec(ctx, *, text):
    encoded_text = functions.hex_to_dec(text)
    await ctx.send(f"Original Text: {text}\nDecimal Value: {encoded_text}")


@bot.command(name='dectohex')
async def dec_to_hex(ctx, *, text):
    encoded_text = functions.dec_to_hex(text)
    await ctx.send(f"Original Text: {text}\nHexadecimal Value: {encoded_text}")


@bot.command(name='bintostr')
async def bin_to_str(ctx, *, text):
    encoded_text = bin_to_str(text)
    await ctx.send(f"Original Text: {text}\nString: {encoded_text}")


@bot.command(name='strtobin')
async def str_to_str(ctx, *, text):
    encoded_text = functions.str_to_bin(text)
    await ctx.send(f"Original Text: {text}\nBinary Value: {encoded_text}")


@bot.command(name="ctfs")
async def get_ctf(ctx):
    events = functions.get_ctf_events()
    events_tostring = ""
    if events:
        for i in range(5):
            dt_str = events[i]['start']
            dt = datetime.fromisoformat(dt_str)
            dt_local = dt.astimezone(ZoneInfo("Asia/Jerusalem"))
            formatted_dt = dt_local.strftime("%Y-%m-%d - %H:%M")
            events_tostring += f"{i+1}. "
            events_tostring += f"**{events[i]['title']}**: "
            events_tostring += formatted_dt
            events_tostring += "\n"
    await ctx.send("These are the 5 upcoming events: \n")
    await ctx.send(events_tostring)


@bot.command(name="team")
async def get_ctf(ctx):
    info = functions.team_info()
    name = info["name"]
    world_rating = info["rating"]["2024"]["rating_place"]
    country_rating = info["rating"]["2024"]["country_place"]
    country = info["country"]
    info_tostring = f"Name: **{name}** \n World Rating: **{world_rating}** \n Country Rating: **{country_rating}** \n Country: **{country}**"
    await ctx.send(info_tostring)

@bot.command(name="jwtdec")
async def jwt_dec(ctx, string: str, key: str):
    info = functions.jwtdec(string, key)
    await ctx.send(info)

@bot.command(name="hash")
async def hashing(ctx, *, string):
    info = functions.hash_text(string)
    await ctx.send(info)
@bot.command(name="commands")
async def help_command(ctx):
    embed = discord.Embed(
        title="Command List",
        description="The list of the commands the bot can execute. The prefix is - '!'",
        color=discord.Color.default()
    )

    embed.add_field(name='\u200b', value="ENCODERS", inline=False)
    embed.add_field(name="64enc", value="Encoding a string using Base64", inline=False)
    embed.add_field(name="32enc", value="Encoding a string using Base32", inline=False)
    embed.add_field(name="urlenc", value="Encoding a URL", inline=False)

    embed.add_field(name='\u200b', value="DECODERS", inline=False)
    embed.add_field(name="64dec", value="Decoding a string that's encoded using Base64", inline=False)
    embed.add_field(name="32dec", value="Decoding a string that's encoded using Base32", inline=False)
    embed.add_field(name="urldec", value="Decoding a URL", inline=False)

    embed.add_field(name='\u200b', value="GENERATORS", inline=False)
    embed.add_field(name="cyc", value="Generating a cyclic pattern", inline=False)
    embed.add_field(name="cycfind", value="Finding a subs in a cyclic pattern", inline=False)

    embed.add_field(name='\u200b', value="Misc", inline=False)
    embed.add_field(name="team", value="Printing the team's stats", inline=False)
    embed.add_field(name="ctfs", value="Printing the 5 upcoming CTF contests", inline=False)

    embed.set_footer(text="Luppole Made This")

    await ctx.send(embed=embed)

@bot.command(name="addplayer")
@commands.check(lambda ctx: functions.has_role(ctx.author, SUPERVISOR_ROLE_ID))
async def add_player_to_db(ctx, *, name):
    db.add_player(name)
    await ctx.send(f"A player named: **{name}** was successfuly added into the database!")



@bot.hybrid_command(name="ping", description="mmmmmmmm")
async def ping(ctx):
    await ctx.reply("Pong!")

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f'{bot.user} has connected to Discord!')

# Run the bot with the token
bot.run('TOKEN')
