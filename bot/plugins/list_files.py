from pyrogram import filters
from pyrogram.types import Message
from bot.client import app
from bot.database import files_col
import datetime

@app.on_message(filters.command('list') & filters.private)
async def list_files(_, message: Message):
    cursor = files_col.find({'user_id': message.from_user.id})
    items = await cursor.to_list(length=100)
    if not items:
        await message.reply('You have no stored files.')
        return
    text = 'Your files:\n'
    for rec in items:
        ts = datetime.datetime.fromtimestamp(rec['timestamp']).strftime('%Y-%m-%d %H:%M')
        text += f"• {rec['file_type']} – `{rec['uuid']}` at {ts}\n"
    await message.reply(text)