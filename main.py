import playback
import utils.load_prompt as load_prompt
import coms.input as i
import coms.commandController
import loop
import encounter

import os

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
	
	





