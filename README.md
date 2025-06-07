# MarketTracker
* **Проект находится в разработке и будет дополняться!** 
* **Описание**: Асинхронный бот для отслеживания цены товара на маркетплейсах. Пользователь отправляет боту ссылку на товар а также желаемую цену. И если цена опускатся до желаемой, бот сообщает об этом пользователю.
* **Стек технологий**  
  Telegram-bot-api, Aiogram, Postgresql, Sqlalchemy + asyncpg, Logging, Playwright, Redis
* **Установка**  

Клонировать репозиторий:

```
git@github.com:KatyaSoloveva/MarketTracker.git
```  

Создать и активировать виртуальное окружение:
```
python -m venv venv
```

Для Windows
```
source venv/Scripts/activate
```

Для Linux
```
source venv/bin/activate
```

Установить зависимости
```
pip install -r requirements.txt
```
В корне проекта создать .env файл по примеру из .env.example

Инициировать базу данных. Выполнить:
```
python -m database.init_db 
```
Запустить бота
```
python main.py
```

* **Created by Ekaterina Soloveva**  
https://github.com/KatyaSoloveva