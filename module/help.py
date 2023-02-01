from aiogram import types
from module.constans import HELP_TEXT


async def help_command(cb: types.CallbackQuery):
    """
        Фунция для просмотра списка доступных команд
    """

    await cb.bot.send_message(
        chat_id=cb.from_user.id,
        text=HELP_TEXT
    )