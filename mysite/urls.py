# mysite/urls.py

from django.contrib import admin
from django.urls import path
# Импортируем наши новые представления из views.py
from . import views # <--- Эту строку нужно добавить или убедиться, что она есть

urlpatterns = [
    path('admin/', admin.site.urls),
    # Добавляем маршрут для главной страницы
    path('', views.home, name='home'), # <--- Эту строку нужно добавить
    # Добавляем маршрут для тестовой страницы Telethon
    path('test-telethon/', views.test_telethon_connection, name='test_telethon'), # <--- Эту строку нужно добавить
]
