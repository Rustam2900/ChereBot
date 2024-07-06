from typing import Callable, Dict, Any, Awaitable

from aiogram import types
from aiogram.dispatcher.event.handler import HandlerObject
from aiogram.dispatcher.flags import get_flag
from aiogram.fsm.context import FSMContext
from aiogram.types import TelegramObject
from django.conf import settings
from django.utils import translation
from django.utils.translation import gettext_lazy as _

from users.models import User
from .base import BaseMiddleware


class CheckUserMiddleware(BaseMiddleware):
    is_outer = True

    async def __call__(self, handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]], event: TelegramObject,
                       data: Dict[str, Any], *args, **kwargs) -> Any:
        user: types.User = data.get('event_from_user')
        user_obj = await User.objects.filter(telegram_id=user.id).afirst()

        if user_obj:
            data['user_obj'] = user_obj
            translation.activate(user_obj.language or settings.LANGUAGE_CODE)
        else:
            data['user_obj'] = None
            state: FSMContext = data.get('state')
            state_data = await state.get_data()
            translation.activate(state_data.get('language') or user.language)
        return await handler(event, data)


class AllowAnyMiddleware(BaseMiddleware):
    is_outer = False

    async def __call__(self, handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
                       event: TelegramObject,
                       data: Dict[str, Any]) -> Any:
        handler_obj: HandlerObject = data.get('handler')
        allow_any = get_flag(handler_obj, 'allow_any')
        user_obj = data.get('user_obj')
        if allow_any or user_obj:
            return await handler(event, data)
        text = _("Please register first or login. To start registration or login send /start")
        if isinstance(event, types.Message):
            await event.answer(str(text))
        elif isinstance(event, types.CallbackQuery):
            await event.message.answer(str(text))
