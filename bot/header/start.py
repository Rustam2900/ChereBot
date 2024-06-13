from aiogram import Router, types
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext

from bot.api import check_user_registration
from bot.conustant import MAIN_TEXT
from bot.header.register import RegisterForm
from bot.keyboard.k_button import main_menu

router = Router()


@router.message(CommandStart())
async def start(message: types.Message, state: FSMContext):
    # Check if user is already registered
    telegram_id = message.from_user.id
    is_user_registered = await check_user_registration(telegram_id)

    if not is_user_registered:
        await state.set_state(RegisterForm.name)
        await message.answer('Ismingizni kiriting, iltimos:')
    else:
        await message.answer(text="Bo‘limni tanlang 〽️:", reply_markup=main_menu())
