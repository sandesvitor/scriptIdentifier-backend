from tkinter import *
from tkinter import filedialog
from resources.scriptMiner import ScriptMiner

root = Tk()
root.title("Screenplay Analytics")
root.iconbitmap('C:/Users/Snades/apps/project_movieScript/imagens/logo.ico')
#root.geometry("800x800")


            

class Tabs:
    def __init__(self, master):
        self.fonte = ("Verdana", "12", "bold")
        
        self.topTab = Frame(master)
        self.leftTab = Frame(master)
        self.workspace = Frame(master)

        self.topTab.pack(side=TOP)
        self.leftTab.pack(side=LEFT)
        self.workspace.pack(side=RIGHT)

        self.lblTop = Label(self.topTab, text="TOP TAB", font=self.fonte)
        self.lblLeft = Label(self.leftTab, text="LEFT TAB", font=self.fonte)
        self.lblTop.pack()
        self.lblLeft.pack()
        

        app = GerenciadorRoteiro(self.workspace)
        

class GerenciadorRoteiro(Tabs):
    def __init__(self, parent=None):
        # Inicializadores Padrão:
        self.parent = parent
        self.fonte = ("Verdana", "12", "bold")
        self.options_list = [0]

        self.lblWorkspace = Canvas(self.parent, bg="grey", height=700, width=1000)
        self.lblWorkspace.pack()

                   
        self.scriptBox = Text(self.lblWorkspace, height=25, width=38)
        self.scriptBox.config(state="normal")
        self.scriptBox["font"] = ( "Courier New", "12") 
        self.scriptBox["pady"] = 30
        self.scriptBox["padx"] = 20
        self.scriptBox.pack()
        #self.verticalSlider = Scale(self.scriptBox, from_=0, to=200)
    
    def openFile(self):
        filename = filedialog.askopenfilename(initialdir="/Users/Snades/Desktop/roteiros", title="Select a File", filetypes=(("pdf files", "*pdf"),("all files", ".")))
        path = filename

        pdf_path = ScriptMiner(path)
        pdf_text = pdf_path.convert_pdf_to_txt()
        pdf_scenes = pdf_path.scenesHeaderNumbered()

        self.scriptBox.insert(INSERT, pdf_text)

        self.options_list = pdf_scenes 

        self.clicked = StringVar()
        self.clicked.set(self.options_list[0])
        self.drop = OptionMenu(self.parent, self.clicked, *self.options_list)
        self.drop.pack(side=TOP)
      
        


tabs = Tabs(root)


my_menu = Menu(root)
root.config(menu=my_menu)


file_menu = Menu(my_menu)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New File")
file_menu.add_command(label="Open File", command=app.openFile)
file_menu.add_command(label="Save")
file_menu.add_separator()
file_menu.add_command(label="Open WorkSpace")
file_menu.add_command(label="Quit", command=root.quit)


edit_menu = Menu(my_menu)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Undo    (Ctrl + Z)")
edit_menu.add_command(label="Redo    (Ctrl + Y)")
edit_menu.add_separator()
edit_menu.add_command(label="Cut     (Ctrl + X)")
edit_menu.add_command(label="Copy    (Ctrl + C)")
edit_menu.add_command(label="Paste   (Ctrl + V)")
edit_menu.add_command(label="Undo    (Ctrl + Z)")
edit_menu.add_command(label="Find    (Ctrl + F)")
edit_menu.add_command(label="Replace (Ctrl + H)")



root.mainloop()