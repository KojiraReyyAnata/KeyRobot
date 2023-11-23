import json
import os
from dotenv import load_dotenv

load_dotenv()


# def get_user_list(config, key):
#     with open(f"{os.getcwd()}/KeyRobot/{config}", "r") as json_file:
#         return json.load(json_file)[key]


# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
class Config(object):
   LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it

   API_ID = int(os.getenv("API_ID", "17250424"))  # integer value, dont use ""
   API_HASH = os.getenv("API_HASH", "753bc98074d420ef57ddf7eb1513162b")
   TOKEN = os.getenv("TOKEN", "6829313514:AAGAOdhcZyUT9msB8enlkhCEsiZExP_z-j0")  # This var used to be API_KEY but it is now TOKEN, adjust accordingly.
   OWNER_ID = os.getenv("OWNER_ID", "935304382")  # If you dont know, run the bot and do /id in your private chat with it, also an integer
   OWNER_USERNAME = os.getenv("OWNER_USERNAME", "Galau912")
   SUPPORT_CHAT = os.getenv("SUPPORT_CHAT", "GokilSupport")  # Your own group for support, do not add the @
   JOIN_LOGGER = os.getenv("JOIN_LOGGER", "-1001961499248")  # Prints any new group the bot is added to, prints just the name and ID.
   EVENT_LOGS = os.getenv("EVENT_LOGS", "-1001961499248")  # Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit
   ERROR_LOGS = os.getenv("ERROR_LOGS", "-1001961499248")  # For capture error logs
    # RECOMMENDED
   SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI", "postgres://vrswzxds:W2GA1-OCqo1KGDYWFYBJMeV12m3RXTM9@bubble.db.elephantsql.com/vrswzxds") # needed for any database modules
   LOAD = []
   NO_LOAD = ["rss", "cleaner", "connection", "math"]
   WEBHOOK = False
   INFOPIC = True
   URL = None
   SPAMWATCH_API = os.getenv("SPAMWATCH_API", None)  # go to support.spamwat.ch to get key
   SPAMWATCH_SUPPORT_CHAT = "@SpamWatchSupport"
   MONGO_DB_URI = os.getenv("MONGO_DB_URI", "mongodb+srv://keyxrobot:gualupabanget@keyxrobot.tzyl5qp.mongodb.net/?retryWrites=true&w=majority")  # Required for any database modules
   MONGO_DB = "keyxrobot"
   MONGO_PORT = "27017"
   ARQ_API = os.getenv("ARQ_API", "PPJZAN-CVFHRQ-QFVBOU-CNESNO-ARQ")  # Get this from @ARQRobot
   ARQ_API_KEY = os.getenv("ARQ_API_KEY", "PPJZAN-CVFHRQ-QFVBOU-CNESNO-ARQ")
   ARQ_API_URL = "https://arq.hamker.in"
   BOT_NAME = "Key x Robot"
   BOT_USERNAME = os.getenv("BOT_USERNAME", "Key_musicbot")
   BOT_ID = os.getenv("BOT_ID", "6829313514")
   OPENWEATHERMAP_ID = "22322"
   

    # OPTIONAL
    ##List of id's -  (not usernames) for users which have sudo access to the bot.
   # DRAGONS = get_user_list("elevated_users.json", "sudos")
    ##List of id's - (not usernames) for developers who will have the same perms as the owner
   DEV_USERS = [816526222]
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
   # DEMONS = get_user_list("elevated_users.json", "supports")
    # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
   # TIGERS = get_user_list("elevated_users.json", "tigers")
   # WOLVES = get_user_list("elevated_users.json", "whitelists")
   DONATION_LINK = None  # EG, paypal
   CERT_PATH = None
   PORT = 5000
   DEL_CMDS = True  # Delete commands that users dont have access to, like delete /ban if a non admin uses it.
   STRICT_GBAN = True
   WORKERS = (
        8  # Number of subthreads to use. Set as number of threads your processor uses
    )
   BAN_STICKER = ""  # banhammer marie sticker id, the bot will send this sticker before banning or kicking a user in chat.
   ALLOW_EXCL = True  # Allow ! commands as well as / (Leave this to true so that blacklist can work)
   CASH_API_KEY = (
        "awoo"  # Get your API key from https://www.alphavantage.co/support/#api-key
    )
   TIME_API_KEY = "awoo"  # Get your API key from https://timezonedb.com/api
   WALL_API = (
        "awoo"  # For wallpapers, get one from https://wall.alphacoders.com/api.php
    )
   AI_API_KEY = "awoo"  # For chatbot, get one from https://coffeehouse.intellivoid.net/dashboard
   HEROKU_API_KEY = "YES"
   REM_BG_API_KEY = "yahoo"
   LASTFM_API_KEY = "yeah"
   CF_API_KEY = "jk"
   HEROKU_APP_NAME = "siap"
   BL_CHATS = []  # List of groups that you want blacklisted.
   SPAMMERS = None
   ALLOW_CHATS = None
   MONGO_DB = "Key x Robot"
   TEMP_DOWNLOAD_DIRECTORY = "./"
   STRING_SESSION = os.getenv("STRING_SESSION", "BQC_AFHdtxAUk-eqpQDVUHbSuTv35ijELZ1SCMvKJGUj2Uiye8vcwhKrbl4-g6mzNsY9bX6PKg7SQXUs-o7SEt9oasiYNOqAZeULaYLSrcca9Q52t28vDxC4w6kkNoBBFYaelaCq8B18UgDX2Qh3baSIVUX7NZ-WWAwJqfZtcMirxe45B6mqnKz_Eu1DHKAbBgCJ0ygvCfZraFqqreKy0XXL4pGmBrCZz3VfrEGBBMIn8cWBZpgYR4CI6-rQ1N1_T0cFqYWDvKGFm3S6oxf9jYovWMe4dyS7rQlnMbmBMFgzQ2G5xlh0D6mOmNFvRteCuvIgNgrniGzip9lsbFgqZkvxAAAAAZcPDeoB")


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
