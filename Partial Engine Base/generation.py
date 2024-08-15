import random
import node
import board
import room

class Generation:
    
    #declare member vars

    #instance board size
    X = 0
    Y = 0

    #instance board
    b = board



    def __init__(self, b:board) -> None:
        self.b = b
        self.X = b.X
        self.Y = b.Y

    def genFloor(self):    
        #create blank floor based on instance board size
        floor = []  
        for i in range(self.Y):
            floor.append([])
            for j in range(self.X):
                floor[i].append('.')     
        return floor        

    def genNodeWalk(self, n:node.Node) -> None:
        #get random co-ordinates
        r0 = random.randint(0, self.X-1)
        r1 = random.randint(0, self.Y-1)
        
        #using the instance board, accessing its board objects
        #move the node passed into this function to then
        #move it to the co-ordinates generated above
        self.b.boardObjs.moveNode(self.b.boardObjs,n,r0,r1)
        
        