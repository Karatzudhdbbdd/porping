import asyncio
import math
import os
import time
import httpx
import aiofiles
import aiohttp
from urllib.parse import urlparse
from filters import command
from pyrogram import Client, filters
from pyrogram.errors import FloodWait, MessageNotModified
from pyrogram.types import Message
from youtubesearchpython import SearchVideos
from yt_dlp import YoutubeDL
from youtube_search import YoutubeSearch
from YMusic import app
from moviepy.editor import VideoFileClip

@app.on_message(command(["يوت", "بحث"]))
async def vsong(client, message: Message):
    urlissed = get_text(message)

    pablo = await client.send_message(message.chat.id, f"**🔎جاري البحث** `{urlissed}`")
    if not urlissed:
        await pablo.edit(
            "صيغة الأمر غير صالحة يرجى مراجعة قائمة التعليمات لمعرفة المزيد!"
        )
        return

    search = SearchVideos(f"{urlissed}", offset=1, mode="dict", max_results=1)
    mi = search.result()
    mio = mi["search_result"]
    mo = mio[0]["link"]
    thum = mio[0]["title"]
    fridayz = mio[0]["id"]
    mio[0]["channel"]
    kekme = f"https://img.youtube.com/vi/{fridayz}/hqdefault.jpg"
    await asyncio.sleep(0.6)
    url = mo
    async with httpx.AsyncClient() as client_httpx:
        response = await client_httpx.get(kekme)
        with open("hqdefault.jpg", "wb") as img_file:
            img_file.write(response.content)
    sedlyf = "hqdefault.jpg"
    opts = {
        "format": "best",
        "addmetadata": True,
        "key": "FFmpegMetadata",
        "prefer_ffmpeg": True,
        "geo_bypass": True,
        "nocheckcertificate": True,
        "postprocessors": [{"key": "FFmpegVideoConvertor", "preferedformat": "mp4"}],
        "outtmpl": "%(id)s.mp4",
        "logtostderr": False,
        "quiet": True,
    }
    try:
        with YoutubeDL(opts) as ytdl:
            ytdl_data = ytdl.extract_info(url, download=True)
    except Exception as e:
        await event.edit(event, f"**التحميل فشل** \n**خطأ :** `{str(e)}`")
        return

    # قم بتحويل الفيديو إلى ملف صوتي
    audio_file = f"{ytdl_data['id']}.mp3"
    clip = VideoFileClip(f"{ytdl_data['id']}.mp4")
    clip.audio.write_audiofile(audio_file, codec='mp3')

    c_time = time.time()
    capy = f"""
**🏷️ اسم الفيديو:** [{thum}]({mo})
**🎧 طلب من العزيز:** {message.from_user.mention}
"""
    await client.send_audio(
        message.chat.id,
        audio=open(audio_file, "rb"),
        duration=int(ytdl_data["duration"]),
        title=str(ytdl_data["title"]),
        thumb=sedlyf,
        caption=capy,
        progress=progress,
        progress_args=(
            pablo,
            c_time,
            f"**📥 جاري التحميل** `{urlissed}`",
            audio_file,
        ),
    )

    await pablo.delete()
    for files in (sedlyf, f"{ytdl_data['id']}.mp4"):
        if files and os.path.exists(files):
            os.remove(files)


@app.on_message(command(["تحميل", "ف"]))
async def vsong(client, message: Message):
    urlissed = get_text(message)

    pablo = await client.send_message(message.chat.id, f"**🔎جاري البحث** `{urlissed}`")
    if not urlissed:
        await pablo.edit(
            "صيغة الأمر غير صالحة يرجى مراجعة قائمة التعليمات لمعرفة المزيد!"
        )
        return

    search = SearchVideos(f"{urlissed}", offset=1, mode="dict", max_results=1)
    mi = search.result()
    mio = mi["search_result"]
    mo = mio[0]["link"]
    thum = mio[0]["title"]
    fridayz = mio[0]["id"]
    mio[0]["channel"]
    kekme = f"https://img.youtube.com/vi/{fridayz}/hqdefault.jpg"
    await asyncio.sleep(0.6)
    url = mo
    async with httpx.AsyncClient() as client_httpx:
    response = await client_httpx.get(kekme)
    with open("hqdefault.jpg", "wb") as img_file:
        img_file.write(response.content)
    sedlyf = "hqdefault.jpg"
    opts = {
        "format": "best",
        "addmetadata": True,
        "key": "FFmpegMetadata",
        "prefer_ffmpeg": True,
        "geo_bypass": True,
        "nocheckcertificate": True,
        "postprocessors": [{"key": "FFmpegVideoConvertor", "preferedformat": "mp4"}],
        "outtmpl": "%(id)s.mp4",
        "logtostderr": False,
        "quiet": True,
    }
    try:
        with YoutubeDL(opts) as ytdl:
            ytdl_data = ytdl.extract_info(url, download=True)
    except Exception as e:
        await event.edit(event, f"**التحميل فشل** \n**خطأ :** `{str(e)}`")
        return
    c_time = time.time()
    file_stark = f"{ytdl_data['id']}.mp4"
    capy = f"""
**🏷️ اسم الفيديو:** [{thum}]({mo})
**🎧 طلب من العزيز:** {message.from_user.mention}
"""
    await client.send_video(
        message.chat.id,
        video=open(file_stark, "rb"),
        duration=int(ytdl_data["duration"]),
        file_name=str(ytdl_data["title"]),
        thumb=sedlyf,
        caption=capy,
        supports_streaming=True,
        progress=progress,
        progress_args=(
            pablo,
            c_time,
            f"**📥 جاري التحميل** `{urlissed}`",
            file_stark,
        ),
    )
    await pablo.delete()
    for files in (sedlyf, file_stark):
        if files and os.path.exists(files):
            os.remove(files)

