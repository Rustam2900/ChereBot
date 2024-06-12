from aiogram import Router, types
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

from bot.api import create_user
from bot.keyboard.k_button import contact_user, location_user

router = Router()


class RegisterForm(StatesGroup):
    name = State()
    number = State()
    location = State()


@router.message(RegisterForm.name)
async def name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)

    await message.answer(text='nomerizni kiriting', reply_markup=contact_user())
    await state.set_state(RegisterForm.number)


@router.message(RegisterForm.number)
async def number(message: types.Message, state: FSMContext):
    contact = message.contact.phone_number
    await state.update_data(number=contact)
    print(contact)

    await message.answer(text='lokatsiyani yuboring', reply_markup=location_user())
    await state.set_state(RegisterForm.location)


@router.message(RegisterForm.location)
async def location(message: types.Message, state: FSMContext):
    print("**************88")
    print("latitude", message.location.latitude)
    print("longitude", message.location.longitude)
    user_data = await state.get_data()
    response_message = create_user(
        telegram_id=message.from_user.id,
        name=message.from_user.first_name,
        username=message.from_user.full_name,
        phone=user_data['number'],
        latitude=message.location.latitude,
        longitude=message.location.longitude,
        language=message.from_user.language_code
    )
    await message.answer(response_message)
    await state.clear()
