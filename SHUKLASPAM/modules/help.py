# © @SHIVANSH474
from telethon import events, Button

from config import X1, SUDO_USERS, CMD_HNDLR as hl


HELP_STRING = f"★ 𝗦𝗧𝗥𝗔𝗡𝗚𝗘𝗥 𝗕𝗢𝗧 𝗛𝗘𝗟𝗣 𝗠𝗘𝗡𝗨 ★\n\n» **ᴄʟɪᴄᴋ ᴏɴ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ ғᴏʀ ʜᴇʟᴘ**\n» **ᴅᴇᴠᴇʟᴏᴘᴇʀ: @SHIVANSHDEVS**"

HELP_BUTTON = [
    [
      Button.inline("𝗦𝗣𝗔𝗠", data="spam"),
      Button.inline("𝗥𝗔𝗜𝗗", data="raid")
    ],
    [
      Button.inline("𝗘𝗫𝗧𝗥𝗔", data="extra")
    ],
    [
      Button.url("𝗦𝗛𝗜𝗩𝗔𝗡𝗦𝗛", "https://t.me/SHIVANSHDEVS"),
      Button.inline("𝗡𝗘𝗪 𝗖𝗢𝗠𝗠𝗔𝗡𝗗", data="shukla")
    ]
  ]


@X1.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
async def help(event):
        try:
          await event.client.send_file(event.chat_id,
              "https://files.catbox.moe/hs3brh.jpg",
              caption=HELP_STRING,
              buttons=HELP_BUTTON
              )
        except Exception as e:
            await event.client.send_message(event.chat_id, f"An Exception Occured!\n\n**ERROR:** {str(e)}")


extra_msg = f"""
**» ᴇxᴛʀᴀ  ᴄᴏᴍᴍᴀɴᴅs:**

🌺 𝗨𝘀𝗲𝗿𝗕𝗼𝘁: **💘ᴜsᴇʀʙᴏᴛ ᴄᴍᴅs💘**
  1) {hl}𝙿𝚒𝚗𝚐
  2) {hl}reb𝚘𝚘𝚝
  3) {hl}𝚂𝚞𝚍𝚘 <𝚛𝚎𝚙𝚕𝚢 𝚝𝚘 𝚞𝚜𝚎𝚛>  --> Owner Cmd
  4) {hl}𝚕𝚘𝚐𝚜 --> Owner Cmd

💫 𝗘𝗰𝗵𝗼: **🌸ᴛᴏ ᴀᴄᴛɪᴠᴇ ᴇᴄʜᴏ ᴏɴ ᴀɴʏ ᴜsᴇʀ🌸**
  1) {hl}𝚎𝚌𝚑𝚘 <𝚛𝚎𝚙𝚕𝚢 𝚝𝚘 𝚞𝚜𝚎𝚛>
  2) {hl}𝚛𝚖𝚎𝚌𝚑𝚘 <𝚛𝚎𝚙𝚕𝚢 𝚝𝚘 𝚞𝚜𝚎𝚛>

❤️‍🔥 𝗟𝗲𝗮𝘃𝗲: **🍁ᴛᴏ ʟᴇᴀᴠᴇ ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ🍁**
  1) {hl}𝚕𝚎𝚊𝚟𝚎 <𝚐𝚛𝚘𝚞𝚙/𝚌𝚑𝚊𝚝 𝚒𝚍>
  2) {hl}𝚕𝚎𝚊𝚟𝚎 : 𝚃𝚢𝚙𝚎 𝚒𝚗 𝚝𝚑𝚛 𝙶𝚛𝚘𝚞𝚘 𝚋𝚘𝚝 𝚠𝚒𝚕𝚕 𝚊𝚞𝚝𝚘 𝚕𝚎𝚊𝚟𝚎 𝚝𝚑𝚊𝚝 𝚐𝚛𝚘𝚞𝚙 


**© @SHIVANSHDEVS**
"""


