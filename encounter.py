import os
import random
import time
import coms.comm as cin
import playback
import coms.commandController
import utils.load_prompt as load_prompt
import utils.setting as setting

pb = playback.Playback
cm = coms.commandController.Commands

lp = load_prompt.PromptLoader

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
		st = lp.getRandomLine(path+"\\bin\\questions\\0.txt", True)

		pb.timedPrint(.15, st)
		time.sleep(2)
		os.system("cls")
		pass

	def intro(path):
		playback.Playback.timedPrint(.01, lp.getSpecificLine(path+"\\bin\\greet.txt",4))
		prompt = lp.getFile(path+"\\bin\\prompt.txt")
		playback.Playback.timedPrint(0.01, prompt)
		time.sleep(.65)
		input()
		os.system("cls")

	def topText(path):
		print("\nUsing working directory @ "+path)
		print("Obelisk v"+version)

	def rawDump(path):
		s = lp.getFile(path+"\\bin\\base64.txt")

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

		code = ["1000","1001","1002","1070","1087","3000","4000"]
		c = code[random.randint(0,len(code)-1)]

		p0 = open(path+"\\bin\\logs\\log"+c+".txt")
		st = p0.readlines()
		pb.timedPrint(.15, st)
		input()

		os.system("cls")
		pass

	def event2(path:str):
		os.system("cls")
		st = lp.getRandomLine(path+"\\bin\\responses\\0.txt",True)

		pb.timedPrint(.15, st)
		time.sleep(2)
		os.system("cls")
		pass

	def event3(path:str):
		pass
