import crackmeup.jokesyou_dotcom_scrape as jokesyou

def getRandomJoke():
	joke = jokesyou.getJoke('retirementjokes')
	return joke