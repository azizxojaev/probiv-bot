from aiogram import types


async def profile_btn():
    btn = types.InlineKeyboardMarkup(row_width=1)
    btn.add(
        types.InlineKeyboardButton('💵 Пополнить', callback_data='profile:add'),
        types.InlineKeyboardButton('🛒 Мои заказы', callback_data='profile:history')
    )
    return btn

async def addbalance_btn():
    btn = types.InlineKeyboardMarkup(row_width=1)
    btn.add(
        types.InlineKeyboardButton('💸 Оплатить', callback_data='profile:pay'),
        types.InlineKeyboardButton('❌ Отменить', callback_data='profile:back')
    )
    return btn

async def products_inline():
    btn = types.InlineKeyboardMarkup(row_width=1)
    fff = 0
    btn.add(
        types.InlineKeyboardButton('Пробив по номеру', callback_data='products:phoneNumber'),
        types.InlineKeyboardButton('МВД', callback_data='products:MVD'),
        types.InlineKeyboardButton('ФНС', callback_data='products:FNS'),
        types.InlineKeyboardButton('ПФР', callback_data='products:PFR'),
        types.InlineKeyboardButton('Мини-досье (автовыдача)', callback_data='products:miniDosye'),
        types.InlineKeyboardButton('Верефикация Готовые кошельки', callback_data='products:verification'),
        types.InlineKeyboardButton('Мобильные операторы', callback_data='products:mobileOperator'),
        types.InlineKeyboardButton('Флуд и рассылка', callback_data='products:Flud'),
        types.InlineKeyboardButton('Пробив КИ', callback_data='products:KI'),
        types.InlineKeyboardButton('Сертификат Ковид', callback_data='products:Covid'),
        types.InlineKeyboardButton('✅документы', callback_data='products:documents')
    )
    return btn



async def buy_inline():
    btn = types.InlineKeyboardMarkup(row_width=1)
    btn.add(
        types.InlineKeyboardButton('💰 Заказать услугу', callback_data='buyproduct:buy'),
        types.InlineKeyboardButton('⬅️ Назад ↩️', callback_data='products:back2')
    )
    return btn


async def phoneNumber_inline():
    btn = types.InlineKeyboardMarkup(row_width=1)
    btn.add(
        types.InlineKeyboardButton('Вспышка | 5500 RUB', callback_data='buyproduct:1'),
        types.InlineKeyboardButton('Номера по Ф.И.О | 5500 RUB', callback_data='buyproduct:2'),
        types.InlineKeyboardButton('⬅️ Назад ↩️', callback_data='products:back')
    )
    return btn
async def MVD_inline():
    btn = types.InlineKeyboardMarkup(row_width=1)
    btn.add(
        types.InlineKeyboardButton('Мигрант | 3800 RUB', callback_data='buyproduct:3'),
        types.InlineKeyboardButton('Магистраль | 3000 RUB', callback_data='buyproduct:4'),
        types.InlineKeyboardButton('Роспаспорт | 4000 RUB', callback_data='buyproduct:5'),
        types.InlineKeyboardButton('ЗАГС - Москва | 9000 RUB', callback_data='buyproduct:6'),
        types.InlineKeyboardButton('ЗАГС - РФ | 9000 RUB', callback_data='buyproduct:7'),
        types.InlineKeyboardButton('ИБДР | 3800 RUB', callback_data='buyproduct:8'),
        types.InlineKeyboardButton('Поток | 9000 RUB', callback_data='buyproduct:9'),
        types.InlineKeyboardButton('Карта учета гаи | 1500 RUB', callback_data='buyproduct:10'),
        types.InlineKeyboardButton('Пробив по гаи прав | 2000 RUB', callback_data='buyproduct:11'),
        types.InlineKeyboardButton('Подбор авто | 4000 RUB', callback_data='buyproduct:12'),
        types.InlineKeyboardButton('Список пассажиров | 5000 RUB', callback_data='buyproduct:13'),
        types.InlineKeyboardButton('⬅️ Назад ↩️', callback_data='products:back')
    )
    return btn
