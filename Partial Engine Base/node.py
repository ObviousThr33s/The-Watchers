class Node:

        #object posistion and character declarations
        x = 0
        y = 0
        c = ''

        #object initial definitions
        def __init__(self, x_:int, y_:int, c_:str) -> None:
            self.x = x_
            self.y = y_
            self.c = c_

        #getters and setters
        def setC(self, c_:str):
            self.c = c_

        def setY(self, y_:int):
            self.y = y_
    
        def setX(self, x_:int):
            self.x = x_
