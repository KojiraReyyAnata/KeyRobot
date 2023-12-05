import html
import re

from telegram import ParseMode, ChatPermissions
from telegram.error import BadRequest
from telegram.ext import CommandHandler, MessageHandler, Filters
from telegram.utils.helpers import mention_html

import Key.modules.sql.blacklist_sql as sql
from Key import dispatcher, LOGGER
from Key.modules.disable import DisableAbleCommandHandler
from Key.modules.helper_funcs.chat_status import user_admin, user_not_admin
from Key.modules.helper_funcs.extraction import extract_text
from Key.modules.helper_funcs.misc import split_message
from Key.modules.log_channel import loggable
from Key .modules.warns import warn
from Key.modules.helper_funcs.string_handling import extract_time
from Key.modules.connection import connected
from Key.modules.sql.approve_sql import is_approved
from Key.modules.helper_funcs.alternate import send_message, typing_action

from pyrogram import filters


BLACKLIST_GROUP = 11


async def get_blacklist_filters_count() -> dict:
    chats_count = 0
    filters_count = 0
    async for chat in blacklist_filtersdb.find({"chat_id": {"$lt": 0}}):
        filters = await get_blacklisted_words(chat["chat_id"])
        filters_count += len(filters)
        chats_count += 1
    return {
        "chats_count": chats_count,
        "filters_count": filters_count,
    }


async def get_blacklisted_words(chat_id: int) -> List[str]:
    _filters = await blacklist_filtersdb.find_one({"chat_id": chat_id})
    return [] if not _filters else _filters["filters"]


async def save_blacklist_filter(chat_id: int, word: str):
    word = word.lower().strip()
    _filters = await get_blacklisted_words(chat_id)
    _filters.append(word)
    await blacklist_filtersdb.update_one(
        {"chat_id": chat_id},
        {"$set": {"filters": _filters}},
        upsert=True,
    )


async def delete_blacklist_filter(chat_id: int, word: str) -> bool:
    filtersd = await get_blacklisted_words(chat_id)
    word = word.lower().strip()
    if word in filtersd:
        filtersd.remove(word)
        await blacklist_filtersdb.update_one(
            {"chat_id": chat_id},
            {"$set": {"filters": filtersd}},
            upsert=True,
        )
        return True
    return False


@user_admin
@typing_action
def bl(_, message):
    if message.reply_to_message:
        kata = message.reply_to_message.text
    else:
        kata = message.text.split(None, 1)[1]
    # huruf = 10
    # kata_pertama = kata.split()[0][:huruf] if kata else ""
    if not kata:
        return await message.reply_text(
            "**Usage**\n__/blacklist [balas pesan/berikan kata]__"
        )
    await message.reply_to_message.delete()
    await message.delete()
    chat_id = message.chat.id
    await save_blacklist_filter(chat_id, kata)
    await message.reply_text(f"__**Blacklisted {kata}.**__")



@user_admin
@typing_action
def blacklist(update, context):
    chat = update.effective_chat
    user = update.effective_user
    args = context.args

    if conn := connected(context.bot, update, chat, user.id, need_admin=False):
        chat_id = conn
        chat_name = dispatcher.bot.getChat(conn).title
    else:
        if chat.type == "private":
            return
        chat_id = update.effective_chat.id
        chat_name = chat.title

    filter_list = f"Current blacklisted words in <b>{chat_name}</b>:\n"

    all_blacklisted = sql.get_chat_blacklist(chat_id)

    if len(args) > 0 and args[0].lower() == "copy":
        for trigger in all_blacklisted:
            filter_list += f"<code>{html.escape(trigger)}</code>\n"
    else:
        for trigger in all_blacklisted:
            filter_list += f" - <code>{html.escape(trigger)}</code>\n"

    # for trigger in all_blacklisted:
    #     filter_list += " - <code>{}</code>\n".format(html.escape(trigger))

    split_text = split_message(filter_list)
    for text in split_text:
        if (
            filter_list
            == f"Current blacklisted words in <b>{html.escape(chat_name)}</b>:\n"
        ):
            send_message(
                update.effective_message,
                f"No blacklisted words in <b>{html.escape(chat_name)}</b>!",
                parse_mode=ParseMode.HTML,
            )
            return
        send_message(update.effective_message, text, parse_mode=ParseMode.HTML)


