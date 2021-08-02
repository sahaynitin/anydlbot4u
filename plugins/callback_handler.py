import asyncio
import os
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery

if bool(os.environ.get("ENV", False)):
    from sample_config import Config
else:
    from config import Config

'''
@Client.on_callback_query(filters.regex(r'^progress$'))
async def ytdl_progress(bot, cb: CallbackQuery):
    file_siz = pgress()
    await cb.answer(f"Downloaded file size : {file_siz}", True)
'''
