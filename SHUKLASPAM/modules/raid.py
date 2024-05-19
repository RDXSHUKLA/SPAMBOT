# © @SHIVANSH474
import asyncio

from random import choice

from telethon import events
from pyrogram import enums

from config import X1, SUDO_USERS, OWNER_ID, CMD_HNDLR as hl
from SHUKLASPAM.data import RAID, REPLYRAID, SHASHANK, LOVERAID, SRAID, CRAID, SHASHANK

REPLY_RAID = []

async def is_admin_or_owner(client, chat_id, user_id):
    try:
        participant = await client.get_participant(chat_id, user_id)
        if participant.is_admin or participant.is_creator:
            return True
        return False
    except:
        return False

@X1.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
async def raid(e):
    if await is_admin_or_owner(e.client, e.chat_id, e.sender_id):
        xraid = e.text.split(" ", 2)

        if len(xraid) == 3:
            entity = await e.client.get_entity(xraid[2])
            uid = entity.id

        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            entity = await e.client.get_entity(a.sender_id)
            uid = entity.id

        try:
            if uid in SHASHANK:
                await e.reply("ɴᴏ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴅᴇᴠᴇʟᴏᴘᴇʀ ᴏꜰ ᴛʜᴇꜱᴇ ʙᴏᴛꜱ✨🥀")
            elif uid == OWNER_ID:
                await e.reply("ɴᴏ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴏᴡɴᴇʀ ᴏꜰ ᴛʜᴇꜱᴇ ʙᴏᴛꜱ🥀")
            elif uid in SUDO_USERS:
                await e.reply("ɴᴏ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴀ ꜱᴜᴅᴏ ᴜꜱᴇʀ✨")
            else:
                first_name = entity.first_name
                counter = int(xraid[1])
                username = f"[{first_name}](tg://user?id={uid})"
                for _ in range(counter):
                    reply = choice(RAID)
                    caption = f"❖ {username} {reply}"
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.1)
        except (IndexError, ValueError, NameError):
            await e.reply(f"❖ 𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 ⏤͟͟͞͞★\n\n● 𝐑𝐚𝐢𝐝 ➥ {hl}raid <ᴄᴏᴜɴᴛ> <ᴜꜱᴇʀɴᴀᴍᴇ ᴏꜰ ᴜꜱᴇʀ>\n● {hl}raid <ᴄᴏᴜɴᴛ> <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ>")
        except Exception as e:
            print(e)


@X1.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
async def rraid(e):
    if await is_admin_or_owner(e.client, e.chat_id, e.sender_id):
        mkrr = e.text.split(" ", 1)
        if len(mkrr) == 2:
            en
