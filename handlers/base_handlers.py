from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import CommandStart

from lexicon.lexicon import LEXICON
from keyboards.keyboards import main_keyboard

router = Router()


@router.message(CommandStart())
async def start_command_react(message: Message):
    await message.answer(LEXICON['/start'].format(message.chat.first_name))


@router.message(F.text == LEXICON['/help'])
async def help_command_reacr(message: Message):
    await message.answer(LEXICON['help_text'],
                         reply_markup=main_keyboard)


@router.message(F.text == LEXICON['button_search'])
async def search_response(message: Message):
    await message.answer(LEXICON['search_response'],
                         reply_markup=main_keyboard)
