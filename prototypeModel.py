from tkinter import *
from tkinter import filedialog
from resources.scriptMiner import ScriptMiner

root = Tk()
root.title("Screenplay Analytics")
root.iconbitmap('C:/Users/Snades/apps/project_movieScript/imagens/logo.ico')
#root.geometry("800x800")


class Tabs:
    def __init__(self, master=None):
        self.fonte = ("Verdana", "12", "bold")
        
        self.topTab = Frame(master)
        self.leftTab = Frame(master)
        self.workspace = Frame(master)

        self.topTab.pack(side=TOP)
        self.leftTab.pack(side=LEFT)
        self.workspace.pack()

        self.lblTop = Label(self.topTab, text="TOP TAB", font=self.fonte)
        self.lblLeft = Label(self.leftTab, text="LEFT TAB", font=self.fonte)
        self.lblWorkspace = PanedWindow(self.workspace, bd=100, bg="grey", height=700, width=1000)
        self.lblTop.pack()
        self.lblLeft.pack()
        self.lblWorkspace.pack(anchor="center")


        self.testlbl = Label(self.lblWorkspace, text="CANVAS", font=self.fonte)
        self.testlbl.pack()

"""

class Application(ScriptMiner):
    def __init__(self, master=None):
        # Inicializadores Padrão:
        self.fonte = ("Verdana", "12", "bold")
        self.options_list = [0]

        self.frame_0_0 = Frame(master)
        self.frame_0_1 = Frame(master)
        self.frame_0_2 = Frame(master)

        self.frame_1_0 = Frame(master)
        self.frame_1_1 = Frame(master)
        self.frame_1_2 = Frame(master)

        self.frame_2_0 = Frame(master)
        self.frame_2_1 = Frame(master)
        self.frame_2_2 = Frame(master)
        
        self.frame_0_0.grid(row=0, column=0)
        self.frame_0_1.grid(row=0, column=1)
        self.frame_0_2.grid(row=0, column=2)

        self.frame_1_0.grid(row=1, column=0)
        self.frame_1_1.grid(row=1, column=1)
        self.frame_1_2.grid(row=1, column=2)

        self.frame_2_0.grid(row=2, column=0)
        self.frame_2_1.grid(row=2, column=1)
        self.frame_2_2.grid(row=2, column=2)
      


        # Top Frame Widgets:
        self.titulo = Label(self.frame_0_2, text="Screenplay Analytics", font=("Helvetica", "16", "bold"), pady=20, width=30)
        self.titulo.pack()
            
        
        # Middle Frames Widgets 

        self.canvas = Canvas(self.frame_1_1, width=20, height=25, bg="red")
        self.canvas.create_text(100, 10, fill="darkblue", font=self.fonte, text="Click the bubblues")    
        
        
        self.scriptBox = Text(self.frame_1_2, height=25, width=38)
        self.scriptBox.config(state="normal")
        self.scriptBox["font"] = ( "Courier New", "12") 
        self.scriptBox["pady"] = 30
        self.scriptBox["padx"] = 20
        self.scriptBox.pack()
        self.verticalSlider = Scale(self.scriptBox, from_=0, to=200)

        self.scenesBox = Text(self.frame_1_1, height=25, width=30)
        self.scenesBox.config(state="normal")
        self.scenesBox["font"] = ( "Courier New", "12", "bold") 
        self.scenesBox["pady"] = 30
        self.scenesBox["padx"] = 30
        self.scenesBox.pack(side=BOTTOM)

        self.btnScenes = Button(self.frame_1_0, text="Scenes", font=self.fonte, width=15, pady=5)
        self.btnScenes.pack()

        self.btnWorkflow = Button(self.frame_1_0, text="Workflow", font=self.fonte, width=15, pady=5)
        self.btnWorkflow.pack()

        self.btnClassifyElements = Button(self.frame_1_0, text="Classify", font=self.fonte, width=15, pady=5)
        self.btnClassifyElements.pack()


        # Bottom Frame Widgets
        self.botLabel = Label(self.frame_2_1, text="Bottom Frame", font=self.fonte, pady=30, width=30)
        self.botLabel.pack()

        

    # Funções de Application:
    def myFunction(self):
        pass

    def openFile(self):
        self.filename = filedialog.askopenfilename(initialdir="/Users/Snades/Desktop/roteiros", title="Select a File", filetypes=(("pdf files", "*pdf"),("all files", ".")))
        path = self.filename

        pdf_path = ScriptMiner(path)
        pdf_text = pdf_path.convert_pdf_to_txt()
        pdf_scenes = pdf_path.scenesHeaderNumbered()

        self.scriptBox.insert(INSERT, pdf_text)

        self.options_list = pdf_scenes 

        self.clicked = StringVar()
        self.clicked.set(self.options_list[0])
        self.drop = OptionMenu(self.frame_1_1, self.clicked, *self.options_list)
        self.drop.pack(side=TOP)
        
        for scene in pdf_scenes:
            self.scenesBox.insert(INSERT, scene)
            self.scenesBox.insert(INSERT, "\n")



        


app = Application(root)


my_menu = Menu(root)
root.config(menu=my_menu)

file_menu = Menu(my_menu)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New File", command=app.myFunction)
file_menu.add_command(label="Open File", command=app.openFile)
file_menu.add_command(label="Save", command=app.myFunction)
file_menu.add_separator()
file_menu.add_command(label="Open WorkSpace", command=app.myFunction)
file_menu.add_command(label="Quit", command=root.quit)


edit_menu = Menu(my_menu)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Undo    (Ctrl + Z)", command=app.myFunction)
edit_menu.add_command(label="Redo    (Ctrl + Y)", command=app.myFunction)
edit_menu.add_separator()
edit_menu.add_command(label="Cut     (Ctrl + X)", command=app.myFunction)
edit_menu.add_command(label="Copy    (Ctrl + C)", command=app.myFunction)
edit_menu.add_command(label="Paste   (Ctrl + V)", command=app.myFunction)
edit_menu.add_command(label="Undo    (Ctrl + Z)", command=app.myFunction)
edit_menu.add_command(label="Find    (Ctrl + F)", command=app.myFunction)
edit_menu.add_command(label="Replace (Ctrl + H)", command=app.myFunction)

"""


tabs = Tabs(root)
root.mainloop()