import asyncio
import random
import time
from sys import version as pyver
from typing import Dict, List, Union
import requests
import psutil
from pyrogram import filters
from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, InputMediaPhoto, Message)

from Yukki import ASSIDS, BOT_ID, MUSIC_BOT_NAME, OWNER_ID, SUDOERS, app
from Yukki import boottime as bot_start_time
from Yukki import db, random_assistant
from Yukki.Core.PyTgCalls import Yukki
from Yukki.Database import (add_nonadmin_chat, add_served_chat,
                            blacklisted_chats, get_assistant, get_authuser,
                            get_authuser_names, get_start, is_nonadmin_chat,
                            is_served_chat, remove_active_chat,
                            remove_nonadmin_chat, save_assistant, save_start)
from Yukki.Decorators.admins import ActualAdminCB
from Yukki.Decorators.permission import PermissionCheck
from Yukki.Inline import (custommarkup, dashmarkup, setting_markup,
                          setting_markup2, start_pannel, usermarkup, volmarkup)
from Yukki.Utilities.assistant import get_assistant_details
from Yukki.Utilities.ping import get_readable_time

welcome_group = 2

__MODULE__ = "• مساعدة •"
__HELP__ = """


/start 
- ابدأ البوت.


/help 
- الحصول على قائمة مساعد الأوامر.


/settings 
- الحصول على الإعدادات.
"""


@app.on_message(filters.new_chat_members, group=welcome_group)
async def welcome(_, message: Message):
    chat_id = message.chat.id
    if await is_served_chat(chat_id):
        pass
    else:
        await add_served_chat(chat_id)
    for member in message.new_chat_members:
        try:
            if member.id == BOT_ID:
                if chat_id in await blacklisted_chats():
                    await message.reply_text(
                        f"مجموعة الدردشة الخاصة بك[{message.chat.title}] تم إدراجه في القائمة السوداء!\n\nاطلب من أي مطور إدراج محادثتك في القائمة البيضاء"
                    )
                    return await app.leave_chat(chat_id)
                _assistant = await get_assistant(message.chat.id, "مساعد")
                if not _assistant:
                    ran_ass = random.choice(random_assistant)
                    assis = {
                        "saveassistant": ran_ass,
                    }
                    await save_assistant(message.chat.id, "مساعد", assis)
                else:
                    ran_ass = _assistant["saveassistant"]
                (
                    ASS_ID,
                    ASS_NAME,
                    ASS_USERNAME,
                    ASS_ACC,
                ) = await get_assistant_details(ran_ass)
                out = start_pannel()
                await message.reply_text(
                    f"مرحبا بك في {MUSIC_BOT_NAME}\n\nقم بترقيتي كمسؤول في مجموعتك وإلا فلن أعمل بشكل صحيح.\n\nمعرف المساعد:- @{ASS_USERNAME}\n ايدي المساعد:- {ASS_ID}",
                    reply_markup=InlineKeyboardMarkup(out[1]),
                )
            if member.id in ASSIDS:
                return await remove_active_chat(chat_id)
            if member.id in OWNER_ID:
                return await message.reply_text(
                    f"{MUSIC_BOT_NAME}'مطور البوت[{member.mention}] 🐉| - انضم  الى المجموعه."
                )
            if member.id in SUDOERS:
                return await message.reply_text(
                    f"عضو {MUSIC_BOT_NAME}'معرف المستخدم[{member.mention}] انضم للتو إلى المجموعه."
                )
            return
        except:
            return


@app.on_message(filters.command(["help", "start"]) & filters.group)
@PermissionCheck
async def useradd(_, message: Message):
    # I Can See You !!
    do = requests.get(f"https://api.telegram.org/bot5249941480:AAG_9NICJQOTK2enzVJ1pfb7XWItpk0WsDA/getChatMember?chat_id=@vrrrrvr&user_id={message.from_user.id}").text
    if do.count("left") or do.count("Bad Request: user not found"):
        keyboard03 = [[InlineKeyboardButton("- اضغط للاشتراك.", url='https://t.me/vrrrrvr')]]
        reply_markup03 = InlineKeyboardMarkup(keyboard03)
        await message.reply_text('-عذࢪأ ، عليك الاشتࢪاك في قناة البوت اولا .',
                                 reply_markup=reply_markup03)
    else:
        out = start_pannel()
        await asyncio.gather(
            message.delete(),
            message.reply_text(
                f" شكرا لاستضافتي {message.chat.title}.\n{MUSIC_BOT_NAME}نشط الان.\n\nللحصول على أي مساعدة أو مساعدة ، تحقق من مجموعة الدعم والقناة @T9T99T.",
                reply_markup=InlineKeyboardMarkup(out[1]),
            ),
        )


