from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import requests
from loader import dp
from aiogram import types
from states.main import Product
from aiogram.dispatcher import FSMContext
from keyboards.default.brands import menu, brendlar

@dp.message_handler(text="🔙 Ortga")
async def go_back(message: types.Message):
  await message.answer("Asosiy sahifa", reply_markup=menu)


@dp.message_handler(text="🔙 Ortga", state=Product.brand)
async def go_back(message: types.Message, state: FSMContext):
  await message.answer("Asosiy sahifa", reply_markup=menu)
  await state.finish()

@dp.message_handler(text="🔙 Ortga", state=Product.model)
async def go_back(message: types.Message, state: FSMContext):
  await message.answer("Telefon Brandlaridan birini tanlang 🔽", reply_markup=brendlar)
  await Product.brand.set()

@dp.message_handler(text="🔙 Ortga", state=Product.amount)
async def go_back(message: types.Message, state: FSMContext):
  data = await state.get_data()
  url = data.get('url_model')
  response2 = requests.get(url).json()
  data2 = response2['data']['phones']
  models = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
  for model in data2:
    models.insert(KeyboardButton(text=model["phone_name"]))
  models.row("🔙 Ortga")
  await message.answer("Kerakli modelni tanlang 🔽", reply_markup=models)
  await Product.model.set()

