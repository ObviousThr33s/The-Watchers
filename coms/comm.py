class Command:
	#command handles
	nocom = [""]
	get_exit  = ["exit", "q", "quit", "exe"]
	get_list_dir = ["list","ls", "dir"]
	get_change_dir  = ["change-directory","cd"]
	get_help = ["help", "?"]

	command_char = '/'

	tokens = [nocom, get_exit, get_list_dir, get_change_dir, get_help]