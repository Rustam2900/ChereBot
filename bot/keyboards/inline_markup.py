from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from django.conf import settings

from bot.filters.callback_data import LanguageCallbackData, ProductCallbackData
from products.models import Product


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


async def get_products():
    products = [product async for product in Product.objects.all()]
    builder = InlineKeyboardBuilder()
    for product in products:
        builder.add(
            InlineKeyboardButton(
                text=f'{product.emoji if product.emoji else ""}{product.name}'.strip(),
                callback_data=ProductCallbackData(id=str(product.id), method='GET').pack()
            )
        )

    builder.add(
        InlineKeyboardButton(
            text='Back',
            callback_data=ProductCallbackData(method='BACK').pack(),
        ),
        InlineKeyboardButton(
            text='Make order',
            callback_data=ProductCallbackData(method='MAKE_ORDER').pack()
        )
    )

    builder.adjust(3)
    return builder.as_markup()
