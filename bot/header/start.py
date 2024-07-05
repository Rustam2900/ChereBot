import aiohttp

from aiogram import Router, types
from aiogram.filters import CommandStart

from bot.api_ import check_user_registration, check_company_registration
from bot.keyboard.k_button import main_menu, lang_change

router = Router()


@router.message(CommandStart())
async def start(message: types.Message):
    telegram_id = message.from_user.id

    async with aiohttp.ClientSession() as session:
        is_user_registered = await check_user_registration(session, telegram_id)
        is_company_registered = await check_company_registration(session, telegram_id)

    if not (is_user_registered or is_company_registered):
        await message.answer("Assalom botga xush kelibsiz tilni tanlang", reply_markup=lang_change())

    else:
        await message.answer(text="Bo‘limni tanlang 〽️:", reply_markup=main_menu())
