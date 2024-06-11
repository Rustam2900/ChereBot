from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def language():
    language_keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="🇺🇿 O'zbekcha")],
            [KeyboardButton(text="🇷🇺 Русский")],
            [KeyboardButton(text="🇬🇧 English")],
        ],
        resize_keyboard=True
    )
    return language_keyboard
