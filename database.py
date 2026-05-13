import aiosqlite

DB_NAME = "data/database.db"

async def init_db():
    async with aiosqlite.connect(DB_NAME) as db:

        await db.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            referral_code TEXT,
            referred_by INTEGER,
            vpn_username TEXT,
            expire_date TEXT
        )
        """)

        await db.commit()

async def add_user(user_id, referral_code, referred_by=None):
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute("""
        INSERT OR IGNORE INTO users
        (user_id, referral_code, referred_by)
        VALUES (?, ?, ?)
        """, (user_id, referral_code, referred_by))

        await db.commit()

async def get_user(user_id):
    async with aiosqlite.connect(DB_NAME) as db:
        cursor = await db.execute("""
        SELECT * FROM users WHERE user_id = ?
        """, (user_id,))

        return await cursor.fetchone()

async def update_subscription(user_id, vpn_username, expire_date):
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute("""
        UPDATE users
        SET vpn_username = ?, expire_date = ?
        WHERE user_id = ?
        """, (vpn_username, expire_date, user_id))

        await db.commit()
