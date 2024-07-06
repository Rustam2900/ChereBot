from aiogram.fsm.state import State, StatesGroup


class Registration(StatesGroup):
    user_type = State()
    phone_number = State()
    first_name = State()
    last_name = State()

    ## extra fields
