from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from bot.client import app
from bot.database import files_col
from bot.utils.stats import is_served_user
from config import settings
from bot.utils.telegram_api import Telegram_API

@app.on_message(filters.command("start") & filters.private)
async def start(_, message: Message):
    if not is_served_user(message.chat.id):
        await files_col.insert_one({"user_id": message.chat.id})
    args = message.text.split()[1:]
    if args:
        uuid = args[0]
        record = await files_col.find_one({"uuid": uuid})
        if not record:
            await message.reply("❌ File not found or expired.")
            return
        Telegram_API().copyMessage(
            chat_id=message.chat.id,
            from_chat_id=settings.STORAGE_CHANNEL_ID,
            message_id=record["file_msg_id"],
        )
    else:
        board = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📢 Updates Channel", url="https://t.me/ongoingdonghuas"
                    ),
                ]
            ]
        )
        await message.reply_photo(
            photo="start.jpg",
            caption="<b>👋 Welcome to <u> Bot</u>!</b>\n\n"
            " 🗂️ <b>This bot is for Storing Files</b> \n\n"
            "✨ <b> Enjoy:</b>\n"
            "• <b>Send me any file</b> \n\n"
            "🚀 <i>Thanks for staring Me</i>",
            reply_markup=board,
        )
