import os
from config import Config
from .fonts import Fonts
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(filters.command('start'))
async def start(c, m):
    owner = await c.get_users(int(Config.OWNER_ID))
    owner_username = owner.username if owner.username else 'senith_0831'

    # start text
    text = f"""ආයුබෝවන්!!!! 🙏🙏🙏 {m.from_user.mention(style='md')},

** I am zoom recording downloder bot

**<b>මම ඔයාලට උදව්වක් කරානම් ඒ ගැන ඔයාගේ අදහස දක්වන්න කියලා මම ඔයගෙන් කාරුණිකව ඉල්ලා සිටිනවා</b>

**send your comments @senithlokitha_chat_bot

** Developer by :** ❤️ ▷ [@Drfoxprojects]
"""

    # Buttons
    buttons = [
        [
            InlineKeyboardButton('👥 Group', url=f"https://t.me/senithlokithatk"),
            InlineKeyboardButton('Channel 📢', url=f"https://t.me/Drfoxprojects")
            ],[
            InlineKeyboardButton('❤️ Credits', url=f"https://t.me/senith_0831"),
            InlineKeyboardButton('GitHup 🤣', url=f"https://github.com/senithfox2")
            ],[
            InlineKeyboardButton('⚜️ vist my web site ⚜️', url=f"http://www.senithlokitha.tk")
            ],[
            InlineKeyboardButton('❌report bug errors❌', url=f"https://t.me/senithlokitha_chat_bot")    
        ]
    ]
    await m.reply_text(
        text=text,
        reply_markup=InlineKeyboardMarkup(buttons)
    )

