import os
import time
import logging

from os import getenv
from dotenv import load_dotenv
from logging.handlers import RotatingFileHandler


logging.basicConfig(
    format="[%(asctime)s]:[%(levelname)s]:[%(name)s]:: %(message)s",
    level=logging.INFO,
    datefmt="%H:%M:%S",
    handlers=[
        RotatingFileHandler(
            "logs.txt", maxBytes=(1024 * 1024 * 5), backupCount=10
        ),
        logging.StreamHandler(),
    ],
)

logging.getLogger("httpx").setLevel(logging.ERROR)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("pytgcalls").setLevel(logging.ERROR)


if os.path.exists("Internal"):
   load_dotenv("Internal")


API_ID = 25742938
API_HASH = "b35b715fe8dc0a58e8048988286fc5b6"
BOT_TOKEN = "7114779693:AAHr0QiVmNgwsPGQM8W-pv6VEpItEoW3a5k"
STRING_SESSION = "BAGIzloAuVqc9pUpiCUzz-RhxrSuiTJGdFo4S0qAmxw3JclCDW3Caq4omKt2-cmlvRGZsthmvlaACB5ULFMlqQdpmI4CGHBygYHNnZmdqSEEpFjm8GUtQ3yOLXCJlHdINlP05dwGH1EDzWnTnDFhza_-lGBqa96Vvj1ggwZMHX9ea4M_U7qoKuNqc8N-vM6YVIREZTEAVSB3KZQwTmtS-m7zOwWg-AhV0hE1vNd9sTSxgrIK0Uilv03xoYtRAXRhd4VF6enxkQcfl4crgTrJO6ttUr2SjF5MsYYlfKVCshh1VS9ajcRTavAb1RbEcr62aeSB1w6z9bfVuDRLkRXxLECdmVmDxgAAAAF6nXj9AA"
MONGO_DB_URL = "mongodb+srv://BADMUNDA:BADMYDAD@badhacker.i5nw9na.mongodb.net/"
LOG_GROUP_ID = -1002093247039
OWNER_ID = int(getenv("OWNER_ID", "6898413162"))
OWNER_USERNAME = "@II_BAD_BABY_II"
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6898413162").split()))
ALIVE_PIC = getenv("ALIVE_PIC", "https://telegra.ph/file/09a3948ee0879834f99b5.png")


# OPTIONAL VARIABLES
SESSION_STRING = getenv("SESSION_STRING", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", ". !").split())



# OTHERS VARIABLES

# PM GUARD VARS
PM_GUARD = bool(getenv("PM_GUARD", True))
PM_GUARD_TEXT = getenv("PM_GUARD_TEXT", "**🥀 Hey, I am an advanced & superfast high quality userbot assistant with an upgraded version security system.\n\n🌿 I can't let you message my owner's dm without my owner's permission.\n\n🌺 My owner is offline now, please wait until my owner allows you.\n\n🍂 Please don't spam here, because spamming will force me to block you from my owner id.**")
PM_GUARD_LIMIT = int(getenv("PM_GUARD_LIMIT", 5))



# USERBOT DEFAULT IMAGE
USERBOT_PICTURE = getenv("USERBOT_PICTURE", "https://graph.org/file/1217cb1e402b99fa47fdf.jpg")



# Don't Edit This Codes From This Line

LOGGER = logging.getLogger("Daxx")
runtime = time.time()

FLOODXD = {}
OLD_MSG = {}
PM_LIMIT = {}
PLUGINS = {}
SUDOERS = []


COMMAND_HANDLERS = []
for x in COMMAND_PREFIXES:
    COMMAND_HANDLERS.append(x)
COMMAND_HANDLERS.append('')

