from tkinter import *
from tkinter.simpledialog import Dialog

class MyDialog(Dialog):
    def body(self, master):
        self.result = None
        for r in range(5):
            for c in range(5):
                b = Button(master, text = "Row {0} Col {1}".format(r, c))
                b.grid(row = r, column = c)
        print("Dialog created")
        
    def apply(self):
        self.result = "OK"
        
class Application(Frame):
    def createDialog(self):
        d = MyDialog(self)
        print(d.result)
    
    def createWidgets(self):
        self.dButton = Button(self, text = "Dialog...", command = self.createDialog)
        self.dButton.pack({"side" : "left"})
        
        self.QUIT = Button(self, text = "Quit", fg = "red", command = self.quit)
        self.QUIT.pack({"side" : "left"})
    
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

root = Tk()
app = Application(master = root)
app.mainloop()