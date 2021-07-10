#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K

# the logging things
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os
import time

# the secret configuration specific things
if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

# the Strings used for this "thing"
from translation import Translation

import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)

from helper_funcs.chat_base import TRChatBase
from helper_funcs.display_progress import progress_for_pyrogram
from helper_funcs.help_Nekmo_ffmpeg import take_screen_shot, cult_small_video

from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
from moviepy.editor import *
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

@pyrogram.Client.on_message(pyrogram.Filters.command(["ffmpegrobot"]))
async def ffmpegrobot_ad(bot, update):
    if update.from_user.id not in Config.AUTH_USERS:
        await bot.delete_messages(
            chat_id=update.chat.id,
            message_ids=update.message_id,
            revoke=True
        )
        return
    TRChatBase(update.from_user.id, update.text, "ffmpegrobot")
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.FF_MPEG_RO_BOT_AD_VER_TISE_MENT,
        disable_web_page_preview=True,
        reply_to_message_id=update.message_id
    )


@pyrogram.Client.on_message(pyrogram.Filters.command(["tri"]))
async def trim(bot, update):
    if update.from_user.id not in Config.AUTH_USERS:
        await bot.delete_messages(
            chat_id=update.chat.id,
            message_ids=update.message_id,
            revoke=True
        )
        return
    TRChatBase(update.from_user.id, update.text, "trim")
    saved_file_path = Config.DOWNLOAD_LOCATION + "/" + str(update.from_user.id) + ".FFMpeg.mkv"
    if os.path.exists(saved_file_path):
        a = await bot.send_message(
            chat_id=update.chat.id,
            text=Translation.DOWNLOAD_START,
            reply_to_message_id=update.message_id
        )
        video_clip = VideoFileClip(saved_file_path).subclip(0, 60)
        video_clip.write_videofile(saved_file_path+'cut.mp4')
        video_file=saved_file_path+"cut.mp4"
        '''commands = update.command
        if len(commands) == 3:
            # output should be video
            cmd, start_time, end_time = commands
            o = await cult_small_video(saved_file_path, Config.DOWNLOAD_LOCATION, start_time, end_time)
            logger.info(o)
            if o is not None:'''
        await bot.edit_message_text(
                    chat_id=update.chat.id,
                    text=Translation.UPLOAD_START,
                    message_id=a.message_id
                )
        c_time = time.time()
        await bot.send_video(
                    chat_id=update.chat.id,
                    video=video_file,
                    # caption=description,
                    # duration=duration,
                    # width=width,
                    # height=height,
                    supports_streaming=True,
                    # reply_markup=reply_markup,
                    # thumb=thumb_image_path,
                    reply_to_message_id=update.message_id,
                    progress=progress_for_pyrogram,
                    progress_args=(
                        Translation.UPLOAD_START,
                        a,
                        c_time
                    )
                )
        os.remove(video_file)
        await bot.edit_message_text(
                    chat_id=update.chat.id,
                    text=Translation.AFTER_SUCCESSFUL_UPLOAD_MSG,
                    disable_web_page_preview=True,
                    message_id=a.message_id
                )
            
