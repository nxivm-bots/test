import os
import logging
from logging.handlers import RotatingFileHandler




BOT_TOKEN = os.environ.get("BOT_TOKEN", "7085020018:AAGrnB-Y_plJPdjXQLc-uVW4JVB1j0KoygE")
API_ID = int(os.environ.get("API_ID", "29872536"))
API_HASH = os.environ.get("API_HASH", "65e1f714a47c0879734553dc460e98d6")


OWNER_ID = int(os.environ.get("OWNER_ID", "6698364560"))
DB_URL = os.environ.get("DB_URL", "mongodb+srv://kratosnigger:GuH0qHewCzuynCE4@telegram.mhwll.mongodb.net/")
DB_NAME = os.environ.get("DB_NAME", "chizuru")


CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002227030160"))
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002471585487"))
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "-1001830521798"))
FORCE_SUB_CHANNEL3 = int(os.environ.get("FORCE_SUB_CHANNEL3", "-1001632411176"))
FORCE_SUB_CHANNEL4 = int(os.environ.get("FORCE_SUB_CHANNEL4", "-1002263370852"))


FILE_AUTO_DELETE = int(os.getenv("FILE_AUTO_DELETE", "1800")) # auto delete in seconds


PORT = os.environ.get("PORT", "9000")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))



try:
    ADMINS=[1110013191]
    for x in (os.environ.get("ADMINS", "1110013191").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")









CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

DISABLE_CHANNEL_BUTTON = True if os.environ.get('DISABLE_CHANNEL_BUTTON', "True") == "True" else False

BOT_STATS_TEXT = "<b>BOT UPTIME :</b>\n{uptime}"







USER_REPLY_TEXT = "❌Don't Send Me Messages Directly I'm Only File Share Bot !"

START_MSG = os.environ.get("START_MESSAGE", "Hello {mention}\n\nI Can Store Private Files In Specified Channel And Other Users Can Access It From Special Link.")

FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {mention}\n\n<b>You Need To Join Our Channels To Use Me.\n\nKindly Join Our Channels</b>")





ADMINS.append(OWNER_ID)
ADMINS.append(6698364560)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
   





# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Backup Channel @JishuBotz
# Developer @JishuDeveloper
