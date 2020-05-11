from tkinter import *
from tkinter import filedialog, Text, Tk
import math
from resources.scriptMiner import ScriptMiner


class Application(ScriptMiner):
    def __init__(self, master=None):
        self.fonte = ("Verdana", "12")

        self.container1 = Frame(master)
        self.container1.pack(side=TOP)
        self.container1.grid_rowconfigure(0, weight=1)
        self.container1.grid_columnconfigure(0, weight=1)
   
    
        self.container2 = Frame(master)
        self.container2["pady"] = 10
        self.container2.pack(side=RIGHT)
        self.container2.grid_rowconfigure(0, weight=1)
        self.container2.grid_columnconfigure(0, weight=1)
        
        self.container3 = Frame(master)
        self.container3["pady"] = 10
        self.container3["padx"] = 100
        self.container3.pack(side=LEFT)
        self.container3.grid_rowconfigure(0, weight=1)
        self.container3.grid_columnconfigure(0, weight=1)

        self.container4 = Frame(master)
        self.container4["pady"] = 10
        self.container4["padx"] = 100
        self.container4.pack(side=LEFT)
        self.container4.grid_rowconfigure(0, weight=1)
        self.container4.grid_columnconfigure(0, weight=1)
        

        self.file = Button
        
        self.lblheader = Label(self.container1, text="Lets get started!", font=self.fonte, width=50) 
        self.lblheader["pady"] = 30
        self.lblheader.pack()

        self.btnUpload = Button(self.container1, text="Upload script PDF", font=self.fonte, width=20)
        self.btnUpload["command"] = self.uploadFile
        self.btnUpload.pack()
     
        self.scriptBox = Text(self.container2)
        self.scriptBox.config(state="normal")
        self.scriptBox.place(width=50, height=200)
        self.scriptBox["font"] =( "Courier New", "12") 
        self.scriptBox.pack(side=RIGHT)

        self.scenesBox = Text(self.container3)
        self.scenesBox.config(state="normal")
        self.scenesBox.place(width=5, height=200)
        self.scenesBox["font"] =( "Courier New", "10", "bold")
        self.scenesBox.pack(side=LEFT)

        self.btnScenes = Button(self.container4, text="Scenes", font=self.fonte, width=15, pady=5)
        self.btnScenes["command"] = self.scenes
        self.btnScenes.pack()

        self.btnWorkflow = Button(self.container4, text="Workflow", font=self.fonte, width=15, pady=5)
        self.btnWorkflow["command"] = self.goToWorkflow
        self.btnWorkflow.pack()

        self.btnClassifyElements = Button(self.container4, text="Classify", font=self.fonte, width=15, pady=5)
        self.btnClassifyElements["command"] = self.classifyWindow
        self.btnClassifyElements.pack()
      
        
    def uploadFile(self):

        self.filename = filedialog.askopenfilename(initialdir="/Users/Snades/Desktop/roteiros", title="Select a File", filetypes=(("pdf files", "*pdf"),("all files", ".")))
        self.lblheader["text"] = "Good work on " + self.filename
        path = self.filename

        pdf_path = ScriptMiner(path)
        pdf_text = pdf_path.convert_pdf_to_txt()
        pdf_scenes = pdf_path.scenesHeaderNumbered()

        self.scriptBox.insert(INSERT, pdf_text)
        
        for scene in pdf_scenes:
            self.scenesBox.insert(INSERT, scene)
            self.scenesBox.insert(INSERT, "\n")



    def scenes(self):
        pass

    def goToWorkflow(self):
        pass

    def classifyWindow(self):
        pass
        

root = Tk()
root.title('Simulation App - Project Screenplay Analytics')
root.iconbitmap('C:/Users/Snades/apps/project_movieScript/imagens/logo.ico')
root.geometry("1200x700")
Application(root)
root.mainloop()