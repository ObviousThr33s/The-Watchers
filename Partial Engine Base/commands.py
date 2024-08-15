import os

class Commands:
    def quit(self):
        os.system("cls")
        exit()
        
        
    def ghelp(self):
        #to do: dynamically generaterd
        print("help, h: Displays this message")
        print("quit, q: quits program")
        print("")
        print("Error codes:")
        print("\tERROR 10: Invalid input")
        print("press enter to continue", end="")
        input()