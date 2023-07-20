import logging
import datetime
import pytz

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import *
from btn import start_btn, remove_btn
from inline import *


logging.basicConfig(level=logging.INFO)

BOT_TOKEN = 'YOUR TOKEN'

bot = Bot(token=BOT_TOKEN, parse_mode='Markdown')
dp = Dispatcher(bot=bot)


is_input_sum = False


@dp.message_handler(commands=['start'])
async def start_bot(message: types.Message):
    is_input_sum = False
    btn = await start_btn()
    await message.answer('🔸 *Бот готов к использованию.*\n🔸 Если не появились вспомогательные кнопки\n▶️ Введите /start', reply_markup=btn)



@dp.message_handler()
async def message_handler(message: types.Message):
    global is_input_sum
    text = message.text
    tz = pytz.timezone("Asia/Tashkent")
    now_date = datetime.datetime.now(tz)
    date_text = now_date.strftime('%d/%m/%Y %H/%M/%S')
    if text == '🎁 Купить':
        is_input_sum = False
        products = await products_inline()
        await message.answer('🎁 Выберите нужную вам услугу:', reply_markup=products)
    elif text == '📱 Профиль':
        is_input_sum = False
        profile_inline_btn = await profile_btn()
        await message.answer(f'📱 Ваш профиль:\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n🔑 Мой ID: `{message.from_user.id}`\n👤 Логин: *@{message.from_user.username}*\n🕜 Регистрация: `{date_text}`\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n💳 Баланс: `0.0` р\n👥Вы пригласили: `0` человек\n🔗Ссылка для приглашения: https://t.me/Probiv2bot?start={message.from_user.id}', reply_markup=profile_inline_btn)
    elif text == 'ℹ️ FAQ':
        is_input_sum = False
        await message.answer('Данный бот, поможет вам найти кого угодно.\nНаши плюсы:\n➕Удобное использование\n➕Автоматическая оплата\n➕Вашим заказом занимаются профессионалы\n➕Прямая связь с саппортом\n➕Выдача заказа в сроки\n\nПомощь/предложить свои услуги - @kaban\_service')
    elif text == '📕 Поддержка':
        is_input_sum = False
        await message.answer('📕 Писать сюда ➡️ @kaban\_service')
    elif text == '▶️ Информация':
        is_input_sum = False
        await message.answer('Работаем быстро и качественно ✅\n\nПомощь/предложить свои услуги - @kaban\_service')
    elif text == '❌ Отменить':
        btn = await start_btn()
        await message.answer('🔸 *Бот готов к использованию.*\n🔸 Если не появились вспомогательные кнопки\n▶️ Введите /start', reply_markup=btn)
        is_input_sum = False
    if is_input_sum == True:
        if text.count('0') > 0 or text.count('1') > 0 or text.count('2') > 0 or text.count('3') > 0 or text.count('4') > 0 or text.count('5') > 0 or text.count('6') > 0 or text.count('7') > 0 or text.count('8') > 0 or text.count('9') > 0:
            sum = int(text)
            if sum >= 500:
                pay_btn = await addbalance_btn()
                await message.answer(f'✅ Ссылка для оплаты создан _(у вас 15 минут чтобы перевести {text}руб.)_', reply_markup=pay_btn)
            else:
                await message.answer('Минимальная сумма пополнение *500*')
        else:
            await message.answer('Некорректный ввод! попробуйте ещё раз.')


