from tkinter import *

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SCREEN_SIZE = f"{SCREEN_WIDTH}x{SCREEN_HEIGHT}"

def onKeyPress(event):
    if (event.char == '/'):
        app.quit()

app = Tk()
app.geometry(SCREEN_SIZE)
app.bind('<KeyPress>', onKeyPress)

frame1 = Frame(app, bg="blue", width=SCREEN_WIDTH, height=SCREEN_HEIGHT//2)
frame1.pack(side=TOP)

frame2 = Frame(app, bg="red", width=SCREEN_WIDTH, height=SCREEN_HEIGHT//2)
frame2.pack(side = BOTTOM)


ent = Entry(frame1, width=SCREEN_WIDTH//2)
ent.pack(side=LEFT)

app.mainloop()