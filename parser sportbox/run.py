import First_parser_football as football
import First_parser_hockey as hockey

user_input = input("Результаты чего ты хочешь узнать? 1 - футбол, 2 - хоккей   ")
print('Это займет буквально 15-20 секунд')
if user_input == "1":
	football.main()
elif user_input == "2":
	hockey.main()
else:
	print("Ну и хули ты пишешь?")
	input()