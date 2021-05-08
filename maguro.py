import os # 基本機能

import discord # ディスコードの基本機能

# Botのトークンを取得
BOT_TOKEN = os.environ["DISCORD_BOT_TOKEN"]

# クライアントオブジェクトを生成
# これが無いとサーバーにアクセスできない
client = discord.Client()

# Botの起動とDiscordサーバーへの接続
client.run(BOT_TOKEN)
