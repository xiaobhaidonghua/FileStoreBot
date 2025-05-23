from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from bot.client import app


@app.on_message(filters.command("help") & filters.private)
async def help_command(_, message: Message):
    board = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "📢 Updates Channel", url="https://t.me/ongoingdonghuas"
                ),
            ]
        ]
    )
    await message.reply(
        "<b>🆘 FileDrawer Bot Help</b>\n\n"
        "Here’s how you can use <u>FileDrawer Bot</u>:\n\n"
        "📥 <b>Store Files:</b>\n"
        " • Just send me any file and I’ll save it for you!\n\n"
        "📋 <b>List Files:</b>\n"
        " • <code>/list</code> – View all your stored files.\n\n"
        "🗑️ <b>Delete File:</b>\n"
        " • <code>/delete &lt;FILE_UUID&gt;</code> – Remove a file by its unique ID.\n\n"
        "👁️ <b>Show File:</b>\n"
        " • <code>/start &lt;FILE_UUID&gt;</code> – Show a file by its unique ID.\n\n"
        "🔗 <b>Share Files:</b>\n"
        " • Use the links I provide after storing a file to share with anyone.\n\n"
        "ℹ️ <b>Other Commands:</b>\n"
        " • <code>/start</code> – Show the welcome message.\n"
        " • <code>/help</code> – Show this help message.\n\n"
        "💡 <i>Tip: Your files are private and only accessible by you unless you share the link!</i>",
        reply_markup=board,
    )
