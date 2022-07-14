import urllib.request
import random

from bs4 import BeautifulSoup

def getJoke(category):
	url = 'http://www.jokesyou.com/' + category + '.php'
	page = urllib.request.urlopen(url)
	handle = page.read()
	soup = BeautifulSoup(handle, "html.parser")
	jokes = []
	for i in range(3):
	    x = soup.find_all('div', class_= "right")[i].find_all('p')[1].get_text()
	    x = x.replace("\r", " ")
	    x = x.replace("\\", " ")
	    x = x.replace("\'", "")
	    jokes.append(x)
	return jokes[random.randint(0,2)]