from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from ..conustant import ORDERS, MY_ORDERS, OPERATOR, SETTINGS, BACK, LANG_CHANGE, LOCATION, SETTINGS_RU, OPERATOR_RU, \
    ORDERS_RU, MY_ORDERS_RU, ORDERS_EN, MY_ORDERS_EN, OPERATOR_EN, SETTINGS_EN


def main_menu():
    kb = [
        [KeyboardButton(text=ORDERS), KeyboardButton(text=MY_ORDERS)],
        [KeyboardButton(text=OPERATOR), KeyboardButton(text=SETTINGS)]
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    return keyboard


def main_menu_ru():
    kb = [
        [KeyboardButton(text=ORDERS_RU), KeyboardButton(text=MY_ORDERS_RU)],
        [KeyboardButton(text=OPERATOR_RU), KeyboardButton(text=SETTINGS_RU)]
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    return keyboard


def main_menu_en():
    kb = [
        [KeyboardButton(text=ORDERS_EN), KeyboardButton(text=MY_ORDERS_EN)],
        [KeyboardButton(text=OPERATOR_EN), KeyboardButton(text=SETTINGS_EN)]
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    return keyboard


def contact_user():
    kb = [
        [KeyboardButton(text='contact', request_contact=True)]
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True, one_time_keyboard=True)
    return keyboard


def location_user():
    kb = [
        [KeyboardButton(text=LOCATION, request_location=True)
         ]
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    return keyboard


def back():
    kb = [
        [KeyboardButton(text=BACK)]
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    return keyboard


def settings():
    kb = [
        [KeyboardButton(text=LANG_CHANGE),
         KeyboardButton(text=BACK)
         ]

    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    return keyboard


def lang_change():
    kb = [
        [KeyboardButton(text='🇺🇿'),
         KeyboardButton(text='🇷🇺'), ],
        [KeyboardButton(text='🇬🇧'),
         KeyboardButton(text=BACK)]

    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    return keyboard
