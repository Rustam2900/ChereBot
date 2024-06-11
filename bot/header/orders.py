from aiogram import Router, types, F
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from conustant import OPERATOR, OPERATOR_TEXT, BACK, SETTINGS, LANG_CHANGE, ORDERS
from keyboard.k_button import main_menu, contact_user, back, settings, lang_change

router = Router()


class UserForm(StatesGroup):
    name = State()
    number = State()
    location = State()

    # product_id = State()
    number05 = State()
    number1 = State()
    number2 = State()
    number5 = State()
    number10 = State()
    number20 = State()


class ProductFrom(StatesGroup):
    template = State()



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


keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🏔 0.5 L", callback_data="water_05"),
     InlineKeyboardButton(text="🏔 1 L", callback_data="water_1"),
     InlineKeyboardButton(text="🏔 2 L", callback_data="water_2")],
    [InlineKeyboardButton(text="🏔 5 L", callback_data="water_5"),
     InlineKeyboardButton(text="🏔 10 L", callback_data="water_10"),
     InlineKeyboardButton(text="🏔 20 L", callback_data="water_20")],

])


@router.message(F.text == ORDERS)
async def orders_(message: types.Message):
    await message.reply_photo(photo="https://t.me/Rustam_python_bot/72")
    await message.answer(text="O'zizga ketrakli suv haqida malumot bilishiz mumkin 😊", reply_markup=keyboard)


@router.callback_query(lambda c: c.data == 'water_05')
async def water_05_(callback_query: types.CallbackQuery):
    keyboard_water05 = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Davom ettirish ✅", callback_data="continue05"),
         InlineKeyboardButton(text="⬅️ Orqaga", callback_data="back")],
        [InlineKeyboardButton(text="Buyutma berish tugatish", callback_data="finish")]
    ])
    await callback_query.message.answer(text="0.5 L suv ... 😊\n\n"
                                             "narxi: 2500 so'm", reply_markup=keyboard_water05)
    await callback_query.answer()


@router.callback_query(lambda c: c.data == 'continue05')
async def continue_(callback_query: types.CallbackQuery, state: FSMContext):
    await state.set_state(UserForm.number05)
    await callback_query.message.answer('0.5 L suvdan nechta olishiz kiring')
    await callback_query.answer()


@router.message(UserForm.number05)
async def number_05(message: types.Message, state: FSMContext):
    await state.update_data(number=message.text)
    user_data = await state.get_data()
    await message.answer(f"Siz 0.5 L suvdan: \n\n"
                         f" {user_data['number']} ta buyurtma berdiz! \n\n"
                         f"Boshqa suvlardan ham olmoqchi bo'lsagiz davom ettirishiz mumkin", reply_markup=keyboard)
    await state.clear()


@router.callback_query(lambda c: c.data == 'water_1')
async def water_1_(callback_query: types.CallbackQuery):
    keyboard_water1 = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Davom ettirish ✅", callback_data="continue1"),
         InlineKeyboardButton(text="⬅️ Orqaga", callback_data="back")],
        [InlineKeyboardButton(text="Buyutma berish tugatish", callback_data="finish")]
    ])
    await callback_query.message.answer(text="1 L suv ... 😊\n\n"
                                             "narxi: 5000 so'm", reply_markup=keyboard_water1)
    await callback_query.answer()


@router.callback_query(lambda c: c.data == 'continue1')
async def continue_(callback_query: types.CallbackQuery, state: FSMContext):
    await state.set_state(UserForm.number1)
    await callback_query.message.answer('1 L suvdan nechta olishiz kiring')
    await callback_query.answer()


@router.message(UserForm.number1)
async def number_1(message: types.Message, state: FSMContext):
    await state.update_data(number=message.text)
    user_data = await state.get_data()
    await message.answer(f"Siz 1 L suvdan: \n\n"
                         f" {user_data['number']} ta buyurtma berdiz! \n\n"
                         f"Boshqa suvlardan ham olmoqchi bo'lsagiz davom ettirishiz mumkin", reply_markup=keyboard)
    await state.clear()


@router.callback_query(lambda c: c.data == 'water_2')
async def water_2_(callback_query: types.CallbackQuery):
    keyboard_water2 = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Davom ettirish ✅", callback_data="continue2"),
         InlineKeyboardButton(text="⬅️ Orqaga", callback_data="back")],
        [InlineKeyboardButton(text="Buyutma berish tugatish", callback_data="finish")]
    ])
    await callback_query.message.answer(text="2 L suv ... 😊\n\n"
                                             "narxi: 1200 so'm", reply_markup=keyboard_water2)
    await callback_query.answer()


@router.callback_query(lambda c: c.data == 'continue2')
async def continue_(callback_query: types.CallbackQuery, state: FSMContext):
    await state.set_state(UserForm.number2)
    await callback_query.message.answer('2 L suvdan nechta olishiz kiring')
    await callback_query.answer()


@router.message(UserForm.number2)
async def number_2(message: types.Message, state: FSMContext):
    await state.update_data(number=message.text)
    user_data = await state.get_data()
    await message.answer(f"Siz 2 L suvdan: \n\n"
                         f" {user_data['number']} ta buyurtma berdiz! \n\n"
                         f"Boshqa suvlardan ham olmoqchi bo'lsagiz davom ettirishiz mumkin", reply_markup=keyboard)
    await state.clear()