@user_admin
@typing_action
def add_blacklist(update, context):
    msg = update.effective_message
    chat = update.effective_chat
    user = update.effective_user
    words = msg.text.split(None, 1)

    if conn := connected(context.bot, update, chat, user.id):
        chat_id = conn
        chat_name = dispatcher.bot.getChat(conn).title
    else:
        chat_id = update.effective_chat.id
        if chat.type == "private":
            return
        chat_name = chat.title

    if len(words) > 1:
        text = words[1]
        to_blacklist = list(
            {trigger.strip() for trigger in text.split("\n") if trigger.strip()},
        )
        for trigger in to_blacklist:
            sql.add_to_blacklist(chat_id, trigger.lower())

        if len(to_blacklist) == 1:
            send_message(
                update.effective_message,
                f"Added blacklist <code>{html.escape(to_blacklist[0])}</code> in chat: <b>{html.escape(chat_name)}</b>!",
                parse_mode=ParseMode.HTML,
            )

        else:
            send_message(
                update.effective_message,
                f"Added blacklist trigger: <code>{len(to_blacklist)}</code> in <b>{html.escape(chat_name)}</b>!",
                parse_mode=ParseMode.HTML,
            )

    else:
        send_message(
            update.effective_message,
            "Tell me which words you would like to add in blacklist.",
        )


@user_admin
@typing_action
def unblacklist(update, context):
    msg = update.effective_message
    chat = update.effective_chat
    user = update.effective_user
    words = msg.text.split(None, 1)

    if conn := connected(context.bot, update, chat, user.id):
        chat_id = conn
        chat_name = dispatcher.bot.getChat(conn).title
    else:
        chat_id = update.effective_chat.id
        if chat.type == "private":
            return
        chat_name = chat.title

    if len(words) > 1:
        text = words[1]
        to_unblacklist = list(
            {trigger.strip() for trigger in text.split("\n") if trigger.strip()},
        )
        successful = 0
        for trigger in to_unblacklist:
            success = sql.rm_from_blacklist(chat_id, trigger.lower())
            if success:
                successful += 1

        if len(to_unblacklist) == 1:
            if successful:
                send_message(
                    update.effective_message,
                    f"Removed <code>{html.escape(to_unblacklist[0])}</code> from blacklist in <b>{html.escape(chat_name)}</b>!",
                    parse_mode=ParseMode.HTML,
                )
            else:
                send_message(
                    update.effective_message,
                    "This is not a blacklist trigger!",
                )

        elif successful == len(to_unblacklist):
            send_message(
                update.effective_message,
                f"Removed <code>{successful}</code> from blacklist in <b>{html.escape(chat_name)}</b>!",
                parse_mode=ParseMode.HTML,
            )

        elif not successful:
            send_message(
                update.effective_message,
                "None of these triggers exist so it can't be removed.",
                parse_mode=ParseMode.HTML,
            )

        else:
            send_message(
                update.effective_message,
                f"Removed <code>{successful}</code> from blacklist. {len(to_unblacklist) - successful} did not exist, so were not removed.",
                parse_mode=ParseMode.HTML,
            )
    else:
        send_message(
            update.effective_message,
            "Tell me which words you would like to remove from blacklist!",
        )


