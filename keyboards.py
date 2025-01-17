from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton

start_kb = InlineKeyboardBuilder()
start_kb.add(
    InlineKeyboardButton(text='Начать', callback_data='start_form'),
    InlineKeyboardButton(text='Подробнее о вакансии', callback_data='vacancy_info'),
)

info_kb = InlineKeyboardBuilder()
info_kb.add(
    InlineKeyboardButton(text='Начать', callback_data='start_form'),
)

work_type_kb = InlineKeyboardBuilder()
work_type_kb.add(
    InlineKeyboardButton(text='Основная работа', callback_data='main_work'),
    InlineKeyboardButton(text='Подработка', callback_data='sub_work'),
)

confirm_work_kb = InlineKeyboardBuilder()
confirm_work_kb.add(
    InlineKeyboardButton(text='Да', callback_data='yes'),
    InlineKeyboardButton(text='Нет', callback_data='no'),
)

create_card_kb = InlineKeyboardBuilder()
create_card_kb.add(
    InlineKeyboardButton(text='Оформить карту', callback_data='referral_program')
)

card_kb = InlineKeyboardBuilder()
card_kb.add(
    InlineKeyboardButton(text='Оформить карту', url='https://google.com'),
    InlineKeyboardButton(text='Оформил', callback_data='card_message'),
    InlineKeyboardButton(text='Получил и активировал', callback_data='card_message'),
)

referral_system_kb = InlineKeyboardBuilder()
referral_system_kb.add(
    InlineKeyboardButton(text='Поделиться', callback_data='referral_share'),
    InlineKeyboardButton(text='Не хочу делиться', callback_data='referral_done'),
    InlineKeyboardButton(text='Готово!', callback_data='referral_done'),
)

after_referral_kb = InlineKeyboardBuilder()
after_referral_kb.add(
    InlineKeyboardButton(text='Готово!', callback_data='referral_done'),
)