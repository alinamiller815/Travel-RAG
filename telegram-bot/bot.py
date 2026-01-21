from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import httpx
import os
import asyncio
from dotenv import load_dotenv

load_dotenv()

TOKEN=os.getenv("TELEGRAM_BOT_TOKEN")
# TOKEN = '8532704905:AAFjyPCIhTn-mBLWZLGq0-sC2lCb6oz62uI'
API_URL = "http://rag-app:8001/answer"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Привет! Отправь вопрос про путешествия.")

@dp.message()
async def handle_query(message: types.Message):
    print("="*25 + message.text + "="*25 )
    async with httpx.AsyncClient(timeout=60.0) as client:  # увеличь timeout
        try:
            resp = await client.post(API_URL, json={"text": message.text}) 
            data = resp.json()
            print(data["answer"])
            await message.answer(str(data["answer"]))
        except httpx.ReadTimeout:
            print('TimeOut')
            await message.answer("API request timeout")
        except Exception as e:
            print('Exception')
            await message.answer(f"Error: {str(e)}")

import asyncio

async def main():
    print("🤖 Bot starting...")
    # Сбрасываем старые webhook и очищаем очередь апдейтов
    await bot.delete_webhook(drop_pending_updates=True)
    # Стартуем polling, пропуская старые апдейты
    await dp.start_polling(bot, skip_updates=True)

if __name__ == "__main__":
    asyncio.run(main())
