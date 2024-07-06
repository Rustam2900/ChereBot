from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from bot import constants
from django.utils.translation import gettext_lazy as _


def request_contact():
    builder = ReplyKeyboardBuilder()
    builder.row(
        KeyboardButton(text=str(_("📱 Send contact")), request_contact=True),
        KeyboardButton(text=str(constants.CANCEL)),
        width=1
    )
    return builder.as_markup(resize_keyboard=True)


def choose_who_is_this_person():
    builder = ReplyKeyboardBuilder()

    builder.add(
        *[
            KeyboardButton(
                text="Jismoniy shaxs",

            ),
            KeyboardButton(
                text="Yuridik shaxs"
            )
        ]
    )

    return builder.as_markup(resize_keyboard=True)
