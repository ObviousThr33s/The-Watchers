import node

class NodeCollection:
    
    #declare node structure
    nodes = []
    
    #might be used later idk
    def __init__(self) -> None:
        pass

    #append a unique node to the node structure
    def addNode(self, n:node.Node):
        self.nodes.append(n)
    
    #clear all nodes from the structure
    def flush(self):
        self.nodes.clear()
    
    #change a nodes unique posistion
    def moveNode(self, n:node.Node, x:int, y:int) -> None:
        n.setX(x)
        n.setY(y)
       