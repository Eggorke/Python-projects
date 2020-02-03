import pyowm

owm = pyowm.OWM('23a625b571a78ef23c44bec7874b813a')

print('Погода в каком городе интересует, сучка?')
place_input = input()

try:
    place = owm.weather_at_place(place_input)
    weather = place.get_weather()
    temperature = weather.get_temperature('celsius')['temp']
    wind = weather.get_wind()['speed']
    print('Температура воздуха в данном городе:',int(temperature),'градусов')
    print('Скорость ветра достигает:',int(wind),'м/с')
except Exception:
    print("Ну хз чувак")