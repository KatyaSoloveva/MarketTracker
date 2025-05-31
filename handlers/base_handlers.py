from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, CommandStart


router = Router()


@router.message(CommandStart())
async def start_command_react(message: Message):
    await message.answer(text='insert later')


@router.message(Command(commands='help'))
async def help_command_reacr(message: Message):
    await message.answer(text="insert later 2")
