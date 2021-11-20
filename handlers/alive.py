#𝚉𝙰𝙸𝙳 𝙿𝚁𝙾𝙹𝙴𝙲𝚃 
#𝚄𝚁 𝙼𝙾𝚃𝙷𝙴𝚁𝙵𝚄𝙲𝙺𝙴𝚁 𝙸𝙵 𝚄 𝙺𝙰𝙽𝙶 𝙰𝙽𝙳 𝙳𝙾𝙽'𝚃 𝙶𝙸𝚅𝙴 𝙲𝚁𝙴𝙳𝙸𝚃𝚂 😡
#𝙼𝙾𝙳𝙸𝙵𝙴𝙳 𝙵𝙾𝚁 𝙰𝙻𝙴𝚇𝙰 𝙼𝚄𝚂𝙸𝙲 

from os import path

from pyrogram import Client, filters
from pyrogram.types import Message

from time import time
from datetime import datetime
from config import ALIVE_IMG, BOT_USERNAME, BOT_NAME, ASSISTANT_NAME, OWNER_NAME, UPDATES_CHANNEL, GROUP_SUPPORT
from helpers.filters import command, other_filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)


@Client.on_message(filters.command(["alive", f"alive@{BOT_USERNAME}"]))
async def alive(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_photo(
        photo=f"{ALIVE_IMG}",
        caption=f"""**➮ Hemloo vaimyaa mee [{BOT_NAME}](https://t.me/{BOT_USERNAME}) [Jass Vaiya](https://t.me/abra_ka_dabra_gili_gili_chuu) ka 🎧 mujikk bot 🎧**

✘ **Me sexy as always**

✘ **𝙰𝙻𝙴𝚇𝙰 𝙼𝚄𝚂𝙸𝙲 ᴠᴇʀꜱɪᴏɴ 𖣘 0.7.0 𝙻𝙴𝚃𝙴𝚂𝚃**

✘ **𝙼𝚈 𝙾𝚆𝙽𝙴𝚁 𖣘 [{OWNER_NAME}](https://t.me/{OWNER_NAME})**

✘ **𝚂𝙴𝚁𝚅𝙸𝙲𝙴 𝚄𝙿𝚃𝙸𝙼𝙴 𖣘 `{uptime}`**

**✘ Thnxx babes mujhe use krne ke liye ❤️**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "〘 ♕ 𝚂𝚄𝙿𝙿𝙾𝚁𝚃 ♕ 〙", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "〘 ♕ 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 ♕ 〙", url=f"https://t.me/{UPDATES_CHANNEL}"
                    )
                ]
            ]
        )
    )
