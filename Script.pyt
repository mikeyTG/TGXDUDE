class script(object):
    START_TXT = """<b>HI {},<a href=https://t.me/{}>{}</a>..,𝖭𝗂𝖼𝖾 𝗍𝗈 𝗆𝖾𝖾𝗍 𝗒𝗈𝗎 🙌</b>
ɪ'ᴍ ᴊᴜsᴛ ᴀ sɪᴍᴘʟᴇ ᴘʀᴇ-ғᴜɴᴄᴛɪᴏɴᴇᴅ ᴀᴜᴛᴏғɪʟᴛᴇʀ ʙᴏᴛ.
ɪᴛs ᴇᴀsʏ ᴛᴏ ᴜsᴇ ᴍᴇ ; ᴊᴜsᴛ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀs ᴀᴅᴍɪɴ """


# ⚠️ Please don't change our credits 👇🏻

    ABOUT_TXT = """<b>○ 𝗠𝘆 𝗡𝗮𝗺𝗲: {}
○ 𝗖𝗿𝗲𝗮𝘁𝗼𝗿   : <a href=tg://settings>Tʜɪꜱ Pᴇʀꜱᴏɴ</a>
○ 𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿 :  <a href=https://t.me/psycho_009>Aᴋ Dᴇᴠᴇʟᴏᴩᴇʀ</a>
○ 𝗟𝗮𝗻𝗴𝘂𝗮𝗴𝗲 : Pyᴛʜᴏɴ3
○ 𝗟𝗶𝗯𝗿𝗮𝗿𝘆   : Pyʀᴏɢʀᴀᴍ
○ 𝗦𝗲𝗿𝘃𝗲𝗿    : Hᴇʀᴏᴋᴜ
○ 𝗗𝗮𝘁𝗮𝗯𝗮𝘀𝗲  : Mᴀɴɢᴏ ᴅʙ
○ 𝗨𝗽𝗱𝗮𝘁𝗲𝘀   : <a href=https://t.me/Ak_Links1>Cʟɪᴄᴋ Hᴇʀᴇ</a></b>"""
    
    
    STATUS_TXT = """<b>📂 Tᴏᴛᴀʟ Fɪʟᴇꜱ: <code>{}</code>
👤 Tᴏᴛᴀʟ Uꜱᴇʀꜱ: <code>{}</code>
♻️ Tᴏᴛᴀʟ Gʀᴏᴜᴩꜱ: <code>{}</code>
🗃️ Uꜱᴇᴅ Sᴛᴏʀᴀɢᴇ: <code>{}</code> 𝙼𝚒𝙱
🆓 Fʀᴇᴇ Sᴛᴏʀᴀɢᴇ: <code>{}</code> 𝙼𝚒𝙱

©Mᴀɪɴᴛᴀɪɴᴇᴅ ʙy:<a href=https://t.me/psycho_009>『ƬǤ』×͜×ʟᴇɢᴇɴᴅ𓄀</a></b>"""


    CHANNEL_CAP = """
<b>Hai 👋 {}</b> 😍

<code>{}</code>

⚠️ <b>This file will be deleted from here within 10 minute as it has copyright ... !!!</b>

<b>കോപ്പിറൈറ്റ് ഉള്ളതുകൊണ്ട് ഫയൽ 10 മിനിറ്റിനുള്ളിൽ ഇവിടെനിന്നും ഡിലീറ്റ് ആകുന്നതാണ് അതുകൊണ്ട് ഇവിടെ നിന്നും മറ്റെവിടെക്കെങ്കിലും മാറ്റിയതിന് ശേഷം ഡൗൺലോഡ് ചെയ്യുക!</b>

<b>© Powered by {}</b>
"""
    SUR_TXT = """<b>HI {},<a href=https://t.me/{}>{}</a>..,𝖭𝗂𝖼𝖾 𝗍𝗈 𝗆𝖾𝖾𝗍 𝗒𝗈𝗎 🙌</b>
ɪ'ᴍ ᴊᴜsᴛ ᴀ sɪᴍᴘʟᴇ ᴘʀᴇ-ғᴜɴᴄᴛɪᴏɴᴇᴅ ᴀᴜᴛᴏғɪʟᴛᴇʀ ʙᴏᴛ.
ɪᴛs ᴇᴀsʏ ᴛᴏ ᴜsᴇ ᴍᴇ ; ᴊᴜsᴛ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀs ᴀᴅᴍɪɴ """


    IMDB_TEMPLATE_TXT = """
<b>⍞ 𝗧𝗶𝘁𝗹𝗲</b> : <b><i><a href={url}>{title}</a></i></b><b>

⌗ 𝗚𝗲𝗻𝗿𝗲𝘀</b> :<b><i>{genres}</i></b><b>
★ 𝗥𝗮𝘁𝗶𝗻𝗴</b> : <b><i><a href={url}/ratings>{rating}</a> / 10 (ʙᴀsᴇᴅ ᴏɴ {votes} ᴜsᴇʀ ʀᴀᴛɪɴɢ.)</i></b><b>

〄 𝗥𝗲𝗹𝗲𝗮𝘀𝗲𝗱</b> : <b><i>{release_date}</i></b><b>
⌬ 𝗟𝗮𝗻𝗴𝘂𝗮𝗴𝗲𝘀</b> : <b><i>{languages}</i></b><b>
⛤ 𝗖𝗼𝘂𝗻𝘁𝗿𝗶𝗲𝘀</b> : <b><i>{countries}</i></b><b>
⎙ 𝗦𝘁𝗼𝗿𝘆 𝗟𝗶𝗻𝗲</b> : <code>{plot}</code><b>

★Requested by</b> : {message.from_user.mention}
"""

    CUSTOM_FILE_CAPTION = """<b>📂Fɪʟᴇɴᴀᴍᴇ : <code>{file_name}</code>

╔════ ᴊᴏɪɴ ᴡɪᴛʜ ᴜs ════╗
➪<a href=https://t.me/Ak_moviesgroup> Aᴋ Mᴏᴠɪᴇꜱ</a>
➪<a href=https://t.me/movies_channel001> Uᴩᴅᴀᴛᴇ Cʜᴀɴɴᴇʟ​ </a>
╚════ ᴊᴏɪɴ ᴡɪᴛʜ ᴜs ════╝</b>"""

    RESTART_TXT = """
<b>Bᴏᴛ Rᴇsᴛᴀʀᴛᴇᴅ !
📅 Dᴀᴛᴇ : <code>{}</code>
⏰Tɪᴍᴇ : <code>{}</code>
🌐 Tɪᴍᴇᴢᴏɴᴇ : <code>Asia/Kolkata</code></b>"""

    MELCOW_ENG = """<b>Hᴇʟʟᴏ {} 😍, Aɴᴅ Wᴇʟᴄᴏᴍᴇ Tᴏ {} Gʀᴏᴜᴘ ❤️"""

    ALRT_TXT = """ᴛʜɪꜱ ɪꜱ ɴᴏᴛ ꜰᴏʀ ʏᴏʏ ꜱɪʀ"""

    OLD_ALRT_TXT = """𝐘𝐨𝐮 𝐚𝐫𝐞 𝐮𝐬𝐢𝐧𝐠 𝐨𝐧𝐞 𝐨𝐟 𝐦𝐲 𝐨𝐥𝐝 𝐦𝐞𝐬𝐬𝐚𝐠𝐞𝐬, 𝐩𝐥𝐞𝐚𝐬𝐞 𝐬𝐞𝐧𝐝 𝐭𝐡𝐞 𝐫𝐞𝐪𝐮𝐞𝐬𝐭 𝐚𝐠𝐚𝐢𝐧 """

    TOP_ALRT_MSG = """♻️ ᴄʜᴇᴄᴋɪɴɢ ꜰɪʟᴇ ᴏɴ ᴍʏ ᴅᴀᴛᴀʙᴀꜱᴇ... ♻️"""

    MVE_NT_FND = """<b>ᴛʜɪꜱ ᴍᴏᴠɪᴇ ɪꜱ ɴᴏᴛ ʏᴇᴛ  ʀᴇʟᴇᴀꜱᴇᴅ ᴏʀ ᴀᴅᴅᴇᴅ ᴛᴏ ᴅᴀᴛᴀʙᴀꜱᴇ</b> """

    I_CUDNT = """ʜᴇʟʟᴏ {} ɪ ᴄᴏᴜʟᴅɴ'ᴛ ꜰɪɴᴅ ᴀɴʏ ᴍᴏᴠɪᴇꜱ ɪɴ ᴛʜᴀᴛ ɴᴀᴍᴇ. 
ᴍᴏᴠɪᴇ ʀᴇǫᴜᴇꜱᴛ ꜰᴏʀᴍᴀᴛ 
➠ ɢᴏ ᴛᴏ ɢᴏᴏɢʟᴇ 
➠ ᴛʏᴘᴇ ᴍᴏᴠɪᴇ ɴᴀᴍᴇ 
➠ ᴄᴏᴘʏ ᴄᴏʀʀᴇᴄᴛ ɴᴀᴍᴇ
➠ ᴘᴀꜱᴛᴇ ᴛʜɪꜱ ɢʀᴏᴜᴘ 
ᴇxᴀᴍᴘʟᴇ : ᴋᴀɴᴛᴀʀᴀ 2022 
🚯 ᴅᴏɴᴛ ᴜꜱᴇ ➠ ' : ( ! , . / )"""

    I_CUD_NT = """ʜᴇʟʟᴏ {} ɪ ᴄᴏᴜʟᴅɴ'ᴛ ꜰɪɴᴅ ᴀɴʏᴛʜɪɴɢ ʀᴇʟᴀᴛᴇᴅ ᴛᴏ ᴛʜᴀᴛ.ᴄʜᴇᴄᴋ ʏᴏᴜʀ ꜱᴘᴇʟʟɪɴɢ."""
    
    CUDNT_FND = """ʜᴇʟʟᴏ {} ɪ ᴄᴏᴜʟᴅɴ'ᴛ ꜰɪɴᴅ ᴀɴʏᴛʜɪɴɢ ʀᴇʟᴀᴛᴇᴅ ᴛᴏ ᴛʜᴀᴛ ᴅɪᴅ ʏᴏᴜ ᴍᴇᴀɴ ᴀɴʏ ᴏɴᴇ ᴏꜰ ᴛʜᴇꜱᴇ?"""

    REPRT_MSG = """ Join our group ask movies there
    <code>[JOIN GROUP](buttonurl:https://t.me/Mowie_world)</code>"""

    
