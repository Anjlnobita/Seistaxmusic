import asyncio
import importlib

from pyrogram import idle

import config
from Seistaxmusic import LOGGER, app, userbot
from Seistaxmusic.core.call import NOBI
from Seistaxmusic.misc import sudo
from Seistaxmusic.plugins import ALL_MODULES
from Seistaxmusic.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error(
            "𝐒𝐭𝐫𝐢𝐧𝐠 𝐒𝐞𝐬𝐬𝐢𝐨𝐧 𝐍𝐨𝐭 𝐅𝐢𝐥𝐥𝐞𝐝, 𝐏𝐥𝐞𝐚𝐬𝐞 𝐅𝐢𝐥𝐥 𝐀 𝐏𝐲𝐫𝐨𝐠𝐫𝐚𝐦 V2 𝐒𝐞𝐬𝐬𝐢𝐨𝐧🤬"
        )

    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("Seistaxmusic.plugins" + all_module)
    LOGGER("Seistaxmusic.plugins").info("𝐀𝐥𝐥 𝐅𝐞𝐚𝐭𝐮𝐫𝐞𝐬 𝐋𝐨𝐚𝐝𝐞𝐝 𝐁𝐚𝐛𝐲🥳...")
    await userbot.start()
    await NOBI.start()
    await NOBI.decorators()
    LOGGER("Seistaxmusic").info("✨ 𝐦𝐚𝐝𝐞 𝐛𝐲 𝐀𝐧𝐣𝐥𝐧𝐨𝐛𝐢𝐭𝐚 💫")
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("AmritaXMusic").info("✨ 𝐦𝐚𝐝𝐞 𝐛𝐲 𝐀𝐧𝐣𝐥𝐧𝐨𝐛𝐢𝐭𝐚 💫")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())