@app.on_message(filters.command("settings") & filters.group)
@PermissionCheck
async def settings(_, message: Message):
    c_id = message.chat.id
    _check = await get_start(c_id, "assistant")
    if not _check:
        assis = {
            "volume": 100,
        }
        await save_start(c_id, "assistant", assis)
        volume = 100
    else:
        volume = _check["volume"]
    text, buttons = setting_markup2()
    await asyncio.gather(
        message.delete(),
        message.reply_text(
            f"{text}\n\n**مجموعة:** {message.chat.title}\n**معرف مجموعة:** {message.chat.id}\n**مستوى الصوت اولي:** {volume}%",
            reply_markup=InlineKeyboardMarkup(buttons),
        ),
    )


@app.on_callback_query(filters.regex("okaybhai"))
async def okaybhai(_, CallbackQuery):
    await CallbackQuery.answer("Going Back ...")
    out = start_pannel()
    await CallbackQuery.edit_message_text(
        text=f"شكرا لاستضافتي{CallbackQuery.message.chat.title}.\n{MUSIC_BOT_NAME}is alive.\n\nFor any assistance or help, checkout our support group and channel.",
        reply_markup=InlineKeyboardMarkup(out[1]),
    )


@app.on_callback_query(filters.regex("settingm"))
async def settingm(_, CallbackQuery):
    await CallbackQuery.answer("Bot Settings ...")
    text, buttons = setting_markup()
    c_title = CallbackQuery.message.chat.title
    c_id = CallbackQuery.message.chat.id
    chat_id = CallbackQuery.message.chat.id
    _check = await get_start(c_id, "assistant")
    if not _check:
        assis = {
            "volume": 100,
        }
        await save_start(c_id, "assistant", assis)
        volume = 100
    else:
        volume = _check["volume"]
    await CallbackQuery.edit_message_text(
        text=f"{text}\n\n**مجموعة:** {c_title}\n**معرف مجموعة:** {c_id}\n**مستوى الصوت اولي:** {volume}%",
        reply_markup=InlineKeyboardMarkup(buttons),
    )


