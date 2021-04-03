numOfNode = 0
nodes = []
numOfConnectedNode = []
connectedNode = []

class Node:
    name = ""
    x = -1
    y = -1
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
    
    def printNode(self):
        print(self.name + " : " + str(self.x) + ", " + str(self.y))
    

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


def convertTextToGraph(fileName):
    try:
        if (len(fileName) < 4):
            return False

        dirNode = "../test/" + fileName
        dirAdj = "../test/" + fileName[:len(fileName)-4] + "_adj.txt"
        
        fileNode = open(dirNode, "r")
        fileAdj = open(dirAdj, "r")

        n = fileNode.readline().split(",")[0]
        global numOfNode 
        numOfNode = int(n)

        for line in fileNode:
            data = line.split(",")
            if (len(data) < 3+1):
                return False
            
            x = int(data[0])
            y = int(data[1])
            name = data[2]
            node = Node(name, x, y)

            nodes.append(node)
            numOfConnectedNode.append(0)
            connectedNode.append([])

        for i in range(numOfNode):
            line = fileAdj.readline()
            data = line.split(",")
            if (len(data) < numOfNode+1):
                return False
            
            connect = []
            for j in range(numOfNode):
                if (data[j] == '1'):
                    connect.append(j)

            numOfConnectedNode[i] = len(connect)
            connectedNode[i] = connect
        
        return True

    except IOError:
        print("Graph cannot be converted!!!")
        return False


ready = convertTextToGraph("01.txt")
if (ready):
    printGraph(numOfNode, nodes, numOfConnectedNode, connectedNode)
    


    


