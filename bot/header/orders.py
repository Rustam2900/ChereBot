import asyncio

from aiogram import Router, types, F, Bot
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from bot.conustant import OPERATOR, OPERATOR_TEXT, BACK, SETTINGS, LANG_CHANGE, ORDERS, MY_ORDERS
from bot.keyboard.k_button import main_menu, back, settings, lang_change, location_user, main_menu_ru, main_menu_en
from bot.api_ import get_product, create_order, fetch_user_orders

from datetime import datetime, timedelta

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
    location = State()


@router.message(F.text == ORDERS)
async def orders_(message: types.Message):
    await message.reply_photo(photo="https://t.me/Rustam_python_bot/72",
                              caption="O'zizga ketrakli suv haqida malumot bilishiz mumkin 😊",
                              reply_markup=keyboard)


@router.callback_query(lambda c: c.data == 'water_05')
async def water_05_(callback_query: types.CallbackQuery):
    await callback_query.message.reply_photo(photo="https://t.me/Rustam_python_bot/73")
    keyboard_water05 = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="⬅️ Orqaga", callback_data="back"),
            InlineKeyboardButton(text="Buyurtma berish", callback_data="Place_order")],

    ])
    await callback_query.message.answer(text=f"{x[0]['name']} \n\n"
                                             f"{x[0]['description']} \n\n"
                                             f"narxi: {x[0]['price']}", reply_markup=keyboard_water05)
    await callback_query.answer()


@router.callback_query(lambda c: c.data == 'water_1')
async def water_1_(callback_query: types.CallbackQuery):
    await callback_query.message.reply_photo(photo="https://t.me/Rustam_python_bot/73")
    keyboard_water1 = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="⬅️ Orqaga", callback_data="back"),
            InlineKeyboardButton(text="Buyurtma berish", callback_data="Place_order")],

    ])
    await callback_query.message.answer(text=f"{x[1]['name']} \n\n"
                                             f"{x[1]['description']} \n\n"
                                             f"narxi: {x[1]['price']}", reply_markup=keyboard_water1)
    await callback_query.answer()


@router.callback_query(lambda c: c.data == 'water_2')
async def water_2_(callback_query: types.CallbackQuery):
    await callback_query.message.reply_photo(photo="https://t.me/Rustam_python_bot/73")
    keyboard_water2 = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="⬅️ Orqaga", callback_data="back"),
            InlineKeyboardButton(text="Buyurtma berish", callback_data="Place_order")],

    ])
    await callback_query.message.answer(text=f"{x[2]['name']} \n\n"
                                             f"{x[2]['description']} \n\n"
                                             f"narxi: {x[2]['price']}", reply_markup=keyboard_water2)
    await callback_query.answer()


@router.callback_query(lambda c: c.data == 'water_5')
async def water_5_(callback_query: types.CallbackQuery):
    await callback_query.message.reply_photo(photo="https://t.me/Rustam_python_bot/73")
    keyboard_water5 = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="⬅️ Orqaga", callback_data="back"),
            InlineKeyboardButton(text="Buyurtma berish", callback_data="Place_order")],

    ])
    await callback_query.message.answer(text=f"{x[3]['name']} \n\n"
                                             f"{x[3]['description']} \n\n"
                                             f"narxi: {x[0]['price']}", reply_markup=keyboard_water5)
    await callback_query.answer()


@router.callback_query(lambda c: c.data == 'water_10')
async def water_10_(callback_query: types.CallbackQuery):
    await callback_query.message.reply_photo(photo="https://t.me/Rustam_python_bot/73")
    keyboard_water10 = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="⬅️ Orqaga", callback_data="back"),
            InlineKeyboardButton(text="Buyurtma berish", callback_data="Place_order")],

    ])
    await callback_query.message.answer(text=f"{x[4]['name']} \n\n"
                                             f"{x[4]['description']} \n\n"
                                             f"narxi: {x[4]['price']}", reply_markup=keyboard_water10)
    await callback_query.answer()


@router.callback_query(lambda c: c.data == 'water_20')
async def water_20_(callback_query: types.CallbackQuery):
    await callback_query.message.reply_photo(photo="https://t.me/Rustam_python_bot/73")
    keyboard_water20 = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="⬅️ Orqaga", callback_data="back"),
            InlineKeyboardButton(text="Buyurtma berish", callback_data="Place_order")],

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
    await message.answer(text="Location yuboring", reply_markup=location_user())
    await state.set_state(UserForm.location)


@router.message(UserForm.location)
async def process_location(message: types.Message, state: FSMContext):
    await state.update_data(location=message.text)
    user_data = await state.get_data()
    product = user_data['product']
    amount = user_data['amount']
    latitude = message.location.latitude
    longitude = message.location.longitude

    await message.reply(f"Siz {product} suvdan \n\n"
                        f"{amount} ta buyurtma qildingiz. \n\n"
                        f"Boshqa turdagi suvdan xarid qilmoqchi bo'lsangiz \n\n"
                        f"yana buyurtma berish tugmasini bosing: ")

    order_message = create_order(user_id=message.from_user.id, product_name=product, amount=amount, latitude=latitude,
                                 longitude=longitude)

    await message.answer(order_message)

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
    await message.answer(text='Выберите действие 〽️:', reply_markup=main_menu_ru())


@router.message(F.text == '🇬🇧')
async def lang_en(message: types.Message):
    await message.answer(text='Choose an action 〽️:', reply_markup=main_menu_en())


@router.callback_query(lambda c: c.data == 'back')
async def back_(callback_query: types.CallbackQuery):
    await callback_query.message.answer(text="Tanlashiz mumkin 〽️", reply_markup=keyboard)
    await callback_query.answer()


def format_time(time_string):
    time_format = "%Y-%m-%dT%H:%M:%S.%f%z"
    original_time = datetime.strptime(time_string, time_format)
    adjusted_time = original_time + timedelta(hours=11, minutes=5)
    return adjusted_time.strftime("%Y-%m-%d %H:%M")


async def send_periodic_notifications(chat_id, order_time, bot: Bot):
    start_time = datetime.strptime(order_time, "%Y-%m-%dT%H:%M:%S.%f%z")
    while True:
        await asyncio.sleep(60)  # Har 1 daqiqada qayta tekshiradi
        elapsed_time = datetime.now(start_time.tzinfo) - start_time
        elapsed_seconds = elapsed_time.total_seconds()
        if elapsed_seconds > 60:  # 60 sekunddan ko'p vaqt o'tganini tekshirish
            await bot.send_message(chat_id,
                                   text=f"Assalom, siz buyurtma berganingizga {int(elapsed_seconds // 60)} vaxt bo'ldi. Suvingiz tugamadimi? Bizning vazifamiz eslatib turish.")
            break


@router.message(F.text == MY_ORDERS)
async def my_orders(message: types.Message, bot: Bot):
    telegram_id = message.from_user.id
    orders = await fetch_user_orders(telegram_id)
    if orders and len(orders) > 0:
        order_list = "\n\n".join(
            [f"Vaxti: {format_time(order['create_at'])}, \n\n"
             f"Mahsulot: {order['product_name']}, \n\n"
             f"Miqdori: {order['amount']}" for order in orders])
        await message.answer(text=f"Sizning buyurtmalaringiz:\n\n{order_list}")
        # Har bir buyurtma uchun xabar yuborishni boshlash
        for order in orders:
            asyncio.create_task(send_periodic_notifications(message.chat.id, order['create_at'], bot))
    else:
        await message.answer(text="Siz hali hech nima buyurtma qilmagansiz.")
