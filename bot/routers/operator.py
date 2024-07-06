from aiogram import Router, types

from users.models import User

router = Router()


async def operator(message: types.Message, user_obj: User):
    await message.answer("Qanday muammo bor?")
