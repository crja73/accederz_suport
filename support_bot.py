import logging
from aiogram import types
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher.filters.state import State, StatesGroup

# Объект бота
bot = Bot(token="1937575560:AAEfovYaNsDEWo3xRocUE4uX3Y9COc9broY")
# Диспетчер для бота
dp = Dispatcher(bot)
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)

class Form(StatesGroup):
    name = State()


@dp.message_handler(commands="faq")
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Чит", "Сайт", "Блокирока"]
    keyboard.add(*buttons)

    await message.answer("С чем у вас проблема?", reply_markup=keyboard)

@dp.message_handler(Text(equals="Проблемы с работой чита"))
async def with_puree(message: types.Message):

    await message.reply("Выйди в окно")

@dp.message_handler(Text(equals="Проблема с работой сайта"))
async def without_puree(message: types.Message):

    await message.reply("Убейся")

@dp.message_handler(Text(equals="Почему меня забанили"))
async def without_puree(message: types.Message):

    await message.reply("Потому что ты гей")

#отправить вопрос админам можно с помощью запроса номера телефона отдельной командой
@dp.message_handler(commands=['leave_contacts'])
async def process_hi6_command(message: types.Message):
    markup_request = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton('Отправить свой контакт ☎️', request_contact=True))

    await message.reply("Ваш номер телефона будет передан администраторам", reply_markup=markup_request)


@dp.message_handler(content_types=['contact'])
async def contact(message):
    if message.contact is not None:
        keyboard2 = types.ReplyKeyboardRemove()
        await bot.send_message(message.chat.id, 'Вы успешно отправили свой номер', reply_markup=keyboard2)
        global phonenumber
        phonenumber= str(message.contact.phone_number)
        print(phonenumber)
        user_id = str(message.contact.user_id)

@dp.message_handler(commands=['ask_question'])
async def question(message: types.Message):
    value = message.text[13::]
    try:
        await message.bot.send_message(message.from_user.id, value)

    except:
        await message.bot.send_message(message.from_user.id, 'Некорректный формат, попробуйте "/ask_question описание проблемы" одной строчкой')

@dp.message_handler(commands=['administrator'])
async def question(message: types.Message):
    pass


if __name__ == "__main__":
    
    executor.start_polling(dp, skip_updates=True)

#https://mastergroosha.github.io/telegram-tutorial-2/buttons/
#https://ru.stackoverflow.com/questions/1332456/%d1%82%d0%b5%d0%ba%d1%81%d1%82-%d0%bd%d0%b5-%d0%b2%d0%bb%d0%b5%d0%b7%d0%b0%d0%b5%d1%82-%d0%b2-%d0%ba%d0%bd%d0%be%d0%bf%d0%ba%d0%b8-%d0%b8-%d0%b2-%d0%bc%d0%b5%d0%bd%d1%8e-%d0%ba%d0%be%d0%bc%d0%b0%d0%bd%d0%b4-python-aiogram