from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

imgcaption = """
☘️ **Random Logo Created Successfully**✅
◇───────────────◇
🔥 **Created by** :  [Anonymous-Image-logo-editor Bot](https://t.me/anonylogo_bot)
🌷 **Requestor** : {message.from_user.username}
⚡️ **Powered By **: `Anonymous Devalopers´
◇───────────────◇
©2022 Anonymous Devaloper team  **All Right Reserved**⚠️️
"""
repmark = InlineKeyboardMarkup(
      [
        [
        InlineKeyboardButton(text="➕Add me to your group ➕", url=f"http://t.me/anonylogo_bot?startgroup=botstart") 
        ],
        [
         InlineKeyboardButton(text="🗣️Join my updates", url=f"https://t.me/anonymousbotz") 
        ],
        [
         InlineKeyboardButton(text="🔰Contact My Master🔰", url=f"https://t.me/networkchukka") 
        ]
      ]      
    )
