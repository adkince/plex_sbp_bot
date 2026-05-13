from aiogram.utils.keyboard import InlineKeyboardBuilder

def main_menu():

    kb = InlineKeyboardBuilder()

    kb.button(text="💳 Купить VPN", callback_data="buy")
    kb.button(text="👤 Профиль", callback_data="profile")
    kb.button(text="👥 Рефералы", callback_data="referrals")
    kb.button(text="🛠 Поддержка", callback_data="support")

    kb.adjust(2)

    return kb.as_markup()

def tariffs_keyboard():

    kb = InlineKeyboardBuilder()

    kb.button(text="1 месяц - $5", callback_data="tariff_1_month")
    kb.button(text="3 месяца - $12", callback_data="tariff_3_month")
    kb.button(text="12 месяцев - $40", callback_data="tariff_12_month")

    kb.adjust(1)

    return kb.as_markup()
