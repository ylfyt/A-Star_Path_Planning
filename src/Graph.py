class Node:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

    def printNode(self):
        print(self.name + " : " + str(self.x) + ", " + str(self.y))


class Graph:

    def __init__(self):
        self.numOfNode = 0
        self.nodes = []                 # array of node
        self.numOfConnectedNode = []    # array of integer
        self.connectedNode = []         # array of array of integer

    def __init__(self, nodesTemp, numOfConnectedNodeTemp, connectedNodeTemp):
        self.numOfNode = 0
        self. nodes = nodesTemp
        self.numOfConnectedNode = numOfConnectedNodeTemp
        self.connectedNode = connectedNodeTemp

    def getListNode(self):
        return self.nodes

    def getNode(self, idxNode):
        return self.nodes[idxNode]
    
    def getListConnectedNode(self, idxNode):
        return self.connectedNode[idxNode]

    def getListListConnected(self):
        return self.connectedNode

    def getListNumOfConnectedNode(self):
        return self.numOfConnectedNode
    
    def getNumOfConnectedNode(self, idxNode):
        return self.numOfConnectedNode[idxNode]
    
    def getNumOfNode(self):
        return len(self.nodes)
    
    def getIdxConnectedNode(self, idxNode, idx):
        return self.connectedNode[idxNode][idx]
    
    def getConnectedNode(self, idxNode, idxConnect):
        return self.nodes[self.getIdxConnectedNode(idxNode, idxConnect)]

    def getIdxNode(self, node):
        count = 0
        for x in self.nodes:
            if x.name == node:
                return count
            else:
                count = count + 1

    def addNode(self, newNode):
        self.nodes.append(newNode)

    def addConnectedNode(self, idxNode, idxConnect):
        self.connectedNode[idxNode].append(idxConnect)

    def addEdge(self, idx1, idx2):
        self.addConnectedNode(idx1, idx2)
        self.addConnectedNode(idx2, idx1)

    def isExistEdge(self, idx1, idx2):
        for x in self.connectedNode[idx1]:
            if x == idx2:
                return True
            else:
                return False

    def printGraph(self):
        for i in range(self.numOfNode):
            name = self.nodes[i].name
            x = self.nodes[i].x
            y = self.nodes[i].y
            numOfconnect = self.numOfConnectedNode[i]
            data = name + "[" + str(x) + "," + str(y) + "]" + str(numOfconnect)
            print(data, end=", ")
        print()

        for i in range(self.numOfNode):
            print(self.connectedNode[i])



# declare node
n1 = Node("A", 0, 0)
n2 = Node("B", 1, 1)
n3 = Node("C", 2, 2)
n4 = Node("D", 3, 3)
n5 = Node("E", 4, 4)

# declare nodes
nodes = [n1, n2, n3, n4, n5]
numOfConnectedNode1 = [1, 0, 0, 0, 1]
connectedNode1 = [
    [0,0,0,0,1],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [1,0,0,0,0]
]

g1 = Graph(nodes, numOfConnectedNode1, connectedNode1)
g1.printGraph()

