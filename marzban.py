import aiohttp
from config import *

async def get_token():

    async with aiohttp.ClientSession() as session:

        data = {
            "username": MARZBAN_USERNAME,
            "password": MARZBAN_PASSWORD
        }

        async with session.post(
            f"{MARZBAN_URL}/api/admin/token",
            data=data
        ) as response:

            result = await response.json()
            return result["access_token"]

async def create_vpn_user(username, days):

    token = await get_token()

    headers = {
        "Authorization": f"Bearer {token}"
    }

    payload = {
        "username": username,
        "proxies": {
            "vless": {}
        },
        "expire": days * 86400,
        "data_limit": 0,
        "data_limit_reset_strategy": "no_reset"
    }

    async with aiohttp.ClientSession() as session:

        async with session.post(
            f"{MARZBAN_URL}/api/user",
            json=payload,
            headers=headers
        ) as response:

            return await response.json()

async def get_subscription(username):

    token = await get_token()

    headers = {
        "Authorization": f"Bearer {token}"
    }

    async with aiohttp.ClientSession() as session:

        async with session.get(
            f"{MARZBAN_URL}/api/user/{username}",
            headers=headers
        ) as response:

            return await response.json()
