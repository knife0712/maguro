import asyncio
import os

import discord
import yt_dlp
from discord.ext import commands

BOT_TOKEN = os.environ["DISCORD_BOT_TOKEN"]
VOICE_CHANNEL_ID = 839366320691609644

# making bot
# command prefix: ~
bot = commands.Bot(command_prefix=commands.when_mentioned_or("~"))

ydl_opts = {
            "cookiefile": "./nicovideo.jp_cookies.txt",
            #"format": "bestaudio",
            #"outtmpl": "downloaded_music" + ".%(ext)s",
            "postprocessors": [{"key": "FFmpegExtractAudio",
                                "preferredcodec": "mp3",
                                #"preferredquality": "512"
                                },
                            {'key': 'FFmpegMetadata'},
                            ]
            }

ffmpeg_options = {
    'options': '-vn'
}

# 音楽のダウンロードに関するクラス
class YTDLPSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=1):
        super().__init__(source, volume)

        self.data = data
        self.title = data.get("title")
        self.url = data.get("url")

    @classmethod
    async def dl_from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            data = await loop.run_in_executor(None,
                                              lambda: ydl.extract_info(url))

        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]
        filename = data["requested_downloads"][0]["filepath"]

        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)


# 音楽再生にかかわるクラス
class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def join(self, ctx):
        await bot.get_channel(VOICE_CHANNEL_ID).connect()

    @commands.command()
    async def play(self, ctx, *, url):
        async with ctx.typing():
            player = await YTDLPSource.dl_from_url(url, loop=self.bot.loop)
            ctx.voice_client.play(player, after=lambda e: print('Player error: %s' % e) if e else None)

        await ctx.send('Now playing: {}'.format("test"))

    @commands.command()
    async def exit(self, ctx):
        await ctx.voice_client.disconnect()

bot.add_cog(Music(bot))
bot.run(BOT_TOKEN)