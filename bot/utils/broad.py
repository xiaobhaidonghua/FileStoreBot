from pyrogram.types import Message


async def broadcast(user_list: list, message: Message, msg: str):
    no_sent = 0
    no_failed = 0
    for i in user_list:
        try:
            y = i
            if "--f" in msg:
                try:
                    await message.forward(y)
                    no_sent += 1
                except Exception:
                    no_failed += 1
                    continue
            else:
                try:
                    await message.copy(y)
                    no_sent += 1
                except Exception:
                    no_failed += 1
                    continue
        except Exception as e:
            print(e)
            no_failed += 1
            continue
    return no_sent, no_failed
