from tkinter import *

class Application(Frame):
    def sayHi(self):
        print("Hi there, everyone!")
        
    def createWidgets(self):
        self.QUIT = Button(self, text = "Goodbye", fg = "red", command = self.quit).pack({"side": "right"}) 
        self.hiThere = Button(self, text = "Hello", fg = "blue", command = self.sayHi).pack({"side" : "left"})
        
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        
root = Tk()
app = Application(master = root)
app.mainloop()