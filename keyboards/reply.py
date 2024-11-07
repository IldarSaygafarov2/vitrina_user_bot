from aiogram.types import WebAppInfo
from aiogram.utils.keyboard import InlineKeyboardBuilder

import settings


def start_kb():
    kb = InlineKeyboardBuilder()
    kb.button(text='Открыть сайт', web_app=WebAppInfo(url=settings.WEB_APP_URL))
    return kb.as_markup()