async def FNS_inline():
    btn = types.InlineKeyboardMarkup(row_width=1)
    btn.add(
        types.InlineKeyboardButton('Полное рег. дело | 3500 RUB', callback_data='buyproduct:14'),
        types.InlineKeyboardButton('Счета физ. лиц | 2500 RUB', callback_data='buyproduct:15'),
        types.InlineKeyboardButton('Книга покупок | 3000 RUB', callback_data='buyproduct:16'),
        types.InlineKeyboardButton('Книга продаж | 3000 RUB', callback_data='buyproduct:17'),
        types.InlineKeyboardButton('2НДФЛ | 5000 RUB', callback_data='buyproduct:18'),
        types.InlineKeyboardButton('Имущество | 2500 RUB', callback_data='buyproduct:19'),
        types.InlineKeyboardButton('Движение средств ( только юр лица ) | 12000 RUB', callback_data='buyproduct:20'),
        types.InlineKeyboardButton('Выписка егрн | 3000 RUB', callback_data='buyproduct:21'),
        types.InlineKeyboardButton('⬅️ Назад ↩️', callback_data='products:back')
    )
    return btn
async def PFR_inline():
    btn = types.InlineKeyboardMarkup(row_width=1)
    btn.add(
        types.InlineKeyboardButton('Мат. капитал | 2700 RUB', callback_data='buyproduct:22'),
        types.InlineKeyboardButton('Присвоить СНИЛС | 5000 RUB', callback_data='buyproduct:23'),
        types.InlineKeyboardButton('СЗИ 6 Информация по документу СЗИ 6 | 2300 RUB', callback_data='buyproduct:24'),
        types.InlineKeyboardButton('Дата смерти | 2800 RUB', callback_data='buyproduct:25'),
        types.InlineKeyboardButton('Место работы | 2200 RUB', callback_data='buyproduct:26'),  
        types.InlineKeyboardButton('Снилс с датой | 5000 RUB', callback_data='buyproduct:27'),  
        types.InlineKeyboardButton('⬅️ Назад ↩️', callback_data='products:back')
    )
    return btn
async def miniDosye_inline():
    btn = types.InlineKeyboardMarkup(row_width=1)
    btn.add(
        types.InlineKeyboardButton('Поиск физ.лица | 950 RUB', callback_data='buyproduct:28'),
        types.InlineKeyboardButton('Поиск по телефону | 1100 RUB', callback_data='buyproduct:29'),
        types.InlineKeyboardButton('⬅️ Назад ↩️', callback_data='products:back')
    )
    return btn
async def verification_inline():
    btn = types.InlineKeyboardMarkup(row_width=1)
    btn.add(
        types.InlineKeyboardButton('Qiwi Профессиональный | Готовый | 4500 RUB', callback_data='buyproduct:30'),
        types.InlineKeyboardButton('Yoomoney Идентифицированный | Готовый | 3000 RUB', callback_data='buyproduct:31'),
        types.InlineKeyboardButton('Идентификация QIWI | 2800 RUB', callback_data='buyproduct:32'),
        types.InlineKeyboardButton('⬅️ Назад ↩️', callback_data='products:back')
    )
    return btn
async def mobileOperator_inline():
    btn = types.InlineKeyboardMarkup(row_width=1)
    btn.add(
        types.InlineKeyboardButton('Tele 2 | Детализация | 38000 RUB', callback_data='buyproduct:33'),
        types.InlineKeyboardButton('Tele 2 | Пробив/поиск | 3000 RUB', callback_data='buyproduct:34'),
        types.InlineKeyboardButton('Tele 2 | Восстановление SIM | 45000 RUB', callback_data='buyproduct:35'),
        types.InlineKeyboardButton('МЕГАФОН | Пробив/поиск | 2000 RUB', callback_data='buyproduct:36'),
        types.InlineKeyboardButton('Билайн | Восстановление SIM карты | 30000 RUB', callback_data='buyproduct:37'),
        types.InlineKeyboardButton('МТС | Детализация | 20500 RUB', callback_data='buyproduct:38'),
        types.InlineKeyboardButton('Билайн | Пробив/поиск | 2000 RUB', callback_data='buyproduct:39'),
        types.InlineKeyboardButton('Билайн | Детализация | 16000 RUB', callback_data='buyproduct:40'),
        types.InlineKeyboardButton('МТС | Пробив/поиск | 2000 RUB', callback_data='buyproduct:41'),
        types.InlineKeyboardButton('МТС | Восстановление SIM | 35000 RUB', callback_data='buyproduct:42'),
        types.InlineKeyboardButton('⬅️ Назад ↩️', callback_data='products:back')
    )
    return btn
