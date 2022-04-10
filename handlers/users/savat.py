
from loader import dp, db
from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


@dp.message_handler(text="🛒 Savatcha", state="*")
async def get_cart(message: types.Message):
  products = db.get_products(tg_id=message.from_user.id)
  if products:
    msg = ""
    mahsulot = ReplyKeyboardMarkup(resize_keyboard=True)
    for product in products:
      mahsulot.add(KeyboardButton(text=f"❌ {product[1]} ❌"))
      msg += f"{product[1]} * {product[2]}\n"
    mahsulot.row("🔙 Ortga")
    await message.answer(msg, reply_markup=mahsulot)
  else:
    await message.answer("Savatchangiz bo'sh")