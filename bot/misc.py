import logging

from aiogram import Dispatcher, Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.enums import ParseMode
from django.conf import settings

from bot.middlewares import setup as setup_middlewares
from bot.helpers import get_webhook_url
from bot.routers import router
from bot.utils.storage import DjangoRedisStorage

dp = Dispatcher(storage=DjangoRedisStorage(), )
bot_session = AiohttpSession()

bot = Bot(settings.BOT_TOKEN, session=bot_session, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

dp.include_router(router)
setup_middlewares(dp)


async def on_startup():
    logging.info('Starting up')
    if not settings.DEBUG:
        webhook_info = await bot.get_webhook_info()
        webhook_url = get_webhook_url()
        if webhook_url != webhook_info.url:
            await bot.set_webhook(
                url=webhook_url,
                allowed_updates=dp.resolve_used_update_types(),
                drop_pending_updates=True
            )


async def on_shutdown():
    logging.info('Shutting down')
    await bot_session.close()
