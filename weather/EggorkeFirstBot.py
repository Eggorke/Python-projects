import telebot
import pyowm

bot = telebot.TeleBot("983943772:AAFqyZh7FbjAYbWfsBS3n85tsQRCHltJ9HM")
owm = pyowm.OWM('23a625b571a78ef23c44bec7874b813a')

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Здарова, пидрила, погода в каком городе тебя интересует?")

@bot.message_handler(content_types=['text'])
def send_echo(message):
	try:
		place = owm.weather_at_place(message.text)
		weather = place.get_weather()
		temperature = weather.get_temperature('celsius')['temp']
		wind = weather.get_wind()['speed']
		answer1 = 'Температура воздуха в данном городе: ' + str(temperature) + ' °С'
		answer2 = 'Скорость ветра достигает: ' + str(wind) + ' м/с'
		bot.send_message(message.chat.id, answer1)
		bot.send_message(message.chat.id, answer2)
	except Exception:
		bot.send_message(message.chat.id, "Хуйню не неси, ок?")


bot.polling(none_stop = True)



