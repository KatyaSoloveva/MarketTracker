from aiogram.filters.state import State, StatesGroup


class FSMPrice(StatesGroup):
    waiting_for_price = State()
