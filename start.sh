#!/bin/bash

echo "🚀 Активируем виртуальное окружение"
source venv/bin/activate

echo "🌐 Запускаем WebApp"
uvicorn webapp.main:app --host 0.0.0.0 --port 8000 --reload &

sleep 2

echo "🤖 Запускаем Telegram-бота"
python bot/main.py
