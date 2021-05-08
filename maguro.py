import os # 基本機能
import datetime # 時刻に関する機能

import discord # ディスコードの基本機能

TEXT_CHANNEL_ID = 839366320691609643
MAGURO_CHANNEL_ID = 840513454497595392

# Botのトークンを取得
BOT_TOKEN = os.environ["DISCORD_BOT_TOKEN"]

# intents の設定
# 一部のイベントを受け取らない設定ができるらしい
# とりあえずすべてのイベントを受け取る設定
intents = discord.Intents.default()
intents=discord.Intents.all()
# クライアントオブジェクトを生成
# これが無いとサーバーにアクセスできない
client = discord.Client(intents=intents)

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    # 自分自身のメッセージに反応しないようにするため
    if message.author.bot:
        return

    # 寿司の絵文字が送られてきたとき
    if "\N{SUSHI}" in message.content:
        # :yum: の絵文字を返す
        await message.channel.send("\N{FACE SAVOURING DELICIOUS FOOD}")

    # 受け取ったメッセージが自分に対するメンションだった場合
    if client.user.mentioned_in(message):
        # "マグロちゃん" がメッセージ中に入っていた場合
        if "マグロちゃん" in message.content:
            # 寿司を提供する
            await message.channel.send("へいおまちっ！" + "\N{SUSHI}")

@client.event
async def on_member_update(before, after):
    # ステータスの変化を日本語にするための変換表
    status_table = {"online":"オンライン" ,"idle":"退席中", "dnd":"取り込み中", "offline":"オフライン"}
    # メッセージを送信するチャンネル
    channel = client.get_channel(MAGURO_CHANNEL_ID)
    # 現在時刻（サーバーの関係で9時間ずれているので補正）
    current_datetime = datetime.datetime.now()+datetime.timedelta(hours=9)

    # 本日が土日である場合
    if current_datetime.weekday() == (5 or 6):
        # 現在時刻が13時以降21時未満である場合
        if ((13 <= current_datetime.hour) and (current_datetime.hour <= 21)):
            if status_table[str(after.status)] == "オフライン":
                await channel.send(after.name + " さんがお休みになられました") 

            if (status_table[str(before.status)] == "オフライン") and (status_table[str(after.status)] == "オンライン"):
                await channel.send(after.name + " さんがお目覚めになられました")

# Botの起動とDiscordサーバーへの接続
client.run(BOT_TOKEN)
