import requests
from bs4 import BeautifulSoup

#
player  = input("Enter full player name in lowercase: ")
player_split= player.split(" ")
page =  requests.get("https://www.basketball-reference.com/players/{}/{}01.html".format(player_split[1][0], player_split[1][0:5] + player_split[0][0:2]))

soup = BeautifulSoup(page.content, 'html.parser')
html = list(soup.children)[3]
body = list(html.children)[3]

div1 = body.find('div',class_="p1")

stats = div1.find_all('p')

totalGames = stats[1].get_text()
ppg = stats[3].get_text()
rebounds = stats[5].get_text()
assists = stats[7].get_text()

print("{} played {} games in his career averaging {} points, {} rebounds, and {} assists.".format(player, totalGames, ppg, rebounds, assists))



