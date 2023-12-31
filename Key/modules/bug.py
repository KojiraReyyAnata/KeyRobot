# Copyright (c) 2022 Shiinobu Project

from datetime import datetime

from pyrogram import filters
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    CallbackQuery,
    Message,
)

from Key import pbot as Client
from Key import (
    OWNER_ID as owner,
    SUPPORT_CHAT as log,
)
from Key.utils.errors import capture_err


def content(msg: Message) -> [None, str]:
    text_to_return = msg.text

    if msg.text is None:
        return None
    if " " not in text_to_return:
        return None
    try:
        return msg.text.split(None, 1)[1]
    except IndexError:
        return None


@Client.on_message(filters.command("bug"))
@capture_err
async def bug(_, msg: Message):
    if msg.chat.username:
        chat_username = (f"@{msg.chat.username} / `{msg.chat.id}`")
    else:
        chat_username = (f"Private Group / `{msg.chat.id}`")

    bugs = content(msg)
    user_id = msg.from_user.id
    mention = f"[{msg.from_user.first_name}](tg://user?id={str(msg.from_user.id)})"
    datetimes_fmt = "%d-%m-%Y"
    datetimes = datetime.utcnow().strftime(datetimes_fmt)

    bug_report = f"""
**#BUG : ** **[⚠️](https://t.me/)**
**Dari Pengguna : ** **{mention}**
**identitas pengguna : ** **{user_id}**
**Grup : ** **{chat_username}**
**Laporan Bug : ** **{bugs}**
**Stempel : ** **{datetimes}**"""


    if msg.chat.type == "private":
        await msg.reply_text("❎ <b>Perintah ini hanya berfungsi di group.</b>")
        return

    if user_id == owner:
        if bugs:
            await msg.reply_text("❎ <b>Lu yang bikin Lu yang lapor, Owner tolol!</b>")
            return
        else:
            await msg.reply_text("❎ <b>Owner noob!</b>")
    elif bugs:
        await msg.reply_text(
            f"<b>Bug Report : {bugs}</b>\n\n✅ <b>Bug berhasil dilaporkan ke group support!</b>",
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("ᴄʟᴏsᴇ", callback_data="close_reply")]]
            ),
        )
        thumb = "https://telegra.ph//file/225a8779f15daf89036cb.jpg"

        await Client.send_photo(
            log,
            photo=thumb,
            caption=f"{bug_report}",
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("➡ ᴠɪᴇᴡ ʙᴜɢ", url=f"{msg.link}")],
                    [
                        InlineKeyboardButton(
                            "ᴄʟᴏsᴇ", callback_data="close_send_photo"
                        )
                    ],
                ]
            ),
        )
    else:
        await msg.reply_text("❎ <b>Tidak ada bug untuk Dilaporkan!</b>")
        
    

@Client.on_callback_query(filters.regex("close_reply"))
async def close_reply(msg, CallbackQuery):
    await CallbackQuery.message.delete()

@Client.on_callback_query(filters.regex("close_send_photo"))
async def close_send_photo(Client, CallbackQuery):
    await CallbackQuery.message.delete()


__mod_name__ = "Bug"
