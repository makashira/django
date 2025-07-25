# mysite/views.py

from django.shortcuts import render
import os
from telethon import TelegramClient

# Асинхронная функция для проверки подключения Telethon
async def test_telethon_connection(request):
    api_id = int(os.environ.get('TELEGRAM_API_ID', 0))
    api_hash = os.environ.get('TELEGRAM_API_HASH', '')
    session_name = 'test_session_for_web_view' # Временная сессия

    message = "Telethon not connected yet."
    try:
        # Создаем клиент
        test_client = TelegramClient(session_name, api_id, api_hash)

        # Подключаемся
        await test_client.connect()

        if test_client.is_connected():
            message = "Telethon connected successfully (but not authorized)! API ID found."
        else:
            message = "Telethon failed to connect (is API ID/Hash correct?)."
    except ValueError:
        message = "Error: TELEGRAM_API_ID or TELEGRAM_API_HASH are missing or invalid."
    except Exception as e:
        message = f"Error connecting Telethon: {e}"
    finally:
        if 'test_client' in locals() and test_client.is_connected():
            await test_client.disconnect() # Отключаемся после проверки

    # Простая функция для главной страницы
    # Если вы хотите, чтобы Telethon не запускался каждый раз, когда кто-то заходит на главную,
    # то эта логика должна быть в отдельной функции и URL.
    # Для простоты, пока оставим так.

    return render(request, 'home.html', {'telethon_status': message})

# Эта функция просто рендерит шаблон home.html без логики Telethon
def home(request):
    return render(request, 'home.html')
