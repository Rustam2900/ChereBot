from aiogram.filters.callback_data import CallbackData


class LanguageCallbackData(CallbackData, prefix="choose-language"):
    language: str
