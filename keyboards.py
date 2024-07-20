from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardMarkup
)

keyboard_start = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='🎲 Сыграть'), KeyboardButton(text='👤 Профиль')],
    ],
    resize_keyboard=True, # Автоматически настраивает размер кнопок
    one_time_keyboard=False, # Не скрывает клавиатуру после 1 использования
    input_field_placeholder='Выберите действие из меню :', # Текст в поле ввода
)