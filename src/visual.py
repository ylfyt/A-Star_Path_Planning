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

    f = graph.getMaxDistanceX()

    if (f < graph.getMaxDistanceY()):
        f = graph.getMaxDistanceY()

    cut = 100

    if (f <= 0):
        f = graphVisualPanel.winfo_reqwidth()
    sc = (graphVisualPanel.winfo_reqwidth()-cut) / f 

    for i in range(graph.getNumOfNode()):
        friend = graph.getListConnectedNode(i)
        for j in range(len(friend)):
            idx = friend[j]
            if (idx > i):
                node1 = graph.getNode(i)
                node2 = graph.getNode(idx)

                xPos1 = (node1.x - graph.getMinX())*sc + cut/2
                yPos1 = (node1.y - graph.getMinY())*sc + cut/2

                xPos2 = (node2.x - graph.getMinX())*sc + cut/2
                yPos2 = (node2.y - graph.getMinY())*sc + cut/2

                drawLine(xPos1, yPos1, xPos2, yPos2)

    for i in range(graph.getNumOfNode()):
        node = graph.getNode(i)
        
        xPos = (node.x - graph.getMinX())*sc + cut/2
        yPos = (node.y - graph.getMinY())*sc + cut/2

        createNode(node.name, xPos, yPos)


def createNode(name, xPos, yPos):
    radius = 20
    graphVisualPanel.create_oval(xPos-radius, yPos-radius, xPos+radius, yPos+radius, fill="cyan")
    graphVisualPanel.create_text(xPos, yPos, fill="darkblue", text=name)

def drawLine(xPos1, yPos1, xPos2, yPos2):
    graphVisualPanel.create_line(xPos1, yPos1, xPos2, yPos2, fill="red", width=2)

# End of Graph Visualization



def onKeyPress(event):
    if (event.char == '/'):
        # graphVisualPanel.delete("all")
        app.quit()

app = Tk()
# app.geometry(SCREEN_SIZE)
app.bind('<KeyPress>', onKeyPress)



frame1 = Frame(app)
frame1.grid(row=0, padx=10, pady=10)

browseButton = Button(frame1, text="Browse")
browseButton.grid(row=0, column=0)

filePathText = Entry(frame1, width=100)
filePathText.grid(row=0, column=1, columnspan=3, padx=10)

frame2 = Frame(app, width=610, height=610)
frame2.grid(row=1)

graphVisualPanel = Canvas(frame2, width=600, height=600, bg="light grey")
graphVisualPanel.grid(row=0, pady=5, padx=5)


graph = convertTextToGraph("01.txt")
showGraphVisualization(graph)


app.mainloop()