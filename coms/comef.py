import coms.comm as comm

com = comm.Command
tokens = com.tokens

class commandDefinitions:
	def do_help():

		longest = 0

		for i in range(len(tokens)):
			for j in range(len(tokens[i])):
				if len(tokens[i][j]) > longest:
					longest = len(tokens[i][j])
			
		seper = " "
		
		for i in range(1,len(tokens)):
			sepr_ = " "*(longest-len(tokens[i][0])) 
			print(str(tokens[i][0]).upper(), end=sepr_+" :")
			for j in range(len(tokens[i])):
				print(tokens[i][j], end=" ")
			print()

	def do_list():
		pass
	def do_change_dir():
		pass

	def do_nothing():
		pass

	def do_exit():
		exit()
		pass