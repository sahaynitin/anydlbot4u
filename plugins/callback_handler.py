import asyncio
import os
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery

'''
ads="PROGRESS..."
@Client.on_callback_query(filters.regex(r'^progress$'))
async def ytdl_progress(bot, cb: CallbackQuery):
    print('Pgreasc'*10)
    await cb.answer(f"{ads}", True)

'''
