class Node:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

    def printNode(self):
        print(self.name + " : " + str(self.x) + ", " + str(self.y))


class Graph:

    # def __init__(self):
        # self.numOfNode = 0
        # self.nodes = []                 # array of node
        # self.numOfConnectedNode = []    # array of integer
        # self.connectedNode = []         # array of array of integer

    def __init__(self, scaleTemp = 1, numOfNodeTemp = 0, nodesTemp = [], numOfConnectedNodeTemp = [], connectedNodeTemp = []):
        self.scale = scaleTemp
        self.numOfNode = numOfNodeTemp
        self.nodes = nodesTemp
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
                count = count + 1

    def addNode(self, newNode):
        self.numOfNode += 1
        self.nodes.append(newNode)
        self.numOfConnectedNode.append(0)
        self.connectedNode.append([])

    def addConnectedNode(self, idxNode, idxConnect):
        self.numOfConnectedNode[idxNode] += 1
        self.connectedNode[idxNode].append(idxConnect)

    def addEdge(self, idx1, idx2):
        self.addConnectedNode(idx1, idx2)
        self.addConnectedNode(idx2, idx1)

    def isExistEdge(self, idx1, idx2):
        for x in self.connectedNode[idx1]:
            if x == idx2:
                return True

        return False
    
    def getDistance(self, idx1, idx2):
        x1 = self.nodes[idx1].x
        y1 = self.nodes[idx1].y

        x2 = self.nodes[idx2].x
        y2 = self.nodes[idx2].y
        
        # Sementara pakau eucludian
        return (((x2-x1)**2 + (y2-y1)**2)**(1/2)) * self.scale

    
    def getMinX(self):
        if (self.numOfNode <= 0):
            return -999
        else:
            minX = self.nodes[0].x
            for i in range(1, self.numOfNode):
                if (minX > self.nodes[i].x):
                    minX = self.nodes[i].x
            
            return minX
    
    def getMaxX(self):
        if (self.numOfNode <= 0):
            return -999
        else:
            maxX = self.nodes[0].x
            for i in range(1, self.numOfNode):
                if (maxX < self.nodes[i].x):
                    maxX = self.nodes[i].x
            
            return maxX
    
    def getMinY(self):
        if (self.numOfNode <= 0):
            return -999
        else:
            minY = self.nodes[0].y
            for i in range(1, self.numOfNode):
                if (minY > self.nodes[i].y):
                    minY = self.nodes[i].y
            
            return minY
    
    def getMaxY(self):
        if (self.numOfNode <= 0):
            return -999
        else:
            maxY = self.nodes[0].y
            for i in range(1, self.numOfNode):
                if (maxY < self.nodes[i].y):
                    maxY = self.nodes[i].y
            
            return maxY
    
    def getDistancePath(self, path):
        sum = 0
        for i in range(len(path)-1):
            idx1 = path[i]
            idx2 = path[i+1]
            sum += self.getDistance(idx1, idx2)
        
        return sum
    
    def getMaxDistanceX(self):
        return self.getMaxX() - self.getMinX()
    
    def getMaxDistanceY(self):
        return self.getMaxY() - self.getMinY()

    def printGraph(self):
        for i in range(self.numOfNode):
            name = self.nodes[i].name
            x = self.nodes[i].x
            y = self.nodes[i].y
            numOfconnect = self.numOfConnectedNode[i]
            # print(numOfconnect)
            data = name + "[" + str(x) + "," + str(y) + "]" + str(numOfconnect)
            print(data, end=", ")
        print()

        for i in range(self.numOfNode):
            print(self.connectedNode[i])