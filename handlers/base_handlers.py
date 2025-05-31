from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, CommandStart

from lexicon.lexicon import LEXICON

router = Router()


@router.message(CommandStart())
async def start_command_react(message: Message):
    await message.answer(LEXICON['/start'].format(message.chat.first_name))


@router.message(Command(commands='help'))
async def help_command_reacr(message: Message):
    await message.answer(LEXICON['/help'])
