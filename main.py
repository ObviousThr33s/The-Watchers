import playback
import load_prompt
import input as i
import coms.commandController
import loop

import time
import random
import os

ld = load_prompt.PromptLoader
pb = playback.Playback
gt = i.Input
cm = coms.commandController.Commands
lp = loop.Loop

version = "0.1.0"

###The roadmap below is missing just about everything 
# and I cant be bothered to write it all down bc I have
# to do stuff

###
# Log: 0.0.0->0.0.6, initial game presentation
# Log: 0.0.0->0.1.0, full concept outline

###
# To Do (for v0.2.0):
#	*comment code stuctures/document how to implement
#	*finish command implementations
#	*refactor so it isn't as spaghetti
###
# After that:
#	*encounters, scenes, gamestates


lineLength = 80

ip = ""
path = os.getcwd()

###
playback.Playback.timedPrint(.01, "Hello... you")
prompt = ld.getFile("prompt.txt")
playback.Playback.timedPrint(0.01, prompt)
time.sleep(.65)
###

s = ld.getFile("C:\\The Watchers\\base64.txt")
l = len(s)

for k in range(lineLength-1):
	os.system("cls")
	print("Using working directory @ "+path)
	print("Obelisk v"+version)
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
pb.timedPrintL(.002, s, 80)
print(line+'\n')

while True:
	print(path, end="")
	ip = gt.getInput()
	opcode = cm.call_command(ip)
	
	print(opcode)
	lp.loop(opcode)
	
	





