i in range(numOfNode):
            name = nodes[i].name
            x = nodes[i].x
            y = nodes[i].y
            numOfconnect = numOfConnectedNode[i]
            data = name + "[" + str(x) + "," + str(y) + "]" + str(numOfconnect)
            print(data, end=", ")
        print()

        for i in range(numOfNode):
            print(connectedNode[i])