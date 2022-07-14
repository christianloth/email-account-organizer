import random

import crackmeup.jokesyou_dotcom_scrape as jokesyou

def getRandomJoke():
	index = random.randint(*(1, 2))
	if index == 1:
		joke = jokesyou.getJoke('womenjokes')
	else:
		joke = jokesyou.getJoke('menjokes')
	return joke