@loggable
@user_admin
@typing_action
def blacklist_mode(update, context):
    chat = update.effective_chat
    user = update.effective_user
    msg = update.effective_message
    args = context.args

    conn = connected(context.bot, update, chat, user.id, need_admin=True)
    if conn:
        chat = dispatcher.bot.getChat(conn)
        chat_id = conn
        chat_name = dispatcher.bot.getChat(conn).title
    else:
        if update.effective_message.chat.type == "private":
            send_message(
                update.effective_message,
                "This command can be only used in group not in PM",
            )
            return ""
        chat = update.effective_chat
        chat_id = update.effective_chat.id
        chat_name = update.effective_message.chat.title

    if args:
        if args[0].lower() in ["off", "nothing", "no"]:
            settypeblacklist = "do nothing"
            sql.set_blacklist_strength(chat_id, 0, "0")
        elif args[0].lower() in ["del", "delete"]:
            settypeblacklist = "delete blacklisted message"
            sql.set_blacklist_strength(chat_id, 1, "0")
        elif args[0].lower() == "warn":
            settypeblacklist = "warn the sender"
            sql.set_blacklist_strength(chat_id, 2, "0")
        elif args[0].lower() == "mute":
            settypeblacklist = "mute the sender"
            sql.set_blacklist_strength(chat_id, 3, "0")
        elif args[0].lower() == "kick":
            settypeblacklist = "kick the sender"
            sql.set_blacklist_strength(chat_id, 4, "0")
        elif args[0].lower() == "ban":
            settypeblacklist = "ban the sender"
            sql.set_blacklist_strength(chat_id, 5, "0")
        elif args[0].lower() == "tban":
            if len(args) == 1:
                teks = """It looks like you tried to set time value for blacklist but you didn't specified time; Try, `/blacklistmode tban <timevalue>`.

    Examples of time value: 4m = 4 minutes, 3h = 3 hours, 6d = 6 days, 5w = 5 weeks."""
                send_message(update.effective_message, teks, parse_mode="markdown")
                return ""
            restime = extract_time(msg, args[1])
            if not restime:
                teks = """Invalid time value!
    Example of time value: 4m = 4 minutes, 3h = 3 hours, 6d = 6 days, 5w = 5 weeks."""
                send_message(update.effective_message, teks, parse_mode="markdown")
                return ""
            settypeblacklist = f"temporarily ban for {args[1]}"
            sql.set_blacklist_strength(chat_id, 6, str(args[1]))
        elif args[0].lower() == "tmute":
            if len(args) == 1:
                teks = """It looks like you tried to set time value for blacklist but you didn't specified  time; try, `/blacklistmode tmute <timevalue>`.

    Examples of time value: 4m = 4 minutes, 3h = 3 hours, 6d = 6 days, 5w = 5 weeks."""
                send_message(update.effective_message, teks, parse_mode="markdown")
                return ""
            restime = extract_time(msg, args[1])
            if not restime:
                teks = """Invalid time value!
    Examples of time value: 4m = 4 minutes, 3h = 3 hours, 6d = 6 days, 5w = 5 weeks."""
                send_message(update.effective_message, teks, parse_mode="markdown")
                return ""
            settypeblacklist = f"temporarily mute for {args[1]}"
            sql.set_blacklist_strength(chat_id, 7, str(args[1]))
        else:
            send_message(
                update.effective_message,
                "I only understand: off/del/warn/ban/kick/mute/tban/tmute!",
            )
            return ""
        if conn:
            text = f"Changed blacklist mode: `{settypeblacklist}` in *{chat_name}*!"
        else:
            text = f"Changed blacklist mode: `{settypeblacklist}`!"
        send_message(update.effective_message, text, parse_mode="markdown")
        return f"<b>{html.escape(chat.title)}:</b>\n<b>Admin:</b> {mention_html(user.id, html.escape(user.first_name))}\nChanged the blacklist mode. will {settypeblacklist}."
    getmode, getvalue = sql.get_blacklist_setting(chat.id)
    if getmode == 0:
        settypeblacklist = "do nothing"
    elif getmode == 1:
        settypeblacklist = "delete"
    elif getmode == 2:
        settypeblacklist = "warn"
    elif getmode == 3:
        settypeblacklist = "mute"
    elif getmode == 4:
        settypeblacklist = "kick"
    elif getmode == 5:
        settypeblacklist = "ban"
    elif getmode == 6:
        settypeblacklist = f"temporarily ban for {getvalue}"
    elif getmode == 7:
        settypeblacklist = f"temporarily mute for {getvalue}"
    if conn:
        text = f"Current blacklistmode: *{settypeblacklist}* in *{chat_name}*."
    else:
        text = f"Current blacklistmode: *{settypeblacklist}*."
    send_message(update.effective_message, text, parse_mode=ParseMode.MARKDOWN)
    return ""


