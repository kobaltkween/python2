from tkinter import *

root = Tk()

w = Label(root, text = "Red Label", bg = "red", fg = "white")
w.pack(side = TOP, fill = BOTH)
w = Label(root, text = "Green Label", bg = "green", fg = "white")
w.pack(side = TOP, fill = BOTH, expand = TRUE)
w = Label(root, text = "Blue Label", bg = "blue", fg = "white")
w.pack(side = TOP, fill = BOTH, expand = TRUE)

mainloop()