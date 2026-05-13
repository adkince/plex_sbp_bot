import asyncio

from aiogram import Bot, Dispatcher

from config import BOT_TOKEN

from database import init_db

from handlers.start import router as start_router
from handlers.buy import router as buy_router
from handlers.profile import router as profile_router
from handlers.referrals import router as referrals_router
from handlers.support import router as support_router

async def main():

    await init_db()

    bot = Bot(BOT_TOKEN)

    dp = Dispatcher()

    dp.include_router(start_router)
    dp.include_router(buy_router)
    dp.include_router(profile_router)
    dp.include_router(referrals_router)
    dp.include_router(support_router)

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
