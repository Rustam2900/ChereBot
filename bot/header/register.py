from aiogram import Router, types
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

from bot.api_ import create_or_update_user
from bot.keyboard.k_button import contact_user, main_menu

router = Router()


class RegisterForm(StatesGroup):
    name = State()
    number = State()


@router.message(RegisterForm.name)
async def name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer(text='Nomerizni kiriting', reply_markup=contact_user())
    await state.set_state(RegisterForm.number)


@router.message(RegisterForm.number)
async def number(message: types.Message, state: FSMContext):
    contact = message.contact.phone_number
    await state.update_data(number=contact)
    print(contact)
    user_data = await state.get_data()
    await message.answer(create_or_update_user(
        telegram_id=message.from_user.id,
        name=user_data['name'],
        phone=contact,
        language=message.from_user.language_code
    ))
    await message.answer(text="Bo‘limni tanlang 〽️:", reply_markup=main_menu())
    await state.clear()
