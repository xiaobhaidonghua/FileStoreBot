from pyrogram import filters, Client
from pyrogram.types import Message
from bot.client import app
from bot.utils.stats import total_users_count, total_files_count, top_users, list_users
from bot.utils.broad import broadcast
from config import settings

ADMINS = settings.ADMIN_USER_IDS


@app.on_message(filters.command("stats") & filters.user(ADMINS))
async def stats_command(_, message: Message):
    total_users = await total_users_count()
    total_files = await total_files_count()
    top = await top_users(5)

    reply = [
        f"📊 **Bot Statistics**",
        f"• Total Users: `{total_users}`",
        f"• Total Files Stored: `{total_files}`",
        "\n**Top 5 Users by Files Stored:**",
    ]
    for idx, user in enumerate(top, 1):
        reply.append(f'{idx}. User `{user["_id"]}` – {user["count"]} files')

    await message.reply("\n".join(reply))


@app.on_message(filters.private & filters.command("broad"))
async def broadcaster(c: Client, m: Message):
    if not int(m.chat.id) in settings.ADMIN_USER_IDS:
        return await m.delete()
    msg_to_br = m.reply_to_message
    if not msg_to_br:
        return await m.reply_text("REPLY TO A MESSAGE !")
    users_list = await list_users()
    no_sent, no_failed = await broadcast(users_list, msg_to_br, m.text)
    await c.send_message(
        chat_id=int(m.chat.id),
        text="<b><i>Broadcast Status:\n\nSuccess: {}\nFailed: {}</i></b>".format(
            no_sent, no_failed
        ),
    )
