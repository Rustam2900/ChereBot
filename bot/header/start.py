from aiogram import Router, types
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext

from conustant import MAIN_TEXT
from header.register import RegisterForm
from keyboard.k_button import main_menu

router = Router()


@router.message(CommandStart())
async def name(message: types.Message, state: FSMContext):
    await message.reply(text=MAIN_TEXT)

    # check user registered or not
    is_user_registered = False

    if not is_user_registered:
        await state.set_state(RegisterForm.name)
        await message.answer('iltimos ismiz kiriting')
        # create_user(message.from_user.username, message.from_user.first_name, message.from_user.id)
    else:
        await message.answer(text="Bo‘limni tanlang 〽️:", reply_markup=main_menu())
