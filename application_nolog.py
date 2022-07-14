import sys
import base64
import os

# server files
from wsgiref.simple_server import make_server

sys.path.insert(0, '/opt/python/current/app')

# [file, [status, [bytes to send], [content-type]]]
resources = []
resourceNotFound = ['404 NOT FOUND', ['NOT FOUND'.encode()], [('Content-Type', 'text/plain')]]

def getResource(path):
	for i in resources:
		if i[0] == path.lower():
			return i[1]
	return resourceNotFound

# all files are kept in RAM and served as needed
# searches '.' and any directories included in input
def loadResources(directories):
	
	for f in os.listdir('.'):
			file = f.lower()
			print(file)
			if file.endswith('.html') or file.endswith('.css') or file.endswith('.js') or file.endswith('.sass'):
				resources.append(loadText(file))
			elif file.endswith('.jpg') or file.endswith('.png'):
				resources.append(loadImg(file))
	
	for d in directories:
		for f in os.listdir(d):
			file = f.lower()
			print(file)
			if file.endswith('.html') or file.endswith('.css') or file.endswith('.js') or file.endswith('.sass'):
				resources.append(loadText(d + file))
			elif file.endswith('.jpg') or file.endswith('.png'):
				resources.append(loadImg(d + file))

def loadImg(file):
	nf = open(file, 'rb')
	img = nf.read()
	nf.close()
	
	contentType = [('Content-type', 'image/png'), ('content-length', str(len(img)))]
	
	return [file, ['200 OK', [img], contentType]]

def loadText(file):
	# load file
	newFile = open(file, "rb")
	contents = newFile.read()
	newFile.close()
	
	# get extension & set content-type
	contentType = []
	ext = file.split('.')[-1]
	if ext == 'html':
		contentType = [('Content-type', 'text/html')]
	if ext == 'js':
		contentType = [('Content-type', 'text/js')]
	if ext == 'css':
		contentType = [('Content-type', 'text/css')]
	if ext == 'sass':
		contentType = [('Content-type', 'text/sass')]
	
	return [file, ['200 OK', [contents], contentType]]

# this function runs every time someone tries to load a resource from the server
def application(environ, start_response):
	
	method  = environ['REQUEST_METHOD']
	
	if method == 'GET':
		# get the path/file they're trying to access
		path = environ.get('PATH_INFO', '').lstrip('/')
		print("Trying to access: " + path)
		
		res = getResource(path)
		print(res[0], res[2])
		
		start_response(res[0], res[2])
		return res[1]
	elif method == 'POST':
		print('posting!')

# starts local server
if __name__ == '__main__':
	srv = make_server('', 8000, application)
	loadResources(['images/', 'assets/css/', 'assets/css/images/', 'assets/js/', 'assets/sass/'])
	print("Serving on port 8000...")
	srv.serve_forever()