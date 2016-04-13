from tkinter import *
from tkinter.filedialog import LoadFileDialog, SaveFileDialog, Directory
from tkinter.colorchooser import askcolor
from tkinter.messagebox import (showinfo, showwarning, showerror, askquestion,
                                 askokcancel, askyesno, askyesnocancel, askretrycancel)

class Application(Frame):
    def askdir(self):
        d = Directory(self)
        print(d.show())
        
    def messages(self):
        print("info", showinfo("Spam", "Egg Information"))
        print("warning", showwarning("Spam", "Egg Warning"))
        print("error", showerror("Spam", "Egg Alert"))
        print("question", askquestion("Spam", "Question"))
        print("proceed", askokcancel("Spam", "Proceed?"))
        print("yes/no", askyesno("Spam", "Got it?"))
        print("yes/no/cancel", askyesnocancel("Spam", "Want it?"))
        print("try again", askretrycancel("Spam", "Try again?"))
        
    def fileOpen(self):
        d = LoadFileDialog(self)
        fname = d.go("nosuch.txt", "*.py")
        if fname is None:
            print("Canceled...")
        else:
            print("Open file", fname)
    
    def fileSave(self):
        d = SaveFileDialog(self)
        fname = d.go("example", "*.py")
        if fname is None:
            print("Canceled...")
        else:
            print("Saving file", fname)
    
    def color(self):
        d = askcolor()
        print(d)
    
    def createWidgets(self):
        dButton = Button(self)
        dButton.config(width = 12, text = "Directory Test", command = self.askdir)
        dButton.pack(side = TOP)
        mButton = Button(self)
        mButton.config(width = 12, text = "Messages Test", command = self.messages)
        mButton.pack()
        cButton = Button(self)
        cButton.config(width = 12, text = "Color Choice", command = self.color)
        cButton.pack()
        lButton = Button(self)
        lButton.config(width = 12, text = "Open File", command = self.fileOpen)
        lButton.pack()
        sButton = Button(self)
        sButton.config(width = 12, text = "Save File", command = self.fileSave)
        sButton.pack()
        self.QUIT = Button(self)
        self.QUIT.config(width = 12, text = "Quit", fg = "red", command = self.quit)
        self.QUIT.pack(side = TOP)
    
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
    
root = Tk()
app = Application(master = root)
app.mainloop()
           