import First_parser_hockey as hockey
import First_parser_football as football
import telebot
from telebot import types


bot = telebot.TeleBot('859651285:AAFHMnTirym_BHT9U5s_CUcifVa4Tue7p_Q')




hockey_results_table = hockey.main()
football_results_table = football.main()
football_results = ""
hockey_results = ""
for el in football_results_table:
	football_results += el + "\n" + "\n"

for el in hockey_results_table:
	hockey_results += el + "\n" + "\n"


markup = types.ReplyKeyboardMarkup()
football_button = types.KeyboardButton("football")
hockey_button = types.KeyboardButton("hockey")
markup.row(football_button, hockey_button)




@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Чтобы узнать результаты топовых матчей по футболу - введи 'football', если же нужен хоккей - введи 'hockey', еще можешь воспользоваться клавиатурой для даунов", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def send_keyboard(message):
	 
	if message.text.lower() == "football":
		bot.send_message(message.chat.id, football_results)
	elif message.text.lower() == "hockey":
		bot.send_message(message.chat.id, hockey_results)
	else:
		bot.send_message(message.chat.id, "Ты тупой что ли? Написано же либо football либо hockey")
	
while True:
	try:
		bot.polling(none_stop=True)

	except Exception:
		time.sleep(15)