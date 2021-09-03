import telebot
from telebot import types

bot = telebot.TeleBot('1937575560:AAEfovYaNsDEWo3xRocUE4uX3Y9COc9broY')

@bot.message_handler(commands=['start'])
def start_command(message):
	if message != 'admin':
	    print('said hello')
	    keyboard = types.InlineKeyboardMarkup()
	    russian = types.InlineKeyboardButton(text='RU', callback_data='ru')
	    keyboard.add(russian)
	    english = types.InlineKeyboardButton(text='EN', callback_data='en')
	    keyboard.add(english)
	    bot.send_message(message.from_user.id, text='Выбери язык / Choose your language ', reply_markup=keyboard)
	else:
		pas


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
	if call.data == "ru":
		bot.send_message(call.message.chat.id, "Привет!")
	else:
		bot.send_message(call.message.chat.id, "Hello!")
bot.polling()
