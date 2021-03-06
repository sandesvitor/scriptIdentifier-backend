from tkinter import *
import tkinter as tk
from tkinter import filedialog
from resources.scriptMiner import ScriptMiner


FONTE_PADRAO = ("Verdana", "10", "bold")


####################################################
############   CLASS DEFINITIONS  ##################

class StartPage:
    def __init__(self, master):
        self.frameStartPage = Frame(master, bg="gray79", height=690, width=1100)
        self.label = Label(self.frameStartPage, text="Escrivaninha de Projetos\n(para começar, por favor crie uma nova pasta de projetos)", bg="gray79", font=("Courier New", "16", "bold"), pady= 20, padx=50)
        self.label.pack(fill=BOTH, expand=0)

        self.button1 = Button(self.frameStartPage, text="Primeiro Projeto", state=NORMAL,command=lambda: self.firstProject())
        self.button1.pack()
    
    def firstProject(self):
        newWindow()
        self.button1.destroy

    def getFrame(self):
        return self.frameStartPage


class PageOne:
    def __init__(self, master):
        self.framePageOne = Frame(master, bg="black", height=690, width=1100)
        #self.label = Label(self.framePageOne, text="Page One", font=FONTE_PADRAO, pady=50, padx=50)
        #self.label.pack(fill=BOTH, expand=True)

    def getFrame(self):
        return self.framePageOne


class GerenciadorRoteiro:
    def __init__(self, master):
        self.frameGerenciadorRoteiro = Frame(master)
        self.frameGerenciadorRoteiro.grid_columnconfigure(0, minsize=400)
        self.frameGerenciadorRoteiro.grid_columnconfigure(1, minsize=400)
        self.frameGerenciadorRoteiro.grid_columnconfigure(3, minsize=600)

        self.options_list = ["Lista de Cenas"]

        # Corrigir formatação do texto!!!           
        self.txtcanvas = Text(self.frameGerenciadorRoteiro, height=45, width=50, bg="old lace", bd = 8, relief=RAISED)
        self.txtcanvas.config(state="normal")
        self.txtcanvas["font"] = ("Courier New", "12") 
        self.txtcanvas["pady"] = 10
        self.txtcanvas["padx"] = 10
        self.txtcanvas.grid(row=0, column=3)
        
        self.verticalSlider = Scale(self.frameGerenciadorRoteiro, from_=0, to=1000)
        self.verticalSlider.grid(row=0, column=4)

        self.clicked = StringVar()
        self.clicked.set(self.options_list[0])
        self.drop = OptionMenu(self.frameGerenciadorRoteiro, self.clicked, *self.options_list)
        self.drop.grid(row=0, column=1, rowspan=2)
        self.drop.grid_columnconfigure(1, weight=1)

        self.sceneBox = Text(self.frameGerenciadorRoteiro, height=30, width=48, bg="white", bd = 8, relief=RAISED)
        self.sceneBox.config(state="normal")
        self.sceneBox["font"] = ("Courier New", "10", "bold") 
        self.sceneBox["pady"] = 10
        self.sceneBox["padx"] = 10
        self.sceneBox.grid(row=0, column=1, rowspan=2)
        self.sceneBox.grid_columnconfigure(1, weight=1)

        

    def novoRoteiro(self):
        filename = filedialog.askopenfilename(initialdir="/Users/Snades/Desktop/roteiros", title="Select a File", filetypes=(("pdf files", "*pdf"),("all files", ".")))
        path = filename

        pdf_path = ScriptMiner(path)
        pdf_text = pdf_path.convert_pdf_to_txt()
        pdf_scenes = pdf_path.scenesHeaderNumbered()

        # Remover cabeçalho e rodapé do pdf!!!

        self.txtcanvas.insert(INSERT, pdf_text) 
        self.sceneBox.insert(INSERT, pdf_scenes)   

        self.options_list = pdf_scenes 

        return path

    def getFrame(self):
        return self.frameGerenciadorRoteiro



####################################################
############   MASTER FRAME (ROOT)  ################

root = Tk()
root.title("Screenplay Analytics - v 0.1")
root.iconbitmap('C:/Users/Snades/apps/project_movieScript/imagens/logo.ico')
root.geometry("1500x1100+0+0")  

                
topTab = Frame(root, bd=4, bg="white", relief=RAISED, width=1000, height=80, pady=30)
leftTab = Frame(root, bd=4, bg="PaleTurquoise1", relief=RAISED, width=50, height=1000, padx=1)
workspace = Frame(root, bg="gray79", height=690, width=1100, bd=10, relief=SUNKEN)

