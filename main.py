import playback
import load_prompt
import input as i
import coms.commandController
import loop
import encounter

import os

ld = load_prompt.PromptLoader
pb = playback.Playback
gt = i.Input
cm = coms.commandController.Commands
lp = loop.Loop
en = encounter.Encounter



ip = ""
path = os.getcwd()

###
en.intro(path)
en.topText(path)
###

while True:
	print(path, end="")
	ip = gt.getInput()
	opcode = cm.call_command(ip)
	
	print(opcode)
	lp.loop(opcode)
	
	





