from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from aiogram.filters import CommandStart
import asyncio
import os
from dotenv import load_dotenv

# Загружаем переменные окружения из .env файла
load_dotenv()

# Получаем токен бота из переменных окружения
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Проверяем наличие токена
if not BOT_TOKEN:
    raise ValueError("Переменная окружения BOT_TOKEN не установлена!")

# Инициализация бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start_handler(message: types.Message) -> None:
    """
    Хэндлер для обработки команды /start.
    Отправляет пользователю приветственное сообщение с кнопкой "Играть".
    """
    # Инлайн-кнопка с WebApp
    play_button = InlineKeyboardButton(
        text="🎮 Играть",
        web_app=WebAppInfo(url="https://hostscore.ru/")
    )
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[play_button]])

    await message.answer(
        "Добро пожаловать в игру! Нажми кнопку ниже, чтобы начать играть 🎲",
        reply_markup=keyboard
    )

async def main() -> None:
    """
    Основная функция для запуска бота.
    """
    await dp.start_polling(bot)

# Точка входа
if __name__ == "__main__":
    asyncio.run(main())
