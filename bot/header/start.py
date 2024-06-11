from aiogram import Router, types
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext

from api import create_user
from conustant import MAIN_TEXT
from header.orders import Form

router = Router()


@router.message(CommandStart())
async def name(message: types.Message, state: FSMContext):
    await message.reply(text=MAIN_TEXT)
    await state.set_state(Form.name)
    await message.answer('iltimos ismiz kiriting')
    create_user(message.from_user.username, message.from_user.first_name, message.from_user.id)
