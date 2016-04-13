from tkinter import *

root = Tk()

def handler(event):
    print("Keystroke '{0}' ({1}) {2}".format(event.char, len(event.char), event.keycode))
    return "break"

def handler2(event):
    print("RootKeystroke '{0}' ({1}) {2} ".format(event.char, len(event.char), event.keycode))

def handler3(event):
    print("Frame clicked at", event.x, event.y)
    if event.x > 50 and event.y > 50:
        return "break"

def handler4(event):
    print("Root clicked at", event.x, event.y)


frame = Frame(root, width = 100, height = 100)
frame.bind("o", handler)
frame.bind("k", handler)
frame.bind("<Button-1>", handler3)
root.bind("<Key>", handler2)
root.bind("<Button-1>", handler4)
frame.pack()
frame.focus()

root.mainloop()