import sys

# handle log files
logFile = None

if len(sys.argv) >= 3:
	logFile = open(sys.argv[2], 'a')

def prt(val):
	if len(sys.argv) < 3:
		print(val)
	else:
		logFile.write(str(val) + '\n')