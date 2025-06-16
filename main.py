import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
import os

API_ID = 27309741
API_HASH = "7c2cabcd8d3f982d6f790eef7262890f"
BOT_TOKEN = "7786395475:AAH7id6w1kjl4JIBzoR5ZgvBNfcftLaqSyw"
OWNER_ID = 6037958673
LOG_CHANNEL = -1002077883652  # converted link to channel ID

bot = Client("KafkaGuardian", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@bot.on_message(filters.command("start") & filters.private)
async def start_cmd(client, message: Message):
    await message.reply(
        "**Welcome to Kafka – Edit and Media Guardian Bot!**\n\n"
        "I protect your groups from unwanted edits and media spam. Use the buttons below to explore features.",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("➕ Add Me to Group", url=f"https://t.me/Kafka_GurdianBot?startgroup=true")],
            [InlineKeyboardButton("👑 My God", callback_data="god_panel")],
            [InlineKeyboardButton("📘 Commands", callback_data="commands_panel")]
        ])
    )

@bot.on_callback_query(filters.regex("commands_panel"))
async def show_commands(_, callback_query):
    await callback_query.message.edit(
        "**🧭 Command Menu:**",
        reply_markup=InlineKeyboardMarkup([
            [
                InlineKeyboardButton("🖼 Media", callback_data="media_cmds"),
                InlineKeyboardButton("✏️ Edit", callback_data="edit_cmds")
            ],
            [
                InlineKeyboardButton("⚙️ Toggle", callback_data="toggle_cmds"),
                InlineKeyboardButton("🛡️ Sudo", callback_data="sudo_cmds")
            ],
            [InlineKeyboardButton("👑 GOD", callback_data="owner_cmds")]
        ])
    )

@bot.on_callback_query(filters.regex("media_cmds"))
async def media_cmds(_, cq):
    await cq.message.edit(
        "**📷 Media Commands:**\n"
        "`/mediatimer <time>` – Set deletion timer\n"
        "`/mpermit` – Permit user\n"
        "`/mrmpermit` – Remove permit\n"
        "`/mpermited` – View permitted users\n"
        "Deletes all stickers, gifs, images except permitted users or bots.",
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("◀️ Back", callback_data="commands_panel")]])
    )

@bot.on_callback_query(filters.regex("edit_cmds"))
async def edit_cmds(_, cq):
    await cq.message.edit(
        "**✏️ Edit Commands:**\n"
        "`/edittimer <time>` – Set edit deletion timer\n"
        "`/epermit` – Permit user\n"
        "`/ermpermit` – Remove permit\n"
        "`/epermited` – View permitted\n"
        "Notifies edited messages and deletes them after delay.",
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("◀️ Back", callback_data="commands_panel")]])
    )

@bot.on_callback_query(filters.regex("toggle_cmds"))
async def toggle_cmds(_, cq):
    await cq.message.edit(
        "**⚙️ Toggle Commands:**\n"
        "`/edit on|off` – Toggle edit protection\n"
        "`/media on|off` – Toggle media protection\n"
        "Admins with full rights, sudo users, and owner can toggle features.",
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("◀️ Back", callback_data="commands_panel")]])
    )

@bot.on_callback_query(filters.regex("sudo_cmds"))
async def sudo_cmds(_, cq):
    await cq.message.edit(
        "**🛡️ SUDO Commands:**\n"
        "`/sudo`, `/rmsudo`, `/sudolist`\n"
        "`/gban`, `/ungban`, `/gmute`, `/ungmute`\n"
        "`/block`, `/unblock`, `/blocked`\n"
        "`/blockchat`, `/unblockchat`, `/blockedchats`",
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("◀️ Back", callback_data="commands_panel")]])
    )

@bot.on_callback_query(filters.regex("owner_cmds"))
async def owner_cmds(_, cq):
    if cq.from_user.id != OWNER_ID:
        return await cq.answer("Only my God can access this 👑", show_alert=True)
    await cq.message.edit(
        "**👑 GOD Commands:**\n"
        "`/sudo`, `/rmsudo`, `/ycast`, `/banall`, `/leave`\n"
        "Only owner can use these.",
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("◀️ Back", callback_data="commands_panel")]])
    )

bot.run()
