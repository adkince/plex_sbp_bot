import aiohttp
from config import CRYPTOBOT_TOKEN

async def create_invoice(amount):

    headers = {
        "Crypto-Pay-API-Token": CRYPTOBOT_TOKEN
    }

    payload = {
        "asset": "USDT",
        "amount": amount
    }

    async with aiohttp.ClientSession() as session:

        async with session.post(
            "https://pay.crypt.bot/api/createInvoice",
            json=payload,
            headers=headers
        ) as response:

            data = await response.json()

            return data["result"]
