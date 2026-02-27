import os, requests
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from openai import OpenAI

TOKEN = os.getenv("TELEGRAM_TOKEN")
API = "http://backend:8000/api/cars"
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

bot = Bot(TOKEN)
dp = Dispatcher(bot)

def parse_query(text):
    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": text}],
        tools=[{
            "type": "function",
            "function": {
                "name": "filter",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "brand": {"type": "string"},
                        "color": {"type": "string"},
                        "max_price": {"type": "number"}
                    }
                }
            }
        }],
        tool_choice="auto"
    )
    call = resp.choices[0].message.tool_calls
    if not call:
        return {}
    return call[0].function.arguments

@dp.message_handler()
async def msg(m: types.Message):
    f = parse_query(m.text)
    cars = requests.get(API).json()
    res = []
    for c in cars:
        if f.get("brand") and f["brand"].lower() not in c["brand"].lower():
            continue
        if f.get("color") and f["color"].lower() not in c["color"].lower():
            continue
        if f.get("max_price") and c["price"] > f["max_price"]:
            continue
        res.append(c)
    if not res:
        await m.answer("Ничего не найдено")
        return
    text = "\n".join(f"{c['brand']} {c['model']} {c['price']}" for c in res[:10])
    await m.answer(text)

if __name__ == "__main__":
    executor.start_polling(dp)