@dp.callback_query_handler(text_contains='products:')
async def products_choice(call: types.CallbackQuery):
    choice = call.data.split(':')[1]
    if choice == 'back':
        product_inline = await products_inline()
        await call.message.edit_text('🎁 Выберите нужную вам услугу:', reply_markup=product_inline)
    elif choice == 'phoneNumber':
        product_inline = await phoneNumber_inline()
        await call.message.edit_text('🎁 Выберите нужную вам услугу из *Номера по Ф.И.О*', reply_markup=product_inline)
    elif choice == 'MVD':
        product_inline = await MVD_inline()
        await call.message.edit_text('🎁 Выберите нужную вам услугу из *Список пассажиров*', reply_markup=product_inline)
    elif choice == 'FNS':
        product_inline = await FNS_inline()
        await call.message.edit_text('🎁 Выберите нужную вам услугу из *Выписка егрн*', reply_markup=product_inline)
    elif choice == 'PFR':
        product_inline = await PFR_inline()
        await call.message.edit_text('🎁 Выберите нужную вам услугу из *Снилс с датой*', reply_markup=product_inline)
    elif choice == 'miniDosye':
        product_inline = await miniDosye_inline()
        await call.message.edit_text('🎁 Выберите нужную вам услугу из *Поиск по телефону*', reply_markup=product_inline)
    elif choice == 'verification':
        product_inline = await verification_inline()
        await call.message.edit_text('🎁 Выберите нужную вам услугу из *Идентификация QIWI*', reply_markup=product_inline)
    elif choice == 'mobileOperator':
        product_inline = await mobileOperator_inline()
        await call.message.edit_text('🎁 Выберите нужную вам услугу из *MTC | Восстановление SIM*', reply_markup=product_inline)
    elif choice == 'Flud':
        product_inline = await Flud_inline()
        await call.message.edit_text('🎁 Выберите нужную вам услугу из *Флуд - Звонками РФ | 1 час*', reply_markup=product_inline)
    elif choice == 'KI':
        product_inline = await KI_inline()
        await call.message.edit_text('🎁 Выберите нужную вам услугу из *НБКИ с банками*', reply_markup=product_inline)
    elif choice == 'Covid':
        product_inline = await Covid_inline()
        await call.message.edit_text('🎁 Выберите нужную вам услугу из *Сертификат Codif-19*', reply_markup=product_inline)
    elif choice == 'documents':
        product_inline = await documents_inline()
        await call.message.edit_text('🎁 Выберите нужную вам услугу из *Стс птс*', reply_markup=product_inline)
    elif choice == 'back2':
        if category == 'Пробив по номеру':
            product_inline = await phoneNumber_inline()
            await call.message.edit_text('🎁 Выберите нужную вам услугу из *Номера по Ф.И.О*', reply_markup=product_inline)
        elif category == 'МВД':
            product_inline = await MVD_inline()
            await call.message.edit_text('🎁 Выберите нужную вам услугу из *Список пассажиров*', reply_markup=product_inline)
        elif category == 'ФНС':
            product_inline = await FNS_inline()
            await call.message.edit_text('🎁 Выберите нужную вам услугу из *Выписка егрн*', reply_markup=product_inline)
        elif category == 'ПФР':
            product_inline = await PFR_inline()
            await call.message.edit_text('🎁 Выберите нужную вам услугу из *Снилс с датой*', reply_markup=product_inline)
        elif category == 'Мини-досье (автовыдача)':
            product_inline = await miniDosye_inline()
            await call.message.edit_text('🎁 Выберите нужную вам услугу из *Поиск по телефону*', reply_markup=product_inline)
        elif category == 'Верефикация Готовые кошельки':
            product_inline = await verification_inline()
            await call.message.edit_text('🎁 Выберите нужную вам услугу из *Идентификация QIWI*', reply_markup=product_inline)
        elif category == 'Мобильные операторы':
            product_inline = await mobileOperator_inline()
            await call.message.edit_text('🎁 Выберите нужную вам услугу из *MTC | Восстановление SIM*', reply_markup=product_inline)
        elif category == 'Флуд и рассылка':
            product_inline = await Flud_inline()
            await call.message.edit_text('🎁 Выберите нужную вам услугу из *Флуд - Звонками РФ | 1 час*', reply_markup=product_inline)
        elif category == 'Пробив КИ':
            product_inline = await KI_inline()
            await call.message.edit_text('🎁 Выберите нужную вам услугу из *НБКИ с банками*', reply_markup=product_inline)
        elif category == 'Сертификат Ковид':
            product_inline = await Covid_inline()
            await call.message.edit_text('🎁 Выберите нужную вам услугу из Сертификат Codif-19', reply_markup=product_inline)
        elif category == '✅документы':
            product_inline = await documents_inline()
            await call.message.edit_text('🎁 Выберите нужную вам услугу из *Стс птс*', reply_markup=product_inline)


category = None
name = None
price = None
about = None

