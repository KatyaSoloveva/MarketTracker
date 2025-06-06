from sqlalchemy import select

from .init_db import async_session
from .models import User
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
            logger.info(LEXICON['data_success_to_db'].format(user_id))
            return user
        except Exception as e:
            await session.rollback()
            logger.critical(f'{LEXICON['mistake_connect_to_bd']}. {e}')
            return None
