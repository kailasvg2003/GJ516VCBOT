from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "17059958"))
API_HASH = getenv("API_HASH", "61f1dff818fccd96e77db4477f360d0d")
BOT_TOKEN = getenv("BOT_TOKEN", 5948256402:AAFYmXHFnHpPmS2TszfToy26DEuGISvGatY)
BOT_NAME = getenv("BOT_NAME","GJ516 MUSIC BOT")
BOT_USERNAME = getenv("BOT_USERNAME", "Darshana_Music_Bot")
OWNER_USERNAME = getenv("OWNER_USERNAME", "Kailas_vg")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "karikku_chatting_group")
CHANNEL_UPDATES = getenv("CHANNEL_UPDATES", "pk_links")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/cb2763a4fd9af49b26cb0.jpg")
PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/262e434f76a5f2e414178.jpg")
SESSION_NAME = getenv("SESSION_NAME", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "? ~ + • / ! ^ .").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5428019786").split()))
