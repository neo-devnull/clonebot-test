import os
import logging
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def get_config(key, cast=str):
    try:
        val = os.environ[key]
    except KeyError:
        exit(f'Please define {key} as part of env vars')

    try:
        return cast(val)
    except ValueError:
        exit(f'Invalid value type for {key}')


class Config(object):
    TG_BOT_TOKEN = get_config('TG_BOT_TOKEN')

    API_ID = get_config('API_ID', cast=int)
    API_HASH = get_config('API_HASH', cast=str)

    AUTH_USERS = get_config('AUTH_USERS', cast=str).split()
    AUTH_USERS = set(int(x) for x in AUTH_USERS)
    print(AUTH_USERS)
    TG_USER_SESSION = get_config('TG_USER_SESSION', cast=str)

    DB_URI = get_config('DATABASE_URL', cast=str)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
