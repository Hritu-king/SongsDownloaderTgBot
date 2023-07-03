from pyrogram import Client
import os

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6202509183:AAFWv7jgUeY96gzhdqthVG1vOIxxAJq5jKc")
API_ID = int(os.environ.get("API_ID", "21203142"))
API_HASH = os.environ.get("API_HASH", "64d92910619503d54fdb9d89ccb805a6")

if __name__ == "__main__" :
    plugins = dict(
        root="plugins"
    )
    bot = Client(
        "SongsDownloaderTgBot",
        bot_token=BOT_TOKEN,
        api_hash=API_HASH,
        api_id=API_ID,
        plugins=plugins
    )
    bot.run()
