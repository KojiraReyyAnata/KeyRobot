from NayaMusic.core.bot import AyaBot
from NayaMusic.core.dir import dirr
from NayaMusic.core.git import git
from NayaMusic.core.userbot import Userbot
from NayaMusic.misc import dbb, heroku

from .logging import LOGGER

# Directories
dirr()

# Check Git Updates
git()

# Initialize Memory DB
dbb()

# Heroku APP
heroku()

# Bot Client
app = AyaBot()

# Assistant Client
userbot = Userbot()

from .platforms import *

YouTube = YouTubeAPI()
Carbon = CarbonAPI()
Spotify = SpotifyAPI()
Apple = AppleAPI()
Resso = RessoAPI()
SoundCloud = SoundAPI()
Telegram = TeleAPI()
