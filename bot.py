import logging
import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from config import *
from keyboards import *

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher()


class UserData(StatesGroup):
    name_and_surname = State()
    contact = State()
    age = State()
    work_type = State()
    city = State()

async def delayed_message(chat_id: int):
    await asyncio.sleep(5)
    await bot.send_message(
        chat_id,
        text=(
            'Благодарим вас за ожидание!\n\n'
            'Поздравляем, вы успешно прошли предварительный отбор!\n\n'
            'Ваши индивидуальные условия:\n'
            '- работа онлайн через нашу CRM-систему, ответы на сообщения пользователей (письменно) по заданному скрипту;\n'
            '- график работы вы составляете индивидуально, от 20 до 48 часов в неделю;\n'
            '- оплата еженедельно, ставка на старте работы 320 рублей/час;\n\n'
            'Для продолжения подтвердите, актуальна ли для вас данная вакансия и сможете ли вы приступить к работе в ближайшие 30 дней.'
        ),
        reply_markup=confirm_work_kb.as_markup(),
    )

@dp.message(Command("start"))
async def welcome(message: types.Message):
    await message.answer(
        HELLO_MESSAGE,
        reply_markup=start_kb.as_markup(),
    )


@dp.callback_query(F.data == 'vacancy_info')
async def vacancy_info(callback_query: types.CallbackQuery):
    await callback_query.message.edit_text(
        text=WORK_INFO
    )
    await callback_query.message.edit_reply_markup(
        reply_markup=info_kb.as_markup()
    )
    
@dp.callback_query(F.data == 'start_form')
async def start_form(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.message.edit_text(NAME_AND_SURNAME)
    await state.set_state(UserData.name_and_surname)

@dp.message(UserData.name_and_surname)
async def set_name(message: types.Message, state: FSMContext):
    await state.update_data(name_and_surname=message.text)
    await message.answer(CONTACT)
    await state.set_state(UserData.contact)

@dp.message(UserData.contact)
async def set_contact(message: types.Message, state: FSMContext):
    await state.update_data(contact=message.text)
    await message.answer(AGE)
    await state.set_state(UserData.age)

@dp.message(UserData.age)
async def set_age(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)
    await message.answer(WORK_TYPE, reply_markup=work_type_kb.as_markup())

@dp.callback_query(F.data == 'main_work')
async def set_work_type(callback: types.CallbackQuery, state: FSMContext):
    await state.update_data(work_type='Основная работа')
    await bot.send_message(callback.from_user.id, CITY)
    await state.set_state(UserData.city)

@dp.callback_query(F.data == 'sub_work')
async def set_work_type(callback: types.CallbackQuery, state: FSMContext):
    await state.update_data(work_type='Подработка')
    await bot.send_message(callback.from_user.id, CITY)
    await state.set_state(UserData.city)

@dp.message(UserData.city)
async def set_city(message: types.Message, state: FSMContext):
    await state.update_data(city=message.text)
    user_data = await state.get_data()
    await message.answer(
        text=END_FORM
    )
    chat = await bot.get_chat(ADMIN_CHANNEL_ID)
    await bot.send_message(
        chat_id=chat.id,
        text=(
            f"Новая анкета кандидата:\n\n"
            f"- Имя и фамилия: {user_data['name_and_surname']}\n"
            f"- Контактные данные: {user_data['contact']}\n"
            f"- Возраст: {user_data['age']}\n"
            f"- Основная работа/Подработка: {user_data['work_type']}\n"
            f"- Город: {user_data['city']}"
        )
    )
    await state.clear()
    asyncio.create_task(delayed_message(chat_id=message.from_user.id))
    
@dp.callback_query(F.data == 'referral_program')
async def referral_program(callback: types.CallbackQuery):
    await callback.message.edit_text(
        text=REFERRAL_NOTIFICATION,
        reply_markup=referral_system_kb.as_markup(),
    )
@dp.callback_query(F.data == 'yes')
async def confirm_work(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.edit_text(
        text=CONFIRM_WORK,
        reply_markup=create_card_kb.as_markup(),
    )

@dp.callback_query(F.data == 'no')
async def confirm_work(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.edit_text(
        text=CANCEL_WORK,
    )
    await state.clear()

@dp.callback_query(F.data == 'referral_share')
async def referral_share(callback: types.CallbackQuery):
    await callback.message.edit_text(
        text=REFERRAL_SHARE,
        reply_markup=after_referral_kb.as_markup(),
    )
    
@dp.callback_query(F.data == 'referral_done')
async def referral_done(callback: types.CallbackQuery):
    await callback.message.edit_text(
        text=END_MESSAGE,
        reply_markup=card_kb.as_markup(),
    )
    
@dp.callback_query(F.data == 'card_message')
async def card_message(callback: types.CallbackQuery):
    await callback.message.edit_text(
        text=CARD_END_MESSAGE
    )

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

