# ディスコードの機能が入っているモジュールをインポートする
import discord

# Botのトークンを取得
BOT_TOKEN = "ODM5MzkxMjQ4ODI4ODU4Mzc4.YJI-BA.UCQKfue37fO6I7S_C8avRI31PR0"

# クライアントオブジェクトを生成
# これが無いとサーバーにアクセスできない
client = discord.Client()

# Botの起動とDiscordサーバーへの接続
client.run(BOT_TOKEN)