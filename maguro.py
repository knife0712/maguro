import os # 基本機能

import discord # ディスコードの基本機能

# Botのトークンを取得
BOT_TOKEN = os.environ["DISCORD_BOT_TOKEN"]

# クライアントオブジェクトを生成
# これが無いとサーバーにアクセスできない
client = discord.Client()

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # 寿司の絵文字が送られてきたとき
    if "\N{SUSHI}" in message.content:
        # :yum: の絵文字を返す
        await message.channel.send("\N{FACE SAVOURING DELICIOUS FOOD}")
        
    # 受け取ったメッセージが自分に対するメンションだった場合
    #if client.user.mentioned_in(message):


# Botの起動とDiscordサーバーへの接続
client.run(BOT_TOKEN)
