from config import Config
from pyrogram import Client


if __name__ == '__main__':
    with Client('', Config.API_ID, Config.API_HASH) as app:
        print(app.export_session_string())
