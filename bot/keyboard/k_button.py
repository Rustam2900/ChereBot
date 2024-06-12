from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from conustant import ORDERS, MY_ORDERS, OPERATOR, SETTINGS, BACK, LANG_CHANGE, LOCATION_CHANGE


def main_menu():
    kb = [
        [KeyboardButton(text=ORDERS), KeyboardButton(text=MY_ORDERS)],
        [KeyboardButton(text=OPERATOR), KeyboardButton(text=SETTINGS)]
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
        [KeyboardButton(text='location', request_location=True)]
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True, one_time_keyboard=True)
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
         KeyboardButton(text=LOCATION_CHANGE, request_location=True)],
        [KeyboardButton(text=BACK)]
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
