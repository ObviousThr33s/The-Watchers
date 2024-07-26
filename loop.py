import coms.commandController

import encounter


import os
cm = coms.commandController.Commands
en = encounter.Encounter

class Loop:

	def initSys():
		pass

	def loop(opcode:int):
		
		#playback.Playback.timedPrint(.5, "Hello... you")
		#prompt = load_prompt.PromptLoader.getFile("prompt.txt")

		#playback.Playback.timedPrint(0.25333, prompt)

		os.system("cls")

		#STORY STEPS
		#how do i find when is best for certain events
		#counters for command usage
		en.rollForEvent(opcode)

