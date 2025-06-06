import asyncio
import logging
import logging.handlers

from aiogram import Bot, Dispatcher

from config_data.config import Config, load_config
from handlers import base_handlers

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
stream_handler = logging.StreamHandler()
file_handler = logging.handlers.RotatingFileHandler('logs.log',
                                                    maxBytes=50000000,
                                                    backupCount=5)
logger.addHandler(stream_handler)
logger.addHandler(file_handler)
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
stream_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)


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
