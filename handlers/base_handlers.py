from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import CommandStart

from lexicon.lexicon import LEXICON
from keyboards.keyboards import main_keyboard
from logging_conf.base_conf import get_logger
from parsers.wb_parser import parse_wb

router = Router()

logger = get_logger()


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


@router.message(F.text.contains('wildberries.ru/catalog/'))
async def handle_wb_link(message: Message):
    user_id = message.chat.id
    product_url = message.text
    result = await parse_wb(product_url, user_id)

    if None in result.values():
        await message.answer(LEXICON['no_data'])
    else:
        await message.answer(LEXICON['data_success'].format(
            shop=result['shop'],
            title=result['title'],
            price=result['price']))
