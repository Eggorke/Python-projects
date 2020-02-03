import telebot
from telebot import types

bot = telebot.TeleBot('859651285:AAFHMnTirym_BHT9U5s_CUcifVa4Tue7p_Q')



markup = types.ReplyKeyboardMarkup()
football_button = types.KeyboardButton("football")
hockey_button = types.KeyboardButton("hockey")
markup.row(football_button, hockey_button)


@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Какие результаты хочешь узнать?")


@bot.message_handler(content_types=['text'])
def send_keyboard(message):
	 
	bot.send_message(message.chat.id,"123", reply_markup=markup)
	if message.text == "football":
		bot.send_message(message.chat.id, "Ну и пошел нахер")

bot.polling(none_stop=True)