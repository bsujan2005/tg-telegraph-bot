import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "1835229655:AAEdRAK_nfOpawP5ed11N2jcn-02O2qcg0E")

    APP_ID = int(os.environ.get("APP_ID", 1850430))

    API_HASH = os.environ.get("API_HASH", "34855281cec673005fcbd7af5ce6fd1d")
