#
# Copyright (C) 2021-2022 by Toni880@Github, < https://github.com/Toni880 >.
#
# This file is part of < https://github.com/Toni880/AyaMusic > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/Toni880/AyaMusic/blob/master/LICENSE >
#
# All rights reserved.

import re
import sys
import os

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get it from my.telegram.org
API_ID = int(os.getenv("API_ID", "1634450"))
API_HASH = os.getenv("API_HASH", "1a42e816cae8d86e71a4c466bba19b8c")

## Get it from @Botfather in Telegram.
BOT_TOKEN = os.getenv("BOT_TOKEN", "6829313514:AAGAOdhcZyUT9msB8enlkhCEsiZExP_z-j0")

# Database to save your chats and stats... Get MongoDB:-  https://telegra.ph/How-To-get-"Mongodb"-URI-04-06
MONGO_DB_URI = os.getenv("MONGO_DB_URI", "mongodb+srv://keyxrobot:gualupabanget@keyxrobot.tzyl5qp.mongodb.net/?retryWrites=true&w=majority")

JOIN = os.getenv("JOIN", "SquirtInYourPussy")

# Custom max audio(music) duration for voice chat. set DURATION_LIMIT in variables with your own time(mins), Default to 60 mins.
DURATION_LIMIT_MIN = int(
    os.getenv("DURATION_LIMIT", "5000000000000000")
)  # Remember to give value in Minutes

# Duration Limit for downloading Songs in MP3 or MP4 format from bot
SONG_DOWNLOAD_DURATION = int(
    os.getenv("SONG_DOWNLOAD_DURATION_LIMIT", "144000")
)  # Remember to give value in Minutes

# You'll need a Private Group ID for this.
LOG_GROUP_ID = int(os.getenv("LOG_GROUP_ID", "-1001961499248"))

# A name for your Music bot.
MUSIC_BOT_NAME = os.getenv("MUSIC_BOT_NAME", "Key X Robot")

# Your User ID.
OWNER_ID = int(os.getenv("OWNER_ID", "935304382"))  # Input type must be interger

# JANGAN HAPUS YA KONTOL



# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = os.getenv("HEROKU_API_KEY")

# You have to Enter the app name which you gave to identify your  Music Bot in Heroku.
HEROKU_APP_NAME = os.getenv("HEROKU_APP_NAME")

# For customized or modified Repository
UPSTREAM_REPO = os.getenv(
    "UPSTREAM_REPO",
    "https://github.com/KojiraReyyAnata/KeyRobot",
)
UPSTREAM_BRANCH = os.getenv("UPSTREAM_BRANCH", "robot")

# GIT TOKEN ( if your edited repo is private)
GIT_TOKEN = os.getenv("GIT_TOKEN", None)

# Only  Links formats are  accepted for this Var value.
SUPPORT_CHANNEL = os.getenv(
    "SUPPORT_CHANNEL", "https://t.me/Geninstore"
)  # Example:- https://t.me/TheYukki
SUPPORT_GROUP = os.getenv(
    "SUPPORT_GROUP", "https://t.me/KeySupport1"
)  # Example:- https://t.me/YukkiSupport

# Set it in True if you want to leave your assistant after a certain amount of time. [Set time via AUTO_LEAVE_ASSISTANT_TIME]
AUTO_LEAVING_ASSISTANT = os.getenv("AUTO_LEAVING_ASSISTANT", None)

# Time after which you're assistant account will leave chats automatically.
AUTO_LEAVE_ASSISTANT_TIME = int(
    os.getenv("ASSISTANT_LEAVE_TIME", "7200")
)  # Remember to give value in Seconds

# Time after which bot will suggest random chats about bot commands.
AUTO_SUGGESTION_TIME = int(
    os.getenv("AUTO_SUGGESTION_TIME", "180")
)  # Remember to give value in Seconds

# Set it True if you want to delete downloads after the music playout ends from your downloads folder
AUTO_DOWNLOADS_CLEAR = os.getenv("AUTO_DOWNLOADS_CLEAR", None)

# Set it True if you want to bot to suggest about bot commands to random chats of your bots.
AUTO_SUGGESTION_MODE = os.getenv("AUTO_SUGGESTION_MODE", None)

# Set it true if you want your bot to be private only [You'll need to allow CHAT_ID via /authorise command then only your bot will play music in that chat.]
PRIVATE_BOT_MODE = os.getenv("PRIVATE_BOT_MODE", None)

# Time sleep duration For Youtube Downloader
YOUTUBE_DOWNLOAD_EDIT_SLEEP = int(os.getenv("YOUTUBE_EDIT_SLEEP", "15000"))

# Time sleep duration For Telegram Downloader
TELEGRAM_DOWNLOAD_EDIT_SLEEP = int(os.getenv("TELEGRAM_EDIT_SLEEP", "15000"))

