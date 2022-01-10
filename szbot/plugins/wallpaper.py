import os
import io
import requests
from requests import get
from pyrogram.types import Message
from szbot import sz as pbot
from bs4 import *
from pyrogram import filters	
from PIL import Image
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from szbot.helpers.fsub import ForceSub

def get_text(message: Message) -> [None, str]:
    text_to_return = message.text
    if message.text is None:
        return None
    if " " in text_to_return:
        try:
            return message.text.split(None, 1)[1]
        except IndexError:
            return None
    else:
        return None
      
caption = """
☘️** Wallpaper Created Successfully**✅
◇───────────────◇
🔥 **Created by** : @anonylogo_bot
🌷 **Requestor** : {message.from_user.mention}
⚡️ **Powered By **  : `Anonymous Devalopers`
◇───────────────◇
©2022 Anonymous Devaloper team ](https://t.me/anonymousbotz) **All Right Reserved**⚠️️
"""

@pbot.on_message(filters.command("wall") & ~filters.edited & ~filters.bot)
async def logo(client, message):
 FSub = await ForceSub(client, message)
 if FSub == 400:
        return            
 quew = get_text(message)
 if not quew:
     await client.send_message(message.chat.id, "😶 **Please Give me A Text For a query!**")
     return
 m = await client.send_message(message.chat.id, "`⚙️ Searching Your wallpapers..`")
 try:
    text = get_text(message)
    LOGO_API = f"https://single-developers.herokuapp.com/wallpaper?search={text}"
    randc = (LOGO_API)
    murl = requests.get(f"https://single-developers.herokuapp.com/wallpaper?search={text}").history[1].url
    img = Image.open(io.BytesIO(requests.get(randc).content))
    fname = "szrosebot.png"
    img.save(fname, "png")
    await m.delete()
    await client.send_photo(message.chat.id, photo=murl, caption =caption.format(message.from_user.mention),
                 reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "••Telegraph Link••", url=f"{murl}"
                    )
                ],
            ]
          ),
    )
    if os.path.exists(fname):
            os.remove(fname)
 except Exception as e:
    await client.send_message(message.chat.id, f'An error occurred! Report this @slbotzone, {e}')
