import asyncio
import logging
import os
import re
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


# Главное меню
main_menu_kb = InlineKeyboardMarkup(row_width=2)
main_menu_kb.add(
    InlineKeyboardButton("📝 Регистрация", callback_data="register"),
    InlineKeyboardButton("📖 Инструкция", callback_data="instruction")
)
main_menu_kb.add(InlineKeyboardButton("🆘 HELP", url="https://t.me/your_support_bot"))
main_menu_kb.add(InlineKeyboardButton("🚀 ПОЛУЧИТЬ СИГНАЛ", web_app=types.WebAppInfo(url="https://hostscore.ru")))


# Меню после ошибки регистрации
registration_error_kb = InlineKeyboardMarkup(row_width=1)
registration_error_kb.add(
    InlineKeyboardButton("🔁 Зарегистрироваться", callback_data="register"),
    InlineKeyboardButton("🏠 Вернуться в главное меню", callback_data="main_menu")
)

# Меню инструкции
instruction_kb = InlineKeyboardMarkup()
instruction_kb.add(InlineKeyboardButton("🏠 Вернуться в главное меню", callback_data="main_menu"))


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.answer("👋 Привет! Добро пожаловать в игру. Выберите действие:", reply_markup=main_menu_kb)


@dp.callback_query_handler(lambda c: c.data == "register")
async def handle_registration(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.edit_message_text(
        text="❌ Ошибка, регистрация не пройдена.",
        chat_id=callback_query.message.chat.id,
        message_id=callback_query.message.message_id,
        reply_markup=registration_error_kb
    )


@dp.callback_query_handler(lambda c: c.data == "instruction")
async def handle_instruction(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.edit_message_text(
        text="📘 Инструкция:\n1. Нажмите \"Регистрация\"\n2. Следуйте шагам на сайте\n3. После регистрации вы получите доступ к сигналам.",
        chat_id=callback_query.message.chat.id,
        message_id=callback_query.message.message_id,
        reply_markup=instruction_kb
    )


@dp.callback_query_handler(lambda c: c.data == "main_menu")
async def back_to_main_menu(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.edit_message_text(
        text="🏠 Вернуться в главное меню:",
        chat_id=callback_query.message.chat.id,
        message_id=callback_query.message.message_id,
        reply_markup=main_menu_kb
    )

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    executor.start_polling(dp, skip_updates=True)
