import logging
from aiogram import types
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage

bot = Bot(token='5013808863:AAEPHiqEJ1inYO8BOTu2hyy5f9hZliqog54')

dp = Dispatcher(bot, storage=MemoryStorage())
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)

class Form(StatesGroup):
    name = State()
    phone = State()
    card = State()


def search_email(email):
    try:
        print(email)
        f = open('bost.txt', encoding='utf-8')
        
        for i in f:
            if email in i:
                print(i)
                return i
        return 'Почта не найдена'
    except:
        return 'Почта не найдена'

def search_card(card):
    try:
        print(card)
        f = open('bost.txt', encoding='utf-8')
        
        for i in f:
            if card in i:
                print(i)
                return i
        return 'Карта не найдена'
    except:
        return 'Карта не найдена'

def search_phone(phone):
    try:
        print(phone)
        f = open('bost.txt', encoding='utf-8')
        
        for i in f:
            #print(i)
            if phone in i:
                print(i)
                return i
        return 'Телефон не найден'
    except:
        return 'Телефон не найден'
    

@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Банковская карта", "email", "Номер телефона"]
    keyboard.add(*buttons)
    await message.answer("Выберите, по какому параметру производить поиск, затем введите данные", reply_markup=keyboard)




@dp.message_handler(Text(equals="email"))
async def with_puree(message: types.Message):

    await message.answer('Введите email интересующего вас пользователя')
    await Form.name.set()

@dp.message_handler(Text(equals="Банковская карта"))
async def with_puree(message: types.Message):

    await message.answer('Введите номер банковской карты интересующего вас пользователя')
    await Form.card.set()

@dp.message_handler(Text(equals="Номер телефона"))
async def with_puree(message: types.Message):

    await message.answer('Введите номер телнфона интересующего вас пользователя')
    await Form.phone.set()




@dp.message_handler(state=Form.name)
async def process_name(message: types.Message, state: FSMContext):
    
    async with state.proxy() as data:
        data['name'] = message.text

    await Form.next()
        
    await message.answer(search_email(data['name']))


@dp.message_handler(state=Form.card)
async def process_name(message: types.Message, state: FSMContext):
    
    async with state.proxy() as data:
        data['name'] = message.text

    await Form.next()
        
    await message.answer(search_card(data['name']))

@dp.message_handler(state=Form.phone)
async def process_name(message: types.Message, state: FSMContext):
    
    async with state.proxy() as data:
        data['name'] = message.text

    await Form.next()
        
    await message.answer(search_phone(data['name']))
    
    


if __name__ == "__main__":
    try:
        executor.start_polling(dp, skip_updates=True)
    except:
        print('Что-то пошло не так, обратитесь к администратору https://accederz.tech/members/merci.6/')
