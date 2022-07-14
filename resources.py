import sys
import os
from util import prt

# Format: [file, [status, [bytes to send], [content-type]]]
resources = []
resourceNotFound = ['404 NOT FOUND', ['NOT FOUND'.encode()], [('Content-Type', 'text/plain')]]

def getResource(path):
	for i in resources:
		if i[0].lower() == path.lower():
			return i[1]
	return resourceNotFound

# all files are kept in RAM and served as needed
# searches '.' and any directories included in input
def loadResources(directories):
	
	for file in os.listdir(sys.path[0] + '/.'):
			prt(file)
			if file.endswith('.html') or file.endswith('.css') or file.endswith('.js') or file.endswith('.sass') or file.endswith('.json'):
				resources.append(loadText(file))
			elif file.endswith('.jpg') or file.endswith('.png'):
				resources.append(loadImg(file))
	
	for d in directories:
		for file in os.listdir(sys.path[0] + '/' + d):
			prt(file)
			if file.endswith('.html') or file.endswith('.css') or file.endswith('.js') or file.endswith('.sass') or file.endswith('.json'):
				resources.append(loadText(d + file))
			elif file.endswith('.jpg') or file.endswith('.png'):
				resources.append(loadImg(d + file))

def loadImg(file):
	nf = open(sys.path[0] + '/' + file, 'rb')
	img = nf.read()
	nf.close()
	
	contentType = [('Content-type', 'image/png'), ('content-length', str(len(img)))]
	
	return [file, ['200 OK', [img], contentType]]

def loadText(file):
	# load file
	newFile = open(sys.path[0] + '/' + file, "rb")
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
	if ext == 'json':
		contentType = [('Content-type', 'text/json')]
	
	return [file, ['200 OK', [contents], contentType]]