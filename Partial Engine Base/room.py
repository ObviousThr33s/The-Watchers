import game
import node
import nodeCollection
import board

class Room:
    #define the room as a collection of nodes
    room = nodeCollection.NodeCollection
    
    #create an origin for the room (top left)
    o = node

    #give it a width, height, and wall type
    w = 0
    h = 0
    c = ""

    def __init__(self, origin:node.Node, width, height, wallCharacter) -> None:
        self.w = width
        self.h = height
        self.c = wallCharacter

        self.o = origin
        #draw the Room object to init the room node collection
        self.drawRoom()
        
    
      
    
    def drawRoom(self):
        #create a temporary room to populate
        tempRoom = nodeCollection.NodeCollection
        
        #populate the room starting at the origin
        for i in range(self.h):
            for j in range(self.w):
                    tempNode = node.Node(i+self.o.x,j+self.o.y,self.c)
                    tempRoom.addNode(tempRoom, tempNode)
        
        #if game is in debug mode, show the origin
        if game.debug:
            tempRoom.addNode(tempRoom, self.o)

        #use the tempRoom to populate the permanent room
        self.room = tempRoom
        
    def updateOrigin(self, x:int, y:int):
        #clear the room using the builtin flush() from nodeCollection
        self.room.flush(self.room)

        #change the origin posistion
        self.o.setX(x)
        self.o.setY(y)

        #regenerate at the new origin
        self.drawRoom()

