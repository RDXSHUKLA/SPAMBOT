# © @SHIVANSH474
import sys
import heroku3

from config import X1, OWNER_ID, SUDO_USERS, HEROKU_APP_NAME, HEROKU_API_KEY, CMD_HNDLR as hl
from pyrogram import enums
from os import execl, getenv
from telethon import events
from datetime import datetime


@X1.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
async def ping(e):
    if e.sender_id == enums.ChatMemberStatus.ADMINISTRATOR or enums.ChatMemberStatus.OWNER:
        start = datetime.now()
        altron = await e.reply(f"» ™°‌𝗦 𝗧 𝗥 𝗔 𝗡 𝗚 𝗘 𝗥")
        end = datetime.now()
        mp = (end - start).microseconds / 1000
        await altron.edit(f"💫🥀 🫧 🇸𝗧 𝗥 𝗔 𝗡 𝗚 𝗘 𝗥\n» {mp} 𝙼𝚂")


@X1.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
async def restart(e):
    if e.sender_id in SUDO_USERS:
        await e.reply(f"🥀ʀᴇsᴛᴀʀᴛɪɴɢ sᴛʀᴀɴɢᴇʀ ʙᴏᴛs🥀...")
        try:
            await X1.disconnect()
        except Exception:
            pass
        
        execl(sys.executable, sys.executable, *sys.argv)

@X1.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
async def addsudo(event):
    if event.sender_id == OWNER_ID:
        Heroku = heroku3.from_key(HEROKU_API_KEY)
        sudousers = getenv("SUDO_USERS", default=None)

        ok = await event.reply(f"» ᴀᴅᴅɪɴɢ ᴜsᴇʀ ᴀs sᴛʀᴀɴɢᴇʀ 💘sᴜᴅᴏ💘...🚀🚀")
        target = ""
        if HEROKU_APP_NAME is not None:
            app = Heroku.app(HEROKU_APP_NAME)
        else:
            await ok.edit("✦ `[HEROKU] ➥" "\n✦ Please Setup Your` **HEROKU_APP_NAME**")
            return
        heroku_var = app.config()
        if event is None:
            return
        try:
            reply_msg = await event.get_reply_message()
            target = reply_msg.sender_id
        except:
            await ok.edit("» 🌺ʀᴇᴘʟʏ ᴛᴏ 𝙰 ᴜsᴇʀ🌺 !!")
            return

        if str(target) in sudousers:
            await ok.edit(f"» 🌸ᴛʜɪs ᴜsᴇʀ ɪs ᴀʟʀᴇᴀᴅʏ ᴀ sᴜᴅᴏ ᴜsᴇʀ ᴏғ sᴛʀᴀɴɢᴇʀ ʙᴏᴛs🌸 !!")
        else:
            if len(sudousers) > 0:
                newsudo = f"{sudousers} {target}"
            else:
                newsudo = f"{target}"
            await ok.edit(f"» ɴᴇᴡ sᴜᴅᴏ ᴜsᴇʀ: {target}\n» 💖ʀᴇsᴛᴀʀᴛɪɴɢ sᴛʀᴀɴɢᴇʀ ʙᴏᴛs💖...`")
            heroku_var["SUDO_USERS"] = newsudo    
    
    elif event.sender_id in SUDO_USERS:
        await event.reply("» sᴏʀʀʏ, ᴏɴʟʏ ᴏᴡɴᴇʀ ᴄᴀɴ ᴀᴄᴇss ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ.")
      