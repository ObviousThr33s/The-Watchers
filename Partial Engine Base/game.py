import board

#sets whether the game is in debug mode or not
#to-do: transfer all globals here from main
global debug

debug = False

class Game:

    b = board.Board
    t = 0

    def __init__(self, boardObject:board.Board) -> None:
        self.b = boardObject
        pass

    def update(self, ticks):
        self.t = ticks
        self.testTask(self)
        
    
    def testTask(self):
        if self.t == 0:
            self.b.testTask0(self.b)
        if self.t >= 1:
            self.b.testTask1(self.b)
        pass
