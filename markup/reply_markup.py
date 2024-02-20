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
            KeyboardButton(text="🔄 Обновить")
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
        ]
    ],
    resize_keyboard=True
)