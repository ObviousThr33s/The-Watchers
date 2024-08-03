
import random
import base64

class PromptLoader:

	def getFile(filename):
		f = open(filename, 'r')
		p = f.read()
		#p = str(p)

		#p = PromptLoader.parse(p)
		#f.close()
		return p

	def getLineCount():
		pass

	def getRandomLine():
		pass
	
	def getSpecificLine():
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

	def parse(s:str, tokens, relations):
		tokens = "<-"
		
		tokenTable = []

		for i in range(len(s)):
			
			c = s[i]

			if c in tokens:
				tokenTable.append(i)
		
		s_ = ""

		for i in range(len(s)):
			if i in tokenTable:
				pass
			else:
				s_ += s[i]

		return s_

	def sacFile():
		pass
