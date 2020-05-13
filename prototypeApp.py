from tkinter import *
import tkinter
from tkinter import filedialog
from resources.scriptMiner import ScriptMiner

root = Tk()
root.title("Screenplay Analytics - v 0.1")
root.iconbitmap('C:/Users/Snades/apps/project_movieScript/imagens/logo.ico')
root.geometry("1300x950+100+0")
#root.resizable(width=False, height=False)


FONTE_PADRAO = ("Verdana", "12", "bold")

class Tabs:
    def __init__(self, master):
        ###### INICIALIZADORES PADRÃO ######
                
        self.topTab = Frame(master, bd=4, bg="white", relief=RAISED, width=1000, height=80, pady=30)
        self.leftTab = Frame(master, bd=4, bg="PaleTurquoise1", relief=RAISED, width=50, height=1000, padx=1)
        self.workspace = Frame(master, bg="gray79", height=690, width=1100, bd=10, relief=SUNKEN)

        self.topTab.pack(side=TOP, fill=BOTH, expand=True)
        self.leftTab.pack(side=LEFT, fill=BOTH, expand=False)
        self.workspace.pack(side=RIGHT, fill=BOTH, expand=1)


        self.tabProject = Label(self.topTab, text="PROJETOS", font=("Verdana", "10", "italic"), width=10, height=2, padx=30)
        self.tabProject.pack(side=LEFT)

        self.tabContacts = Label(self.topTab, text="CONTATOS", font=("Verdana", "10", "italic"), width=10, height=2, padx=30)
        self.tabContacts.pack(side=LEFT)

        self.tabProdutora = Label(self.topTab, text="PRODUTORA", font=("Verdana", "10", "italic"), width=10, height=2, padx=30)
        self.tabProdutora.pack(side=LEFT)


def raiseFrame(self, frame):
    frame.tkraise()
   
class TabProjetos(Tabs):
    def __init__(self, master):
        self.frameMaster = master

        self.frameChild = Frame(self.frameMaster)

        self.labeltest = Label(self.frameChild, text="PROJETOS FUNCIONANDO", font=FONTE_PADRAO)
        self.labeltest.pack()
        

class TabContatos(Tabs):
    def __init__(self, master):
        self.frameMaster = master

        self.frameChild = Frame(self.frameMaster)

        self.labeltest = Label(self.frameChild, text="CONTATOS FUNCIONANDO", font=FONTE_PADRAO)
        self.labeltest.pack()


class TabProdutora(Tabs):
    def __init__(self, master):
        pass



class GerenciadorRoteiro(Tabs):
    def __init__(self, master):
        self.master = master

        self.frameChild = Frame(self.master)

        self.options_list = [0]


        # Corrigir formatação do texto!!!           
        self.txtcanvas = Text(self.frameChild, height=45, width=50, bg="old lace", bd = 8, relief=RAISED)
        self.txtcanvas.config(state="normal")
        self.txtcanvas["font"] = ( "Courier New", "12") 
        self.txtcanvas["pady"] = 53
        self.txtcanvas["padx"] = 50
        self.txtcanvas.pack()
        #self.verticalSlider = Scale(self.scriptBox, from_=0, to=200)
    
    def novoRoteiro(self):
        filename = filedialog.askopenfilename(initialdir="/Users/Snades/Desktop/roteiros", title="Select a File", filetypes=(("pdf files", "*pdf"),("all files", ".")))
        path = filename

        pdf_path = ScriptMiner(path)
        pdf_text = pdf_path.convert_pdf_to_txt()
        pdf_scenes = pdf_path.scenesHeaderNumbered()

        self.scriptBox.insert(INSERT, pdf_text)

        self.options_list = pdf_scenes 

        self.clicked = StringVar()
        self.clicked.set(self.options_list[0])
        self.drop = OptionMenu(self.master, self.clicked, *self.options_list)
        self.drop.pack(side=TOP)


class AnaliseTecnica(TabProjetos):
    def __init__(self, master):
        pass

class PlanoDeFilmagem(TabProjetos):
    def __init__(self, master):
        pass

class StoryBoard(TabProjetos):
    def __init__(self, master):
        pass

class OrdemDoDia(TabProjetos):
    def __init__(self, master):
        pass

class Calendario(TabProjetos):
    def __init__(self, master):
        pass

class Equipe(TabProjetos):
    def __init__(self, master):
        pass
        





my_menu = Menu(root)
root.config(menu=my_menu)


file_menu = Menu(my_menu)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New Project")
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



##########  MAIN PROGRAM  ##########
def raiseFrame(frame):
    frame.tkraise()


tabs = Tabs(root)
new_root = tabs.workspace

frameProjetos = TabProjetos(new_root).frameChild
frameContatos = TabContatos(new_root).frameChild
frameRoteiro = GerenciadorRoteiro(new_root).frameChild


for frame in (frameProjetos, frameContatos, frameRoteiro):
    frame.pack()


raiseFrame(frameProjetos)




root.mainloop()