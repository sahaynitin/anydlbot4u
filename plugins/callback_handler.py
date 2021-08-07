import asyncio
import os
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery

if bool(os.environ.get("ENV", False)):
    from sample_config import Config
else:
    from config import Config

ads="PROGRESS..."
@Client.on_callback_query(filters.regex(r'^progress$'))
async def ytdl_progress(bot, cb: CallbackQuery):
    print('Pgreasc'*10)
    await cb.answer(f"{ads}", True)

