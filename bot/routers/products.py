from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery

from bot.filters.callback_data import ProductCallbackData
from bot.keyboards.inline_markup import get_products
from products.models import Product
from users.models import User

router = Router()


@router.message(Command("make-order"))
async def products_handler(message: Message, user_obj: User):
    if user_obj:
        await message.answer("Mahsulotlar", reply_markup=await get_products())


@router.callback_query(ProductCallbackData.filter())
async def products_callback(callback: CallbackQuery, user_obj: User):
    if user_obj:
        await callback.answer(str(callback.data))
