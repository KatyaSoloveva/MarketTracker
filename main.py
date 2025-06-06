import asyncio

from aiogram import Bot, Dispatcher

from config_data.config import Config, load_config
from handlers import base_handlers

from logging_conf.base_conf import get_logger

logger = get_logger()


async def main():
    logger.info('Бот начал работу.')
    config: Config = load_config()

    bot = Bot(token=config.tg_bot.token)
    dp = Dispatcher()

    dp.include_router(base_handlers.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