@router.callback_query(lambda c: c.data == 'water_5')
async def water_5_(callback_query: types.CallbackQuery):
    keyboard_water5 = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Davom ettirish ✅", callback_data="continue5"),
         InlineKeyboardButton(text="⬅️ Orqaga", callback_data="back")],
        [InlineKeyboardButton(text="Buyutma berish tugatish", callback_data="finish")]
    ])
    await callback_query.message.answer(text="5 L suv ... 😊\n\n"
                                             "narxi: 15000 so'm", reply_markup=keyboard_water5)
    await callback_query.answer()


@router.callback_query(lambda c: c.data == 'continue5')
async def continue_(callback_query: types.CallbackQuery, state: FSMContext):
    await state.set_state(UserForm.number5)
    await callback_query.message.answer('5 L suvdan nechta olishiz kiring')
    await callback_query.answer()


@router.message(UserForm.number5)
async def number_5(message: types.Message, state: FSMContext):
    await state.update_data(number=message.text)
    user_data = await state.get_data()
    await message.answer(f"Siz 5 L suvdan: \n\n"
                         f" {user_data['number']} ta buyurtma berdiz! \n\n"
                         f"Boshqa suvlardan ham olmoqchi bo'lsagiz davom ettirishiz mumkin", reply_markup=keyboard)
    await state.clear()


@router.callback_query(lambda c: c.data == 'water_10')
async def water_10_(callback_query: types.CallbackQuery):
    keyboard_water10 = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Davom ettirish ✅", callback_data="continue10"),
         InlineKeyboardButton(text="⬅️ Orqaga", callback_data="back")],
        [InlineKeyboardButton(text="Buyutma berish tugatish", callback_data="finish")]
    ])
    await callback_query.message.answer(text="10 L suv ... 😊\n\n"
                                             "narxi: 20000 so'm", reply_markup=keyboard_water10)
    await callback_query.answer()


@router.callback_query(lambda c: c.data == 'continue10')
async def continue_(callback_query: types.CallbackQuery, state: FSMContext):
    await state.set_state(UserForm.number10)
    await callback_query.message.answer('10 L suvdan nechta olishiz kiring')
    await callback_query.answer()


@router.message(UserForm.number10)
async def number_10(message: types.Message, state: FSMContext):
    await state.update_data(number=message.text)
    user_data = await state.get_data()
    await message.answer(f"Siz 10 L suvdan: \n\n"
                         f" {user_data['number']} ta buyurtma berdiz! \n\n"
                         f"Boshqa suvlardan ham olmoqchi bo'lsagiz davom ettirishiz mumkin", reply_markup=keyboard)
    await state.clear()


@router.callback_query(lambda c: c.data == 'water_20')
async def water_20_(callback_query: types.CallbackQuery):
    keyboard_water20 = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Davom ettirish ✅", callback_data="continue20"),
         InlineKeyboardButton(text="⬅️ Orqaga", callback_data="back")],
        [InlineKeyboardButton(text="Buyutma berish tugatish", callback_data="finish")]

    ])
    await callback_query.message.answer(text="20 L suv ... 😊 \n\n"
                                             "narxi: 25000 so'm", reply_markup=keyboard_water20)
    await callback_query.answer()


@router.callback_query(lambda c: c.data == 'continue20')
async def continue_(callback_query: types.CallbackQuery, state: FSMContext):
    await state.set_state(UserForm.number20)
    await callback_query.message.answer('20 L suvdan nechta olishiz kiring')
    await callback_query.answer()


@router.message(UserForm.number20)
async def number_20(message: types.Message, state: FSMContext):
    await state.update_data(number=message.text)
    user_data = await state.get_data()
    await message.answer(f"Siz 20 L suvdan: \n\n"
                         f" {user_data['number']} ta buyurtma berdiz! \n\n"
                         f"Boshqa suvlardan ham olmoqchi bo'lsagiz davom ettirishiz mumkin", reply_markup=keyboard)
    await state.clear()


@router.callback_query(UserForm.number20, lambda c: c.data == 'finish')
async def finish_count(callback_query: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    name = data.get('name')
    number = data.get('number')
    number05 = data.get('number05')
    number1 = data.get('number1')
    number2 = data.get('number2')
    number5 = data.get('number5')
    number10 = data.get('number10')
    number20 = data.get('number20')

    await callback_query.message.answer(
        f"Sizni malumotlariz ismiz: {name} \n\n"
        f"Raqamiz: {number} \n\n"
        f"0.5 L: {number05} ta \n\n"
        f"1 L: {number1} ta \n\n"
        f"2 L: {number2} ta \n\n"
        f"5 L: {number5} ta \n\n"
        f"10 L: {number10} ta \n\n"
        f"20 L: {number20} ta \n\n"
        f"siz bergan buyurtmalariz uchun rahmat 😊"
    )


@router.callback_query(lambda c: c.data == 'back')
async def back_(callback_query: types.CallbackQuery):
    await callback_query.message.answer(text="Tanlashiz mumkin 〽️", reply_markup=keyboard)
    await callback_query.answer()
