#https://lolz.guru/threads/2671457/


import logging
from aiogram import types
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher.filters.state import State, StatesGroup
import autoreg
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage

bot = Bot(token='5093831982:AAGyFc1tJZintwjhcW2eRiLOMfBZXZkMJ40')


# Диспетчер для бота
dp = Dispatcher(bot, storage=MemoryStorage())
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)

class Form(StatesGroup):
    logging2 = State()


@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ['Авторизация', 'Вопросы и предложения']
    keyboard.add(*buttons)

    await message.answer("Для продолжения работы необходимо авторизоваться", reply_markup=keyboard)

@dp.message_handler(Text(equals="Авторизация"))
async def with_puree(message: types.Message):
    await message.answer("Введите логин и пароль в формате login:password")
   
    await Form.logging2.set()
    

@dp.message_handler(Text(equals="Вопросы и предложения"))
async def with_puree(message: types.Message):
    await message.answer("При некорректной работе бота, или с предложениями по усовершенствованию пишите админу на нашем форуме https://accederz.tech/members/merci.6/")
   
 



@dp.message_handler(state=Form.logging2)
async def process_name(message: types.Message, state: FSMContext):
    try:
        
        
        async with state.proxy() as data:
            
            data['name'] = message.text

        await Form.next()
        spis  = data['name'].split(':')
        await message.answer('Производим поиск по базе...')
        
        if autoreg.main(spis[0], spis[1]) == True:
            await message.answer('Добро пожаловать, ' spis[0])
            await message.answer('<a href="t.me/Osint_accederz_bot">Osint бот</a>',parse_mode="HTML")
            await message.answer('<a href="t.me/Bruteforce_accederz_bot">Bruteforce бот</a>',parse_mode="HTML")
            await message.answer('<a href="t.me/accederz_discord_nitro_bot">Discord_nitro бот</a>',parse_mode="HTML")

        else:
            await message.answer('Пользователь не найден или неверно введен пароль')
    except:
        await message.answer('Некорректный формат данных, нажмите кнопку login, и введите данные в формате login:password')

   

if __name__ == "__main__":
    
    executor.start_polling(dp, skip_updates=True)