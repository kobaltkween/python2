from tkinter import *
import decimal

class Application(Frame):
    
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        
    def createWidgets(self):
        px = 10
        py = 5
        tw = 8
        topFrame = Frame(self)
        
        leftFrame = Frame(topFrame)
        self.num1 = Entry(leftFrame)
        self.num1['width'] = tw
        self.num1.pack(side = TOP)
        self.num2 = Entry(leftFrame)
        self.num2["width"] = tw
        self.num2.pack(side = TOP)
        leftFrame.pack(side = LEFT, padx = px, pady = py)
        
        rightFrame = Frame(topFrame)
        self.label = Label(rightFrame, text = "Sum of the Fields", width = 15, anchor = "w")
        self.label.pack(side = TOP)
        self.addIt = Button(rightFrame, text = "Add", command = self.addIt).pack(side = LEFT, pady = py)
        rightFrame.pack(side = TOP, padx = px, pady = py)
        
        topFrame.pack(side = TOP)
        
        bottomFrame = Frame(self)
        self.QUIT = Button(bottomFrame, text = "Quit", command = self.quit).pack(side = TOP)
        bottomFrame.pack(side = BOTTOM)
    
    def addIt(self):
        num1 = self.num1.get()
        num2 = self.num2.get()
        decimal.getcontext().prec = 6
        try:
            num1 = decimal.Decimal(float(num1))
            num2 = decimal.Decimal(float(num2))
            output = num1 + num2
        except ValueError:
            output = "***ERROR***"
        self.label.config(text = output)

root = Tk()
app = Application (master = root)
app.mainloop()