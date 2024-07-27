import os
import random
import time
import coms.comm as cin
import playback
import coms.commandController
import load_prompt
import setting

pb = playback.Playback
cm = coms.commandController.Commands

ld = load_prompt.PromptLoader

debug = setting.debug
lineLength = setting.lineLength
version = setting.version

class Encounter:

	def rollForEvent(opcode:int):
		path = ""
		path = os.getcwd()

		os.system("cls")

		if opcode == 0:
			if not debug:
				Encounter.event1(path)
			
			cm.return_exe(opcode)

		if opcode == 1:
			if not debug:
				Encounter.event0(path)
			
			cm.return_exe(opcode)

		if opcode == 4:
			if not debug:
				Encounter.event2(path)

			cm.return_exe(opcode)


	### Event functions

	def event0(path:str):
		p0 = open(path+"\\questions\\0.txt")
		length = len(p0.readlines())
		p0.close()
		p0 = open(path+"\\questions\\0.txt")

		st = ""

		for i in range(random.randint(0, length)):
			st = p0.readline()
		p0.close()

		pb.timedPrint(.15, st)
		time.sleep(2)
		os.system("cls")
		pass

	def intro(path):
		playback.Playback.timedPrint(.01, "Hello... you")
		prompt = ld.getFile("prompt.txt")
		playback.Playback.timedPrint(0.01, prompt)
		time.sleep(.65)
		os.system("cls")

	def topText(path):
		print("\nUsing working directory @ "+path)
		print("Obelisk v"+version)

	def rawDump(path):
		s = ld.getFile(path+"\\base64.txt")

		lines = 100
		m = lineLength*lines

		a = 0+random.randint(0,(len(s)-400))
		b = m+a
		s = s[a:b]
		l = len(s)

		for k in range(lineLength-1):
			os.system("cls")
			Encounter.topText(path)
			print()
			print("::LOAD<<: [REDACTED]")
			print("::SIZE>>: "+str(l)+"B")
			print("::LOAD::\n[", end='')
			st = "#"*k
			st += " "*(lineLength-k-2)
			st += "]"
			pb.timedPrint(.00001, st)


		print('\n')
		time.sleep(2)
		#
		#???
		#
		line = '<'
		line += "="*(lineLength-2)
		line += '>\n'
		print(line)

		print("::RAW>>:")
		pb.timedPrintL(.002, s, lineLength)
		print('\n'+line+'\n')



	def event1(path:str):
		os.system("cls")

		code = ["1000","2000","2001","3000"]
		c = code[random.randint(0,len(code)-1)]

		p0 = open(path+"\\logs\\log"+c+".txt")
		st = p0.readlines()
		pb.timedPrint(.15, st)
		input()

		os.system("cls")
		pass

	def event2(path:str):
		os.system("cls")
		p0 = open(path+"\\responses\\0.txt")
		length = len(p0.readlines())
		p0.close()
		p0 = open(path+"\\responses\\0.txt")
		st = ""

		for i in range(random.randint(0, length)):
			st = p0.readline()
		p0.close()

		pb.timedPrint(.15, st)
		time.sleep(2)
		os.system("cls")
		pass

	def event3(path:str):
		pass
