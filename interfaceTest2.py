from tkinter import *
from tkinter import filedialog, Text, Tk
import math
from resources.scriptMiner import ScriptMiner


class Application(ScriptMiner):
    def __init__(self, master=None):
        self.fonte = ("Verdana", "12")

        self.container = Frame(master)
        self.container["pady"] = 10
        self.container.pack(side="top", fill="both", expand=False) 
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)
   
        self.frames = {}

        for F in (StartPage, ScripEditorMain): #always add the new page class to this loop!
            frame = F(self.container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)
    

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(Application):
    def __init__(self):
        Application.__init__(self, master=None)
        self.lblheader = Label(self.container1, text="Lets get started!", font=self.fonte, width=50) 
        self.lblheader.pack()

        self.btnUpload = Button(self.container2, text="Upload script PDF", font=self.fonte, width=20)
        self.btnUpload["command"] = self.uploadFile() 
        self.btnUpload.pack(side=LEFT)


    def uploadFile(self):

        self.filename = filedialog.askopenfilename(initialdir="/Users/Snades/Desktop/roteiros", title="Select a File", filetypes=(("pdf files", "*pdf"),("all files", ".")))
        path = self.filename

        pdf_path = ScriptMiner(path)
        pdf_text = pdf_path.convert_pdf_to_txt()
        self.scriptBox.insert(INSERT, pdf_text)
    
        button1 = tk.Button(self, text="Visit Page 1", command=lambda: self.show_frame(ScripEditorMain))
        button1.pack()


class ScripEditorMain(Application):
    def __init__(self):
        Application.__init__(self, master=None)
        self.lblheader = Label(self.container1, text="Lets get started!", font=self.fonte, width=50) 
        self.lblheader.pack()

     
        self.scriptBox = Text(self.container3)
        self.scriptBox.config(state="normal")
        self.scriptBox.place(width=70, height=200)
        self.scriptBox["font"] =( "Courier New", "12") 
        self.scriptBox.grid(sticky="nsew")

root = Tk()
Application(root)
root.mainloop()