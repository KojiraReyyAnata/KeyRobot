import random
import math
from pyrogram.types import InlineKeyboardButton
from config import *
from NayaMusic.utils.formatters import time_to_seconds

def stream_markup_timer(_, videoid, chat_id, played, dur):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)
    percentage = (played_sec / duration_sec) * 100
    naya = math.floor(percentage)
    if 0 < naya <= 10:
        bar = "◯───────────"
    elif 10 < naya < 20:
        bar = "─◯──────────"
    elif 20 <= naya < 30:
        bar = "──◯─────────"
    elif 30 <= naya < 40:
        bar = "───◯────────"
    elif 40 <= naya < 50:
        bar = "────◯───────"
    elif 50 <= naya < 60:
        bar = "─────◯──────"
    elif 60 <= naya < 70:
        bar = "──────◯─────"
    elif 70 <= naya < 80:
        bar = "───────◯────"
    elif 80 <= naya < 95:
        bar = "────────◯───"
    elif 95 <= naya < 100:
        bar = "─────────◯──"
    else:
        bar = "───────────◯"
        
    buttons = [
        [
            InlineKeyboardButton(
                text=f"{played} {bar} {dur}",
                callback_data="GetTimer",
            )
        ],
        [
            InlineKeyboardButton(
                text=_["KY_1"], 
                url=f"https://t.me/kontenfilm",
            ),
            InlineKeyboardButton(
                text=_["KY_2"],
                callback_data=f"PanelMarkup {videoid}|{chat_id}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSEMENU_BUTTON"], callback_data="close"
            )
        ],
    ]
    return buttons


def telegram_markup_timer(_, chat_id, played, dur):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)
    percentage = (played_sec / duration_sec) * 100
    naya = math.floor(percentage)
    if 0 < naya <= 10:
        bar = "◯───────────"
    elif 10 < naya < 20:
        bar = "─◯──────────"
    elif 20 <= naya < 30:
        bar = "──◯─────────"
    elif 30 <= naya < 40:
        bar = "───◯────────"
    elif 40 <= naya < 50:
        bar = "────◯───────"
    elif 50 <= naya < 60:
        bar = "─────◯──────"
    elif 60 <= naya < 70:
        bar = "──────◯─────"
    elif 70 <= naya < 80:
        bar = "───────◯────"
    elif 80 <= naya < 95:
        bar = "────────◯───"
    elif 95 <= naya < 100:
        bar = "─────────◯──"
    else:
        bar = "───────────◯"
        
    buttons = [
        [
            InlineKeyboardButton(
                text=f"{played} {bar} {dur}",
                callback_data="GetTimer",
            )
        ],
        [
            InlineKeyboardButton(
                text=_["KY_1"], 
                url=f"https://t.me/kontenfilm",
            ),
            InlineKeyboardButton(
                text=_["KY_2"],
                callback_data=f"PanelMarkup None|{chat_id}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSEMENU_BUTTON"], callback_data="close"
            ),
        ],
    ]
    return buttons


## Inline without Timer Bar


def stream_markup(_, videoid, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["KY_1"], 
                url=f"https://t.me/kontenfilm",
            ),
            InlineKeyboardButton(
                text=_["KY_2"],
                callback_data=f"PanelMarkup None|{chat_id}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSEMENU_BUTTON"], callback_data="close"
            ),
        ],
    ]
    return buttons


def telegram_markup(_, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["KY_2"],
                callback_data=f"PanelMarkup None|{chat_id}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSEMENU_BUTTON"], callback_data="close"
            ),
        ],
    ]
    return buttons


## Search Query Inline


def track_markup(_, videoid, user_id, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            )
        ],
    ]
    return buttons


def playlist_markup(_, videoid, user_id, ptype, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"YukkiPlaylists {videoid}|{user_id}|{ptype}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"YukkiPlaylists {videoid}|{user_id}|{ptype}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ],
    ]
    return buttons


## Live Stream Markup


def livestream_markup(_, videoid, user_id, mode, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_3"],
                callback_data=f"LiveStream {videoid}|{user_id}|{mode}|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["CLOSEMENU_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ],
    ]
    return buttons


## Slider Query Markup


def slider_markup(
    _, videoid, user_id, query, query_type, channel, fplay
):
    query = f"{query[:20]}"
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="≪",
                callback_data=f"slider B|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text="≫",
                callback_data=f"slider F|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
        ],
        [
          InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {query}|{user_id}",
            )
        ],
    ]
    return buttons


## Cpanel Markup


def panel_markup_1(_, videoid, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                text="⏸ Pause", callback_data=f"ADMIN Pause|{chat_id}"
            ),
            InlineKeyboardButton(
                text="▶️ Resume",
                callback_data=f"ADMIN Resume|{chat_id}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="⏯ Skip", callback_data=f"ADMIN Skip|{chat_id}"
            ),
            InlineKeyboardButton(
                text="⏹ Stop", callback_data=f"ADMIN Stop|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="≪",
                callback_data=f"Pages Back|0|{videoid}|{chat_id}",
            ),
            InlineKeyboardButton(
                text="≫",
                callback_data=f"Pages Forw|0|{videoid}|{chat_id}",
            ),
        ],
        [
          InlineKeyboardButton(
                text="ᴋᴇᴍʙᴀʟɪ",
                callback_data=f"MainMarkup {videoid}|{chat_id}",
            )
        ],
    ]
    return buttons


def panel_markup_2(_, videoid, chat_id):
    buttons = [
       [
            InlineKeyboardButton(
                text="🔇 Mute", callback_data=f"ADMIN Mute|{chat_id}"
            ),
            InlineKeyboardButton(
                text="🔈 Unmute",
                callback_data=f"ADMIN Unmute|{chat_id}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="🔀 Shuffle",
                callback_data=f"ADMIN Shuffle|{chat_id}",
            ),
            InlineKeyboardButton(
                text="🔁 Loop ", callback_data=f"ADMIN Loop|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="≪",
                callback_data=f"Pages Back|1|{videoid}|{chat_id}",
            ),
            InlineKeyboardButton(
                text="≫",
                callback_data=f"Pages Forw|1|{videoid}|{chat_id}",
            ),
        ],
        [
          InlineKeyboardButton(
                text="ᴋᴇᴍʙᴀʟɪ",
                callback_data=f"MainMarkup {videoid}|{chat_id}",
            )
        ],
    ]
    return buttons


def panel_markup_3(_, videoid, chat_id):
    buttons = [
                [
            InlineKeyboardButton(
                text="⏪ 10 Seconds",
                callback_data=f"ADMIN 1|{chat_id}",
            ),
            InlineKeyboardButton(
                text="⏩ 10 Seconds",
                callback_data=f"ADMIN 2|{chat_id}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="⏮ 30 Seconds",
                callback_data=f"ADMIN 3|{chat_id}",
            ),
            InlineKeyboardButton(
                text="⏭ 30 Seconds",
                callback_data=f"ADMIN 4|{chat_id}",
            ),
        ],
        [
          InlineKeyboardButton(
                text="ᴋᴇᴍʙᴀʟɪ",
                callback_data=f"MainMarkup {videoid}|{chat_id}",
            )
        ],
    ]
    return buttons
