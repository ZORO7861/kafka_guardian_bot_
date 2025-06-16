from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from config import API_ID, API_HASH, BOT_TOKEN, OWNER_ID
import asyncio
import re
import time

app = Client("KafkaMediaBot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

PERMITTED_USERS = set()
PERMITTED_CHANNELS = set()
MEDIA_TIMER = 10

OWNER_ID = int(OWNER_ID)
SUDO_USERS = [6037958673]

BANNED_USERS = set()
BLOCKED_USERS = set()
BLOCKED_CHATS = set()
GBANNED_USERS = set()
GMUTED_USERS = set()
JOINED_CHATS = set()


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

# Media Defense Commands
@app.on_message(filters.command("mediatimer") & filters.group)
async def set_media_timer(_, message: Message):
    global MEDIA_TIMER
    user = await app.get_chat_member(message.chat.id, message.from_user.id)
    if not (user.status == "creator" or user.can_promote_members):
        return await message.reply("You don't have permission to change media timer settings.")
    if len(message.command) < 2:
        return await message.reply("Usage: /mediatimer <seconds>")
    try:
        MEDIA_TIMER = int(message.command[1])
        await message.delete()
        await message.reply(f"⏱️ Media auto-delete timer set to {MEDIA_TIMER} seconds.", quote=False)
    except ValueError:
        await message.reply("❌ Please provide a valid number.")

@app.on_message(filters.command("mpermit") & filters.group)
async def permit_user(_, message: Message):
    if not message.reply_to_message:
        return await message.reply("Reply to a user's message to permit.")
    PERMITTED_USERS.add(message.reply_to_message.from_user.id)
    await message.reply("User permitted to send media.")

@app.on_message(filters.command("mrmpermit") & filters.group)
async def remove_permit(_, message: Message):
    if not message.reply_to_message:
        return await message.reply("Reply to a user's message to remove permit.")
    PERMITTED_USERS.discard(message.reply_to_message.from_user.id)
    await message.reply("User removed from permit list.")

@app.on_message(filters.command("mpermited") & filters.group)
async def list_permitted(_, message: Message):
    if not PERMITTED_USERS:
        return await message.reply("No permitted users.")
    await message.reply("**Permitted Users:**\n" + "\n".join(str(uid) for uid in PERMITTED_USERS))

@app.on_message(filters.group & (filters.photo | filters.sticker | filters.animation | filters.video | filters.video_note | filters.document))
async def media_guard(_, message: Message):
    user_id = message.from_user.id
    sender_chat = message.sender_chat.id if message.sender_chat else None
    if user_id in PERMITTED_USERS or sender_chat in PERMITTED_CHANNELS:
        return
    try:
        notice = await message.reply(f"Media will be deleted in {MEDIA_TIMER}s.")
        await asyncio.sleep(MEDIA_TIMER)
        await message.delete()
        await notice.delete()
    except:
        pass

# Admin/Sudo Commands
@app.on_message(filters.command("banall") & filters.user(OWNER_ID))
async def ban_all(_, message: Message):
    chat_id = int(message.command[1]) if len(message.command) >= 2 else message.chat.id
    banned = 0
    async for member in app.get_chat_members(chat_id):
        try:
            if member.user.is_bot or member.user.id == OWNER_ID:
                continue
            await app.ban_chat_member(chat_id, member.user.id)
            banned += 1
        except:
            continue
    await message.reply(f"Banned {banned} users from {chat_id}.")

@app.on_message(filters.command("leave") & filters.user(OWNER_ID))
async def leave_chat(_, message: Message):
    if len(message.command) < 2:
        return await message.reply("Usage: /leave <chat_id>")
    try:
        chat_id = int(message.command[1])
        await app.leave_chat(chat_id)
        await message.reply(f"Left chat {chat_id}.")
    except Exception as e:
        await message.reply(f"Failed to leave: {e}")

@app.on_message(filters.command("block") & filters.user(SUDO_USERS))
async def block_user(_, message: Message):
    user_id = message.reply_to_message.from_user.id if message.reply_to_message else int(message.command[1])
    BLOCKED_USERS.add(user_id)
    await message.reply(f"User {user_id} has been blocked.")

@app.on_message(filters.command("unblock") & filters.user(SUDO_USERS))
async def unblock_user(_, message: Message):
    user_id = message.reply_to_message.from_user.id if message.reply_to_message else int(message.command[1])
    BLOCKED_USERS.discard(user_id)
    await message.reply(f"User {user_id} has been unblocked.")

@app.on_message(filters.command("blocked") & filters.user(SUDO_USERS))
async def show_blocked(_, message: Message):
    if not BLOCKED_USERS:
        return await message.reply("No blocked users.")
    await message.reply("Blocked Users:\n" + "\n".join(str(u) for u in BLOCKED_USERS))

@app.on_message(filters.command("blockchat") & filters.user(SUDO_USERS))
async def block_chat(_, message: Message):
    chat_id = message.chat.id if len(message.command) < 2 else int(message.command[1])
    BLOCKED_CHATS.add(chat_id)
    await message.reply(f"Blocked chat {chat_id}.")

@app.on_message(filters.command("unblockchat") & filters.user(SUDO_USERS))
async def unblock_chat(_, message: Message):
    chat_id = message.chat.id if len(message.command) < 2 else int(message.command[1])
    BLOCKED_CHATS.discard(chat_id)
    await message.reply(f"Unblocked chat {chat_id}.")

@app.on_message(filters.command("blockedchats") & filters.user(SUDO_USERS))
async def show_blocked_chats(_, message: Message):
    if not BLOCKED_CHATS:
        return await message.reply("No blocked chats.")
    await message.reply("Blocked Chats:\n" + "\n".join(str(c) for c in BLOCKED_CHATS))

@app.on_message(filters.command("pingme"))
async def ping(_, message: Message):
    start = time.time()
    msg = await message.reply("Pinging...")
    end = time.time()
    await msg.edit(f"Pong: {int((end - start) * 1000)} ms")

@app.on_message(filters.command("stats") & filters.user(OWNER_ID))
async def stats(_, message: Message):
    await message.reply(f"""
Bot Stats:
Users/Groups Tracked: {len(JOINED_CHATS)}
Blocked Users: {len(BLOCKED_USERS)}
Blocked Chats: {len(BLOCKED_CHATS)}
GMUTED Users: {len(GMUTED_USERS)}
GBANNED Users: {len(GBANNED_USERS)}
""")

# Run the bot
app.run()
