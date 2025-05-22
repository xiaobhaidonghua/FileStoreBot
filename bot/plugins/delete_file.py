from pyrogram import filters
from pyrogram.types import Message
from bot.client import app
from bot.database import files_col

@app.on_message(filters.command('delete') & filters.private)
async def delete_file(_, message: Message):
    args = message.text.split()[1:]
    if not args:
        await message.reply('❌ Usage: /delete FILE_UUID')
        return
    res = await files_col.delete_one({'uuid': args[0], 'user_id': message.from_user.id})
    if res.deleted_count:
        await message.reply('✅ Deleted.')
    else:
        await message.reply('❌ Not found or unauthorized.')