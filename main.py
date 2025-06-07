import asyncio

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.redis import RedisStorage
from redis.asyncio import Redis

from config_data.config import load_config
from handlers import base_handlers

from logging_conf.base_conf import get_logger

logger = get_logger()


async def main():
    logger.info('Бот начал работу.')
    config = load_config()

    redis = Redis(host='localhost')
    storage = RedisStorage(redis=redis)

    bot = Bot(token=config.tg_bot.token,
              default=DefaultBotProperties(parse_mode='HTML'))
    dp = Dispatcher(storage=storage)

    dp.include_router(base_handlers.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
