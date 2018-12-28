#東南亞
import requests
requests.get('https://movies.yahoo.com.tw/theater_result.html/id=53')
res = requests.get('https://movies.yahoo.com.tw/theater_result.html/id=53')
res.text

from bs4 import BeautifulSoup
Soup = BeautifulSoup(res.text,'html.parser')

tag_name = 'div.theaterlist_name a'
movie_time = 'ul.theater_time  '
articles = Soup.select(tag_name)
article2 = Soup.select(movie_time)


東南亞movie = []
for art in articles:
	art = str(art)
	num1 = art.find('>')
	art = art[num1+1:-4]
	東南亞movie.append(art)

東南亞long = []
東南亞time = []
find_time1=0

for art in article2:
	art = str(art)
	num2 = art.find('">')
	art = art[num2+2:-5]
	東南亞long.append(art)
for i in 東南亞long:
	n=0
	ava_time=[]
	東南亞time.append(ava_time)
	for j in i:
		n+=1
		if j == 't':
			find_time1=i.find('t">',n-1)
			ava_time.append(i[find_time1+3:find_time1+8])
for i in 東南亞time:
	if len(i)==0:
		i.append('今日已無場次')
for a in range(len(東南亞movie)):
	print(東南亞movie[a],東南亞time[a])
