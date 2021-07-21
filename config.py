import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "1762030201:AAFUe2COlYJ2gBHvM-DuFmHK8zqW5n1Q0QI")

    APP_ID = int(os.environ.get("APP_ID", 6))

    API_HASH = os.environ.get("API_HASH", "eb06d4abfb49dc3eeb1aeb98ae0f581e")
