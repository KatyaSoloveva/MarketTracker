from dataclasses import dataclass
from environs import Env


@dataclass
class TgBot:
    token: str


@dataclass
class DataBase:
    db: str


@dataclass
class Config:
    tg_bot: TgBot
    db: DataBase


def load_config(path: str | None = None):
    env = Env()
    env.read_env(path)
    return Config(tg_bot=TgBot(token=env('BOT_TOKEN')),
                  db=DataBase(db=env('DATABASE')))
