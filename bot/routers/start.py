import logging

import phonenumbers
from aiogram import Router, types, flags
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from django.conf import settings
from django.utils import translation

from bot import constants
from bot.filters.callback_data import LanguageCallbackData
from bot.filters.enums import UserType
from bot.filters.states import Registration
from bot.keyboards import inline_markup, keyboard_markup
from users.models import User, Profile

router = Router()


@router.message(CommandStart())
@flags.allow_any
@flags.rate_limit(key="start_handler")
async def start_handler(message: types.Message, user_obj: User):
    if user_obj:
        await message.answer(text=str(constants.CHOOSE_SECTION), reply_markup=keyboard_markup.main_menu())
    else:
        await message.answer(text=str(constants.CHOOSE_LANGUAGE), reply_markup=inline_markup.choose_language())


@router.callback_query(LanguageCallbackData.filter())
@flags.allow_any
@flags.rate_limit(key="language_callback")
async def language_callback(query: types.CallbackQuery, user_obj: User,
                            state: FSMContext, callback_data: LanguageCallbackData):
    await query.answer()
    if user_obj:
        user_obj.language = callback_data.language
        await user_obj.asave()
        await query.message.edit_reply_markup()
        translation.activate(callback_data.language)
        return await start_handler(query.message, user_obj)
    translation.activate(callback_data.language)
    await query.message.edit_reply_markup()
    await state.update_data(language=str(callback_data.language))

    await state.set_state(Registration.user_type)
    await query.message.answer(str(constants.ASK_WHO_IS_THIS_PERSON),
                               reply_markup=keyboard_markup.choose_who_is_this_person())


@router.message(Registration.user_type)
@flags.allow_any
@flags.rate_limit(key="registration_user_type")
async def user_type_callback(message: types.Message, state: FSMContext):
    if message.text == str(constants.INDIVIDUAL):
        await state.update_data(user_type=UserType.INDIVIDUAL)
        await state.set_state(Registration.full_name)
        await message.answer("Please enter your full name.", reply_markup=types.ReplyKeyboardRemove())
    elif message.text == str(constants.LEGAL_ENTITY):
        await state.update_data(user_type=UserType.LEGAL_ENTITY)
        await state.set_state(Registration.full_name)
        await message.answer("Please enter your full name.", reply_markup=types.ReplyKeyboardRemove())


@router.message(Registration.full_name)
@flags.allow_any
@flags.rate_limit(key="registration_full_name")
async def full_name_callback(message: types.Message, state: FSMContext):
    text = message.text  # TODO validate input string later
    await state.update_data(full_name=text)
    await message.answer(str(constants.REQUEST_CONTACT_TEXT), reply_markup=keyboard_markup.request_contact())
    await state.set_state(Registration.phone_number)


@router.message(Registration.phone_number)
@flags.allow_any
@flags.rate_limit(key="registration_phone_number")
async def phone_number_callback(message: types.Message, state: FSMContext):
    try:
        phone = phonenumbers.parse(message.contact.phone_number, settings.PHONENUMBER_DEFAULT_REGION)
        if phone:
            telegram_id = message.from_user.id
            data = await state.get_data()
            full_name = data["full_name"]
            user_type = data["user_type"]
            language = data["language"]
            phone = "+" + str(phone.country_code) + str(phone.national_number)
            user, created = await User.objects.aupdate_or_create(
                phone=phone,
                first_name=full_name,
                telegram_id=telegram_id,
                language=language,
            )
            if created:
                if user_type == UserType.INDIVIDUAL:
                    await Profile.objects.aupdate_or_create(
                        user=user,
                        profile_type=Profile.LEGAL_ENTITY,
                    )
                elif user_type == UserType.LEGAL_ENTITY:
                    await Profile.objects.aupdate_or_create(
                        user=user,
                        profile_type=Profile.INDIVIDUAL,
                    )
            await message.answer("Successfully registered.", reply_markup=types.ReplyKeyboardRemove())
            await state.clear()
            await start_handler(message, user)
        else:
            await message.answer(str("Please send phone number with send contact button."),
                                 reply_markup=keyboard_markup.request_contact())
    except Exception as e:  # noqa
        logging.error(e)
        await message.answer(str(constants.COMMON_ERROR_TEXT), reply_markup=types.ReplyKeyboardRemove())
