import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, Router
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from config import bot_token
from bot.header.start import router as router_start
from bot.header.orders import router as router_orders

router = Router()
router.include_router(router_start)
router.include_router(router_orders)

# @router.message(CommandStart())
# async def command_start_handler(message: Message) -> None:
#     await message.reply(text='Botga xush kelibsiz😊😊 \n'
#                              'Til tanlang', reply_markup=language())
#

# locales = {
#     'uz': Locale.parse('uz'),
#     'en': Locale.parse('en'),
#     'ru': Locale.parse('ru')
# }
#
#
# def get_translation(locale, message):
#     translations = {
#         'uz': {
#             "Tilni tanlang": "Tilni tanlang",
#             "Siz O'zbek tilini tanladingiz!": "Siz O'zbek tilini tanladingiz!",
#             "Siz yuborgan xabar: {text}": "Siz yuborgan xabar: {text}"
#         },
#         'en': {
#             "Tilni tanlang": "Choose a language",
#             "Siz English tilini tanladingiz!": "You have selected Uzbek!",
#             "Siz yuborgan xabar: {text}": "You sent: {text}"
#         },
#         'ru': {
#             "Tilni tanlang": "Выберите язык",
#             "Siz Русский tilini tanladingiz!": "Вы выбрали узбекский язык!",
#             "Siz yuborgan xabar: {text}": "Вы отправили: {text}"
#         }
#     }
#     return translations[locale].get(message, message)
#
#
# user_languages = {}
#
#
# @router.message(lambda message: message.text in ["🇺🇿 O'zbekcha", "🇷🇺 Русский", "🇬🇧 English"])
# async def set_language(message: types.Message):
#     if message.text == "🇺🇿 O'zbekcha":
#         user_languages[message.from_user.id] = 'uz'
#         await message.reply(get_translation('uz', "Siz O'zbek tilini tanladingiz!"))
#     elif message.text == "🇷🇺 Русский":
#         user_languages[message.from_user.id] = 'ru'
#         await message.reply(get_translation('ru', "Вы выбрали узбекский язык!"))
#     elif message.text == "🇬🇧 English":
#         user_languages[message.from_user.id] = 'en'
#         await message.reply(get_translation('en', "You have selected Uzbek!"))
#
#
# @router.message(lambda message: message.text not in ["🇺🇿 O'zbekcha", "🇷🇺 Русский", "🇬🇧 English"])
# async def echo_message(message: types.Message):
#     user_id = message.from_user.id
#     locale = user_languages.get(user_id, 'uz')
#     await message.reply(get_translation(locale, "Siz yuborgan xabar: {text}").format(text=message.text))

bot = Bot(token=bot_token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))


async def main() -> None:
    db = Dispatcher()

    db.include_router(router)

    await db.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
