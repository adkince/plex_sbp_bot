import random
import string

from aiogram import Router, F
from aiogram.types import Message

from database import add_user
from keyboards import main_menu

router = Router()

def generate_ref_code():
    return ''.join(
        random.choices(
            string.ascii_uppercase + string.digits,
            k=8
        )
    )

@router.message(F.text == "/start")
async def start(message: Message):

    args = message.text.split()

    referred_by = None

    if len(args) > 1:
        referred_by = args[1]

    await add_user(
        message.from_user.id,
        generate_ref_code(),
        referred_by
    )

    await message.answer(
        "🚀 Добро пожаловать в VPN сервис",
        reply_markup=main_menu()
    )
