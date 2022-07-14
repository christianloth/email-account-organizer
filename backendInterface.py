import json

import backendAPI as bk
from util import prt

# calls a function, returns the page to go to
def callFunction(lastPage, function, input, session):
	dict = parseInput(input)
	prt("Calling " + function + ": " + str(dict))
	
	# refreshes page on error by default
	if lastPage == 'login':
		lastPage = 'loginPage.html'
	elif lastPage == 'register':
		lastPage = 'registerPage.html'
	res = lastPage
	
	# handle functions
	if function == 'login':
		if "username" in dict and "password" in dict:
			r = bk.login(dict["username"], dict["password"])
			if r != ("Error: 1" or "Error: 2"):
				res = 'home.html'
				session['logged-in'] = 1
				session['username'] = dict["username"]
				session['password'] = dict["password"]
	elif function == 'register':
		if "username" in dict and "password1" in dict and "password2" in dict:
			if dict['password1'] == dict['password2']:
				r = bk.createAccount(dict['username'], dict['password1'], [], [], [], [])
				if r != "Error creating user.":
					res = 'loginPage.html'
	elif function == 'updateAccount' and 'logged-in' in session:
		if "account" in dict and "password" in dict:
			r = updateAccount(session['username'], session['password'], [input['account']], [input['password']], [], [])
	
	return res

def getSensitiveData(input, requestString):
	res = json.dumps('{"name": "error"}')
	
	spt = requestString.split('(')
	if len(spt) > 1:
		val = spt[0]
		name = spt[1].rstrip(').json')
		if val == 'checkaccount':
			r = bk.checkAccount(name)
			res = json.dumps(r)
			return res
		elif val == 'joke':
			r = bk.getJoke(name)
			print(r, name)
			return json.dumps('{"joke": "' + r.replace('"', '') + '"}')
	
	if 'username' in input and 'password' in input:
		if requestString == 'emails.json':
			res = bk.getEmailsInbox(input['username'], input['password'], 100)
			print(res)
		elif requestString == 'settings.json':
			res = bk.getSettings(input['username'], input['password'])
	
	return res

def parseInput(input):
	realIn = str(input, 'utf-8').split('&')
	dict = {}
	for val in realIn:
		act = val.split('=')
		dict[act[0]] = act[1]
	return dict
