from Graph import *

def convertTextToGraph(filePath):
    
    try:
        if (len(filePath) < 4):
            dummy = Graph()
            return dummy
        
        dirNode = filePath
        dirAdj = filePath[:len(filePath)-4] + "_adj.txt"
        
        fileNode = open(dirNode, "r")
        fileAdj = open(dirAdj, "r")
        
        scale = int(fileNode.readline().split(",")[0])

        numOfNode = int(fileNode.readline().split(",")[0])
        
        graph = Graph(scale, 0, [], [], [])
        
        for line in fileNode:
            data = line.split(",")
            if (len(data) < 3+1):
                dummy = Graph()
                return dummy
            
            x = float(data[0])
            y = float(data[1])
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

    


