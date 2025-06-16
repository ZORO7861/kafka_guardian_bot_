from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

# /start command
@Client.on_message(filters.command("start") & filters.private)
async def start_handler(client, message: Message):
    user = message.from_user.first_name or "User"

    text = f"""
𝖧𝖾𝗅𝗅𝗈, {user} 🧸  
➻ 𝖬𝗒𝗌𝖾𝗅𝖿 𝐊ᴀғᴋᴀ 𝐇ᴏɴᴋᴀɪ – 𝖳𝗁𝖾 𝖬𝗈𝗌𝗍 𝖯𝗈𝗐𝖾𝗋𝖿𝗎𝗅 𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆 𝖡𝗈𝗍 𝖥𝗈𝗋 𝖤𝖽𝗂𝗍 & 𝖬𝖾𝖽𝗂𝖺 𝖣𝖾𝖿𝖾𝗇𝗌𝖾 ✨  
━━━━━━━━━━━━━━━━━━━━━━━  
🔹 Automatically deletes spammy media  
🔹 Removes edited messages after a set delay  
🔹 Use timers, permit users, smart controls  
🔹 Powerful SUDO & OWNER system  
🔹 Secure logging and moderation  
━━━━━━━━━━━━━━━━━━━━━━━  
📚 Tap "Commands" below for features list.
"""

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("➕ 𝐀ᴅᴅ 𝐌ᴇ 𝐓ᴏ 𝐘ᴏᴜʀ 𝐆ʀᴏᴜᴘ", url=f"https://t.me/{client.me.username}?startgroup=true")],
        [InlineKeyboardButton("📚 𝐂ᴏᴍᴍᴀɴᴅ𝐬", callback_data="command_menu")],
        [
            InlineKeyboardButton("🔄 𝐔ᴘᴅᴀᴛᴇ", url="https://t.me/kafkahonkaisupport"),
            InlineKeyboardButton("💬 𝐒ᴜᴘᴘᴏʀᴛ", url="https://t.me/kafkahonkainetworks")
        ],
        [InlineKeyboardButton("👑 𝐎ᴡɴᴇʀ", url="https://t.me/ScorgeVirus")]
    ])

    await message.reply_photo(
        photo="https://files.catbox.moe/v2y36k.jpg",
        caption=text,
        reply_markup=keyboard
    )

# Main command menu
@Client.on_callback_query(filters.regex("command_menu"))
async def command_menu_handler(client, callback_query: CallbackQuery):
    text = "<b>📚 Kafka Honkai Command Menu</b>\n\nSelect a category below:"
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("⚙️ Basic", callback_data="basic_cmds")],
        [InlineKeyboardButton("📝 Edit Defense", callback_data="edit_cmds")],
        [InlineKeyboardButton("🎞 Media Defense", callback_data="media_cmds")],
        [InlineKeyboardButton("👑 Admin & Sudo", callback_data="admin_cmds")],
        [InlineKeyboardButton("🛡 Moderation", callback_data="mod_cmds")],
    ])
    await callback_query.message.edit_text(text, reply_markup=keyboard, parse_mode="html")

# Basic Commands
@Client.on_callback_query(filters.regex("basic_cmds"))
async def basic_cmds(client, callback_query: CallbackQuery):
    text = """
<b>⚙️ Basic Commands:</b>

/start - Start the bot  
/help - Show help and features  
/pingme - Check bot ping  
/alive - Show bot status  
/stats - Usage stats
"""
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("🔙 Back", callback_data="command_menu")]
    ])
    await callback_query.message.edit_text(text, reply_markup=keyboard, parse_mode="html")

# Edit Commands
@Client.on_callback_query(filters.regex("edit_cmds"))
async def edit_cmds(client, callback_query: CallbackQuery):
    text = """
<b>📝 Edit Defense:</b>

/edittimer - Set edit delete timer  
/epermit - Allow user to edit  
/ermpermit - Remove edit permit  
/epermited - List edit-permitted users  
/edit on - Enable edit defense  
/edit off - Disable edit defense
"""
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("🔙 Back", callback_data="command_menu")]
    ])
    await callback_query.message.edit_text(text, reply_markup=keyboard, parse_mode="html")

# Media Commands
@Client.on_callback_query(filters.regex("media_cmds"))
async def media_cmds(client, callback_query: CallbackQuery):
    text = """
<b>🎞 Media Defense:</b>

/mediatimer - Set media auto-delete  
/mpermit - Allow user/bot to send media  
/mrmpermit - Remove media permit  
/mpermited - List media-permitted users  
/media on - Enable media defense  
/media off - Disable media defense
"""
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("🔙 Back", callback_data="command_menu")]
    ])
    await callback_query.message.edit_text(text, reply_markup=keyboard, parse_mode="html")

# Admin/Sudo Commands
@Client.on_callback_query(filters.regex("admin_cmds"))
async def admin_cmds(client, callback_query: CallbackQuery):
    text = """
<b>👑 Admin & Sudo:</b>

/sudo - Add sudo user  
/rmsudo - Remove sudo  
/sudolist - List sudo users  
/block - Block user from bot  
/unblock - Unblock user  
/blocked - Blocked users list  
/blockchat - Block group  
/unblockchat - Unblock group  
/blockedchats - Blocked chats list
"""
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("🔙 Back", callback_data="command_menu")]
    ])
    await callback_query.message.edit_text(text, reply_markup=keyboard, parse_mode="html")

# Moderation Commands
@Client.on_callback_query(filters.regex("mod_cmds"))
async def mod_cmds(client, callback_query: CallbackQuery):
    text = """
<b>🛡 Moderation:</b>

/gban - Globally ban user  
/ungban - Unban user  
/gmute - Globally mute  
/ungmute - Unmute globally
"""
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("🔙 Back", callback_data="command_menu")]
    ])
    await callback_query.message.edit_text(text, reply_markup=keyboard, parse_mode="html")
