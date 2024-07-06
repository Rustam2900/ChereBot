import logging
import sys

from django.core.management import BaseCommand

from bot.misc import dp, bot, on_startup, on_shutdown

logging.basicConfig(level=logging.INFO)  # or another level, like DEBUG
logger = logging.getLogger(__name__)


class Command(BaseCommand):
    def handle(self, *args, **options):
        logging.basicConfig(level=logging.INFO, stream=sys.stdout)
        dp.startup.register(on_startup)
        dp.shutdown.register(on_shutdown)
        logger.info('Starting aiogram bot...')
        try:
            dp.run_polling(bot)
        except Exception as e:
            logger.error(f'An error occurred while running the bot: {e}')
        else:
            logger.info('Bot polling stopped gracefully.')
