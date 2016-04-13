from tkinter import *

class Application(Frame):
    
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.configure(height = 75, width = 75)
        # create a menu bar
        m1 = Menu(root)
        root.config(menu = m1)
        filemenu = Menu(m1, tearoff=False)
        m1.add_cascade(label = "File", menu = filemenu)
        filemenu.add_command(label = "New", command = self.callback1)
        filemenu.add_command(label = "Open...", command = self.callback2)
        filemenu.add_separator()
        filemenu.add_command(label = "Exit", command = self.callback3)
        helpmenu = Menu(m1, tearoff=False )
        m1.add_cascade(label = "Help", menu = helpmenu)
        helpmenu.add_command(label = "About...", command = self.callback4)
        
        self.cmenu = Menu(self, tearoff=False)
        self.cmenu.add_command(label = "Copy", command = self.copy)
        self.cmenu.add_command(label = "Paste", command = self.paste)
        self.bind("<Button-3>", self.popup)
        self.pack()
        
    def callback1(self):
        print("You selected 'File | New'")
        
    def callback2(self):
        print("You selected 'File | Open...'")
    
    def callback3(self):
        print("You selected 'File | Exit'")
    
    def callback4(self):
        print("You selected 'Help | About..'")
        
    def copy(self):
        print("Contet command 'Copy' selected")
        
    def paste(self):
        print("Context command 'Paste' selected")
    
    def popup(self, event):
        self.cmenu.post(event.x_root, event.y_root)

root = Tk()
app = Application(master = root)
app.mainloop()