raid_msg = f"""
**» ʀᴀɪᴅ ᴄᴏᴍᴍᴀɴᴅs:**

💘 𝗥𝗮𝗶𝗱: **🌟ᴀᴄᴛɪᴠᴀᴛᴇs ʀᴀɪᴅ ᴏɴ ᴀɴʏ ɪɴᴅɪᴠɪᴅᴜᴀʟ ᴜsᴇʀ ғᴏʀ ɢɪᴠᴇɴ ʀᴀɴɢᴇ🌟**
  1) {hl}𝚛𝚊𝚒𝚍 <𝚌𝚘𝚞𝚗𝚝> <𝚞𝚜𝚎𝚛𝚗𝚊𝚖𝚎>
  2) {hl}𝚛𝚊𝚒𝚍 <𝚌𝚘𝚞𝚗𝚝> <𝚛𝚎𝚙𝚕𝚢 𝚝𝚘 𝚞𝚜𝚎𝚛>

💖 𝗥𝗲𝗽𝗹𝘆𝗥𝗮𝗶𝗱: **✨ᴀᴄᴛɪᴠᴀᴛᴇs ʀᴇᴘʟʏ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜsᴇʀ✨**
  1) {hl}𝚛𝚛𝚊𝚒𝚍 <𝚛𝚎𝚙𝚕𝚢𝚒𝚗𝚐 𝚝𝚘 𝚞𝚜𝚎𝚛>
  2) {hl}𝚛𝚛𝚊𝚒𝚍 <𝚞𝚜𝚎𝚛𝚗𝚊𝚖𝚎>
  3) {hl}𝚑𝚛𝚛𝚊𝚒𝚍 <𝚛𝚎𝚙𝚕𝚢𝚒𝚗𝚐 𝚝𝚘 𝚞𝚜𝚎𝚛>
  4) {hl}𝚑𝚛𝚛𝚊𝚒𝚍 <𝚞𝚜𝚎𝚛𝚗𝚊𝚖𝚎>

🌺 𝗗𝗥𝗲𝗽𝗹𝘆𝗥𝗮𝗶𝗱: **🍁ᴅᴇᴀᴄᴛɪᴠᴀᴛᴇs ʀᴇᴘʟʏ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜsᴇʀ🍁**
  1) {hl}𝚍𝚛𝚛𝚊𝚒𝚍 <𝚛𝚎𝚙𝚕𝚢𝚒𝚗𝚐 𝚝𝚘 𝚞𝚜𝚎𝚛>
  2) {hl}𝚍𝚛𝚛𝚊𝚒𝚍 <𝚞𝚜𝚎𝚛𝚗𝚊𝚖𝚎>
  3) {hl}𝚍𝚑𝚛𝚊𝚒𝚍 <𝚛𝚎𝚙𝚕𝚢𝚒𝚗𝚐 𝚝𝚘 𝚞𝚜𝚎𝚛>
  4) {hl}𝚍𝚑𝚛𝚊𝚒𝚍 <𝚞𝚜𝚎𝚛𝚗𝚊𝚖𝚎>

🌟 𝐋𝐨𝐯𝐞 𝐑𝐚𝐢𝐝: **❤️‍🔥ʟᴏᴠᴇ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜsᴇʀ❤️‍🔥**
  1) {hl}𝚖𝚛𝚊𝚒𝚍 <𝚌𝚘𝚞𝚗𝚝> <𝚞𝚜𝚎𝚛𝚗𝚊𝚖𝚎>
  2) {hl}𝚕𝚘𝚟𝚎𝚛𝚊𝚒𝚍 <𝚌𝚘𝚞𝚗𝚝> <𝚞𝚜𝚎𝚛𝚗𝚊𝚖𝚎>

💖 𝐇𝐢𝐧𝐝𝐢 𝐑𝐚𝐢𝐝: **💫ʜɪɴᴅɪ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜsᴇʀ💫**
  1) {hl}𝚑𝚛𝚊𝚒𝚍 <𝚌𝚘𝚞𝚗𝚝> <username>
  2) {hl}𝚑𝚛𝚊𝚒𝚍 <𝚌𝚘𝚞𝚗𝚝> <𝚛𝚎𝚙𝚕𝚢 𝚝𝚘 𝚞𝚜𝚎𝚛>

💘 𝐂𝐑𝐚𝐢𝐝: **🍁ᴀʙᴄᴅ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜsᴇʀ🍁**
  1) {hl}𝚌𝚛𝚊𝚒𝚍 <𝚌𝚘𝚞𝚗𝚝> <𝚞𝚜𝚎𝚛𝚗𝚊𝚖𝚎>
  2) {hl}𝚌𝚛𝚊𝚒𝚍 <𝚌𝚘𝚞𝚗𝚝> <𝚛𝚎𝚙𝚕𝚢 𝚝𝚘 𝚞𝚜𝚎𝚛>


**© @SHIVANSHDEVS**💘
"""

