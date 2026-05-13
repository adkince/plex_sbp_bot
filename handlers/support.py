from aiogram import Router, F
from aiogram.types import CallbackQuery

from config import SUPPORT_USERNAME

router = Router()

@router.callback_query(F.data == "support")
async def support(callback: CallbackQuery):

    await callback.message.answer(
        f"🛠 Поддержка: {SUPPORT_USERNAME}"
    )
