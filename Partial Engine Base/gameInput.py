import commands
import game

class gameInput:	

    #define error codes
    INVALID_INPUT = 10
    INVALID_SIZE  = 11

    #define command aliases
    QUIT          = ["quit", "q"]
    HELP          = ["help", "h"]

    #create command executable
    c = commands.Commands()

    #define command aliases that can be executed
    COMMANDS = [QUIT, HELP]
    #define executable command map
    EXE      = [c.quit, c.ghelp]
        
    def error(errorCode: int):
        #if game is in debug mode throw errors
        #takes error code defined by constants
        if game.debug:
            print("ERROR ", errorCode)
            input("Press enter to continue.")

    def checkInt(check):
        #checks whether a string is an integer
        #throws catchable error
        try:
            s = int(s)
            return True
        except:
            gameInput.error(gameInput.INVALID_INPUT)
            return False
    
    def getCommandKey(command:str):
        #takes command input string and looks up the
        #key that is mapped to that command based on the
        #command aiases 
        
        #itterates over commands
        for i in gameInput.COMMANDS:
            #itterates over command aliases
            for j in i:
                if command == j:
                    return gameInput.COMMANDS.index(i)
                else:
                    continue
        #throws error code
        return -1
    

    def exeCommand(key):
        #executes a command key
        gameInput.EXE[key]()

    def cs(self):
        #grabs user input
        command = input()
        #checks of the user just wants to update the screen
        if len(command) < 1:
            return
        
        #look up command key
        key = gameInput.getCommandKey(command)
        
        #throw error if command key isn't found
        if key < 0:
            gameInput.error(gameInput.INVALID_INPUT)
            return
        else:
            #execute command based on key
            gameInput.exeCommand(key)
            return