# Your Github Repo.. Will be shown on /start Command
GITHUB_REPO = os.getenv("GITHUB_REPO", "https://github.com/KojiraReyyAnata/KeyRobot")

# Spotify Client.. Get it from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")


# Maximum number of video calls allowed on bot. You can later set it via /set_video_limit on telegram
VIDEO_STREAM_LIMIT = int(os.getenv("VIDEO_STREAM_LIMIT", "500"))

# Maximum Limit Allowed for users to save playlists on bot's server
SERVER_PLAYLIST_LIMIT = int(os.getenv("SERVER_PLAYLIST_LIMIT", "500"))

# MaximuM limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(os.getenv("PLAYLIST_FETCH_LIMIT", "500"))

# Cleanmode time after which bot will delete its old messages from chats
CLEANMODE_DELETE_MINS = int(
    os.getenv("CLEANMODE_MINS", "7200")
)  # Remember to give value in Seconds


# Telegram audio  and video file size limit

TG_AUDIO_FILESIZE_LIMIT = int(
    os.getenv("TG_AUDIO_FILESIZE_LIMIT", "5000000000000000")
)  # Remember to give value in bytes

TG_VIDEO_FILESIZE_LIMIT = int(
    os.getenv("TG_VIDEO_FILESIZE_LIMIT", "5000000000000000")
)  # Remember to give value in bytes

# Chceckout https://www.gbmb.org/mb-to-bytes  for converting mb to bytes


# You'll need a Pyrogram String Session for these vars. Generate String from our session generator bot @YukkiStringBot
STRING1 = os.getenv("STRING1", "AQAY8JIAGh6oqeWTDYMH-h3gBSZTTw_DKTZFA92QNLGhv2lG4yAD5PBvx05xrMwIrUs9IEnkHttf0IpTLSAStK9mXHJY95RmhZWtlB-og-JuBj5JLKJqPA3aT5Fcf5DPJxEMveIweQPS_Uic26I473ttnvjlwO0jJjgJ5MuTW5z2OHbCuFlCE1uhtVWlw0OhJRI1VFOmoPzZGjenM6wnpYlZxmPoAgRcducV-QLj86kRO-9xGSumt1VZnEhERD2RWUILF_kHativc-B3No1-qIyABWzFxRcbIkUxZ9BmaX4Fodfq9YG-ulKr6A1Pco3LdkuLFdfEUD7ExL2kal-hTUHH19iA8wAAAAGL6MYjAA")
STRING2 = os.getenv("STRING2", None)
STRING3 = os.getenv("STRING3", None)
STRING4 = os.getenv("STRING4", None)
STRING5 = os.getenv("STRING5", None)
STRING6 = os.getenv("STRING6", None)
STRING7 = os.getenv("STRING7", None)
STRING8 = os.getenv("STRING8", None)
STRING9 = os.getenv("STRING9", None)
STRING10 = os.getenv("STRING10", None)

### DONT TOUCH or EDIT codes after this line
BANNED_USERS = filters.user()
YTDOWNLOADER = 1
LOG = 2
LOG_FILE_NAME = "logs.txt"
adminlist = {}
lyrical = {}
chatstats = {}
userstats = {}
clean = {}

autoclean = []


# Images
START_IMG_URL = os.getenv("START_IMG_URL", None)

PING_IMG_URL = os.getenv(
    "PING_IMG_URL",
    "https://graph.org/file/d9d88e4ed3112acab81d5.jpg",
)

PLAYLIST_IMG_URL = os.getenv(
    "PLAYLIST_IMG_URL",
    "https://graph.org/file/d9d88e4ed3112acab81d5.jpg",
)

GLOBAL_IMG_URL = os.getenv(
    "GLOBAL_IMG_URL",
    "https://graph.org/file/d9d88e4ed3112acab81d5.jpg",
)

STATS_IMG_URL = os.getenv(
    "STATS_IMG_URL",
    "https://graph.org/file/d9d88e4ed3112acab81d5.jpg",
)

TELEGRAM_AUDIO_URL = os.getenv(
    "TELEGRAM_AUDIO_URL",
    "https://graph.org/file/d9d88e4ed3112acab81d5.jpg",
)

TELEGRAM_VIDEO_URL = os.getenv(
    "TELEGRAM_VIDEO_URL",
    "https://graph.org/file/d9d88e4ed3112acab81d5.jpg",
)

STREAM_IMG_URL = os.getenv(
    "STREAM_IMG_URL",
    "https://graph.org/file/d9d88e4ed3112acab81d5.jpg",
)

SOUNCLOUD_IMG_URL = os.getenv(
    "SOUNCLOUD_IMG_URL",
    "https://graph.org/file/d9d88e4ed3112acab81d5.jpg",
)