def findall(p, s):
    i = s.find(p)
    while i != -1:
        yield i
        i = s.find(p, i + 1)


@user_not_admin
def del_blacklist(update, context):
    chat = update.effective_chat
    message = update.effective_message
    user = update.effective_user
    bot = context.bot
    to_match = extract_text(message)
    if not to_match:
        return
    if is_approved(chat.id, user.id):
        return
    getmode, value = sql.get_blacklist_setting(chat.id)

    chat_filters = sql.get_chat_blacklist(chat.id)
    for trigger in chat_filters:
        pattern = r"( |^|[^\w])" + re.escape(trigger) + r"( |$|[^\w])"
        if re.search(pattern, to_match, flags=re.IGNORECASE):
            try:
                if getmode == 0:
                    return
                if getmode == 1:
                    try:
                        message.delete()
                    except BadRequest:
                        pass
                elif getmode == 2:
                    try:
                        message.delete()
                    except BadRequest:
                        pass
                    warn(
                        update.effective_user,
                        chat,
                        f"Using blacklisted trigger: {trigger}",
                        message,
                        update.effective_user,
                    )
                    return
                elif getmode == 3:
                    message.delete()
                    bot.restrict_chat_member(
                        chat.id,
                        update.effective_user.id,
                        permissions=ChatPermissions(can_send_messages=False),
                    )
                    bot.sendMessage(
                        chat.id,
                        f"Muted {user.first_name} for using Blacklisted word: {trigger}!",
                    )
                    return
                elif getmode == 4:
                    message.delete()
                    if res := chat.unban_member(update.effective_user.id):
                        bot.sendMessage(
                            chat.id,
                            f"Kicked {user.first_name} for using Blacklisted word: {trigger}!",
                        )
                    return
                elif getmode == 5:
                    message.delete()
                    chat.ban_member(user.id)
                    bot.sendMessage(
                        chat.id,
                        f"Banned {user.first_name} for using Blacklisted word: {trigger}",
                    )
                    return
                elif getmode == 6:
                    message.delete()
                    bantime = extract_time(message, value)
                    chat.ban_member(user.id, until_date=bantime)
                    bot.sendMessage(
                        chat.id,
                        f"Banned {user.first_name} until '{value}' for using Blacklisted word: {trigger}!",
                    )
                    return
                elif getmode == 7:
                    message.delete()
                    mutetime = extract_time(message, value)
                    bot.restrict_chat_member(
                        chat.id,
                        user.id,
                        until_date=mutetime,
                        permissions=ChatPermissions(can_send_messages=False),
                    )
                    bot.sendMessage(
                        chat.id,
                        f"Muted {user.first_name} until '{value}' for using Blacklisted word: {trigger}!",
                    )
                    return
            except BadRequest as excp:
                if excp.message != "Message to delete not found":
                    LOGGER.exception("Error while deleting blacklist message.")
            break


def __import_data__(chat_id, data):
    # set chat blacklist
    blacklist = data.get("blacklist", {})
    for trigger in blacklist:
        sql.add_to_blacklist(chat_id, trigger)


def __migrate__(old_chat_id, new_chat_id):
    sql.migrate_chat(old_chat_id, new_chat_id)


def __chat_settings__(chat_id, user_id):
    blacklisted = sql.num_blacklist_chat_filters(chat_id)
    return f"There are {blacklisted} blacklisted words."


