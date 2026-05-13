from aiogram import Router, F
from aiogram.types import CallbackQuery

from database import get_user

router = Router()

@router.callback_query(F.data == "referrals")
async def referrals(callback: CallbackQuery):

    user = await get_user(callback.from_user.id)

    ref_code = user[1]

    link = f"https://t.me/YOUR_BOT?start={ref_code}"

    await callback.message.answer(
        f"👥 Ваша реферальная ссылка:\n\n{link}"
    )
