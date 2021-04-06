from Graph import *
# from Node import *
from file import *



def euclidian(node1, node2):
    # input berupa node
    return ((node1.x-node2.x)**2+(node1.y-node2.y)**2)**(0.5)

def getHeuristic(graph, idxTujuan, heuristic):
    # heuristic = []
    print(idxTujuan)
    nodeTujuan = graph.nodes[idxTujuan]
    dist = 0
    for node in graph.nodes:
        dist = euclidian(node, nodeTujuan)
        heuristic.append(dist)
    
    # untuk cek saja
    for distance in heuristic:
        print(distance)
    return heuristic

def fillArrNone(list, graph):
    for i in range(len(graph.nodes)):
        list.append(-1)

def firstValue(list):
    for idx in range(len(list)):
        if list[idx] != 0:
            return idx

def searchMin(list):
    # idxMin = firstValue(list)
    # min = list[idxMin]
    idxMin = 0
    min = list[idxMin]
    for i in range(1, len(list)):
        if list[i] < min and list[i] != -1:
            idxMin = i
            min = list[i]

    # return index yang nilainya paling kecil
    return idxMin

def Astar(graph, stack, buntu, idxFrom, idxTo, visited, h):
    # memasukkan nilai heuristik berdasarkan index tujuan
    # h = []
    # getHeuristic(graph, idxTo, h)

    idxCurNode = idxFrom
    curNode = graph.nodes[idxCurNode]
    
    
    # while len(open) > 0:
    #     friend = graph.connectedNode[idxCurNode]
        
    #     for fNode in friend:
    #         # fNode = friend node
    #         if fNode not in stack and fNode not in buntu:
    #             weight = euclidian(curNode, fNode)
    #             distance = weight + h[fNode]



    if (idxCurNode == idxTo):
        return stack
    elif len(visited) == len(graph.nodes):
        return []
    else:
        friend = graph.connectedNode[idxCurNode]
        curDistance = []
        fillArrNone(curDistance, graph)

        for fIdxNode in friend:
            # fIdxNode = friend index node
            if (fIdxNode not in stack) and (fIdxNode not in buntu) and (fIdxNode not in visited):
                weight = euclidian(curNode, graph.nodes[fIdxNode])
                distance = weight + h[fIdxNode]
                curDistance[fIdxNode] = distance
            # elif fIdxNode in buntu:
            #     buntu.append(fIdxNode)
            else:
                pass
    
        
        idxMin = searchMin(curDistance)
        stack.append(idxMin)
        visited.append(idxCurNode)
        
        return Astar(graph, stack, buntu, idxMin, idxTo, visited)


        



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
# g1.printGraph()
# h = []
# getHeuristic(g1, 3, h)


g2 = convertTextToGraph("01.txt")

h2 = getHeuristic(g2, 2, [])
# stack = Astar(g2,[],[],0,2, [], h2)

# for el in stack:
#     print(el)
