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
    
    def getNumOfConnectedNode(self idxNode):
        return self.numOfConnectedNode[idxNode]
    
    def getNumOfNode(self):
        return self.numOfNode
    
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
                count++

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

    def printGraph(numOfNode, nodes, numOfConnectedNode, connectedNode):
    for i in range(numOfNode):
        name = nodes[i].name
        x = nodes[i].x
        y = nodes[i].y
        numOfconnect = numOfConnectedNode[i]
        data = name + "[" + str(x) + "," + str(y) + "]" + str(numOfconnect)
        print(data, end=", ")
    print()

    for i in range(numOfNode):
        print(connectedNode[i])


    # // assign
    # void addNode(Node node);
    # void addConnectedNode(int idxNode, int idxConnect);
    # void addEdge(int idx1, int idx2);

    # bool isExistEdge(int idx1, int idx2);
    # void print();