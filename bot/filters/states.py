from aiogram.fsm.state import State, StatesGroup


class Registration(StatesGroup):
    user_type = State()
    full_name = State()
    phone_number = State()

    ## extra fields
