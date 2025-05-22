from bot.client import create_web_app, start_webapp, stop_webapp
import os, asyncio
from pyrogram import idle
from bot.client import app as client


async def main():
    bot = client
    app = create_web_app()
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", "8080"))
    runner = await start_webapp(app, host, port)
    await bot.start()
    await idle()
    await stop_webapp(runner)
    await bot.stop()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
