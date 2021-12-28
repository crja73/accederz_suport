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
import requests
import req
import time
import json


bot = Bot(token='5098851664:AAFSsHrpWDL58oR6m--bMsOcjoD1FkZ-yak')


# Диспетчер для бота
dp = Dispatcher(bot, storage=MemoryStorage())
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)

class Form(StatesGroup):
    name = State()
    log = State()


def json_req(data_1):
    return req.main(data_1)

def log_req(data_2):
    return req.second(data_2)

@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["email", "login", "help/questions"]
    keyboard.add(*buttons)
    

    await message.answer("Выберите, по какому параметру производить поиск, затем введите данные", reply_markup=keyboard)

@dp.message_handler(Text(equals="email"))
async def with_puree(message: types.Message):

    await message.answer('Введите email интересующего вас пользователя')
    await Form.name.set()

@dp.message_handler(Text(equals="login"))
async def with_puree(message: types.Message):

    await message.answer('Введите login интересующего вас пользователя')
    await Form.log.set()


@dp.message_handler(Text(equals="help/questions"))
async def with_puree(message: types.Message):

    await message.answer('По всем вопросам пишите администратору на форуме: MERCI')
    

@dp.message_handler(state=Form.name)
async def process_name(message: types.Message, state: FSMContext):
    try:
        async with state.proxy() as data:
            data['name'] = message.text

        await Form.next()
        spis = []
        print(data['name'])
        jsonn = json.loads(json_req(data['name']))
        for i in jsonn['result']:
            print(i['line'])
            spis.append(i['line'])
       # ans = [x.get('line', None) for x in json]
        if len(spis) >= 50:
            spis = spis[:50]
        await message.answer('\n'.join(spis))
    except:
        await message.answer('Почта не найдена')
        return


@dp.message_handler(state=Form.log)
async def process_name(message: types.Message, state: FSMContext):
    
    async with state.proxy() as data:
        data['name'] = message.text

    await Form.next()
    spis = []
    print(data['name'])
    try:
        jsonn = json.loads(log_req(data['name']))
        print(jsonn)
        for i in jsonn['result']:
            print(i['line'])
            spis.append(i['line'])
           # ans = [x.get('line', None) for x in json]
        if len(spis) >= 50:
            spis = spis[:50]
        await message.answer('\n'.join(spis))
    except:
        await message.answer('Логин не найден')
    
if __name__ == "__main__":
    try:
        executor.start_polling(dp, skip_updates=True)
    except:
        time.sleep(15)


#https://ru.stackoverflow.com/questions/1365447/%d0%9a%d0%b0%d0%ba-%d0%bf%d1%80%d0%be%d0%b2%d0%b5%d1%80%d0%b8%d1%82%d1%8c-%d0%b8%d1%81%d1%82%d0%b8%d0%bd%d0%bd%d0%be%d1%81%d1%82%d1%8c-%d0%bf%d0%be%d1%87%d1%82%d1%8b-%d0%b8-%d0%bf%d0%b0%d1%80%d0%be%d0%bb%d1%8f-%d0%bf%d0%be%d0%bb%d1%8c%d0%b7%d0%be%d0%b2%d0%b0%d1%82%d0%b5%d0%bb%d1%8f-%d0%bd%d0%b0-%d1%81%d0%b0%d0%b9%d1%82%d0%b5-%d0%ba%d0%be%d1%82%d0%be%d1%80%d1%8b%d0%b9-%d0%bd%d0%b0%d0%bf%d0%b8%d1%81%d0%b0%d0%bd-%d0%bd