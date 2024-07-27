import os

cwd = os.getcwd()

def parseBool(s:str):
	s = s.lower()

	if(s.find('true') != -1):
		return True
	if(s.find('false') != -1):
		return False

path = cwd+"\\settings.txt"

#print(path)
#input()

settings = open(path, 'r')

debug_ = settings.readline()
lineLength = settings.readline()
lineLength = int(lineLength)
version = settings.readline()
version = str(version)

debug  = parseBool(debug_)

if debug:
	print(lineLength)
	print(version)
	print(debug_)


	print(debug) 

	input()

settings.close()

