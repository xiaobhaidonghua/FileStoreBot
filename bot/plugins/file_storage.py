import uuid, time, requests
from pyrogram import filters, Client
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from bot.client import app
from bot.database import files_col
from bot.utils.qr_generator import make_qr_bytes
from config import settings


@app.on_message(filters.media)
async def handle_file(client: Client, message: Message):
    code = str(uuid.uuid4())
    sent = await message.copy(chat_id=settings.STORAGE_CHANNEL_ID)
    await files_col.insert_one(
        {
            "uuid": code,
            "file_msg_id": sent.id,
            "user_id": message.from_user.id,
            "file_type": "file",
            "timestamp": time.time(),
        }
    )
    apper = await client.get_me()
    link = f"https://t.me/{apper.username}?start={code}"
    try:
        link2 = requests.get(
            f"https://linkpays.in/api?api=e64b0b252a329c9648740bf059a6cecd3ae4a73f&url={link}"
        ).json()["shortenedUrl"]
    except:
        link2 = link
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "🔗 Share File", url=f"https://t.me/share/url?url={link}"
                )
            ],
            [
                InlineKeyboardButton(
                    "🔗 Share File (secured)", url=f"https://t.me/share/url?url={link2}"
                )
            ],
        ]
    )
    qr_png = make_qr_bytes(link)
    await message.reply_photo(
        photo=qr_png,
        caption=f"✅ Stored!🔗\n\nLink-1: {link}\nLink-2 (secured): {link2}\n\nFILE_UUID: `{code}`",
        reply_to_message_id=message.id,
        reply_markup=keyboard,
    )
