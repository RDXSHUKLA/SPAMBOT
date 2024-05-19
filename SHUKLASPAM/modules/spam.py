import asyncio
from SHUKLASPAM.data import GROUP, PORMS
from config import X1, SUDO_USERS, CMD_HNDLR as hl
from pyrogram import enums
from random import choice
from telethon import events, functions, types

async def gifspam(e, smex):
    try:
        await e.client(
            functions.messages.SaveGifRequest(
                id=types.InputDocument(
                    id=smex.media.document.id,
                    access_hash=smex.media.document.access_hash,
                    file_reference=smex.media.document.file_reference,
                ),
                unsave=True,
            )
        )
    except Exception:
        pass

async def is_admin_or_owner(event):
    participant = await event.client.get_participant(event.chat_id, event.sender_id)
    return participant.status in (enums.ChatMemberStatus.ADMINISTRATOR, enums.ChatMemberStatus.OWNER)

@X1.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
async def spam(event):
    if await is_admin_or_owner(event):
        altron = event.text.split(" ", 2)
        mk = await event.get_reply_message()

        try:
            if len(altron) == 3:
                message = altron[2]
                for _ in range(int(altron[1])):
                    if event.reply_to_msg_id:
                        await mk.reply(message)
                    else:
                        await event.client.send_message(event.chat_id, message)
                    await asyncio.sleep(0.2)
            elif event.reply_to_msg_id and mk.media:
                for _ in range(int(altron[1])):
                    mk = await event.client.send_file(event.chat_id, mk, caption=mk.text)
                    await gifspam(event, mk) 
                    await asyncio.sleep(0.2)  
            elif event.reply_to_msg_id and mk.text:
                message = mk.text
                for _ in range(int(altron[1])):
                    await event.client.send_message(event.chat_id, message)
                    await asyncio.sleep(0.2)
            else:
                await event.reply(f"❖ **ᴜsᴀɢᴇ ➥** {hl}spam 13 Text\n\n● {hl}spam 13 <ʀᴇᴘʟʏ ᴛᴏ ᴛᴇxᴛ>\n\n**❖ To do spam with replying to a user.**\n\n● {hl}spam 13 Text <ʀᴇᴘʟʏ ᴛᴏ ᴜꜱᴇʀ>")
        except (IndexError, ValueError):
            await event.reply(f"❖ **ᴜsᴀɢᴇ ➥** {hl}spam 13 Text\n\n● {hl}spam 13 <ʀᴇᴘʟʏ ᴛᴏ ᴛᴇxᴛ>\n\n**❖ To do spam with replying to a user.**\n\n● {hl}spam 13 Text <ʀᴇᴘʟʏ ᴛᴏ ᴜꜱᴇʀ>")
        except Exception as e:
            print(e)

@X1.on(events.NewMessage(incoming=True, pattern=r"\%spspam(?: |$)(.*)" % hl))
async def pspam(event):
    if await is_admin_or_owner(event):
        if event.chat_id in GROUP:
            await event
