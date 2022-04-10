from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from data.info import brand_names

menu = ReplyKeyboardMarkup(
  keyboard=[
    [KeyboardButton(text="🔙 Ortga")],
   ],
  resize_keyboard=True
)
