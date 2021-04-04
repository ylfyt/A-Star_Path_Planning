from Graph import *


def convertTextToGraph(fileName):
    
    try:
        if (len(fileName) < 4):
            dummy = Graph()
            return dummy
        
        dirNode = "../test/" + fileName
        dirAdj = "../test/" + fileName[:len(fileName)-4] + "_adj.txt"
        
        fileNode = open(dirNode, "r")
        fileAdj = open(dirAdj, "r")
        
        numOfNode = int(fileNode.readline().split(",")[0])
        
        graph = Graph()
        
        for line in fileNode:
            data = line.split(",")
            if (len(data) < 3+1):
                dummy = Graph()
                return dummy
            
            x = int(data[0])
            y = int(data[1])
            name = data[2]
            node = Node(name, x, y)

            graph.addNode(node)

        for i in range(numOfNode):
            line = fileAdj.readline()
            data = line.split(",")
            if (len(data) < numOfNode+1):
                dummy = Graph()
                return dummy

            for j in range(numOfNode):
                if (data[j] == '1'):
                    graph.addConnectedNode(i, j)
        
        return graph

    except IOError:
        print("Graph cannot be converted!!!")
        dummy = Graph()
        return dummy


# graph = convertTextToGraph("01.txt")

# if (graph.getNumOfNode() != 0):
#     graph.printGraph()
#     graph.getDistance(0, 2)
# else:
#     print("Master Karlsen")
    
# graph = convertTextToGraph("01.txt")
# graph.printGraph()

    


