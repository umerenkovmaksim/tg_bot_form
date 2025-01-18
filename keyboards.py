import random

from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton

from config import CARD_CREATE_URL, REFERRAL_SHARE

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
    InlineKeyboardButton(text='Нет', callback_data='referral_program'),
)

create_card_kb = InlineKeyboardBuilder()
create_card_kb.add(
    InlineKeyboardButton(text='Оформить карту', url=CARD_CREATE_URL),
    InlineKeyboardButton(text='Далее', callback_data='referral_program'),
)

card_kb = InlineKeyboardBuilder()
card_kb.row(
    InlineKeyboardButton(text='Оформить карту', url=CARD_CREATE_URL)
)
card_kb.row(
    InlineKeyboardButton(text='Оформил', callback_data='card_message')
)
card_kb.row(
    InlineKeyboardButton(text='Получил и активировал', callback_data='card_message')
)

referral_system_kb = InlineKeyboardBuilder()
referral_system_kb.add(
    InlineKeyboardButton(text='Поделиться', switch_inline_query=REFERRAL_SHARE),
    InlineKeyboardButton(text='Не хочу делиться', callback_data='referral_done'),
    InlineKeyboardButton(text='Готово!', callback_data='referral_done'),
)

after_referral_kb = InlineKeyboardBuilder()
after_referral_kb.add(
    InlineKeyboardButton(text='Готово!', callback_data='referral_done'),
)

end_kb = InlineKeyboardBuilder()    
end_kb.add(
    InlineKeyboardButton(text='Оформить карту', url=CARD_CREATE_URL),
    InlineKeyboardButton(text='Поделиться', switch_inline_query=REFERRAL_SHARE),
)