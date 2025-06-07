import asyncio

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from .models import Base
from config_data.config import load_config

config = load_config()


engine = create_async_engine(config.db.db, echo=True)
async_session = async_sessionmaker(engine, expire_on_commit=False)


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

if __name__ == "__main__":
    asyncio.run(init_db())
