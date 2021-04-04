from Graph import *
from file import *

from tkinter import *

SCREEN_WIDTH = 720
SCREEN_HEIGHT = 720
SCREEN_SIZE = f"{SCREEN_WIDTH}x{SCREEN_HEIGHT}"




def onKeyPress(event):
    if (event.char == '/'):
        app.quit()

def createNode(name, x, y):
    graphVisualPanel.create_oval(x, y, 50, 50, fill="cyan")

app = Tk()
# app.geometry(SCREEN_SIZE)
app.bind('<KeyPress>', onKeyPress)

frame1 = Frame(app)
frame1.grid(row=0)

browseButton = Button(frame1, text="Browse")
browseButton.grid(row=0, column=0)

filePathText = Entry(frame1, width=100)
filePathText.grid(row=0, column=1, columnspan=3)

frame2 = Frame(app, bg="blue", width=610, height=610)
frame2.grid(row=1)

graphVisualPanel = Canvas(frame2, width=600, height=600, bg="white")
graphVisualPanel.grid(row=0, pady=5, padx=5)

graph = convertTextToGraph("01.txt")

if (graph.getNumOfNode() == 0):
    print("Graph is empty!!")

for i in range(graph.getNumOfNode()):
    node = graph.getNode(i)
    createNode(node.name, node.x, node.y)


app.mainloop()