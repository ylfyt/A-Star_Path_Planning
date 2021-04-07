from tkinter import filedialog
from tkinter import ttk
from tkinter import *

from Graph import *
from File import *
from Astar import findPath

SCREEN_WIDTH = 720
SCREEN_HEIGHT = 720
SCREEN_SIZE = f"{SCREEN_WIDTH}x{SCREEN_HEIGHT}"

graph = Graph(1, 0, [], [], [])

# Graph visualization

def showGraphVisualization(graph, path):
    if (graph.getNumOfNode() == 0):
        print("Graph is empty!!")
        return
    
    edges = []
    if (len(path) > 1):
        for i in range(0, len(path)-1):
            edge = []
            edge.append(path[i])
            edge.append(path[i+1])
            edges.append(edge)

    for i in range(graph.getNumOfNode()):
        friend = graph.getListConnectedNode(i)
        for j in range(len(friend)):
            idx = friend[j]
            if (idx > i):
                node1 = graph.getNode(i)
                node2 = graph.getNode(idx)
                distance = graph.getDistance(i, idx)
                xPos1 = getPosXRelative(graph, node1.x)
                yPos1 = getPosYRelative(graph, node1.y)
                
                xPos2 = getPosXRelative(graph, node2.x)
                yPos2 = getPosYRelative(graph, node2.y)

                color = "red"

                if (len(edges) > 0):
                    e1 = [i, idx]
                    e2 = [idx, i]
                    if (e1 in edges or e2 in edges):
                        color = "black"


                drawLine(distance, xPos1, yPos1, xPos2, yPos2, color)

    for i in range(graph.getNumOfNode()):
        node = graph.getNode(i)
        
        xPos = getPosXRelative(graph, node.x)
        yPos = getPosYRelative(graph, node.y)

        color = "cyan"
        
        if (len(path) > 0):
            if (i in path):
                color = "orange"

        createNode(node.name, xPos, yPos, color)
    
def getPosXRelative(graph, x):
    pad = 70

    xPanelCenter = (graphVisualPanel.winfo_reqwidth()-4-pad)/2
    xCenterPos = (graph.getMaxX() + graph.getMinX())/2
    xMaxDisCenter = graph.getMaxDistanceX()/2

    dis = x - xCenterPos

    if (xMaxDisCenter == 0):
        return xPanelCenter + pad/2
    else:
        return dis/xMaxDisCenter * xPanelCenter + xPanelCenter + pad/2

def getPosYRelative(graph, y):
    pad = 70

    yPanelCenter = (graphVisualPanel.winfo_reqheight()-4-pad)/2
    yCenterPos = (graph.getMaxY() + graph.getMinY())/2
    yMaxDisCenter = graph.getMaxDistanceY()/2

    dis = y - yCenterPos

    if (yMaxDisCenter == 0):
        return yPanelCenter + pad/2
    else:
        return dis/yMaxDisCenter * yPanelCenter + yPanelCenter + pad/2


def createNode(name, xPos, yPos, color):
    radius = 20
    graphVisualPanel.create_oval(xPos-radius, yPos-radius, xPos+radius, yPos+radius, fill=color)
    graphVisualPanel.create_text(xPos, yPos, fill="darkblue", text=name)

def drawLine(dis, xPos1, yPos1, xPos2, yPos2, color):
    graphVisualPanel.create_line(xPos1, yPos1, xPos2, yPos2, fill=color, width=2)
    xTextPos = (xPos2 + xPos1)/2
    yTextPos = (yPos2 + yPos1)/2
    graphVisualPanel.create_text(xTextPos, yTextPos, text=round(dis, 2), fill="black")


def showMinimumPath(graph, path):
    print("Show minimum path")
    s = ""
    if (len(path) > 0):
        resetGraphVisualizationPanel()
        resetPathText()
        s = getStringPath(path)
        dis = graph.getDistancePath(path)
        sDis = "Distance : " + str(round(dis, 2)) + "\n"
        s = sDis + s
        pathText.insert(END, s)
        showGraphVisualization(graph, path)
    else:
        s = "Path is not Found!!"
        resetPathText()
        pathText.insert(END, s)

def showDistanceHeuristic(graph, heu):
    resetHeuText()
    row = 1
    val = ""
    for i in range(len(heu)):
        temp = ""
        name = graph.getNode(i).name
        temp += name
        temp += " : " + str(round(heu[i], 2)) + "; "
        if (len(val + temp) >= 50*row):
            row += 1
            val += '\n' + temp
        else:
            val += temp
    heuText.insert(END, val)

