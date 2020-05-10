from tkinter import *
import tkinter
from tkinter import messagebox
from resources.scriptMiner import ScriptMiner


class Application():
    def __init__(self, master=None):
        self.fonte = ("Verdana", "12")

        self.container1 = Frame(master)
        self.container1["pady"] = 20
        self.container1.pack(side="top", fill="both", expand=True) 
        self.container1.grid_rowconfigure(0, weight=1)
        self.container1.grid_columnconfigure(0, weight=1)

        self.container2 = Frame(master)
        self.container2["pady"] = 30
        self.container2.pack()
        self.container2.grid_rowconfigure(0, weight=1)
        self.container2.grid_columnconfigure(0, weight=1) 

        self.lblheader = Label(self.container1, text="Lets get started!", font=self.fonte, width=50) 
        self.lblheader.pack()

        self.btnUpload = Button(self.container2, text="Upload script PDF", font=self.fonte, width=20)
        self.btnUpload["command"] = self.getFile_nextStep
        self.btnUpload.pack(side=LEFT)

        
    def getFile_nextStep(self):
        tkinter.messagebox.showinfo("Debugging", "Tudo certo até aqui.")    
        

root = Tk()
Application(root)
root.mainloop()