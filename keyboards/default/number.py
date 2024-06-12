from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

number = ReplyKeyboardMarkup(resize_keyboard=True,
    keyboard=[
    [
        KeyboardButton(text="📲 Raqamni yuborish",request_contact=True)
    ]
])