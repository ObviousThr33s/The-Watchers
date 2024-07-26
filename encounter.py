import os
import random
import time
import coms.comm as cin
import playback
import coms.commandController
import load_prompt

pb = playback.Playback
cm = coms.commandController.Commands

lp = load_prompt.PromptLoader

class Encounter:

	def rollForEvent(opcode:int):
		path = ""
		path = os.getcwd()

		os.system("cls")

		if opcode == 1:

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
			cm.return_exe(opcode)

		if opcode == 0:
			os.system("cls")

			code = ["1000","2000","2001","3000"]
			c = code[random.randint(0,len(code)-1)]

			p0 = open(path+"\\logs\\log"+c+".txt")
			st = p0.readlines()
			pb.timedPrint(.15, st)
			input()

			os.system("cls")
			cm.return_exe(opcode)
		
		if opcode == 4:
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
			cm.return_exe(opcode)