import sys
from user import User
from pyrogram import Client
from presets import Presets as Msg
from pyrogram.enums import ParseMode


from config import Config
from config import LOGGER


class Bot(Client):
    USER: User = None
    USER_ID: int = None

    def __init__(self):
        super().__init__(
            name="bot_session",
            api_hash=Config.API_HASH,
            api_id=Config.API_ID,
            bot_token=Config.TG_BOT_TOKEN,
            sleep_threshold=30,
            workers=8,
            plugins={
                "root": "plugins"
            }
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        usr_bot_me = await self.get_me()
        self.set_parse_mode(ParseMode.HTML)
        self.LOGGER(__name__).info(
            f"@{usr_bot_me.username}  started! "
        )
        self.USER, self.USER_ID = await User().start()
        try:
            await self.USER.send_message(usr_bot_me.username,
                                         "%session_start%")
        except Exception as e:
            print(str(e))
            print(Msg.BOT_BLOCKED_MSG)
            sys.exit(str(e))

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot stopped. Bye.")
