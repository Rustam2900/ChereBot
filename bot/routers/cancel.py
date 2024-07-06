from aiogram import Router, types, F, flags
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from bot import constants
from bot.keyboards import keyboard_markup
from users.models import User

router = Router()


@router.message(Command("cancel"))
@router.message(F.text == str(constants.CANCEL))
@flags.allow_any
@flags.rate_limit(key="cancel_actions")
async def cancel_handler(message: types.Message, state: FSMContext,
                         user_obj: User):
    if user_obj:
        await message.answer(text=str(constants.CANCEL), reply_markup=types.ReplyKeyboardRemove())
        await state.clear()
        await message.answer(text=str(constants.CHOOSE_SECTION), reply_markup=keyboard_markup.main_menu())
    else:
        await message.answer(text=str(constants.CANCEL), reply_markup=types.ReplyKeyboardRemove())
        await state.clear()
