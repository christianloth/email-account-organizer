from crackmeup import blond, kidfriendly, oneline, religious, sport, yo_mama, popular, chuck_norris, math_joke, \
	police, retirement, men_women, walks_into_a_bar, family, political, school, work


def joke(category):
	switcher = {
		"Blonde": 			blond.getRandomJoke(),
		"KidFriendly": 		kidfriendly.getRandomJoke(),
		"OneLiner": 		oneline.getRandomJoke(),
		"Religious":		religious.getRandomJoke(),
		"Sport":			sport.getRandomJoke(),
		"YoMama":			yo_mama.getRandomJoke(),
		"Popular":			popular.getRandomJoke(),
		"ChuckNorris":		chuck_norris.getRandomJoke(),
		"Math":				math_joke.getRandomJoke(),
		"Police":			police.getRandomJoke(),
		"Retirement":		retirement.getRandomJoke(),
		"Gender":			men_women.getRandomJoke(),
		"Bar":				walks_into_a_bar.getRandomJoke(),
		"Family":			family.getRandomJoke(),
		"Political":		political.getRandomJoke(),
		"School": 			school.getRandomJoke(),
		"Work":				work.getRandomJoke()
	}
	return switcher.get(category)
