from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, KeyboardBuilder
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
                text=str(constants.INDIVIDUAL),

            ),
            KeyboardButton(
                text=str(constants.LEGAL_ENTITY)
            )
        ]
    )

    return builder.as_markup(resize_keyboard=True)


def main_menu():
    builder = ReplyKeyboardBuilder()
    builder.add(
        KeyboardButton(text=str(constants.MAKE_ORDER)),
        KeyboardButton(text=str(constants.MY_ORDERS)),
        KeyboardButton(text=str(constants.OPERATOR)),
        KeyboardButton(text=str(constants.SETTINGS))

    )
    builder.adjust(2)

    return builder.as_markup(resize_keyboard=True)


def cancel():
    builder = ReplyKeyboardBuilder()
    builder.row(
        KeyboardButton(text=str(constants.CANCEL)),
        width=1
    )
    return builder.as_markup(resize_keyboard=True)