@dp.callback_query_handler(text_contains='buyproduct:')
async def buy_choice(call: types.CallbackQuery):
    global category
    global name
    global price
    global about
    choice = call.data.split(':')[1]
    if True:
        if choice == '1':
            category = 'Пробив по номеру'
            name = 'Вспышка'
            price = '5500руб'
            about = 'Узнать местоположение абонента в данный момент'
        elif choice == '2':
            category = 'Пробив по номеру'
            name = 'Номера по Ф.И.О'
            price = '5500руб'
            about = 'Поиск по операторам по Фио'
        elif choice == '3':
            category = 'МВД'
            name = 'Мигрант'
            price = '3800руб'
            about = 'Паспорт по имени фамилии и дате рождения для иностранных граждан'
        elif choice == '4':
            category = 'МВД'
            name = 'Магистраль'
            price = '3000руб'
            about = 'Самолёт и поезд все паспорта и билеты'
        elif choice == '5':
            category = 'МВД'
            name = 'Роспаспорт'
            price = '4000руб'
            about = 'Паспорт прописка данные'
        elif choice == '6':
            category = 'МВД'
            name = 'ЗАГС - Москва'
            price = '9000руб'
            about = 'Поиск информации по ЗАГСу'
        elif choice == '7':
            category = 'МВД'
            name = 'ЗАГС - РФ'
            price = '9000руб'
            about = 'Поиск информации по ЗАГСу'
        elif choice == '8':
            category = 'МВД'
            name = 'ИБДР'
            price = '3800руб'
            about = 'Судимости'
        elif choice == '9':
            category = 'МВД'
            name = 'Поток'
            price = '9000руб'
            about = 'Поток поиск авто по камерам'
        elif choice == '10':
            category = 'МВД'
            name = 'Карта учета гаи'
            price = '1500руб'
            about = 'Данные авто собственника карта гаи'
        elif choice == '11':
            category = 'МВД'
            name = 'Пробив по гаи прав'
            price = '2000руб'
            about = 'Поиск фото гаи по базе пробив водительских прав'
        elif choice == '12':
            category = 'МВД'
            name = 'Подбор авто'
            price = '4000руб'
            about = 'Подбор авто по вашим данным'
        elif choice == '13':
            category = 'МВД'
            name = 'Список пассажиров'
            price = '5000руб'
            about = 'Список рейса пассажиров'
        elif choice == '14':
            category = 'ФНС'
            name = 'Полное Рег. дело'
            price = '3500руб'
            about = '-'
        elif choice == '15':
            category = 'ФНС'
            name = 'Счета физ. лиц'
            price = '2500руб'
            about = '-'
        elif choice == '16':
            category = 'ФНС'
            name = 'Книга покупок'
            price = '3000руб'
            about = '1 книга покупок за квартал'
        elif choice == '17':
            category = 'ФНС'
            name = 'Книга продаж'
            price = '3000руб'
            about = '1 книга продаж за квартал'
        elif choice == '18':
            category = 'ФНС'
            name = '2НДФЛ'
            price = '5000руб'
            about = '-'
        elif choice == '19':
            category = 'ФНС'
            name = 'Имущество'
            price = '2500руб'
            about = 'Информации о имуществе человека'
        elif choice == '20':
            category = 'ФНС'
            name = 'Движение средств ( только юр лица)'
            price = '12000руб'
            about = 'Движение средст счета за год'
        elif choice == '21':
            category = 'ФНС'
            name = 'Выписка егрн'
            price = '3000руб'
            about = 'Выписка'
        elif choice == '22':
            category = 'ПФР'
            name = 'Мат. капитал'
            price = '2700руб'
            about = 'Прочерк'
        elif choice == '23':
            category = 'ПФР'
            name = 'Присвоить СНИЛС'
            price = '5000руб'
            about = 'Присвоение Снилс'
        elif choice == '24':
            category = 'ПФР'
            name = 'СЗИ 6 Информация по документу СЗИ 6'
            price = '2300руб'
            about = 'Прочерк'
        elif choice == '25':
            category = 'ПФР'
            name = 'Дата смерти'
            price = '2800руб'
            about = 'ФИО'
        elif choice == '26':
            category = 'ПФР'
            name = 'Место работы'
            price = '2200руб'
            about = 'Место работы'
        elif choice == '27':
            category = 'ПФР'
            name = 'Снилс с датой'
            price = '3000руб'
            about = 'Прочерк'
        elif choice == '28':
            category = 'Мини-досье (автовыдача)'
            name = 'Поиск физ.лица'
            price = '950руб'
            about = 'Поиск физ лица по Ф.И.О и дате рождения, по имеющимся базам'
        elif choice == '29':
            category = 'Мини-досье (автовыдача)'
            name = 'Поиск по телефону'
            price = '1100руб'
            about = 'Вся возможна информация по номеру телефона'
        elif choice == '30':
            category = 'Верефикация Готовые кошельки'
            name = 'Qiwi Профессиональный | Готовый'
            price = '4500руб'
            about = 'QIWI кошелек со статусом "Профессиональный"'
        elif choice == '31':
            category = 'Верефикация Готовые кошельки'
            name = 'Yoomoney Идентифицированный | Готовый'
            price = '3000руб'
            about = 'Готовый кошелек Yoomoney'
        elif choice == '32':
            category = 'Верефикация Готовые кошельки'
            name = 'Идентификация QIWI'
            price = '2800руб'
            about = 'Идентифицируем QIWI кошелек на ваши паспортные данные'
        elif choice == '33':
            category = 'Мобильные операторы'
            name = 'TELE 2 | Детализация'
            price = '38000руб'
            about = 'За месяц'
        elif choice == '34':
            category = 'Мобильные операторы'
            name = 'TELE 2 | Пробив/поиск'
            price = '3000руб'
            about = 'Поиск'
        elif choice == '35':
            category = 'Мобильные операторы'
            name = 'TELE 2 | Восстановление SIM'
            price = '45000руб'
            about = 'Пробив поиск'
        elif choice == '36':
            category = 'Мобильные операторы'
            name = 'МЕГАФОН | Пробив/поиск'
            price = '2000руб'
            about = 'Поиск'
        elif choice == '37':
            category = 'Мобильные операторы'
            name = 'Билайн | Восстановление SIM карты'
            price = '30000руб'
            about = 'Восстановление'
        elif choice == '38':
            category = 'Мобильные операторы'
            name = 'MTC | Детализация'
            price = '20500руб'
            about = 'Деталь за месяц'
        elif choice == '39':
            category = 'Мобильные операторы'
            name = 'Билайн | Пробив/поиск'
            price = '2000руб'
            about = 'Пробив поиск'
        elif choice == '40':
            category = 'Мобильные операторы'
            name = 'Билайн | Детализация'
            price = '16000руб'
            about = 'За месяц'
        elif choice == '41':
            category = 'Мобильные операторы'
            name = 'MTC | Пробив/поиск'
            price = '2000руб'
            about = 'МТС'
        elif choice == '42':
            category = 'Мобильные операторы'
            name = 'MTC | Восстановление SIM'
            price = '35000руб'
            about = 'Восстановление'
        elif choice == '43':
            category = 'Флуд и рассылка'
            name = 'Флуд - Телеграм | 1000 сообщений'
            price = '2500руб'
            about = '1000 сообщений в личные сообщения телеграм'
        elif choice == '44':
            category = 'Флуд и рассылка'
            name = 'Флуд - Чата телеграмм | 1000 сообщений'
            price = '3500руб'
            about = '1000 сообщений в чат телеграм'
        elif choice == '45':
            category = 'Флуд и рассылка'
            name = 'Флуд - SMS | 1 час'
            price = '1000руб'
            about = 'Час беспрерывного флуда смс на телефон'
        elif choice == '46':
            category = 'Флуд и рассылка'
            name = 'Рассылка по WhatsApp | 100 сообщений'
            price = '1000руб'
            about = 'Рассылка по WhatsApp номерам'
        elif choice == '47':
            category = 'Флуд и рассылка'
            name = 'Флуд - Почты | 1 час'
            price = '1500руб'
            about = 'Час беспрерывного письмами звонками на почту'
        elif choice == '48':
            category = 'Флуд и рассылка'
            name = 'Флуд - Звонками РФ | 1 час'
            price = '950руб'
            about = 'Час беспрерывного флуда звонками на телефон ТОЛЬКО РФ НОМЕРА'
        elif choice == '49':
            category = 'Пробив КИ'
            name = 'Центральный каталог кредитных историй'
            price = '1000руб'
            about = 'Центральный каталог кредитных историй по паспорту/скану'
        elif choice == '50':
            category = 'Пробив КИ'
            name = 'Кредитный рейтинг | Расширенный'
            price = '800руб'
            about = 'Кредитный рейтинг расширенный Требуемые данные: Фамилия др + номер серия паспорта'
        elif choice == '51':
            category = 'Пробив КИ'
            name = 'ЭКВИФАКС'
            price = '4600руб'
            about = 'ЭКВИФАКС по фото/скану паспорта'
        elif choice == '52':
            category = 'Пробив КИ'
            name = 'Русский Стандарт'
            price = '2900руб'
            about = 'Русский Стандарт по фото/скану паспорта'
        elif choice == '53':
            category = 'Пробив КИ'
            name = 'НБКИ на юр. лицо'
            price = '4300руб'
            about = 'НБКИ на юр. лицо по фото/скану паспортa'
        elif choice == '54':
            category = 'Пробив КИ'
            name = 'НБКИ расширенная + ЦККИ'
            price = '4200руб'
            about = 'НБКИ расширенная + ЦККИ по фото/скану паспорта'
        elif choice == '55':
            category = 'Пробив КИ'
            name = 'Кредитный рейтинг обычный'
            price = '2600руб'
            about = 'Кредитный рейтинг обычный Требуемые данные: Фамилия др + номер серия паспорта'
        elif choice == '56':
            category = 'Пробив КИ'
            name = 'НБКИ с банками | Отрисовка'
            price = '6500руб'
            about = 'НБКИ с банками с отрисовкой скана по паспортным данным'
        elif choice == '57':
            category = 'Пробив КИ'
            name = 'НБКИ без банков'
            price = '5500руб'
            about = 'НБКИ без банков по фото/скану паспорта'
        elif choice == '58':
            category = 'Пробив КИ'
            name = 'НБКИ с банками'
            price = '5800руб'
            about = 'НБКИ с банками по фото/скану паспорта'
        elif choice == '59':
            category = 'Сертификат Ковид'
            name = 'Сертификат Codif-19'
            price = '8500руб'
            about = 'Сертификат Covid'
        elif choice == '60':
            category = '✅документы'
            name = 'Права'
            price = '15000руб'
            about = 'Права зеркало дубликат'
        elif choice == '61':
            category = '✅документы'
            name = 'Мед справка 003'
            price = '4000руб'
            about = 'Справка на замену прав'
        elif choice == '62':
            category = '✅документы'
            name = 'Осаго без выплат'
            price = '1900руб'
            about = 'Для учета и передвижения на год'
        elif choice == '63':
            category = '✅документы'
            name = 'Диплом аттестат'
            price = '23000руб'
            about = 'Дипломы аттестаты корочки'
        elif choice == '64':
            category = '✅документы'
            name = 'Техосмотр легковой'
            price = '2600руб'
            about = 'На легковой авто а так же мото'
        elif choice == '65':
            category = '✅документы'
            name = 'Техосмотр грузовой авто'
            price = '3500руб'
            about = 'Груз тех осмотр'
        elif choice == '66':
            category = '✅документы'
            name = 'Стс птс'
            price = '25000руб'
            about = 'Стс птс'
        elif choice == 'buy':
            await call.answer('У вас не хватает денег :(', show_alert=True)

    buy_product_inline = await buy_inline()
    await call.message.edit_text(f'🎁 Заказ услуги:\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n📦 Категория: `{category}`\n🏷 Название: `{name}`\n💰 Стоимость: `{price}`\n📜 Описание: {about}', reply_markup=buy_product_inline)


@dp.callback_query_handler(text_contains='profile:')
async def profile_choice(call: types.CallbackQuery):
    global is_input_sum
    choice = call.data.split(':')[1]
    if choice == 'history':
        await call.answer('У вас нет истории покупок :(', show_alert=True)
    elif choice == 'add':
        input_sum_btn = await remove_btn()
        await call.message.answer('✍️ Введите сумму _(минимум 500 руб.):_ ', reply_markup=input_sum_btn)
        is_input_sum = True
    elif choice == 'back':
        await call.answer('❌ Пополнение отменено!', show_alert=True)
        await call.message.delete()
        btn = await start_btn()
        await call.message.answer('🔸 *Бот готов к использованию.*\n🔸 Если не появились вспомогательные кнопки\n▶️ Введите /start', reply_markup=btn)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
