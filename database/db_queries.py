from sqlalchemy import select

from .init_db import async_session
from .models import User, Product
from logging_conf.base_conf import get_logger
from lexicon.lexicon import LEXICON

logger = get_logger()


async def add_user(user_id, username):
    async with async_session() as session:
        try:
            existing_user = await session.scalar(
                select(User).where(User.user_id == user_id)
            )
            if existing_user:
                logger.info(LEXICON['user_exists'].format(user_id))
                return None
            user = User(user_id=user_id, username=username)
            session.add(user)
            await session.commit()
            await session.refresh(user)
            logger.info(LEXICON['data_success_to_db_user'].format(user_id))
            return user
        except Exception as e:
            await session.rollback()
            logger.critical(f'{LEXICON['mistake_connect_to_bd']}. {e}')
            return None


async def add_product(data):
    async with async_session() as session:
        try:
            product = Product(
                shop=data['shop'],
                title=data['title'],
                price=data['price'],
                desired_price=data['desired_price'],
                product_url=data['product_url'],
                article_number=int(data['article_number']),
                user_id=data['user_id']
            )
            session.add(product)
            await session.commit()
            await session.refresh(product)
            logger.info(LEXICON['data_success_to_db_product'])
            return product
        except Exception as e:
            await session.rollback()
            logger.critical(f'{LEXICON['mistake_connect_to_bd']}. {e}')
            return None
