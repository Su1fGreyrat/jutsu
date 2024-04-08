from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton 
)

main_admin = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="💫 Рандом")
        ],
        [
            KeyboardButton(text="💊 Просмотренные"),
            KeyboardButton(text="💝 Избранное")
        ],
        [
            KeyboardButton(text="🔄 Обновить"),
            KeyboardButton(text='⚙️ Настройки')      
        ]
    ],
    resize_keyboard=True
)

main = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="💫 Рандом")
        ],
        [
            KeyboardButton(text="💊 Просмотренные"),
            KeyboardButton(text="💝 Избранное")
        ],
        [
            KeyboardButton(text='⚙️ Настройки')
        ]
    ],
    resize_keyboard=True
)