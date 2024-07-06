from typing import Optional

from aiogram.filters.callback_data import CallbackData


class LanguageCallbackData(CallbackData, prefix="choose-language"):
    language: str


class OperatorCallbackData(CallbackData, prefix="operator"):
    pass


class ProductCallbackData(CallbackData, prefix="product"):
    id: Optional[str] = None
    method: str
    quantity: Optional[int] = None
