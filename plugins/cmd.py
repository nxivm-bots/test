# Import required libraries and modules
from bot import Bot
from pyrogram import Client, filters
from config import *
from datetime import datetime
from plugins.start import *
from pyrogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums import ParseMode
import time
from database.database import *

# Command: Add a Channel
@Bot.on_message(filters.command("add_channel") & filters.user(ADMINS))  # ADMINS = Admin User ID
async def add_force_sub_channel(client, message):
    try:
        args = message.text.split(maxsplit=1)
        if len(args) != 2:
            await message.reply("Usage: /add_channel <channel_id>")
            return
        channel_id = int(args[1])
        await add_channel(channel_id)
        await message.reply(f"✅ Channel {channel_id} has been added to the force-subscription list.")
    except Exception as e:
        await message.reply(f"❌ Error adding channel: {e}")

# Command: Remove a Channel
@Bot.on_message(filters.command("remove_channel") & filters.user(ADMINS))
async def remove_force_sub_channel(client, message):
    try:
        args = message.text.split(maxsplit=1)
        if len(args) != 2:
            await message.reply("Usage: /remove_channel <channel_id>")
            return
        channel_id = int(args[1])
        await remove_channel(channel_id)
        await message.reply(f"✅ Channel {channel_id} has been removed from the force-subscription list.")
    except Exception as e:
        await message.reply(f"❌ Error removing channel: {e}")

# Command: List All Channels
@Bot.on_message(filters.command("list_channels") & filters.user(ADMINS))
async def list_force_sub_channels(client, message):
    try:
        channels = await list_channels()
        if not channels:
            await message.reply("No channels in the force-subscription list.")
            return
        channel_list = "\n".join([f"- {channel_id}" for channel_id in channels])
        await message.reply(f"📜 Force-Subscription Channels:\n{channel_list}")
    except Exception as e:
        await message.reply(f"❌ Error listing channels: {e}")



# /help command to show available commands
@Bot.on_message(filters.command('help') & filters.private )
async def help_command(bot: Bot, message: Message):
    help_text = """
📖 <b>Available Commands:</b>

/start - Start the bot and see welcome message.
/help - Show this help message.
/batch - Create link for more than one posts.
/genlink - Create link for one post.
/stats - Check your bot uptime.
/users - View bot statistics (Admins only).
/broadcast - Broadcast any messages to bot users (Admins only).
/add_channel - (Admins only).
/remove_channel - (Admins only).
/list_channels - (Admins only).

"""
    await message.reply(help_text, parse_mode=ParseMode.HTML)