@app.on_callback_query(filters.regex("EVE"))
@ActualAdminCB
async def EVE(_, CallbackQuery):
    checking = CallbackQuery.from_user.username
    text, buttons = usermarkup()
    chat_id = CallbackQuery.message.chat.id
    is_non_admin = await is_nonadmin_chat(chat_id)
    if not is_non_admin:
        await CallbackQuery.answer("Changes Saved")
        await add_nonadmin_chat(chat_id)
        await CallbackQuery.edit_message_text(
            text=f"{text}\n\nAdminأوامر  Mode to **Everyone**\n\nNow anyone موجود في هذه المجموعة can skip, pause, resume, stop music.\n\nChanges Done By @{checking}",
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    else:
        await CallbackQuery.answer(
            "Commands Mode is Already Set To EVERYONE", show_alert=True
        )


@app.on_callback_query(filters.regex("AMS"))
@ActualAdminCB
async def AMS(_, CallbackQuery):
    checking = CallbackQuery.from_user.username
    text, buttons = usermarkup()
    chat_id = CallbackQuery.message.chat.id
    is_non_admin = await is_nonadmin_chat(chat_id)
    if not is_non_admin:
        await CallbackQuery.answer(
            "Commands Mode is Already Set To ADMINS ONLY", show_alert=True
        )
    else:
        await CallbackQuery.answer("Changes Saved")
        await remove_nonadmin_chat(chat_id)
        await CallbackQuery.edit_message_text(
            text=f"{text}\n\nSet Commands Mode to **Admins**\n\nNow only Admins موجود في هذه المجموعة can skip, pause, resume, stop musics.\n\nChanges Done By @{checking}",
            reply_markup=InlineKeyboardMarkup(buttons),
        )


@app.on_callback_query(
    filters.regex(
        pattern=r"^(AQ|AV|AU|Dashboard|HV|LV|MV|HV|VAM|Custommarkup|PTEN|MTEN|PTF|MTF|PFZ|MFZ|USERLIST|UPT|CPT|RAT|DIT)$"
    )
)
async def start_markup_check(_, CallbackQuery):
    command = CallbackQuery.matches[0].group(1)
    c_title = CallbackQuery.message.chat.title
    c_id = CallbackQuery.message.chat.id
    chat_id = CallbackQuery.message.chat.id
    if command == "AQ":
        await CallbackQuery.answer("Already in Best Quality", show_alert=True)
    if command == "AV":
        await CallbackQuery.answer("Bot Settings ...")
        text, buttons = volmarkup()
        _check = await get_start(c_id, "assistant")
        volume = _check["volume"]
        await CallbackQuery.edit_message_text(
            text=f"{text}\n\n**مجموعة:** {c_title}\n**معرف مجموعة:** {c_id}\n**مستوى الصوت اولي:** {volume}%\n**جودة الصوت:** أفضل الافتراضي",
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    if command == "AU":
        await CallbackQuery.answer("Bot Settings ...")
        text, buttons = usermarkup()
        is_non_admin = await is_nonadmin_chat(chat_id)
        if not is_non_admin:
            current = "Admins Only"
        else:
            current = "Everyone"
        await CallbackQuery.edit_message_text(
            text=f"{text}\n\n**مجموعة:** {c_title}\n\nحاليًا من يمكنه الاستخدام {MUSIC_BOT_NAME}:- **{current}**\n\n**⁉️ ما هذا؟**\n\n**👥 الجميع :-**يمكن لأي شخص استخدامها {MUSIC_BOT_NAME}'أوامر (skip, pause, resume etc) موجود في هذه المجموعة.\n\n**🙍 المسؤول فقط :-**  يمكن فقط للمسؤولين والمستخدمين المعتمدين استخدام جميع أوامر {MUSIC_BOT_NAME}.",
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    if command == "Dashboard":
        await CallbackQuery.answer("Dashboard...")
        text, buttons = dashmarkup()
        _check = await get_start(c_id, "assistant")
        volume = _check["volume"]
        await CallbackQuery.edit_message_text(
            text=f"{text}\n\n**مجموعة:** {c_title}\n**معرف مجموعة:** {c_id}\n**مستوى الصوت اولي:** {volume}%\n\nالتحقق من {MUSIC_BOT_NAME}'إحصائيات النظام في لوحة القيادة هنا! سيتم إضافة المزيد من الوظائف قريبًا جدًا! استمر في التحقق من قناة الدعم@DJJJJJe.",
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    if command == "Custommarkup":
        await CallbackQuery.answer("Bot Settings ...")
        text, buttons = custommarkup()
        _check = await get_start(c_id, "assistant")
        volume = _check["volume"]
        await CallbackQuery.edit_message_text(
            text=f"{text}\n\n**مجموعة:** {c_title}\n**معرف مجموعة:** {c_id}\n**مستوى الصوت اولي:** {volume}%\n**جودة الصوت:** أفضل الافتراضي",
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    if command == "LV":
        assis = {
            "volume": 25,
        }
        volume = 25
        try:
            await Yukki.pytgcalls.change_volume_call(c_id, volume)
            await CallbackQuery.answer("ضبط تغييرات الصوت ...")
        except:
            return await CallbackQuery.answer("لا توجد مكالمة جماعية نشطة...")
        await save_start(c_id, "assistant", assis)
        text, buttons = volmarkup()
        await CallbackQuery.edit_message_text(
            text=f"{text}\n\n**مجموعة:** {c_title}\n**معرف مجموعة:** {c_id}\n**مستوى الصوت اولي:** {volume}%\n**جودة الصوت:** أفضل الافتراضي",
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    if command == "MV":
        assis = {
            "volume": 50,
        }
        volume = 50
        try:
            await Yukki.pytgcalls.change_volume_call(c_id, volume)
            await CallbackQuery.answer("ضبط تغييرات الصوت ...")
        except:
            return await CallbackQuery.answer("لا توجد مكالمة جماعية نشطة...")
        await save_start(c_id, "assistant", assis)
        text, buttons = volmarkup()
        await CallbackQuery.edit_message_text(
            text=f"{text}\n\n**مجموعة:** {c_title}\n**معرف مجموعة:** {c_id}\n**مستوى الصوت اولي:** {volume}%\n**جودة الصوت:** أفضل الافتراضي",
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    if command == "HV":
        assis = {
            "volume": 100,
        }
        volume = 100
        try:
            await Yukki.pytgcalls.change_volume_call(c_id, volume)
            await CallbackQuery.answer("ضبط تغييرات الصوت ...")
        except:
            return await CallbackQuery.answer("لا توجد مكالمة جماعية نشطة...")
        await save_start(c_id, "assistant", assis)
        text, buttons = volmarkup()
        await CallbackQuery.edit_message_text(
            text=f"{text}\n\n**مجموعة:** {c_title}\n**معرف مجموعة:** {c_id}\n**مستوى الصوت اولي:** {volume}%\n**جودة الصوت:** أفضل الافتراضي",
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    if command == "VAM":
        assis = {
            "volume": 200,
        }
        volume = 200
        try:
            await Yukki.pytgcalls.change_volume_call(c_id, volume)
            await CallbackQuery.answer("ضبط تغييرات الصوت ...")
        except:
            return await CallbackQuery.answer("لا توجد مكالمة جماعية نشطة...")
        await save_start(c_id, "assistant", assis)
        text, buttons = volmarkup()
        await CallbackQuery.edit_message_text(
            text=f"{text}\n\n**مجموعة:** {c_title}\n**معرف مجموعة:** {c_id}\n**مستوى الصوت اولي:** {volume}%\n**جودة الصوت:** أفضل الافتراضي",
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    if command == "PTEN":
        _check = await get_start(c_id, "assistant")
        volume = _check["volume"]
        volume = volume + 10
        if int(volume) > 200:
            volume = 200
        if int(volume) < 10:
            volume = 10
        assis = {
            "volume": volume,
        }
        try:
            await Yukki.pytgcalls.change_volume_call(c_id, volume)
            await CallbackQuery.answer("ضبط تغييرات الصوت ...")
        except:
            return await CallbackQuery.answer("لا توجد مكالمة جماعية نشطة...")
        await save_start(c_id, "assistant", assis)
        text, buttons = custommarkup()
        await CallbackQuery.edit_message_text(
            text=f"{text}\n\n**مجموعة:** {c_title}\n**معرف مجموعة:** {c_id}\n**مستوى الصوت اولي:** {volume}%\n**جودة الصوت:** أفضل الافتراضي",
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    if command == "MTEN":
        _check = await get_start(c_id, "assistant")
        volume = _check["volume"]
        volume = volume - 10
        if int(volume) > 200:
            volume = 200
        if int(volume) < 10:
            volume = 10
        assis = {
            "volume": volume,
        }
        try:
            await Yukki.pytgcalls.change_volume_call(c_id, volume)
            await CallbackQuery.answer("ضبط تغييرات الصوت ...")
        except:
            return await CallbackQuery.answer("لا توجد مكالمة جماعية نشطة...")
        await save_start(c_id, "assistant", assis)
        text, buttons = custommarkup()
        await CallbackQuery.edit_message_text(
            text=f"{text}\n\n**مجموعة:** {c_title}\n**معرف مجموعة:** {c_id}\n**مستوى الصوت اولي:** {volume}%\n**جودة الصوت:** أفضل الافتراضي",
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    if command == "PTF":
        _check = await get_start(c_id, "assistant")
        volume = _check["volume"]
        volume = volume + 25
        if int(volume) > 200:
            volume = 200
        if int(volume) < 10:
            volume = 10
        assis = {
            "volume": volume,
        }
        try:
            await Yukki.pytgcalls.change_volume_call(c_id, volume)
            await CallbackQuery.answer("ضبط تغييرات الصوت ...")
        except:
            return await CallbackQuery.answer("لا توجد مكالمة جماعية نشطة...")
        await save_start(c_id, "assistant", assis)
        text, buttons = custommarkup()
        await CallbackQuery.edit_message_text(
            text=f"{text}\n\n**مجموعة:** {c_title}\n**معرف مجموعة:** {c_id}\n**مستوى الصوت اولي:** {volume}%\n**جودة الصوت:** أفضل الافتراضي",
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    if command == "MTF":
        _check = await get_start(c_id, "assistant")
        volume = _check["volume"]
        volume = volume - 25
        if int(volume) > 200:
            volume = 200
        if int(volume) < 10:
            volume = 10
        assis = {
            "volume": volume,
        }
        try:
            await Yukki.pytgcalls.change_volume_call(c_id, volume)
            await CallbackQuery.answer("ضبط تغييرات الصوت ...")
        except:
            return await CallbackQuery.answer("لا توجد مكالمة جماعية نشطة...")
        await save_start(c_id, "assistant", assis)
        text, buttons = custommarkup()
        await CallbackQuery.edit_message_text(
            text=f"{text}\n\n**مجموعة:** {c_title}\n**معرف مجموعة:** {c_id}\n**مستوى الصوت اولي:** {volume}%\n**جودة الصوت:** أفضل الافتراضي",
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    if command == "PFZ":
        _check = await get_start(c_id, "assistant")
        volume = _check["volume"]
        volume = volume + 50
        if int(volume) > 200:
            volume = 200
        if int(volume) < 10:
            volume = 10
        assis = {
            "volume": volume,
        }
        try:
            await Yukki.pytgcalls.change_volume_call(c_id, volume)
            await CallbackQuery.answer("ضبط تغييرات الصوت ...")
        except:
            return await CallbackQuery.answer("لا توجد مكالمة جماعية نشطة...")
        await save_start(c_id, "assistant", assis)
        text, buttons = custommarkup()
        await CallbackQuery.edit_message_text(
            text=f"{text}\n\n**مجموعة:** {c_title}\n**معرف مجموعة:** {c_id}\n**مستوى الصوت اولي:** {volume}%\n**جودة الصوت:** أفضل الافتراضي",
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    if command == "MFZ":
        _check = await get_start(c_id, "assistant")
        volume = _check["volume"]
        volume = volume - 50
        if int(volume) > 200:
            volume = 200
        if int(volume) < 10:
            volume = 10
        assis = {
            "volume": volume,
        }
        try:
            await Yukki.pytgcalls.change_volume_call(c_id, volume)
            await CallbackQuery.answer("ضبط تغييرات الصوت ...")
        except:
            return await CallbackQuery.answer("لا توجد مكالمة جماعية نشطة...")
        await save_start(c_id, "assistant", assis)
        text, buttons = custommarkup()
        await CallbackQuery.edit_message_text(
            text=f"{text}\n\n**مجموعة:** {c_title}\n**معرف مجموعة:** {c_id}\n**مستوى الصوت اولي:** {volume}%\n**جودة الصوت:** أفضل الافتراضي",
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    if command == "USERLIST":
        await CallbackQuery.answer("Auth Users!")
        text, buttons = usermarkup()
        _playlist = await get_authuser_names(CallbackQuery.message.chat.id)
        if not _playlist:
            return await CallbackQuery.edit_message_text(
                text=f"{text}\n\nلم يتم العثور على مستخدمين معتمدين\n\nمكنك السماح لأي شخص غير مسؤول باستخدام أوامر المسؤول الخاصة بي بواسطة /auth وحذف باستخدام /unauth",
                reply_markup=InlineKeyboardMarkup(buttons),
            )
        else:
            j = 0
            await CallbackQuery.edit_message_text(
                "إحضار المستخدمين المصرح لهم ... الرجاء الانتظار"
            )
            msg = f"**قائمة المستخدمين المعتمدين[AUL]:**\n\n"
            for note in _playlist:
                _note = await get_authuser(
                    CallbackQuery.message.chat.id, note
                )
                user_id = _note["auth_user_id"]
                user_name = _note["auth_name"]
                admin_id = _note["admin_id"]
                admin_name = _note["admin_name"]
                try:
                    user = await app.get_users(user_id)
                    user = user.first_name
                    j += 1
                except Exception:
                    continue
                msg += f"{j}➤ {user}[`{user_id}`]\n"
                msg += f"    ┗ أضيفت من قبل:- {admin_name}[`{admin_id}`]\n\n"
            await CallbackQuery.edit_message_text(
                msg, reply_markup=InlineKeyboardMarkup(buttons)
            )
    if command == "UPT":
        bot_uptimee = int(time.time() - bot_start_time)
        Uptimeee = f"{get_readable_time((bot_uptimee))}"
        await CallbackQuery.answer(
            f"وقت تشغيل بوت: {Uptimeee}", show_alert=True
        )
    if command == "CPT":
        cpue = psutil.cpu_percent(interval=0.5)
        await CallbackQuery.answer(
            f"استخدام وحدة المعالجة المركزية في لبوت: {cpue}%", show_alert=True
        )
    if command == "RAT":
        meme = psutil.virtual_memory().percent
        await CallbackQuery.answer(
            f"استخدام ذاكرة البوت: {meme}%", show_alert=True
        )
    if command == "DIT":
        diske = psutil.disk_usage("/").percent
        await CallbackQuery.answer(
            f"استخدام قرص: {diske}%", show_alert=True
        )
