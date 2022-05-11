from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, InputMediaPhoto, Message)

from config import MUSIC_BOT_NAME, SUPPORT_CHANNEL, SUPPORT_GROUP
from Yukki import BOT_USERNAME


def setting_markup2():
    buttons = [
        [
            InlineKeyboardButton(text="🔈 جودة الصوت", callback_data="AQ"),
            InlineKeyboardButton(text="🎚 حجم الصوت", callback_data="AV"),
        ],
        [
            InlineKeyboardButton(
                text="👥 المستخدمون المعتمدون", callback_data="AU"
            ),
            InlineKeyboardButton(
                text="💻لوحة القيادة", callback_data="Dashboard"
            ),
        ],
        [
            InlineKeyboardButton(text="• اغلاق •", callback_data="close"),
        ],
    ]
    return f"🔧  **{MUSIC_BOT_NAME} الاعدادت", buttons


def start_pannel():
    if not SUPPORT_CHANNEL and not SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="• اوامر البوت •", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="🔧 الإعدادات", callback_data="settingm"
                )
            ],
        ]
        return f"🎛  **هذا هو {MUSIC_BOT_NAME}**", buttons
    if not SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="• اوامر البوت •", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="🔧 الإعدادات", callback_data="settingm"
                )
            ],
            [
                InlineKeyboardButton(
                    text="‹ المطور ›", url=f"{SUPPORT_GROUP}"
                ),
            ],
        ]
        return f"🎛  **هذا هو {MUSIC_BOT_NAME}*", buttons
    if SUPPORT_CHANNEL and not SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="• اوامر البوت •", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="🔧 الإعدادات", callback_data="settingm"
                )
            ],
            [
                InlineKeyboardButton(
                    text="‹ قناه السورس ›", url=f"{SUPPORT_CHANNEL}"
                ),
            ],
        ]
        return f"🎛  **هذا هو {MUSIC_BOT_NAME}**", buttons
    if SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="• اوامر البوت •", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="🔧 الإعدادات", callback_data="settingm"
                )
            ],
            [
                InlineKeyboardButton(
                    text="‹ قناه السورس ›", url=f"{SUPPORT_CHANNEL}"
                ),
                InlineKeyboardButton(
                    text="‹ المطور ›", url=f"{SUPPORT_GROUP}"
                ),
            ],
        ]
        return f"🎛  **هذا هو {MUSIC_BOT_NAME}**", buttons


def private_panel():
    if not SUPPORT_CHANNEL and not SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="• اوامر البوت •", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    "‹ اضف البوت في مجموعتك ›",
                    url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                )
            ],
        ]
        return f"🎛  **هذا هو {MUSIC_BOT_NAME}**", buttons
    if not SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="• اوامر البوت •", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    "‹ اضف البوت في مجموعتك ›",
                    url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                )
            ],
            [
                InlineKeyboardButton(
                    text="‹ المطور ›", url=f"{SUPPORT_GROUP}"
                ),
            ],
        ]
        return f"🎛  **هذا هو {MUSIC_BOT_NAME}*", buttons
    if SUPPORT_CHANNEL and not SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="• اوامر البوت •", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    "‹ اضف البوت في مجموعتك ›",
                    url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                )
            ],
            [
                InlineKeyboardButton(
                    text="‹ قناه السورس ›", url=f"{SUPPORT_CHANNEL}"
                ),
            ],
        ]
        return f"🎛  **هذا هو {MUSIC_BOT_NAME}**", buttons
    if SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="• اوامر البوت •", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    "‹ اضف البوت في مجموعتك ›",
                    url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                )
            ],
            [
                InlineKeyboardButton(
                    text="‹ قناه السورس ›", url=f"{SUPPORT_CHANNEL}"
                ),
                InlineKeyboardButton(
                    text="‹ المطور ›", url=f"{SUPPORT_GROUP}"
                ),
            ],
        ]
        return f"🎛  **هذا هو {MUSIC_BOT_NAME}**", buttons


def setting_markup():
    buttons = [
        [
            InlineKeyboardButton(text="🔈 جودة الصوت", callback_data="AQ"),
            InlineKeyboardButton(text="🎚 حجم الصوت", callback_data="AV"),
        ],
        [
            InlineKeyboardButton(
                text="👥 المستخدمون المعتمدون", callback_data="AU"
            ),
            InlineKeyboardButton(
                text="💻لوحة القيادة", callback_data="Dashboard"
            ),
        ],
        [
            InlineKeyboardButton(text="• اغلاق •", callback_data="close"),
            InlineKeyboardButton(text="• رجوع •", callback_data="okaybhai"),
        ],
    ]
    return f"🔧  **{MUSIC_BOT_NAME} الاعدادت", buttons


def volmarkup():
    buttons = [
        [
            InlineKeyboardButton(
                text="🔄 Reset حجم الصوت 🔄", callback_data="HV"
            )
        ],
        [
            InlineKeyboardButton(text="🔈حجم منخفض", callback_data="LV"),
            InlineKeyboardButton(text="🔉حجم متوسط", callback_data="MV"),
        ],
        [
            InlineKeyboardButton(text="🔊 حجم صوت مرتفع", callback_data="HV"),
            InlineKeyboardButton(text="🔈 تضخيم حجم", callback_data="VAM"),
        ],
        [
            InlineKeyboardButton(
                text="🔽 حجم مخصص🔽", callback_data="Custommarkup"
            )
        ],
        [InlineKeyboardButton(text="• رجوع •", callback_data="settingm")],
    ]
    return f"🔧  **{MUSIC_BOT_NAME} الاعدادت", buttons


def custommarkup():
    buttons = [
        [
            InlineKeyboardButton(text="+10", callback_data="PTEN"),
            InlineKeyboardButton(text="-10", callback_data="MTEN"),
        ],
        [
            InlineKeyboardButton(text="+25", callback_data="PTF"),
            InlineKeyboardButton(text="-25", callback_data="MTF"),
        ],
        [
            InlineKeyboardButton(text="+50", callback_data="PFZ"),
            InlineKeyboardButton(text="-50", callback_data="MFZ"),
        ],
        [InlineKeyboardButton(text="🔼حجم مخصص🔼", callback_data="AV")],
    ]
    return f"🔧  **{MUSIC_BOT_NAME} الاعدادت", buttons


def usermarkup():
    buttons = [
        [
            InlineKeyboardButton(text="👥 Everyone", callback_data="EVE"),
            InlineKeyboardButton(text="🙍 Admins", callback_data="AMS"),
        ],
        [
            InlineKeyboardButton(
                text="📋 المستخدمون المعتمدون Lists", callback_data="USERLIST"
            )
        ],
        [InlineKeyboardButton(text="• رجوع •", callback_data="settingm")],
    ]
    return f"🔧  **{MUSIC_BOT_NAME} الاعدادت", buttons


def dashmarkup():
    buttons = [
        [
            InlineKeyboardButton(text="✔️ Uptime", callback_data="UPT"),
            InlineKeyboardButton(text="💾 Ram", callback_data="RAT"),
        ],
        [
            InlineKeyboardButton(text="💻 Cpu", callback_data="CPT"),
            InlineKeyboardButton(text="💽 Disk", callback_data="DIT"),
        ],
        [InlineKeyboardButton(text="• رجوع •", callback_data="settingm")],
    ]
    return f"🔧  **{MUSIC_BOT_NAME} الاعدادت", buttons
