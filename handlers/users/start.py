import asyncpg
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.start_keyboard import menu
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from loader import dp, db, bot
from data.config import ADMINS

async def create_debts_keyboard(user_credit):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    if user_credit is not None and user_credit > 0:
        keyboard.add(KeyboardButton("Mening qarzim"))
    return keyboard


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    user_credit = await db.get_user_debt(message.from_user.id)
    debts_keyboard = await create_debts_keyboard(user_credit)

    try:
        user = await db.add_user(
            telegram_id=message.from_user.id,
            full_name=message.from_user.full_name,
            username=message.from_user.username,
        )
    except asyncpg.exceptions.UniqueViolationError:
        user = await db.select_user(telegram_id=message.from_user.id)

    await message.answer(
        f"Xush kelibsiz! Sizning qarzingiz: {user_credit}.Do'konimizdagi mahsulotlarni ko'rish uchun quyidagi Menu tugmasini bosing",
        reply_markup=menu,
    )
    await message.answer(
        "Davom etish uchun amalni tanlang:",
        reply_markup=debts_keyboard,
    )

    # ADMINGA xabar beramiz
    # count = await db.count_users()
    # msg = f"{user[1]} bazaga qo'shildi.\nBazada {count} ta foydalanuvchi bor."
    # await bot.send_message(chat_id=ADMINS[0], text=msg)
