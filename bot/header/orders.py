from aiogram import Router, types, F
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from bot.conustant import OPERATOR, OPERATOR_TEXT, BACK, SETTINGS, LANG_CHANGE, ORDERS, LOCATION_CHANGE
from bot.keyboard.k_button import main_menu, back, settings, lang_change, location_user
from bot.api import get_product, create_order

router = Router()

keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🏔 0.5 L", callback_data="water_05"),
     InlineKeyboardButton(text="🏔 1 L", callback_data="water_1"),
     InlineKeyboardButton(text="🏔 2 L", callback_data="water_2")],
    [InlineKeyboardButton(text="🏔 5 L", callback_data="water_5"),
     InlineKeyboardButton(text="🏔 10 L", callback_data="water_10"),
     InlineKeyboardButton(text="🏔 20 L", callback_data="water_20")],
    [InlineKeyboardButton(text="Buyurtma berish", callback_data="Place_order")]

])

x = get_product()


class UserForm(StatesGroup):
    product = State()
    amount = State()


@router.message(F.text == ORDERS)
async def orders_(message: types.Message):
    await message.reply_photo(photo="https://t.me/Rustam_python_bot/72")
    await message.answer(text="O'zizga ketrakli suv haqida malumot bilishiz mumkin 😊", reply_markup=keyboard)


@router.callback_query(lambda c: c.data == 'water_05')
async def water_05_(callback_query: types.CallbackQuery):
    keyboard_water05 = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="⬅️ Orqaga", callback_data="back")],

    ])
    await callback_query.message.answer(text=f"{x[0]['name']} \n\n"
                                             f"{x[0]['description']} \n\n"
                                             f"narxi: {x[0]['price']}", reply_markup=keyboard_water05)
    await callback_query.answer()


@router.callback_query(lambda c: c.data == 'water_1')
async def water_1_(callback_query: types.CallbackQuery):
    keyboard_water1 = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="⬅️ Orqaga", callback_data="back")],

    ])
    await callback_query.message.answer(text=f"{x[1]['name']} \n\n"
                                             f"{x[1]['description']} \n\n"
                                             f"narxi: {x[1]['price']}", reply_markup=keyboard_water1)
    await callback_query.answer()


@router.callback_query(lambda c: c.data == 'water_2')
async def water_2_(callback_query: types.CallbackQuery):
    keyboard_water2 = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="⬅️ Orqaga", callback_data="back")],

    ])
    await callback_query.message.answer(text=f"{x[2]['name']} \n\n"
                                             f"{x[2]['description']} \n\n"
                                             f"narxi: {x[2]['price']}", reply_markup=keyboard_water2)
    await callback_query.answer()


@router.callback_query(lambda c: c.data == 'water_5')
async def water_5_(callback_query: types.CallbackQuery):
    keyboard_water5 = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="⬅️ Orqaga", callback_data="back")],

    ])
    await callback_query.message.answer(text=f"{x[3]['name']} \n\n"
                                             f"{x[3]['description']} \n\n"
                                             f"narxi: {x[0]['price']}", reply_markup=keyboard_water5)
    await callback_query.answer()


@router.callback_query(lambda c: c.data == 'water_10')
async def water_10_(callback_query: types.CallbackQuery):
    keyboard_water10 = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="⬅️ Orqaga", callback_data="back")],

    ])
    await callback_query.message.answer(text=f"{x[4]['name']} \n\n"
                                             f"{x[4]['description']} \n\n"
                                             f"narxi: {x[4]['price']}", reply_markup=keyboard_water10)
    await callback_query.answer()


@router.callback_query(lambda c: c.data == 'water_20')
async def water_20_(callback_query: types.CallbackQuery):
    keyboard_water20 = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="⬅️ Orqaga", callback_data="back")],

    ])
    await callback_query.message.answer(text=f"{x[5]['name']} \n\n"
                                             f"{x[5]['description']} \n\n"
                                             f"narxi: {x[5]['price']}", reply_markup=keyboard_water20)
    await callback_query.answer()


@router.callback_query(lambda c: c.data == 'Place_order')
async def place_order_(callback_query: types.CallbackQuery, state: types.CallbackQuery):
    await state.set_state(UserForm.product)
    await callback_query.message.answer('Iltimos, suv turini kiriting: \n\n'
                                        'Namuna: 5 L ')
    await callback_query.answer()


@router.message(UserForm.product)
async def process_product(message: types.Message, state: FSMContext):
    await state.update_data(product=message.text)
    await message.answer(text="Iltimos, sonnini  kiriting: \n\n"
                              "Namuna: 10 ta ")
    await state.set_state(UserForm.amount)


@router.message(UserForm.amount)
async def process_amount(message: types.Message, state: FSMContext):
    await state.update_data(amount=message.text)
    user_data = await state.get_data()
    product = user_data['product']
    amount = user_data['amount']
    print(product)
    print(amount)
    await message.reply(f"Siz {product} suvdan \n\n"
                        f"{amount} ta buyurtma qildingiz. \n\n"
                        f"Boshqa turdagi suvdan qarid qilmoqchi bo'lsangiz \n\n"
                        f"yana buyurtma berish tugmasini bosing: ")
    await message.answer(
        create_order(product_name=product, amount=amount))
    await state.clear()


@router.message(F.text == BACK)
async def back_(message: types.Message):
    await message.answer(text='Bo‘limni tanlang 〽️:', reply_markup=main_menu())


@router.message(F.text == OPERATOR)
async def operator_help(message: types.Message):
    await message.answer(text=OPERATOR_TEXT, reply_markup=back())


@router.message(F.text == SETTINGS)
async def settings_help(message: types.Message):
    await message.answer(text='Harakatni tanlang 〽️:', reply_markup=settings())


@router.message(F.text == LANG_CHANGE)
async def lang_chan(message: types.Message):
    await message.answer(text='Tilni tanlang 〽️:', reply_markup=lang_change())


@router.message(F.text == '🇺🇿')
async def lang_uz(message: types.Message):
    await message.answer(text='Harakatni tanlang 〽️:', reply_markup=main_menu())


@router.message(F.text == '🇷🇺')
async def lang_ru(message: types.Message):
    await message.answer(text='Выберите действие 〽️:', reply_markup=None)


@router.message(F.text == '🇬🇧')
async def lang_en(message: types.Message):
    await message.answer(text='Choose an action 〽️:', reply_markup=None)


@router.callback_query(lambda c: c.data == 'back')
async def back_(callback_query: types.CallbackQuery):
    await callback_query.message.answer(text="Tanlashiz mumkin 〽️", reply_markup=keyboard)
    await callback_query.answer()


@router.message(F.text == LOCATION_CHANGE)
async def location_change(message: types.Message):
    await message.answer('Location yuboring', reply_markup=location_user())
