from tkinter import *

root = Tk()

def handler(event):
    print("clicked at", event.x, event.y)

frame = Frame(root, width = 100, height = 100)
frame.bind("<Button-1>", handler)
frame.pack()

root.mainloop()