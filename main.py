import asyncio

from program import LOGS
from pytgcalls import idle
from driver.core import calls, bot, user


async def start_bot():
    await bot.start()
    LOGS.info("[ INFO ] BOT & USERBOT CLIENT STARTED")
    await calls.start()
    LOGS.info("[ INFO ] PY-TGCALLS CLIENT STARTED")
    await user.join_chat("Jepthon2")
    await user.join_chat("jepthon")
    await idle()
    LOGS.info("[ INFO ] BOT & USERBOT CLIENT STOPPED")
    await bot.stop()

loop = asyncio.get_event_loop_policy().get_event_loop()
loop.run_until_complete(start_bot())
