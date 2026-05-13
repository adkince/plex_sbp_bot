from aiogram import Router, F
from aiogram.types import CallbackQuery

from database import get_user

router = Router()

@router.callback_query(F.data == "profile")
async def profile(callback: CallbackQuery):

    user = await get_user(callback.from_user.id)

    text = f"""
👤 Ваш профиль

ID: {user[0]}
VPN: {user[3]}
Подписка до: {user[4]}
"""

    await callback.message.answer(text)
