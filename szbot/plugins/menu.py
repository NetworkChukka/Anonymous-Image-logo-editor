from szbot import sz
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery







START_BTN = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("🙇 About 🙇", callback_data="aboutmenu"),
                    InlineKeyboardButton("🆘️ Help 🆘️", callback_data="helpmenu")
                ],
                [
                    InlineKeyboardButton("🗣Updates", url="https://t.me/anonymousbotz"),
                    InlineKeyboardButton("👥Support", url="https://t.me/anonymousbotzchat")
                ],
                [
                    InlineKeyboardButton("➕Add me to your group ➕", url="http://t.me/anonylogo_bot?startgroup=botstart") 
                ],
                [
                    InlineKeyboardButton(text="🔰Contact My Master🔰", url=f"https://t.me/networkchukka") 
                ]
            ]
        )

GROUP_BTN = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("🆘️ Help 🆘️", callback_data="helpmenu")
                ],
                [
                    InlineKeyboardButton("🗣️Update channel", url="https://t.me/anonymousbotz")
                ]
            ]
        )

HELP_TEXT = f"""
**🆘️This is @anonylogo_bot Help Menu 🆘️**

⚠️️Read this before useing me ...

♞/logo logo name 
♞/logohq logo name 
♞/rmbg reply to photo 
♞/edit reply to photo 
♞/carbon reply to text
♞/text reply to text
♞/rlogo logo name

©2022[Anonymous Devaloper Team ](https://t.me/anonymousbotz)✌️
"""

BACKTOHOME = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("🔙Back", callback_data="startmenu")
                ]
            ]
        )

ABOUT_TEXT = """
🌟**Logo Design Platform in Telegram , 
World First Time With Image Editor tools**🌟

🔥You Can Create Many Type Of **Logo Design**
For your Dp & More Usage , Remove Background  
With full **Advance image Editor Features** Included 
This Bot Based on @MalithRukshan **Logo Api Key**
& **TroJanzHex Image editor** 
Speacial credits gone **Dᴀᴍᴀɴᴛʜᴀ Jᴀsɪɴɢʜᴇ & <sz/> Team ** ...🤗

💁‍♂**Logo Types & Image editor Features** : 

🍀Api Based logo Creator
💐Rando logo Creator 
♣️ Carbon maker
🍃Background Remover
✍Text art Genarator 80+ styles
⭕️Image editor 
           💡Bright 
           🖼 Mixed 
           🔘 Black & White 
           ⚪️ Circle 
           🩸 Blur
           🔲 Border 
           🗯 Sticker 
           🔄 Rotate
           🌀 Contrast 
           🌇 Sepia 
           ✏️ Pencil 
           ⛄️ Cartoon 
           ✨ Invert 
           🖲 Glitch
           🗑 Remove Background
◈──────────────────◈
⚠️ **Please Note** ⚠️

✍**We have added force sub to image bot  
because of some users spaming our bot 
by sending command  😑 So now bot works
only for people who are subscribed our channel 😒 
So If you send /start ,bot will reply you
a message to Subscribe Our Updates Channel , 
So If you recieved that message simply
go the given inline button andJoin our Channel Then /start again 😊
Then You Can Use Our Bot For limited  To Create logo 💫😊**

🎁 `Thank you all for following this´♥️
◈──────────────────◈
💐Try it Now , Enjoy Unlimited logo creator !!!  💐
"""

CLOSE_BTN =  InlineKeyboardMarkup(
        [
        [
        InlineKeyboardButton(text="Anonymous Botz", url=f"https://t.me/anonymousbotz")    
        ]
        ]      
    )

FSUB_TEXT = " **You cant use me untill subscribe our updates channel** ☹️\n\n So Please join our updates channel by the following button and hit on the ` /start ` again 😊"

FSUB_BTN = InlineKeyboardMarkup(
        [
        [
        InlineKeyboardButton(text="🗣 Join our update Channel ", url=f"https://t.me/anonymousbotz") 
        ]
        ]      
    )

@sz.on_callback_query(filters.regex("startmenu"))
async def startmenu(_, query: CallbackQuery):
    await query.edit_message_text(START_TEXT,
        reply_markup=START_BTN,
     disable_web_page_preview=True
    )

@sz.on_callback_query(filters.regex("helpmenu"))
async def helpmenu(_, query: CallbackQuery):
    await query.edit_message_text(HELP_TEXT,
        reply_markup=BACKTOHOME,
     disable_web_page_preview=True
    )

@sz.on_callback_query(filters.regex("aboutmenu"))
async def aboutenu(_, query: CallbackQuery):
    await query.edit_message_text(ABOUT_TEXT,
        reply_markup=BACKTOHOME,
     disable_web_page_preview=True
    )

@sz.on_callback_query(filters.regex("closeit"))
async def close(_, query: CallbackQuery):
    await query.message.delete()        
