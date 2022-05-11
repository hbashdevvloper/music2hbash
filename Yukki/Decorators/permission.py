from typing import Dict, List, Union

from Yukki import BOT_ID, app


def PermissionCheck(mystic):
    async def wrapper(_, message):
        a = await app.get_chat_member(message.chat.id, BOT_ID)
        if a.status != "administrator":
            return await message.reply_text(
                "أحتاج أن أكون مشرفًا مع بعض الصلاحيات:\n"
                + "\n- *صلاحيه لإدارة الدردشات الصوتية "
                + "\n- **صلاحيه حذف الرسائل:** لحذف نفايات البوت التي تم البحث عنها"
                + "\n- **صلاحيه دعوه المستخدمين**: لدعوة الحساب المساعد للدردشة."
            )
        if not a.can_manage_voice_chats:
            await message.reply_text(
                "انا لا امتلك صلاحيات  كامله يرجى ترقيتي."
                + "\n**صلاحيه لإدارة الدردشات الصوتية"
            )
            return
        if not a.can_delete_messages:
            await message.reply_text(
                "انا لا امتلك صلاحيات  كامله يرجى ترقيتي."
                + "\n**صلاحيه حذف الرسائل"
            )
            return
        if not a.can_invite_users:
            await message.reply_text(
                "انا لا امتلك صلاحيات  كامله يرجى ترقيتي."
                + "\n**صلاحيه دعوه المستخدمين  واضافه مستخدمين"
            )
            return
        return await mystic(_, message)

    return wrapper
