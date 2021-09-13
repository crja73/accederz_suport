import telebot
from telebot import types

scenario = {}

request_list = {}

bot = telebot.TeleBot('1937575560:AAEfovYaNsDEWo3xRocUE4uX3Y9COc9broY')

@bot.message_handler(content_types=['text'])  # comands=

def start_command(message):

	if '/admin' in message.text:
		request_list[message.from_user.id] = message.text
		print(request_list)

	elif message.text != 'admin':
		if str(message.text)[0].lower() in 'йцукенгшщзхъфывапролджэячсмитьбю':
			print('said hello')

			keyboard = types.InlineKeyboardMarkup()

			enter = types.InlineKeyboardButton(text='Проблема со входом', callback_data='enter')
			keyboard.add(enter)

			cheat = types.InlineKeyboardButton(text='Не работает чит', callback_data='work')
			keyboard.add(cheat)

			send_to_admin = types.InlineKeyboardButton(text='Задать вопрос администраторам', callback_data='administrator')
			keyboard.add(send_to_admin)

			bot.send_message(message.from_user.id, text='Выберите один из вариантов', reply_markup=keyboard)

		else:

			keyboard = types.InlineKeyboardMarkup()

			enter = types.InlineKeyboardButton(text='Login problem', callback_data='enter_en')
			keyboard.add(enter)

			cheat = types.InlineKeyboardButton(text='Cheat does not work', callback_data='work_en')
			keyboard.add(cheat)

			send_to_admin = types.InlineKeyboardButton(text='Ask a question to administrators', callback_data='administrator_en')
			keyboard.add(send_to_admin)

			bot.send_message(message.from_user.id, text='Choose one of the options', reply_markup=keyboard)


	else:

		bot.send_message(message.from_user.id, text='Введите пароль')
		if message.text == 'password':
			print('Добро пожаловать')


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
	if call.data == "enter":
		bot.send_message(call.message.chat.id, "Введи правильный пароль, долбоеб")

	elif call.data == 'work':
		bot.send_message(call.message.chat.id, "Потому что ты чмо")

	elif call.data == 'administrator':
		bot.send_message(call.message.chat.id, "Коротко и ясно опишите свою проюлему, в конце запроса не забудьте добавить '/admin'")

	elif call.data == 'administrator_en':
		bot.send_message(call.message.chat.id, "Don't forget to add '/ admin' at the end of the request")

	elif call.data == 'enter_en':
		bot.send_message(call.message.chat.id, "Enter the correct password, dumbass")

	elif call.data == 'work_en':
		bot.send_message(call.message.chat.id, "Because you are a schmuck")

bot.polling()