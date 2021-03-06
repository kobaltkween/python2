from tkinter import *
from maildb import msgs
import datetime
import mysql.connector as mysqlc
from database import loginInfo

def getDate(s):
    """
    Assumes a date form of yyyy-mm-dd, returns a corresponding datetime.date.
    """
    syear = s[:4]
    smonth = s[5:7]
    sday = s[8:]
    return datetime.date(int(syear), int(smonth), int(sday))

class Application(Frame):
    
    def __init__(self, master = None):
        """
        Establish the window structure, leaving some widgets accessible
        as app instance variables.  Connect button clicks to searchMail
        method and subject double-clicks to displayMail method.
        """
        Frame.__init__(self, master)
        self.master.rowconfigure(0, weight = 1)
        self.master.columnconfigure(0, weight = 1)
        self.grid(sticky = W + E + N + S)
        l0 = Label(self, text = "Email Database Search", font = ("Helvetica", 16))
        l0.grid(row = 0, column = 1, columnspan = 2)
        l1 = Label(self, text = "Not Before (yyyy-mm-dd):")
        l1.grid(row = 1, column = 1, sticky = E + N + S)
        self.mindate = Entry(self)
        self.mindate.grid(row = 1, column = 2, sticky = W + N + S)
        l2 = Label(self, text="Not After (yyyy-mm-dd):")
        l2.grid(row = 2, column = 1, sticky = E + N + S)
        self.maxdate = Entry(self)
        self.maxdate.grid(row = 2, column = 2, sticky = W + N + S)
        l3 = Label(self, text= "Sender's E-mail Contains:")
        l3.grid(row = 3, column = 1, sticky = E + N + S)
        self.addsearch = Entry(self)
        self.addsearch.grid(row = 3, column = 2, sticky = W + N + S)
        l4 = Label (self, text = "Sender's Name Contains:")
        l4.grid(row = 4, column = 1, sticky = E + N + S)
        self.namesearch = Entry(self)
        self.namesearch.grid(row = 4, column = 2, sticky = W + N + S)
        button = Button(self, text = "Search", command = self.searchMail)
        button.grid(row = 5, column = 2)
        self.msgsubs = Listbox(self, height = 10, width = 100)
        self.msgsubs.grid(row = 8, column = 1, columnspan = 2)
        self.msgsubs.bind("<Double-Button-1>", self.displayMail)
        self.message = Text(self, width = 100)
        self.message.grid(row = 9, column = 1, columnspan = 2)
        
    def searchMail(self):
        """
        Take the database search parameters provided by the user
        (trying to make sense of the dates) and select the appropriate
        messages from the database, displaying the subject lines of the 
        messages in a scrolling selection list.
        """
        mindate = self.mindate.get()
        if not mindate:
            mindate = None
        else:
            mindate = getDate(mindate)
        maxdate = self.maxdate.get()
        if not maxdate:
            maxdate = None
        else:
            maxdate = getDate(maxdate)
        addsearch = self.addsearch.get()
        if not addsearch:
            addsearch = None
        namesearch = self.namesearch.get()
        if not namesearch:
            namesearch = None
        conn = mysqlc.Connect(**loginInfo)
        curs = conn.cursor()
        table = "testMessage"
        self.msglist = msgs(conn, curs, table, mindate = mindate, maxdate = maxdate, addsearch = addsearch, namesearch = namesearch)
        self.msgsubs.delete(0, END)
        for pk, msg in self.msglist:
            self.msgsubs.insert(END, msg['subject'])
    
    def displayMail(self, event):
        """
        Display the message corresoponding to the subject line the
        user just clicked on.
        """
        indexes = self.msgsubs.curselection()
        if len(indexes) != 1:
            return
        self.message.delete(1.0, END)
        pk, msg = self.msglist[int(indexes[0])]
        for headerName in "Subject", "Date", "From":
            hdr = msg[headerName]
            if hdr:
                self.message.insert(INSERT, "{0}: {1}\n".format(headerName, hdr))
        self.message.insert(END, "\n")
        if msg.is_multipart():
            self.message.insert(END, "MULTIPART MESSAGE - SORRY!")
        self.message.insert(END, msg.get_payload())
        
if __name__ == "__main__":
    root = Tk()
    app = Application(master = root)
    app.searchMail()
    app.mainloop()
        