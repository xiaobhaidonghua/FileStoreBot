from pyrogram import filters
from pyrogram.types import Message
from bot.client import app
from bot.database import files_col
from bot.utils.stats import is_served_user


@app.on_message(filters.private & filters.text)
async def unknown(_, message: Message):
    if not is_served_user(message.chat.id):
        await files_col.insert_one({"user_id": message.from_user.id})
    await message.reply(
        "<b>❓ Unknown command!</b>\n\n"
        "<i>I didn't recognize that command.\n"
        "Use /help to see all available commands.</i>",
    )
