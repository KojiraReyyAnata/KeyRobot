from pyrogram import filters
from pyrogram.types import Message

from Key import pbot as app
from Key.utils.errors import capture_err

__mod_name__ = "Webshot​"


@app.on_message(filters.command("webss"))
@capture_err
async def take_ss(_, message: Message):
    try:
        if len(message.command) != 2:
            return await message.reply_text(
                "Give A Url To Fetch Screenshot."
            )
        url = message.text.split(None, 1)[1]
        m = await message.reply_text("**Taking Screenshot**")
        await m.edit("**Uploading**")
        try:
            await message.reply_photo(
                photo=f"https://webshot.amanoteam.com/print?q={url}",
                quote=False,
            )
        except TypeError:
            return await m.edit("No Such Website.")
        await m.delete()
    except Exception as e:
        await message.reply_text(str(e))
