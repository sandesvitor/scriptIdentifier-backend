from tkinter import *
import tkinter as tk
from tkinter import filedialog
from resources.scriptMiner import ScriptMiner


FONTE_PADRAO = ("Verdana", "10", "bold")


class StartPage:
    def __init__(self, master):
        self.frameStartPage = Frame(master, bg="gray79", height=690, width=1100)
        self.label = Label(self.frameStartPage, text="Start Page", font=FONTE_PADRAO, pady= 50, padx=50)
        self.label.pack()

        self.button1 = Button(self.frameStartPage, text="Visit Page 1", command=lambda: raise_frame(framePageOne))
        self.button1.pack()
    
    def getFrame(self):
        return self.frameStartPage


class PageOne:
    def __init__(self, master):
        self.framePageOne = Frame(master, bg="gray79", height=690, width=1100)
        self.label = Label(self.framePageOne, text="Page One", font=FONTE_PADRAO, pady=50, padx=50)
        self.label.pack(side=TOP, fill=BOTH, expand=True)

    def getFrame(self):
        return self.framePageOne

class GerenciadorRoteiro:
    def __init__(self, master):
        self.frameGerenciadorRoteiro = Frame(master)

        self.options_list = [0]


        # Corrigir formatação do texto!!!           
        self.txtcanvas = Text(self.frameGerenciadorRoteiro, height=45, width=50, bg="old lace", bd = 8, relief=RAISED)
        self.txtcanvas.config(state="normal")
        self.txtcanvas["font"] = ( "Courier New", "12") 
        self.txtcanvas["pady"] = 53
        self.txtcanvas["padx"] = 50
        self.txtcanvas.pack(side=TOP)
        #self.verticalSlider = Scale(self.scriptBox, from_=0, to=200)
    
    def novoRoteiro(self):
        filename = filedialog.askopenfilename(initialdir="/Users/Snades/Desktop/roteiros", title="Select a File", filetypes=(("pdf files", "*pdf"),("all files", ".")))
        path = filename

        pdf_path = ScriptMiner(path)
        pdf_text = pdf_path.convert_pdf_to_txt()
        pdf_scenes = pdf_path.scenesHeaderNumbered()

        self.txtcanvas.insert(INSERT, pdf_text)

        self.options_list = pdf_scenes 

        self.clicked = StringVar()
        self.clicked.set(self.options_list[0])
        self.drop = OptionMenu(self.frameGerenciadorRoteiro, self.clicked, *self.options_list)
        self.drop.pack(side=TOP)

        return path
     
    def getFrame(self):
        return self.frameGerenciadorRoteiro



####################################################
############   MASTER FRAME (ROOT)  ################

def raise_frame(frame):
    frame.tkraise()


def newWindow(master):
    objFunc = GerenciadorRoteiro(master)

    new_window = Tk()
    new_window.title("New Project")
    new_window.geometry("450x230+450+475")
    new_window.resizable(width=False, height=False)

    lblnew = Label(new_window, text="Nome do Projeto", font=("Arial", "13", "bold"), pady=30, padx=50)
    lblnew.grid(row=0, column=0)
    
    entrynew = Entry(new_window, width=30)
    entrynew.grid(row=1, column=0)
    
    separador = Canvas(new_window, bg="grey", bd=1, width=2, height=200, relief=SOLID)
    separador.grid(row=0, column=1, rowspan=3)

    lblAdd_roteiro = Label(new_window, text="Importe o pdf", pady=30)
    lblAdd_roteiro.grid(row=1, column=2)

    add_roteiro = Button(new_window, text="+ Adicionar Roteiro", font=("Arial", "10", "bold"), pady=30, padx=50, command=lambda: objFunc.novoRoteiro)
    add_roteiro.grid(row=0, column=2)
    
    btnContinuar = Button(new_window, text="Continuar", font=("Arial", "10", "bold"), pady=15, padx=50, command=lambda: new_window.destroy())
    btnContinuar.grid(row=2, column=2)



root = Tk()
root.title("Screenplay Analytics - v 0.1")
root.iconbitmap('C:/Users/Snades/apps/project_movieScript/imagens/logo.ico')
root.geometry("1300x950+0+0")  

                
topTab = Frame(root, bd=4, bg="white", relief=RAISED, width=1000, height=80, pady=30)
leftTab = Frame(root, bd=4, bg="PaleTurquoise1", relief=RAISED, width=50, height=1000, padx=1)
workspace = Frame(root, bg="gray79", height=690, width=1100, bd=10, relief=SUNKEN)

topTab.pack(side=TOP, fill=BOTH, expand=True)
leftTab.pack(side=LEFT, fill=BOTH, expand=False)
workspace.pack(side=RIGHT, fill=BOTH, expand=1)


tabProject = Label(topTab, text="PROJETOS", font=("Verdana", "10", "italic"), width=10, height=2, padx=30)
tabProject.pack(side=LEFT)

tabContacts = Label(topTab, text="CONTATOS", font=("Verdana", "10", "italic"), width=10, height=2, padx=30)
tabContacts.pack(side=LEFT)

tabProdutora = Label(topTab, text="PRODUTORA", font=("Verdana", "10", "italic"), width=10, height=2, padx=30)
tabProdutora.pack(side=LEFT)

newProject = Button(topTab, text="+ New Project", font=FONTE_PADRAO, width=30, height=4, bd=5, bg="coral3", relief=RAISED)
newProject["command"] = lambda: newWindow(workspace)
newProject.pack(side=RIGHT)




my_menu = Menu(root)
root.config(menu=my_menu)


file_menu = Menu(my_menu)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New Project", command=lambda: newWindow(workspace))
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

"""
workspace properties:
bg="gray79", height=690, width=1100, bd=10, relief=SUNKEN
"""


startPageObj = StartPage(workspace)
pageOneObj = PageOne(workspace)
roteiroObj = GerenciadorRoteiro(workspace)

frameStartPage = startPageObj.getFrame()
framePageOne = pageOneObj.getFrame()
frameRoteiro = roteiroObj.getFrame()


for frame in (frameStartPage, framePageOne, frameRoteiro): #always add the new page class to this loop!
            frame.grid(row=0, column=0, sticky="news")



###############################################
############   MAIN PROGRAM   #################

raise_frame(frameStartPage)    
root.mainloop()
