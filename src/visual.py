from tkinter import filedialog
from tkinter import *

from Graph import *
from file import *

SCREEN_WIDTH = 720
SCREEN_HEIGHT = 720
SCREEN_SIZE = f"{SCREEN_WIDTH}x{SCREEN_HEIGHT}"


# Graph visualization

def showGraphVisualization(graph):
    if (graph.getNumOfNode() == 0):
        print("Graph is empty!!")
        return
    
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

                drawLine(distance, xPos1, yPos1, xPos2, yPos2)

    for i in range(graph.getNumOfNode()):
        node = graph.getNode(i)
        
        xPos = getPosXRelative(graph, node.x)
        yPos = getPosYRelative(graph, node.y)

        createNode(node.name, xPos, yPos)
    
def getPosXRelative(graph, x):
    pad = 100

    xPanelCenter = (graphVisualPanel.winfo_reqwidth()-4-pad)/2
    xCenterPos = (graph.getMaxX() + graph.getMinX())/2
    xMaxDisCenter = graph.getMaxDistanceX()/2

    dis = x - xCenterPos

    if (xMaxDisCenter == 0):
        return xPanelCenter + pad/2
    else:
        return dis/xMaxDisCenter * xPanelCenter + xPanelCenter + pad/2

def getPosYRelative(graph, y):
    pad = 100

    yPanelCenter = (graphVisualPanel.winfo_reqheight()-4-pad)/2
    yCenterPos = (graph.getMaxY() + graph.getMinY())/2
    yMaxDisCenter = graph.getMaxDistanceY()/2

    dis = y - yCenterPos

    if (yMaxDisCenter == 0):
        return yPanelCenter + pad/2
    else:
        return dis/yMaxDisCenter * yPanelCenter + yPanelCenter + pad/2


def createNode(name, xPos, yPos):
    radius = 20
    graphVisualPanel.create_oval(xPos-radius, yPos-radius, xPos+radius, yPos+radius, fill="cyan")
    graphVisualPanel.create_text(xPos, yPos, fill="darkblue", text=name)

def drawLine(dis, xPos1, yPos1, xPos2, yPos2):
    graphVisualPanel.create_line(xPos1, yPos1, xPos2, yPos2, fill="red", width=2)
    xTextPos = (xPos2 + xPos1)/2
    yTextPos = (yPos2 + yPos1)/2
    graphVisualPanel.create_text(xTextPos, yTextPos, text=round(dis, 2))

# End of Graph Visualization


def browse():
    print("browse!!")
    filePath = filedialog.askopenfilename(initialdir="/", title="Select Graph File", filetypes=(('text files', 'txt'),))
    # print(filePath)
    if (len(filePath) > 0):
        filePathText.delete(0, END)
        filePathText.insert(0, filePath)
        resetGraphVisualizationPanel()
        graph = convertTextToGraph(filePath)
        showGraphVisualization(graph)

def resetGraphVisualizationPanel():
    graphVisualPanel.delete("all")

def onKeyPress(event):
    if (event.char == '/'):
        # graphVisualPanel.delete("all")
        app.quit()

app = Tk()
# app.geometry(SCREEN_SIZE)
app.bind('<KeyPress>', onKeyPress)



frame1 = Frame(app)
frame1.grid(row=0, padx=10, pady=10)

browseButton = Button(frame1, text="Browse", command=browse)
browseButton.grid(row=0, column=0)

filePathText = Entry(frame1, width=100)
filePathText.grid(row=0, column=1, columnspan=3, padx=10)

frame2 = Frame(app, width=610, height=610)
frame2.grid(row=1)

graphVisualPanel = Canvas(frame2, width=600, height=600, bg="light grey")
graphVisualPanel.grid(row=0, pady=5, padx=5)

app.mainloop()