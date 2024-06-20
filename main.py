import asyncio
from configparser import ConfigParser
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
import logging

from telegram.handlers import router


# Запуск бота
async def main():
    logging.basicConfig(level=logging.INFO)
    config = ConfigParser()
    config.read('telegram/config.ini')
    data = config["data"]
    api_key = str(data['API_KEY'])
    bot = Bot(token=api_key)
    dp = Dispatcher()
    dp.include_routers(router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, skip_updates=True)


if __name__ == "__main__":
    asyncio.run(main())
