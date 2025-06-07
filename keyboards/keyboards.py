from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from lexicon.lexicon import LEXICON

button_help = KeyboardButton(text=LEXICON['/help'])
button_search = KeyboardButton(text=LEXICON['button_search'])
button_shopping_cart = KeyboardButton(text=LEXICON['button_shopping_cart'])
button_delete_from_shopping_cart = KeyboardButton(
    text=LEXICON['button_delete_from_shopping_cart']
)

main_keyboard = ReplyKeyboardMarkup(
    keyboard=[[button_help, button_search],
              [button_shopping_cart, button_delete_from_shopping_cart]],
    resize_keyboard=True
)

exit = KeyboardButton(text=LEXICON['exit'])

exit_from_state_keyboard = ReplyKeyboardMarkup(keyboard=[exit])
