import sys
import base64
import os
import cgi
from beaker.middleware import SessionMiddleware

from util import prt
from resources import loadResources, getResource
from backendInterface import callFunction, getSensitiveData

if len(sys.argv) < 2:
	print("Usage: application_nolog.py PORT_NUMBER [LOG_FILE]")
	sys.exit()

# server files
from wsgiref.simple_server import make_server

def setupJSONReturn(json):
	return ['200 OK', [json.encode()], [('Content-Type', 'text/json')]]

# this function runs every time someone tries to load a resource from the server
def application(environ, start_response):
	
	method  = environ['REQUEST_METHOD']
	session = environ['beaker.session']
	path = environ.get('PATH_INFO', '').lstrip('/')
	prt("Trying to access: " + path)
	
	# must be logged in, then can access any json file
	if path.endswith('.json'):
		if 'logged-in' in session:
			# get json data if logged in
			r = getSensitiveData(session, path)
			res = setupJSONReturn(r)
			session.save()
			start_response(res[0], res[2])
			return res[1]
		else:
			# return not found if not logged in
			session.save()
			res = getResource('404 NOT FOUND')
			start_response(res[0], res[2])
			return res[1]
	
	if method == 'GET':
		# get the path/file they're trying to access
		
		res = getResource(path)
		prt(str(res[0]) + ", " + str(res[2]))
		session.save()
		start_response(res[0], res[2])
		return res[1]
	elif method == 'POST':
		try:
			requestBodySize = int(environ.get('CONTENT_LENGTH', 0))
		except (ValueError):
			requestBodySize = 0
		
		lastPage = environ.get('HTTP_REFERER').split('/')[-1]
		requestBody = environ['wsgi.input'].read(requestBodySize)
		
		print(lastPage)
		
		res = callFunction(lastPage, path, requestBody, session)
		print(res)
		newRes = getResource(res)
		session.save()
		start_response(newRes[0], newRes[2])
		return newRes[1]

# beaker session
session_opts = {
	'session.type': 'file',
	'session.cookie_expires': True,
	'session.data_dir': 'session_data'
}

# starts local server
if __name__ == '__main__':
	srv = make_server('', int(sys.argv[1]), SessionMiddleware(application, session_opts))
	loadResources(['images/', 'assets/css/', 'assets/css/images/', 'assets/js/', 'assets/sass/', 'assets/sass/libs/', 'assets/bootstrap/css/', 'assets/bootstrap/js/', 'assets/fonts/', 'crackmeup/', 'emailrep/'])
	prt(f"Serving on port {sys.argv[1]}...")
	srv.serve_forever()