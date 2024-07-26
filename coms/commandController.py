import coms.comef as comef
import coms.comm as comm
cd = comef.commandDefinitions
com = comm.Command

class Commands:

	functions = {0:cd.do_nothing, 1:cd.do_exit, 2:cd.do_list, 3:cd.do_change_dir, 4:cd.do_help}

	def call_command(t:str):

		tL = len(com.tokens)
		i_ = 0
		for i in range(tL):
			for j in range(len(com.tokens[i])):
				if com.tokens[i][j] == t:
					i_ = i
				else:
					continue

		return i_

	def return_exe(opcode:int):
		if opcode in Commands.functions.keys():
			Commands.functions[opcode]()
		else:
			cd.do_nothing