YOUTUBE_IMG_URL = os.getenv(
    "YOUTUBE_IMG_URL",
    "https://graph.org/file/d9d88e4ed3112acab81d5.jpg",
)

SPOTIFY_ARTIST_IMG_URL = os.getenv(
    "SPOTIFY_ARTIST_IMG_URL",
    "https://graph.org/file/d9d88e4ed3112acab81d5.jpg",
)

SPOTIFY_ALBUM_IMG_URL = os.getenv(
    "SPOTIFY_ALBUM_IMG_URL",
    "https://graph.org/file/d9d88e4ed3112acab81d5.jpg",
)

SPOTIFY_PLAYLIST_IMG_URL = os.getenv(
    "SPOTIFY_PLAYLIST_IMG_URL",
    "https://graph.org/file/d9d88e4ed3112acab81d5.jpg",
)


def time_to_seconds(time):
    stringt = str(time)
    return sum(
        int(x) * 60**i
        for i, x in enumerate(reversed(stringt.split(":")))
    )


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00")
)

if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        print(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )
        sys.exit()

if SUPPORT_GROUP:
    if not re.match("(?:http|https)://", SUPPORT_GROUP):
        print(
            "[ERROR] - Your SUPPORT_GROUP url is wrong. Please ensure that it starts with https://"
        )
        sys.exit()

if UPSTREAM_REPO:
    if not re.match("(?:http|https)://", UPSTREAM_REPO):
        print(
            "[ERROR] - Your UPSTREAM_REPO url is wrong. Please ensure that it starts with https://"
        )
        sys.exit()

if GITHUB_REPO:
    if not re.match("(?:http|https)://", GITHUB_REPO):
        print(
            "[ERROR] - Your GITHUB_REPO url is wrong. Please ensure that it starts with https://"
        )
        sys.exit()


if PING_IMG_URL:
    if PING_IMG_URL != "https://graph.org/file/d9d88e4ed3112acab81d5.jpg":
        if not re.match("(?:http|https)://", PING_IMG_URL):
            print(
                "[ERROR] - Your PING_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()

if PLAYLIST_IMG_URL:
    if PLAYLIST_IMG_URL != "https://graph.org/file/d9d88e4ed3112acab81d5.jpg":
        if not re.match("(?:http|https)://", PLAYLIST_IMG_URL):
            print(
                "[ERROR] - Your PLAYLIST_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()

if GLOBAL_IMG_URL:
    if GLOBAL_IMG_URL != "https://graph.org/file/d9d88e4ed3112acab81d5.jpg":
        if not re.match("(?:http|https)://", GLOBAL_IMG_URL):
            print(
                "[ERROR] - Your GLOBAL_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if STATS_IMG_URL:
    if STATS_IMG_URL != "https://graph.org/file/d9d88e4ed3112acab81d5.jpg":
        if not re.match("(?:http|https)://", STATS_IMG_URL):
            print(
                "[ERROR] - Your STATS_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if TELEGRAM_AUDIO_URL:
    if TELEGRAM_AUDIO_URL != "https://graph.org/file/d9d88e4ed3112acab81d5.jpg":
        if not re.match("(?:http|https)://", TELEGRAM_AUDIO_URL):
            print(
                "[ERROR] - Your TELEGRAM_AUDIO_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if STREAM_IMG_URL:
    if STREAM_IMG_URL != "https://graph.org/file/d9d88e4ed3112acab81d5.jpg":
        if not re.match("(?:http|https)://", STREAM_IMG_URL):
            print(
                "[ERROR] - Your STREAM_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if SOUNCLOUD_IMG_URL:
    if SOUNCLOUD_IMG_URL != "https://graph.org/file/d9d88e4ed3112acab81d5.jpg":
        if not re.match("(?:http|https)://", SOUNCLOUD_IMG_URL):
            print(
                "[ERROR] - Your SOUNCLOUD_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()

if YOUTUBE_IMG_URL:
    if YOUTUBE_IMG_URL != "https://graph.org/file/d9d88e4ed3112acab81d5.jpg":
        if not re.match("(?:http|https)://", YOUTUBE_IMG_URL):
            print(
                "[ERROR] - Your YOUTUBE_IMG_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if TELEGRAM_VIDEO_URL:
    if TELEGRAM_VIDEO_URL != "https://graph.org/file/d9d88e4ed3112acab81d5.jpg":
        if not re.match("(?:http|https)://", TELEGRAM_VIDEO_URL):
            print(
                "[ERROR] - Your TELEGRAM_VIDEO_URL url is wrong. Please ensure that it starts with https://"
            )
            sys.exit()


if not MUSIC_BOT_NAME.isascii():
    print(
        "[ERROR] - You've defined MUSIC_BOT_NAME wrong. Please don't use any special characters or Special font for this... Keep it simple and small."
    )
    sys.exit()
