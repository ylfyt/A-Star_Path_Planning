from Graph import *

def getHeuristic(graph, destination):
    heu = []
    for i in range(graph.getNumOfNode()):
        dis = graph.getDistance(i, destination)
        heu.append(dis)
    
    return heu

def getMinDistance(dis):
    if (len(dis) <= 0):
        return -1
    else:
        idxMin = 0
        for i in range(1, len(dis)):
            tup = dis[i]
            tupMin = dis[idxMin]

            if (tup[1] < tupMin[1]):
                idxMin = i

        return idxMin

def astar(graph, idxDestinastion, heu, distance, stack, blacklist):
    if (stack[-1] == idxDestinastion):
        return stack
    
    idxFrom = stack[-1]

    friend = graph.getListConnectedNode(idxFrom)
    count = 0
    for i in range(len(friend)):
        idxFriend = friend[i]

        if (idxFriend not in stack):
            gn = graph.getDistance(idxFrom, idxFriend)
            hn = heu[idxFriend]
            fn = gn + hn
            tempStack = [e for e in stack]
            tempStack.append(idxFriend)

            tempDistance = [tempStack, fn]
            
            if (tempDistance not in distance and tempStack not in blacklist):
                distance.append(tempDistance)
                count += 1
    

    if (count == 0 and len(distance) != 0):
        idxMinDistance = getMinDistance(distance)
        blacklist.append(distance[idxMinDistance][0])
        distance.pop(idxMinDistance)

    if (len(distance) == 0):
        return []

    idxMinDistance = getMinDistance(distance)
    tup = distance[idxMinDistance]
    stack = tup[0]
    
    if (stack[-1] == idxDestinastion):
        return stack
    
    return astar(graph, idxDestinastion, heu, distance, stack, blacklist)



def findPath(graph, idxFrom, idxTo):
    if (graph.getNumOfNode() > 0):
        heu = getHeuristic(graph, idxTo)
        path = astar(graph, idxTo, heu, [], [idxFrom], [])
        
        if (len(path) <= 0):
            return [[], heu]
        else:
            return [path, heu]
    else:
        return [[], []]