def __stats__():
    return f"• {sql.num_blacklist_filters()} blacklist triggers, across {sql.num_blacklist_filter_chats()} chats."


__mod_name__ = "ʙʟᴀᴄᴋʟɪsᴛs"

__help__ = """

Daftar hitam digunakan untuk menghentikan pemicu tertentu agar tidak diucapkan dalam grup. Kapan pun pemicunya disebutkan, pesan akan segera dihapus. Kombo yang bagus terkadang memasangkan ini dengan filter peringatan!

*CATATAN*: Daftar hitam tidak memengaruhi admin grup.

⩺ /blacklist*:* Lihat kata-kata yang masuk daftar hitam saat ini.

Admin only:
⩺ /addblacklist <pemicu>*:* Tambahkan pemicu ke daftar hitam. Setiap baris dianggap sebagai satu pemicu, jadi menggunakan baris yang berbeda akan memungkinkan Anda untuk menambahkan beberapa pemicu.
⩺ /unblacklist <pemicu>*:* Hapus pemicu dari daftar hitam. Logika baris baru yang sama berlaku di sini, sehingga Anda dapat menghapus beberapa pemicu sekaligus.
⩺ /blacklistmode <off/del/warn/ban/kick/mute/tban/tmute>*:* Tindakan yang harus dilakukan ketika seseorang mengirim kata-kata yang masuk daftar hitam.

Stiker daftar hitam digunakan untuk menghentikan stiker tertentu. Setiap kali stiker dikirim, pesan akan segera dihapus.
*CATATAN:* Stiker daftar hitam tidak memengaruhi admin grup
⩺ • /blsticker*:* Lihat stiker daftar hitam saat ini
*Only admin:*
⩺ /addblsticker <sticker link>*:* Tambahkan pemicu stiker ke daftar hitam. Dapat ditambahkan melalui stiker balasan
⩺ /unblsticker <sticker link>*:* Hapus pemicu dari daftar hitam. Logika baris baru yang sama berlaku di sini, sehingga Anda dapat menghapus beberapa pemicu sekaligus
⩺ /rmblsticker <sticker link>*:* Sama seperti di atas
⩺ /blstickermode <delete/ban/tban/mute/tmute>*:* menyiapkan tindakan default tentang apa yang harus dilakukan jika pengguna menggunakan stiker yang masuk daftar hitam
Note:
⩺ <sticker link> dapat `https://t.me/addstickers/<sticker>` atau hanya `<sticker>` atau balas pesan stiker

"""
BLACKLIST_HANDLER = DisableAbleCommandHandler(
    "blacklist",
    blacklist,
    pass_args=True,
    admin_ok=True,
    run_async=True,
)
ADD_BLACKLIST_HANDLER = CommandHandler("addblacklist", add_blacklist, run_async=True)
UNBLACKLIST_HANDLER = CommandHandler("unblacklist", unblacklist, run_async=True)
BLACKLISTMODE_HANDLER = CommandHandler(
    "blacklistmode", blacklist_mode, pass_args=True, run_async=True
)
BLACKLIST_DEL_HANDLER = MessageHandler(
    (Filters.text | Filters.command | Filters.sticker | Filters.photo)
    & Filters.chat_type.groups,
    del_blacklist,
    allow_edit=True,
    run_async=True,
)

dispatcher.add_handler(BLACKLIST_HANDLER)
dispatcher.add_handler(ADD_BLACKLIST_HANDLER)
dispatcher.add_handler(UNBLACKLIST_HANDLER)
dispatcher.add_handler(BLACKLISTMODE_HANDLER)
dispatcher.add_handler(BLACKLIST_DEL_HANDLER, group=BLACKLIST_GROUP)

__handlers__ = [
    BLACKLIST_HANDLER,
    ADD_BLACKLIST_HANDLER,
    UNBLACKLIST_HANDLER,
    BLACKLISTMODE_HANDLER,
    (BLACKLIST_DEL_HANDLER, BLACKLIST_GROUP),
]
