import generation
import node
import room
import nodeCollection

class Board:

    #declare a generator object for this board
    g = generation

    #not implemented yet
    #to-do: impliment dynamic charsets
    WALL = ["#"]
    FLOOR = ["."]
    charSet = [FLOOR, WALL]

    #declare the floor for the board which will act as a background
    floor = []

    #declare board size variables
    X = 0
    Y = 0

    #test objects
    Room1 =  room.Room
    Node1 =  node.Node

    #declare the board object collection
    boardObjs = nodeCollection.NodeCollection

    def __init__(self, X_, Y_) -> None:
        #define the board size
        self.X = X_
        self.Y = Y_
        #define the board generator
        self.g = generation.Generation(self)

        #define the floor
        self.floor = self.g.genFloor()

        #define test objects
        #define test node as (x,y,character representation)
        self.Node1 = node.Node(0,0,'c')
        #define the room via (origin node, width, height, wall representation)
        self.Room1 = room.Room(node.Node(15,15,"O"),5,10,"#")

    #changes the posistion of the room and adds a test node to the board
    def testTask0(self):
        self.Room1.updateOrigin(1,1)
        self.boardObjs.addNode(self.boardObjs, self.Node1)
    
    #randomly changes the test nodes posistion
    def testTask1(self):
        self.g.genNodeWalk(self.Node1)

    #updates the room by re-drawing the floor background 
    #and then placing objects on the floor background
    #to-do: board layers
    def update(self):
        self.floor = self.g.genFloor()
        for i in self.boardObjs.nodes:
            #places the i node of boardObjs at that nodes posistion 
            #with that nodes character representation
            self.floor[i.y][i.x] = i.c

    #itterates over what is on the board, printing it to screen
    #uses the board size to determine line
    def printBoard(self):
        for i in range(self.Y):
            for j in range(self.X):
                print(self.floor[i][j], end='')
            print()
        