shukla_msg = f"""
**» ɴᴇᴡ ᴄᴏᴍᴍᴀɴᴅs:**

💘 𝗚𝗼𝗼𝗱 𝗔𝗳𝘁𝗲𝗿𝗻𝗼𝗼𝗻: **🌟ᴀғᴛᴇʀ ɴᴏᴏɴ ʀᴀɪᴅ ᴏɴ ᴀɴʏ ɪɴᴅɪᴠɪᴅᴜᴀʟ ᴜsᴇʀ ғᴏʀ ɢɪᴠᴇɴ ʀᴀɴɢᴇ🌟**
  1) {hl}𝚐𝚊 <𝚌𝚘𝚞𝚗𝚝> <𝚞𝚜𝚎𝚛𝚗𝚊𝚖𝚎>
  2) {hl}𝚐𝚊 <𝚌𝚘𝚞𝚗𝚝> <𝚛𝚎𝚙𝚕𝚢 𝚝𝚘 𝚞𝚜𝚎𝚛>

💖 𝗘𝗺𝗼𝗷𝗶: **✨ᴇᴍᴏᴊɪ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜsᴇʀ✨**
  1) {hl}𝚎𝚖𝚘𝚓𝚒 <𝚛𝚎𝚙𝚕𝚢𝚒𝚗𝚐 𝚝𝚘 𝚞𝚜𝚎𝚛>
  2) {hl}𝚎𝚖𝚘𝚓𝚒 <𝚞𝚜𝚎𝚛𝚗𝚊𝚖𝚎>

🌺 𝗚𝗼𝗼𝗱 𝗠𝗼𝗿𝗻𝗶𝗻𝗴: **🍁ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜsᴇʀ🍁**
  1) {hl}𝚐𝚖 <𝚛𝚎𝚙𝚕𝚢𝚒𝚗𝚐 𝚝𝚘 𝚞𝚜𝚎𝚛>
  2) {hl}𝚐𝚖 <𝚞𝚜𝚎𝚛𝚗𝚊𝚖𝚎>

🌟 𝗚𝗼𝗼𝗱 𝗡𝗶𝗴𝗵𝘁: **❤️‍🔥ɢᴏᴏᴅ ɴɪɢʜᴛ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜsᴇʀ❤️‍🔥**
  1) {hl}𝚐𝚗 <𝚌𝚘𝚞𝚗𝚝> <𝚞𝚜𝚎𝚛𝚗𝚊𝚖𝚎>
  2) {hl}𝚐𝚗 <𝚌𝚘𝚞𝚗𝚝> <𝚛𝚎𝚙𝚕𝚢 𝚝𝚘 𝚞𝚜𝚎𝚛>

💖 𝗦𝗵𝗮𝘆𝗿𝗶 𝗥𝗮𝗶𝗱: **💫sʜʏʀɪ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜsᴇʀ💫**
  1) {hl}𝚜𝚛𝚊𝚒𝚍 <𝚌𝚘𝚞𝚗𝚝> <username>
  2) {hl}𝚜𝚛𝚊𝚒𝚍 <𝚌𝚘𝚞𝚗𝚝> <𝚛𝚎𝚙𝚕𝚢 𝚝𝚘 𝚞𝚜𝚎𝚛>

💘 𝗙𝗹𝗶𝗿𝘁𝗶𝗻𝗴: **🍁ғʟɪʀᴛ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜsᴇʀ🍁**
  1) {hl}𝚏𝚕𝚒𝚛𝚝 <𝚌𝚘𝚞𝚗𝚝> <𝚞𝚜𝚎𝚛𝚗𝚊𝚖𝚎>
  2) {hl}𝚏𝚕𝚒𝚛𝚝 <𝚌𝚘𝚞𝚗𝚝> <𝚛𝚎𝚙𝚕𝚢 𝚝𝚘 𝚞𝚜𝚎𝚛>

💘 𝗕𝗶𝗿𝘁𝗵𝗱𝗮𝘆: **🍁ғʟɪʀᴛ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜsᴇʀ🍁**
  1) {hl}𝚋𝚜𝚙𝚊𝚖 <𝚌𝚘𝚞𝚗𝚝> <𝚞𝚜𝚎𝚛𝚗𝚊𝚖𝚎>
  2) {hl}𝚋𝚜𝚙𝚊𝚖 <𝚌𝚘𝚞𝚗𝚝> <𝚛𝚎𝚙𝚕𝚢 𝚝𝚘 𝚞𝚜𝚎𝚛>


**© @SHIVANSHDEVS**💘
"""

