from aiogram import types
from config import bot
import asyncio
import aioschedule


async def remind_command(cb: types.CallbackQuery):
    '''
        Функция оповещения о напоминалке
    '''
    await cb.bot.send_message(chat_id=cb.from_user.id,
                              text=f"Напишите, что вам нужно напомнить;"
                                   f"Пример: напомни встать через 5 минут!")


async def schedule_command(message: types.Message):
    '''
        Функция для добавления напоминалки
    '''
    global chat_id
    global rem
    rem = message.text[8:]
    chat_id = message.from_user.id
    await message.answer(text='okay')


async def notice():
    '''
        Функция делает напоминание
    '''
    await bot.send_message(
        chat_id=chat_id,
        text=rem
    )


async def schedule():
    """
        Функция самой напоминалки
    """
    aioschedule.every(10).seconds.do(notice)

    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)