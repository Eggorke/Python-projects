import requests
from bs4 import BeautifulSoup


#делаем запрос на сервер и возвращаем адрес в url
def get_html(url):
	r = requests.get(url)
	return r.text
#Получаем список ссылок с главной страницы
def get_links(html):
	soup = BeautifulSoup(html, 'html.parser')
	k = soup.find_all("a", attrs={"class": "_Sportbox_Spb2015_Components_GameRow_GameRow"})
	links = []
	for link in k:
		a = "https://news.sportbox.ru/Vidy_sporta/Futbol"
		b = a + link['href']
		links.append(b)
	return links


#ищем и возвращаем только команды
def get_teams(html):
	soup = BeautifulSoup(html, 'html.parser')

	teams_pre = soup.find_all("a", attrs={"class" : "b-match__team-title"})
	teams = []
	for team in teams_pre:
		a = team.text
		teams.append(a)
	return teams

#ищем и возвращаем результаты матчей
def get_score(html):
	soup = BeautifulSoup(html, 'html.parser')

	score_soup = soup.find('span', attrs={'class' : 'b-match__monitor__count'}).get_text()
	score = score_soup.split()
	
	return score

#ищем дату и время матчей и возвращаем
def get_match_dateTime(html):
	soup = BeautifulSoup(html, 'html.parser')

	pre_time = soup.find('span' , attrs={'class' : 'match_count_date'}).get_text()
	final_time = pre_time.split()

	return final_time

#ищем что за турнир/чемпионат
def get_turnir(html):
	soup = BeautifulSoup(html, 'html.parser')

	ul = soup.find('ul', attrs={'class' : 'node-header__rubrics'}).get_text().split()
	del ul[0]
	del ul[0]
	return ul






def main():
	url = 'https://news.sportbox.ru/Vidy_sporta/Futbol'
	html = get_html(url)
	links = get_links(html)
	teams = []
	scores = []
	date_nTime = []
	championat = []

	result_teams = []
	result_scores = []
	result_date_nTime = []
	championat_result = []

	print("Сейчас я покажу тебе уличную магию и все топовые футбольные матчи")
	print()
	end_programm = []

	for link in links:
		html_team = get_html(link)
		team = get_teams(html_team)
		teams.append(team)
		score = get_score(html_team)
		scores.append(score)
		dateTime = get_match_dateTime(html_team)
		date_nTime.append(dateTime)
		championat_html = get_turnir(html_team)
		championat.append(championat_html)
	for el in teams:
		team1 = el[0]
		team2 = el[1]
		result = team1 + " - " + team2
		result_teams.append(result)
	for el in scores:
		team1 = el[0]
		team2 = el[2]
		result = "(" + team1 + " - " + team2 + ")"
		result_scores.append(result)

	for el in date_nTime:
		date = el[0]
		time = el[1]
		result = " Дата матча: " + date + ", " + time
		result_date_nTime.append(result)

	for el in championat:
		c = []
		j = 0
		k = ""
		for inner_el in el:
			k = k + inner_el + " "
		championat_result.append(k)
		k = ""


	#Вывод всего безобразия на экран
	i = 0
	while i < len(result_teams):
		final_result = result_teams[i] + " " + result_scores[i] + " / " + result_date_nTime[i] + " / " + championat_result[i]
		end_programm.append(final_result)
		i += 1
		print("  " + final_result)
		print()
		
	input()	




if __name__ == "__main__":
	main()

