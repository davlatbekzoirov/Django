from aiogram.dispatcher.filters.state import StatesGroup, State

class Debt(StatesGroup):
    name = State()
    price = State() 
    phoneNum = State() 