# End of Graph Visualization

def searchPath():
    print("A Star")
    global graph

    if (graph.getNumOfNode() > 0):
        
        if (nodeFromDropdown.current() < 0 or nodeToDropdown.current() < 0):
            print("Node is not selected!!")
        else:
            pathAndHeu = findPath(graph, nodeFromDropdown.current(), nodeToDropdown.current())
            path = pathAndHeu[0]
            showDistanceHeuristic(graph, pathAndHeu[1])
            showMinimumPath(graph, path)
    else:
        print("Graph is not ready!!")

def browse():
    print("browse!!")
    filePath = filedialog.askopenfilename(initialdir="/", title="Select Graph File", filetypes=(('text files', 'txt'),))
    # print(filePath)
    if (len(filePath) > 0):
        filePathText.delete(0, END)
        filePathText.insert(0, filePath)
        resetGraphVisualizationPanel()
        resetDropdown()
        resetHeuText()
        resetPathText()
        global graph
        graph = convertTextToGraph(filePath)
        
        if (graph.getNumOfNode() > 0):
            showGraphVisualization(graph, [])
            setDrowdownMenu(graph.getListNode())
                

def getStringPath(path):
    s = ""
    row = 1
    for i in range(len(path)):
        temp = ""
        name = graph.getNode(path[i]).name
        temp += name
        if (i != len(path)-1):
            temp += " -> "
        
        if (len(s+temp) >= 50*row):
            row += 1
            temp += '\n'
        
        s += temp
    
    return s

def resetGraphVisualizationPanel():
    graphVisualPanel.delete("all")

def resetPathText():
    pathText.delete("1.0", "end")

def resetHeuText():
    heuText.delete("1.0", "end")

def resetDropdown():
    print("Reset Dropdown")
    nodeFromDropdown.set('')
    nodeToDropdown.set('')
    nodeFromDropdown["values"] = []
    nodeToDropdown["values"] = []
    nodeFromDropdown.select_clear()
    nodeToDropdown.select_clear()

def setDrowdownMenu(nodes):
    val = []
    for i in range(len(nodes)):
        val.append(nodes[i].name)
    
    nodeFromDropdown["values"] = val
    nodeToDropdown["values"] = val

app = Tk()
app.title("A Start Path Planning")

frameLeft = Frame(app)
frameLeft.grid(row=0, column=0)
frameRight = Frame(app)
frameRight.grid(row=0, column=1)


# =========================================================
frame1 = Frame(frameLeft)
frame1.grid(row=0, padx=10, pady=10)

browseButton = Button(frame1, text="Browse", command=browse)
browseButton.grid(row=0, column=0)

filePathText = Entry(frame1, width=65)
filePathText.grid(row=0, column=1, columnspan=3, padx=10)

# =========================================================
frame2 = Frame(frameLeft)
frame2.grid(row=1, padx=10, pady=10)

labelTextFrom = Label(frame2, text="From : ")
labelTextFrom.grid(row=0, column=0)
nodeFromDropdown = ttk.Combobox(frame2, values=(), state="readonly")
nodeFromDropdown.grid(row=0, column=1)

fillLabel = Label(frame2, text=" ")
fillLabel.grid(row=0, column=2, padx=0)

labelTextTo = Label(frame2, text="To : ")
labelTextTo.grid(row=0, column=3)
nodeToDropdown = ttk.Combobox(frame2, values=(), state="readonly")
nodeToDropdown.grid(row=0, column=4)

searchButton = Button(frame2, text="Search", width=10, height=2, command=searchPath)
searchButton.grid(row=0, column=7, padx=20)

# =========================================================
frame3 = Frame(frameLeft)
frame3.grid(row=2, padx=10, pady=10)

pathTextLabel = Label(frame3, text="Path : ")
pathTextLabel.grid(row=0, column=0)
pathText = Text(frame3, height=10, width=50)
pathText.grid(row=1, column=0)

# =========================================================
frame4 = Frame(frameLeft)
frame4.grid(row=3, padx=10, pady=10)
heuTextLabel = Label(frame4, text="Heuristic : ")
heuTextLabel.grid(row=0, column=0)
heuText = Text(frame4, height=10, width=50)
heuText.grid(row=1, column=0)

# =========================================================
frame5 = Frame(frameRight, width=610, height=610)
frame5.grid(row=0, padx=10, pady=10)

graphVisualPanel = Canvas(frame5, width=700, height=700, bg="light grey")
graphVisualPanel.grid(row=0, pady=5, padx=5)

app.mainloop()