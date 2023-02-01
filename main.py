# 25.01.2023 - отредактировано 01.02.2023
from aiogram import types, executor
from aiogram.dispatcher.filters import Text
import logging
from config import dp
import asyncio
from module.start import start_command
from module.help import help_command
from module.remind_bot import remind_command, schedule_command, schedule


async def startup(_):
    """
        Асинкхронная функция для старта сторонних сервисов
    """
    asyncio.create_task(schedule())


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    dp.register_message_handler(start_command, commands=['start'])
    dp.register_callback_query_handler(help_command, text='help')
    dp.register_callback_query_handler(remind_command, text='remind')
    dp.register_message_handler(schedule_command, Text(startswith='напомни'))

    executor.start_polling(dp, skip_updates=True, on_startup=startup)