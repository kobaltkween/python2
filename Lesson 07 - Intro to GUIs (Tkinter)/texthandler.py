from tkinter import *

class Application(Frame):
    """ Application main window class."""
    def __init__(self, master = None):
        """Main frame initialization (mostly delegated)"""
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
    
    def createWidgets(self):
        """Add all the widgets to the main frame."""
        topFrame = Frame(self)
        self.textIn = Entry(topFrame)
        self.label = Label(topFrame, text = "Output label")
        self.textIn.pack()
        self.label.pack()
        self.r = IntVar()
        Radiobutton(topFrame, text = "Upper case", variable = self.r, value = 1).pack(side = LEFT)
        Radiobutton(topFrame, text = "Lower case", variable = self.r, value = 2).pack(side = LEFT)
        Radiobutton(topFrame, text = "Title case", variable = self.r, value = 3).pack(side = LEFT)
        topFrame.pack(side = TOP)
        
        bottomFrame = Frame(self)
        bottomFrame.pack(side = BOTTOM)
        self.QUIT = Button(bottomFrame, text = "Quit", command = self.quit)
        self.QUIT.pack(side = LEFT)
        self.handleb = Button(bottomFrame, text = "Convert", command = self.handle)
        self.handleb.pack(side = LEFT)
        
    def handle(self):
        """Handle a click of the button by processing any text the user
        has placed in the Entry widget according to the selected radio
        button"""
        
        text = self.textIn.get()
        operation = self.r.get()
        if operation == 1:
            output = text.upper()
        elif operation == 2:
            output = text.lower()
        elif operation == 3:
            output = text.title()
        else:
            output = "********"
        self.label.config(text = output)
        
root = Tk()
app = Application (master = root)
app.mainloop()