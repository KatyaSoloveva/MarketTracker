from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import CommandStart, StateFilter
from aiogram.fsm.state import default_state

from lexicon.lexicon import LEXICON
from keyboards.keyboards import main_keyboard, exit_from_state_keyboard
from logging_conf.base_conf import get_logger
from parsers.wb_parser import parse_wb
from database.db_queries import add_user, add_product
from states.states import FSMPrice

router = Router()

logger = get_logger()


@router.message(CommandStart())
async def start_command_react(message: Message):
    await message.answer(LEXICON['/start'].format(message.chat.first_name),
                         reply_markup=main_keyboard)
    user = await add_user(message.chat.id, message.chat.username)
    if user:
        await message.answer(LEXICON['success_registration'],
                             reply_markup=main_keyboard)


@router.message(F.text == LEXICON['/help'])
async def help_command_reacr(message: Message):
    await message.answer(LEXICON['help_text'],
                         reply_markup=main_keyboard)


@router.message(F.text == LEXICON['button_search'])
async def search_response(message: Message):
    await message.answer(LEXICON['search_response'],
                         reply_markup=main_keyboard)


@router.message(F.text.contains('wildberries.ru/catalog/'))
async def handle_wb_link(message: Message, state: FSMPrice):
    user_id = message.chat.id
    product_url = message.text
    result = await parse_wb(product_url, user_id)

    if None in result.values():
        await message.answer(LEXICON['no_data'])
        return

    await state.update_data(product_data=result)
    await message.answer(LEXICON['data_success'].format(
            shop=result['shop'],
            title=result['title'],
            price=result['price']), reply_markup=exit_from_state_keyboard)
    await state.set_state(FSMPrice.waiting_for_price)


@router.message(F.text == LEXICON['exit'], ~StateFilter(default_state))
async def cancel_from_state(message: Message, state: FSMPrice):
    await message.answer(LEXICON['cancel'], reply_markup=main_keyboard)
    await state.clear()
    logger.info(LEXICON['cancel_log'])


@router.message(StateFilter(FSMPrice.waiting_for_price),
                lambda msg: msg.text.isdigit())
async def handle_price(message: Message, state: FSMPrice):
    data = await state.get_data()
    product_data = data['product_data']
    if int(message.text) >= product_data['price']:
        await message.answer(LEXICON['incorrect_price'],
                             reply_markup=exit_from_state_keyboard)
        return
    product_data['desired_price'] = int(message.text)
    product = await add_product(product_data)
    if product:
        await message.answer(LEXICON['correct_price'].format(
            shop=product_data['shop'],
            title=product_data['title'],
            price=product_data['price'],
            desired_price=product_data['desired_price'],
            url=product_data['product_url']
        ), reply_markup=main_keyboard)
        await state.clear()
        logger.info(LEXICON['cancel_log'])
    else:
        await message.answer(LEXICON['mistake_msg'],
                             reply_markup=main_keyboard)


@router.message(StateFilter(FSMPrice.waiting_for_price))
async def handle_incorrect_price(message: Message):
    await message.answer(LEXICON['not_digit_price'],
                         reply_markup=exit_from_state_keyboard)
