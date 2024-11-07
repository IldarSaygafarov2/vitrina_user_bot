from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from keyboards.reply import start_kb

router = Router()


@router.message(CommandStart())
async def user_start(message: Message):
    await message.answer('Добро пожаловать в бот "Витрины недвижимости"', reply_markup=start_kb())