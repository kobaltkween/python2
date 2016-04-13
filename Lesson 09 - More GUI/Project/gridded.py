from tkinter import *
import os

ALL = N + S + W + E
p = 20

class Application(Frame):
    
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.master.rowconfigure(0, weight = 1)
        self.master.columnconfigure(0, weight = 1)
        self.grid(sticky = ALL)
        self.columnconfigure(1, weight = 2)
        
        #Frames 1 & 2
        rw = 1
        for r, color in enumerate(["red", "blue"]):
            self.rowconfigure(r + 1, weight = rw)
            f = Frame(self, bg = color)
            f.myName = "Frame " + str(r + 1)
            f.grid(row = r + 1, column = 1, columnspan = 2, sticky = ALL)
            f.bind("<Button-1>", self.handle1)
            l = Label(f, text = f.myName, bg = color, fg = "white")
            l.grid(padx = p, pady = p)
        
        #Frame 3
        self.rowconfigure(1, weight = rw)
        self.columnconfigure(2, weight = 3)
        f3 = Frame(self, bg = "grey")
        f3.grid(row = 1, column = 3, columnspan = 3, rowspan = 2, sticky = ALL)
        #l3 = Label(f3, text = "Frame 3", bg = "white", fg = "blue")
        #l3.grid(padx = 1.5 * p, pady = 1.5 * p)
        f3.rowconfigure(1, weight = 0)
        f3.columnconfigure(1, weight = 1)
        self.entry = Entry(f3, width = 20)
        self.entry.grid(row = 1, column = 1, columnspan = 2, padx = p/4, pady = p/4, sticky = ALL)
        self.entry.insert(0, "testtext.txt")
        f3.rowconfigure(2, weight = 1)
        self.text = Text(f3, width = 20)
        self.text.grid(row = 2, column = 1, padx = p/4, pady = p/4, sticky = ALL)
        scrollbar = Scrollbar(f3)
        scrollbar.grid(row = 2, column = 2, sticky = N + S)
        self.text.configure(wrap = WORD, yscrollcommand = scrollbar.set)
        scrollbar.config(command = self.text.yview)
        #Buttons
        self.rowconfigure(3, weight = 0)
        colors = ['red', 'blue', 'green', 'black']
        for i, color in enumerate(colors):
            self.columnconfigure(i + 1, weight = 1)
            Button(self, width = 10, text = color.title(), command = lambda c = color: self.colorText(c)).grid(row = 3, column = i + 1, sticky = ALL)
        self.columnconfigure(5, weight = 1)
        Button(self, width = 10, text = "Open", command = self.loadText).grid(row = 3, column = 5, sticky = ALL)
        
    def handle1(self, event):
        print(event.widget.myName, "clicked at", event.x, event.y)
    
    def colorText(self, color):
        self.text.configure(fg = color)
    
    def loadText(self):
        fn = self.entry.get()
        newText = ""
        # If the file exists
        if os.path.isfile(fn):
            f = open(fn, "r")
            newText =  f.read()
            f.close()
        else:
            newText = "Could not load file's text."
        self.text.delete(1.0, END)
        self.text.insert(INSERT, newText)

root = Tk()
app = Application(master = root)
app.mainloop()