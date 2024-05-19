# © @SHIVANSH474
import asyncio
from SHUKLASPAM.data import GROUP, PORMS
from config import X1, SUDO_USERS, CMD_HNDLR as hl
from pyrogram import enums, Client
from random import choice
from telethon import events, functions, types

async def gifspam(e, smex):
    try:
        await e.client(
            functions.messages.SaveGifRequest(
                id=types.InputDocument(
                    id=sandy.media.document.id,
                    access_hash=smex.media.document.access_hash,
                    file_reference=smex.media.document.file_reference,
                ),
                unsave=True,
            )
        )
    except Exception:
        pass

async def is_chat_owner_or_admin(client: Client, chat_id: int, user_id: int) -> bool:
    member = await client.get_chat_member(chat_id, user_id)
    return member.status in [enums.ChatMemberStatus.ADMINISTRATOR, enums.ChatMemberStatus.OWNER]

@X1.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
async def spam(event: events):
    if await is_chat_owner_or_admin(X1, event.chat_id, event.sender_id):
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
            await event.reply(f"❖ **ᴜsᴀɢᴇ ➥** {hl}spam 13 Text\n\n● {hl}spam 13 <ʀᴇᴘʟʏ ᴛᴏ ᴛᴇxᴛ>\n\n**❖ To do spam with replying to a user.**\n\n● {h
