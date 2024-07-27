import time
import os
import random

debug = False

class Playback:
	def timedPrint(spacing, prompt):
		if not debug:
			d0 = time.thread_time()
			for i in range(len(prompt)):
				print(prompt[i], flush=True, end='')
				time.sleep(spacing*random.random())	
		else:
			print(prompt)

	def timedPrintL(spacing, prompt:str, lineLen=0):
		if lineLen == 0:
			print("ERROR:",prompt)
			return
		
		if not debug:
			d0 = time.thread_time()
			k = 0
			g = 0
			prompt = prompt.replace(' ', '')
			prompt = prompt.replace('\n', ' ')
			l = len(prompt)
			
			for i in range(l):
				if k == l-1:
					break

				k += 1
				print(prompt[i], flush=True, end='')
				time.sleep(spacing*random.random())	
				if (k/lineLen == 1):
					k = 0
					print()
		else:
			print(prompt)