spam_msg = f"""
**» sᴘᴀᴍ ᴄᴏᴍᴍᴀɴᴅs:**

🌺 𝗦𝗽𝗮𝗺: **❤️‍🔥sᴘᴀᴍs ᴀ ᴍᴇssᴀɢᴇ❤️‍🔥**
  1) {hl}𝚂𝚙𝚊𝚖 <𝚌𝚘𝚞𝚗𝚝> <𝚖𝚎𝚜𝚜𝚊𝚐𝚎 𝚝𝚘 𝚜𝚙𝚊𝚖> (𝚢𝚘𝚞 𝚌𝚊𝚗 𝚛𝚎𝚙𝚕𝚢 𝚊𝚗𝚢 𝚖𝚎𝚜𝚜𝚊𝚐𝚎 𝚒𝚏 𝚢𝚘𝚞 𝚠𝚊𝚗𝚝 𝚋𝚘𝚝 𝚝𝚘 𝚛𝚎𝚙𝚕𝚢 𝚝𝚑𝚊𝚝 𝚖𝚎𝚜𝚜𝚊𝚐𝚎 𝚊𝚗𝚍 𝚍𝚘 𝚜𝚙𝚊𝚖𝚖𝚒𝚗𝚐)
  2) {hl}𝚜𝚙𝚊𝚖 <𝚌𝚘𝚞𝚗𝚝> <𝚛𝚎𝚙𝚕𝚢𝚒𝚗𝚐 𝚊𝚗𝚢 𝚖𝚎𝚜𝚜𝚊𝚐𝚎>

💖 𝗣𝗼𝗿𝗻𝗦𝗽𝗮𝗺: **🍁ᴘᴏʀɴᴏɢʀᴀᴘʜʏ  sᴘᴀᴍ🍁**
  1) {hl}𝙿𝚜𝚙𝚊𝚖 <𝚌𝚘𝚞𝚗𝚝>

🌸 𝗛𝗮𝗻𝗴: **🌺sᴘᴀᴍs ʜᴀɴɢ ᴍᴇssᴀɢᴇ ғᴏʀ ɢɪᴠᴇɴ ᴄᴏᴜɴᴛᴇʀs🌺**
  1) {hl}𝚑𝚊𝚗𝚐 <𝚌𝚘𝚞𝚗𝚝𝚎𝚛>

💖 𝗔𝗯𝘂𝘀𝗲𝗦𝗽𝗮𝗺: **🌺ᴏɴᴇ ᴡᴏʀᴅ ʙɪɢ ɢᴀᴀʟɪ sᴘᴀᴍ🌺**
  1) {hl}𝚊𝚋𝚞𝚜𝚎 <𝚌𝚘𝚞𝚗𝚝> <𝚞𝚜𝚎𝚛𝚗𝚊𝚖𝚎>
  
** © @SHIVANSHDEVS**
"""                     


@X1.on(events.CallbackQuery(pattern=r"help_back"))
async def helpback(event):
        await event.edit(
            HELP_STRING,
            buttons=[
              [
                Button.inline("𝗦𝗣𝗔𝗠", data="spam"),
                Button.inline("𝗥𝗔𝗜𝗗", data="raid")
              ],
              [
                Button.inline("𝗘𝗫𝗧𝗥𝗔", data="extra")
              ],
              [
                Button.url("𝗦𝗛𝗜𝗩𝗔𝗡𝗦𝗛", "https://t.me/SHIVANSHDEVS"),
                Button.inline("𝗡𝗘𝗪 𝗖𝗢𝗠𝗠𝗔𝗡𝗗", data="shukla")
              ]
            ]
          )


@X1.on(events.CallbackQuery(pattern=r"spam"))
async def help_spam(event):   
        await event.edit(spam_msg,
              buttons=[[Button.inline("< Back", data="help_back"),],],
              ) 


@X1.on(events.CallbackQuery(pattern=r"raid"))
async def help_raid(event):
        await event.edit(raid_msg,
            buttons=[[Button.inline("< Back", data="help_back"),],],
          )


@X1.on(events.CallbackQuery(pattern=r"extra"))
async def help_extra(event):
        await event.edit(extra_msg,
            buttons=[[Button.inline("< Back", data="help_back"),],],
            )
            

@X1.on(events.CallbackQuery(pattern=r"shukla"))
async def help_shukla(event):
        await event.edit(shukla_msg,
            buttons=[[Button.inline("< Back", data="help_back"),],],
            )
   