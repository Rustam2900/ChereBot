from aiogram import Router, types, F
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from conustant import OPERATOR, OPERATOR_TEXT, BACK, SETTINGS, LANG_CHANGE, ORDERS
from keyboard.k_button import main_menu, contact_user, back, settings, lang_change


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

    # user_data = await state.get_data()

    # keyboard = InlineKeyboardMarkup(inline_keyboard=[
    #     [InlineKeyboardButton(text="Davom ettirish ✅", callback_data="continue")],
    #     [InlineKeyboardButton(text="Bekor qilish ❌", callback_data="cancel")]
    # ])
    # text_data = f"Rahmat, ismiz: {user_data['name']}! \n\n "
    # f"Sizning nomeringiz: {user_data['number']} \n\n"
    # f"agar malumotlariz to'g'ri bo'lsa davom ettiring"

    await message.answer(text='lokatsiyani yuboring')
    await state.set_state(RegisterForm.location)
    # await state.clear()


# @router.callback_query(lambda c: c.data == 'continue')
# async def process_continue(callback_query: types.CallbackQuery):
#     await callback_query.message.answer(text="Bo‘limni tanlang 〽️:", reply_markup=main_menu())
#     await callback_query.answer()
# @router.callback_query(lambda c: c.data == 'cancel')
# async def process_cancel(callback_query: types.CallbackQuery):
#     await callback_query.message.reply("Bekor qilindi. /start buyrug'ini qayta kiriting.")
#     await callback_query.answer()


@router.message(RegisterForm.location)
async def location(message: types.Message, state: FSMContext):
    print("**************88")
    print(message.location)
    # await state.update_data(number=contact)
    await message.answer('shit bruh')
    state.clear()
