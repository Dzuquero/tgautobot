
import os
import re
import requests
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

TOKEN = os.getenv("TELEGRAM_TOKEN")
API_URL = "http://backend:8000/api/cars"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

def parse_query(text: str):
    brand = None
    color = None
    max_price = None

    for b in ["bmw", "audi"]:
        if b in text.lower():
            brand = b

    for c in ["red", "black"]:
        if c in text.lower():
            color = c

    m = re.search(r"(\d+)", text)
    if m:
        max_price = int(m.group(1))

    return brand, color, max_price

@dp.message_handler()
async def handler(message: types.Message):
    brand, color, max_price = parse_query(message.text)

    params = {}
    if brand: params["brand"] = brand
    if color: params["color"] = color
    if max_price: params["max_price"] = max_price

    r = requests.get(API_URL, params=params, headers={"Authorization": "Bearer test"})
    cars = r.json() if r.status_code == 200 else []

    if not cars:
        await message.answer("Ничего не найдено")
        return

    text = "\n".join(f"{c['brand']} {c['model']} {c['year']} — {c['price']}₽" for c in cars)
    await message.answer(text)

if __name__ == "__main__":
    executor.start_polling(dp)
