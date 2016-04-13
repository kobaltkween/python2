from tkinter import *

ALL = N + S + W + E
p = 20

class Application(Frame):
    
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.master.rowconfigure(0, weight = 1)
        self.master.columnconfigure(0, weight = 1)
        self.grid(sticky = ALL)
        self.columnconfigure(1, weight = 2)
        
        #Frame 1
        c = 1
        cs = 2
        rw = 1
        self.rowconfigure(1, weight = rw)
        f1 = Frame(self, bg = "blue")
        f1.grid(row = 1, column = c, columnspan = cs, sticky = ALL)
        l1 = Label(self, text = "Frame 1", bg = "blue", fg = "white")
        l1.grid(row =1, column = c, columnspan = cs, padx = p, pady = p)
        
        #Frame 2
        self.rowconfigure(2, weight = rw)
        f2 = Frame(self, bg = "red")
        f2.grid(row = 2, column = c, columnspan = cs, sticky = ALL)
        l2 = Label(self, text = "Frame 2", bg = "red", fg = "white")
        l2.grid(row =2, column = c, columnspan = cs, padx = p, pady = p)
        
        #Frame 3
        self.rowconfigure(1, weight = rw)
        self.columnconfigure(2, weight = 3)
        f3 = Frame(self, bg = "white")
        f3.grid(row = 1, column = 3, columnspan = 3, rowspan = 2, sticky = ALL)
        l3 = Label(self, text = "Frame 3", bg = "white", fg = "blue")
        l3.grid(row =1, column = 3, rowspan = 2, columnspan = 3, padx = 1.5 * p, pady = 1.5 * p)
       
        #Buttons
        self.rowconfigure(3, weight = 0)
        for c in range(1,6):
            self.columnconfigure(c, weight = 1)
            Button(self, text = "Button {0}".format(c)).grid(row = 3, column = c, sticky = ALL)


root = Tk()
app = Application(master = root)
app.mainloop()