from aiogram import types


async def start_btn():
    btn = types.ReplyKeyboardRemove()
    btn = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn.row('🎁 Купить', '📱 Профиль', 'ℹ️ FAQ')
    btn.row('📕 Поддержка', '▶️ Информация')
    return btn

async def remove_btn():
    btn = types.ReplyKeyboardRemove()
    btn = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn.row('❌ Отменить')
    return btn