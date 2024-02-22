import os


class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6995744028:AAEfAuJkdreorU_OsWsRU_w7MFOxQifbDJY")

    APP_ID = int(os.environ.get("APP_ID", "20244703"))

    API_HASH = os.environ.get("API_HASH", "aecd498f68e85c1c925a6a9f95103aee")

    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "onsbase")