async def Flud_inline():
    btn = types.InlineKeyboardMarkup(row_width=1)
    btn.add(
        types.InlineKeyboardButton('Флуд - Телеграм | 1000 сообщений | 2500 RUB', callback_data='buyproduct:43'),
        types.InlineKeyboardButton('Флуд - Чата телеграмм | 1000 сообщений | 3500 RUB', callback_data='buyproduct:44'),
        types.InlineKeyboardButton('Флуд - SMS | 1 час | 1000 RUB', callback_data='buyproduct:45'),
        types.InlineKeyboardButton('Рассылка по WhatsApp | 100 сообщений | 1000 RUB', callback_data='buyproduct:46'),
        types.InlineKeyboardButton('Флуд - Почты | 1 час | 1500 RUB', callback_data='buyproduct:47'),
        types.InlineKeyboardButton('Флуд - Звонкам РФ | 1 час | 950 RUB', callback_data='buyproduct:48'),
        types.InlineKeyboardButton('⬅️ Назад ↩️', callback_data='products:back')
    )
    return btn
async def KI_inline():
    btn = types.InlineKeyboardMarkup(row_width=1)
    btn.add(
        types.InlineKeyboardButton('Центральный каталог кредитных историй | 1000 RUB', callback_data='buyproduct:49'),
        types.InlineKeyboardButton('Кредитный рейтинг | Расширенный | 800 RUB', callback_data='buyproduct:50'),
        types.InlineKeyboardButton('ЭКВИФАКС | 4600 RUB', callback_data='buyproduct:51'),
        types.InlineKeyboardButton('Русский Стандарт | 2900 RUB', callback_data='buyproduct:52'),
        types.InlineKeyboardButton('НБКИ на юр.лицо | 4300 RUB', callback_data='buyproduct:53'),
        types.InlineKeyboardButton('НБКИ расширенная + ЦККИ | 4200 RUB', callback_data='buyproduct:54'),
        types.InlineKeyboardButton('Кредитный рейтинг обычный | 2600 RUB', callback_data='buyproduct:55'),
        types.InlineKeyboardButton('НБКИ с банками | Отрисовка | 6500 RUB', callback_data='buyproduct:56'),
        types.InlineKeyboardButton('НБКИ без банков | 5500 RUB', callback_data='buyproduct:57'),
        types.InlineKeyboardButton('НБКИ с банками | 5800 RUB', callback_data='buyproduct:58'),
        types.InlineKeyboardButton('⬅️ Назад ↩️', callback_data='products:back')
    )
    return btn
async def Covid_inline():
    btn = types.InlineKeyboardMarkup(row_width=1)
    btn.add(
        types.InlineKeyboardButton('Сертификат Codif-19 | 8500 RUB', callback_data='buyproduct:59'),
        types.InlineKeyboardButton('⬅️ Назад ↩️', callback_data='products:back')
    )
    return btn
async def documents_inline():
    btn = types.InlineKeyboardMarkup(row_width=1)
    btn.add(
        types.InlineKeyboardButton('Права | 15000 RUB', callback_data='buyproduct:60'),
        types.InlineKeyboardButton('Мед справка 003 | 4000 RUB', callback_data='buyproduct:61'),
        types.InlineKeyboardButton('Осаго без выплат | 1900 RUB', callback_data='buyproduct:62'),
        types.InlineKeyboardButton('Диплом аттестат | 23000 RUB', callback_data='buyproduct:63'),
        types.InlineKeyboardButton('Техосмотр легковой | 2600 RUB', callback_data='buyproduct:64'),
        types.InlineKeyboardButton('Техосмотр грузовой авто | 3500 RUB', callback_data='buyproduct:65'),
        types.InlineKeyboardButton('Стс птс | 25000 RUB', callback_data='buyproduct:66'),
        types.InlineKeyboardButton('⬅️ Назад ↩️', callback_data='products:back')
    )
    return btn