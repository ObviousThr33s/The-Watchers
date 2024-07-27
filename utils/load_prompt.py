
import random
import base64

class PromptLoader:

	def getFile(filename):
		f = open(filename, 'r')
		p = f.read()
		f.close()
		return p

	def getLineCount(path):
		f = open(path, 'r')
		leng = len(f.readlines())
		f.close()
		return leng

	def getRandomLine(path:str, includeBlank:bool):
		#get a line from 0/1 to a random number less
		#than the number of lines in the file

		length = PromptLoader.getLineCount(path)
		p0 = open(path)
		st = ""
		
		#if blank is not set to 1, a blank may appear
		bl = 1

		if includeBlank:
			bl = 0

		for i in range(random.randint(bl, length)):
			st = p0.readline()
		p0.close()
		
		return st
	
	def getSpecificLine(path:str,line:int):
		#find line, return said line as string,
		#return if line doesnt exist
		if (line < 1 or line > PromptLoader.getLineCount(path)):
			return "ERROR: OUT OF BOUNDS"
		p0 = open(path)
		st = ""
		
		for i in range(1,line):
			st = p0.readline()
		p0.close()
		
		return st
		pass
	
	def getLines(path:str, a:int, b:int):
		pass

	def getRandLines(path:str, a:int, b:int):
		pass
	#not within scope
	#'fuzzes' pieces of text using base64
	#def getCracked(filename):
	#	#p = #int(PromptLoader.getFile(filename))
	#	p = 100
	#	f = open("C:\\The Watchers\\base64.txt")
	#	s = f.readline()
	#	
	#	print(p)


	#parse string given tokens
	#not implemented
	def parse(s:str):
		tokens = "<-"
		
		tokenTable = []

		#go through table and match, picking out what matches
		for i in range(len(s)):
			
			c = s[i]

			if c in tokens:
				tokenTable.append(i)
		
		s_ = ""
		#rmv via str cpy and return
		for i in range(len(s)):
			if i in tokenTable:
				pass
			else:
				s_ += s[i]

		return s_


	#i have no idea what this is
	#maybe save/set active file
	#maybe super awesome cool file
	#may parse files/tokenize them for lightweight psuedo scripting
	#show all commands?
	#i know I'll have to write it eventually
	#see all contents
	#its see all contents
	def sacFile(path):
		s = PromptLoader.getFile(path)
		print(s)
		pass