topTab.pack(side=TOP, fill=BOTH, expand=True)
leftTab.pack(side=LEFT, fill=BOTH, expand=False)

workspace.pack(side=RIGHT, fill=BOTH, expand=1)
workspace.grid_rowconfigure(0, weight=1)
workspace.grid_columnconfigure(0, weight=1)


#############################################
###########   NEW PROJECT   #################
roteiroObj = GerenciadorRoteiro(workspace)


def raise_frame(frame):
    frame.tkraise()


def sequence(*functions):
    def func(*args, **kwargs):
        return_value = None
        for function in functions:
            return_value = function(*args, **kwargs)
        return return_value
    return func

def newWindow():

    new_window = Tk()
    new_window.attributes("-topmost", True)
    new_window.title("New Project")
    new_window.iconbitmap('C:/Users/Snades/apps/project_movieScript/imagens/logo.ico')
    new_window.geometry("520x230+450+475")
    new_window.resizable(width=False, height=False)

    lblNewProject = Label(new_window, text="Nome do Projeto", font=("Arial", "13", "bold"), pady=30, padx=50)
    lblNewProject.grid(row=0, column=0)
    
    entryNewProject = Entry(new_window, width=30)
    entryNewProject.grid(row=1, column=0)
    
    separador_barra = Canvas(new_window, bg="grey", bd=1, width=2, height=200, relief=RAISED)
    separador_barra.grid(row=0, column=1, rowspan=3)

    lblAddRoteiro = Label(new_window, text="Importe o pdf", pady=30)
    lblAddRoteiro.grid(row=1, column=2)

    def alterLbl():
        new_window.attributes("-topmost", False)
        lblAddRoteiro["text"] = roteiroObj.novoRoteiro()
        new_window.attributes("-topmost", True)
        btnContinuar["state"] = NORMAL

    btnAddRoteiro = Button(new_window, text="+ Adicionar Roteiro", font=("Arial", "10", "bold"), pady=30, padx=50, command=lambda: alterLbl())
    btnAddRoteiro.grid(row=0, column=2)

    btnContinuar = Button(new_window, text="Continuar", font=("Arial", "10", "bold"), state=DISABLED, pady=15, padx=50, command=lambda:sequence(raise_frame(frameRoteiro), new_window.destroy()))
    btnContinuar.grid(row=2, column=2)


#############################################
#########  HIGH HIERARCHY WIDGETS  ##########


tabProject = Label(topTab, text="PROJETOS", font=("Verdana", "10", "italic"), width=10, height=2, padx=30)
tabProject.pack(side=LEFT)

tabContacts = Label(topTab, text="CONTATOS", font=("Verdana", "10", "italic"), width=10, height=2, padx=30)
tabContacts.pack(side=LEFT)

tabProdutora = Label(topTab, text="PRODUTORA", font=("Verdana", "10", "italic"), width=10, height=2, padx=30)
tabProdutora.pack(side=LEFT)

newProject = Button(topTab, text="+ New Project", font=FONTE_PADRAO, width=30, height=4, bd=5, bg="coral3", relief=RAISED)
newProject["command"] = lambda: newWindow()
newProject.pack(side=RIGHT)



my_menu = Menu(root)
root.config(menu=my_menu)


file_menu = Menu(my_menu)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New Project", command=lambda: newWindow())
file_menu.add_command(label="Open Project")
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

help_menu = Menu(my_menu)
my_menu.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="Welcome")
help_menu.add_command(label="Documentation")
help_menu.add_command(label="About")


###############################################
############    CHILD FRAMES   ################


startPageObj = StartPage(workspace)
pageOneObj = PageOne(workspace)


frameStartPage = startPageObj.getFrame()
framePageOne = pageOneObj.getFrame()
frameRoteiro = roteiroObj.getFrame()


for frame in (frameStartPage, framePageOne, frameRoteiro): #always add the new page class to this loop!
            frame.grid(row=0, column=0, sticky="news")



###############################################
############   MAIN PROGRAM   #################

raise_frame(frameStartPage)    
root.mainloop()
