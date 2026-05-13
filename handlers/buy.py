from aiogram import Router, F
from aiogram.types import CallbackQuery

from keyboards import tariffs_keyboard
from payments import create_invoice
from config import TARIFFS

router = Router()

@router.callback_query(F.data == "buy")
async def buy_menu(callback: CallbackQuery):

    await callback.message.edit_text(
        "💳 Выберите тариф",
        reply_markup=tariffs_keyboard()
    )

@router.callback_query(F.data.startswith("tariff_"))
async def buy_tariff(callback: CallbackQuery):

    tariff = callback.data.replace("tariff_", "")

    invoice = await create_invoice(
        TARIFFS[tariff]["price"]
    )

    pay_url = invoice["pay_url"]

    await callback.message.answer(
        f"💰 Оплатите подписку:\n{pay_url}"
    )
