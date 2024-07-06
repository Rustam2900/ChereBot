from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from django.conf import settings

from bot.filters.callback_data import LanguageCallbackData


def get_language_emoji(lang: str):
    _emojis = {
        "uz": "🇺🇿",
        "ru": "🇷🇺",
        "en": "🇺🇸",
    }
    if lang in _emojis:
        return _emojis[lang]
    return ""


def choose_language():
    builder = InlineKeyboardBuilder()

    builder.add(
        *[
            InlineKeyboardButton(text=str(get_language_emoji(language[0]) + language[1]).strip(),
                                 callback_data=LanguageCallbackData(language=language[0]).pack())
            for language in settings.LANGUAGES
        ]
    )
    builder.adjust(2)

    return builder.as_markup()

