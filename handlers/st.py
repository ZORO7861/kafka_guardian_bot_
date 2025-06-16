from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_message(filters.command("start") & filters.private)
async def start_handler(client, message: Message):
    user = message.from_user.first_name or "User"

    text = f"""
𝖧𝖾𝗅𝗅𝗈, {user} 🧸  
➻ 𝖬𝗒𝗌𝖾𝗅𝖿 𝐊ᴀғᴋᴀ 𝐇ᴏɴᴋᴀɪ – 𝖳𝗁𝖾 𝖬𝗈𝗌𝗍 𝖯𝗈𝗐𝖾𝗋𝖿𝗎𝗅 𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆 𝖡𝗈𝗍 𝖥𝗈𝗋 𝖤𝖽𝗂𝗍 & 𝖬𝖾𝖽𝗂𝖺 𝖣𝖾𝖿𝖾𝗇𝗌𝖾 ✨  
━━━━━━━━━━━━━━━━━━━━━━━  
🔹 Automatically deletes spammy media (stickers, gifs, etc.)  
🔹 Removes edited messages after a set delay  
🔹 Use timers, permit trusted users, and enjoy smart controls  
🔹 Features secured SUDO & OWNER access levels  
🔹 Logs and approvals forwarded to my GOD 👑  
━━━━━━━━━━━━━━━━━━━━━━━  
📚 𝖴𝗌𝖾 𝗍𝗁𝖾 𝖼𝗈𝗆𝗆𝖺𝗇𝖽𝗌 𝖻𝗎𝗍𝗍𝗈𝗇 𝖿𝗈𝗋 𝖿𝗎𝗅𝗅 𝖿𝖾𝖺𝗍𝗎𝗋𝖾𝗌 & 𝗆𝗈𝖽𝗎𝗅𝖾𝗌.
"""

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("𝐀ᴅᴅ 𝐌ᴇ 𝐓ᴏ 𝐘ᴏᴜʀ 𝐆ʀᴏᴜᴘ", url=f"https://t.me/{client.me.username}?startgroup=true")],
        [InlineKeyboardButton("𝐂ᴏᴍᴍᴀɴᴅs", callback_data="command_menu")],
        [
            InlineKeyboardButton("𝐔ᴘᴅᴀᴛᴇ", url="https://t.me/kafkahonkaisupport"),
            InlineKeyboardButton("𝐒ᴜᴘᴘᴏʀᴛ 𝐂ʜᴀɴɴᴇʟ", url="https://t.me/kafkahonkainetworks")
        ],
        [InlineKeyboardButton("𝐎ᴡɴᴇʀ", url="https://t.me/ScorgeVirus")]
    ])

    await message.reply_photo(
        photo="https://files.catbox.moe/v2y36k.jpg",
        caption=text,
        reply_markup=keyboard
    )
