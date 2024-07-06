from typing import Dict, List, Type

from aiogram import Dispatcher

from .base import BaseMiddleware
from .user import CheckUserMiddleware, AllowAnyMiddleware
from .throttling import ThrottlingMiddleware

__all__ = [
    'setup'
]

middlewares: Dict[str, List[Type[BaseMiddleware]]] = {
    "update": [],
    "message": [CheckUserMiddleware, AllowAnyMiddleware, ThrottlingMiddleware],
    "edited_message": [],
    "channel_post": [],
    "edited_channel_post": [],
    "inline_query": [],
    "chosen_inline_result": [],
    "callback_query": [CheckUserMiddleware, AllowAnyMiddleware, ThrottlingMiddleware],
    "shipping_query": [],
    "pre_checkout_query": [],
    "poll": [],
    "poll_answer": [],
    "my_chat_member": [],
    "chat_member": [],
    "chat_join_request": [],
    "error": [],
}


def setup(dp: Dispatcher):
    for observer in middlewares:
        for middleware in middlewares[observer]:
            if middleware.is_outer:
                dp.observers[observer].outer_middleware.register(middleware())
            else:
                dp.observers[observer].middleware.register(middleware())
