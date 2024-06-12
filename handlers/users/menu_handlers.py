from typing import Union
from aiogram.dispatcher import FSMContext
from states.debt import Debt
from aiogram import types
from aiogram.types import CallbackQuery, Message
from keyboards.inline.menu_keyboards import *
from loader import dp, db, bot
from keyboards.default.number import *
from aiogram.types import ReplyKeyboardRemove

# Bosh menyu matni uchun handler
@dp.message_handler(text="Bosh menyu")
async def show_menu(message: types.Message):
    # Foydalanuvchilarga barcha kategoriyalarni qaytaramiz
    await list_categories(message)


# Kategoriyalarni qaytaruvchi funksiya. Callback query yoki Message qabul qilishi ham mumkin.
# **kwargs yordamida esa boshqa parametrlarni ham qabul qiladi: (category, subcategory, item_id)
async def list_categories(message: Union[CallbackQuery, Message], **kwargs):
    # Keyboardni chaqiramiz
    markup = await categories_keyboard()

    # Agar foydalanuvchidan Message kelsa Keyboardni yuboramiz
    if isinstance(message, Message):
        await message.answer("Bo'lim tanlang", reply_markup=markup)

    # Agar foydalanuvchidan Callback kelsa Callback natbibi o'zgartiramiz
    elif isinstance(message, CallbackQuery):
        call = message
        await call.message.edit_reply_markup(markup)


# Ost-kategoriyalarni qaytaruvchi funksiya
async def list_subcategories(callback: CallbackQuery, category, **kwargs):
    markup = await subcategories_keyboard(category)

    # Xabar matnini o'zgartiramiz va keyboardni yuboramiz
    await callback.message.edit_reply_markup(markup)


# Ost-kategoriyaga tegishli mahsulotlar ro'yxatini yuboruvchi funksiya
async def list_items(callback: CallbackQuery, category, subcategory, **kwargs):
    markup = await items_keyboard(category, subcategory)

    await callback.message.edit_text(text="Mahsulot tanlang", reply_markup=markup)


# Biror mahsulot uchun Xarid qilish tugmasini yuboruvchi funksiya
async def show_item(callback: CallbackQuery, category, subcategory, item_id, debt, my_debt):
    markup = item_keyboard(category, subcategory, item_id, debt, my_debt)


    # Mahsulot haqida ma'lumotni bazadan olamiz
    item = await db.get_product(item_id)

    if item["photo"]:
        text = f"<a href=\"{item['photo']}\">{item['productname']}</a>\n\n"
    else:
        text = f"{item['productname']}\n\n"
    text += f"Narxi: {item['price']}$\n{item['description']}"

    await callback.message.edit_text(text=text, reply_markup=markup)


# Yuqoridagi barcha funksiyalar uchun yagona handler
@dp.callback_query_handler(menu_cd.filter())
async def navigate(call: CallbackQuery, callback_data: dict):
    """
    :param call: Handlerga kelgan Callback query
    :param callback_data: Tugma bosilganda kelgan ma'lumotlar
    """

    # Foydalanuvchi so'ragan Level (qavat)
    current_level = callback_data.get("level")

    # Foydalanuvchi so'ragan Kategoriya
    category = callback_data.get("category")

    # Ost-kategoriya (har doim ham bo'lavermaydi)
    subcategory = callback_data.get("subcategory")

    # Mahsulot ID raqami (har doim ham bo'lavermaydi)
    item_id = int(callback_data.get("item_id"))
    debt = int(callback_data.get("debt"))
    my_debt = int(callback_data.get("my_debt"))

    # Har bir Level (qavatga) mos funksiyalarni yozib chiqamiz
    levels = {
        "0": list_categories,  # Kategoriyalarni qaytaramiz
        "1": list_subcategories,  # Ost-kategoriyalarni qaytaramiz
        "2": list_items,  # Mahsulotlarni qaytaramiz
        "3": show_item,  # Mahsulotni ko'rsatamiz
    }

    # Foydalanuvchidan kelgan Level qiymatiga mos funksiyani chaqiramiz
    current_level_function = levels[current_level]

    # Tanlangan funksiyani chaqiramiz va kerakli parametrlarni uzatamiz
    # if current_level == "2":
    #     await current_level_function(call, category, subcategory)
    # else:
    await current_level_function(call, category=category, subcategory=subcategory, item_id=item_id, debt=debt, my_debt=my_debt)


@dp.callback_query_handler(buy_item.filter(item_id="0", debt="0", my_debt="0"), state=None)
async def handle_buy_on_credit(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer("Iltimos ismingizni kiriting:")
    await Debt.name.set()

@dp.message_handler(state=Debt.name)
async def handle_buy_on_credit(message: Message, state: FSMContext):
    name = message.text
    await state.update_data({"name": name})
    await message.answer("Qarzga olmoqchi bo'lgan narxni kiriting:")
    await Debt.next()

@dp.message_handler(state=Debt.price)
async def handle_buy_on_credit(message: Message, state: FSMContext):
    price = message.text
    await state.update_data({"price": price})
    await message.answer("Telefon raqamni yuboring:",reply_markup=number)
    await Debt.next()

@dp.message_handler(content_types=types.ContentType.CONTACT, state=Debt.phoneNum)
async def handle_phone_number(message: types.Message, state: FSMContext):
    data = await state.get_data()
    name = data.get("name")
    price = data.get("price")

    # item_id = data.get("item_id")
    # item = await db.get_product(item_id)
    contact = message.contact
    phone_number = contact.phone_number
    await message.answer("Sizning raqamingiz: " + phone_number, reply_markup=ReplyKeyboardRemove())
    await state.update_data(phone_number=phone_number)

    user_id = message.from_user.id
    await bot.send_message(chat_id='-1002077533723', text=f"""
{name} {price}$-ni qarzga oldi:
Raqami- {phone_number}""")
    await db.add_debt(user_id, price, phone_number, name)
