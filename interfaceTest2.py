from tkinter import *

root = Tk()
root.title('Simulation App - Project Screenplay Analytics')
root.iconbitmap('C:/Users/Snades/apps/project_movieScript/imagens/logo.ico')
root.geometry("1200x700")


my_menu = Menu(root)
root.config(menu=my_menu)

# Click "New..."
def our_command():
    pass


# Create a menu item
file_menu = Menu(my_menu)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New File", command=our_command)
file_menu.add_command(label="Save", command=our_command)
file_menu.add_separator()
file_menu.add_command(label="Open WorkSpace", command=our_command)
file_menu.add_command(label="Quit", command=root.quit)

# Create edit menu item
edit_menu = Menu(my_menu)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Undo    (Ctrl + Z)", command=our_command)
edit_menu.add_command(label="Redo    (Ctrl + Y)", command=our_command)
file_menu.add_separator()
edit_menu.add_command(label="Cut     (Ctrl + X)", command=our_command)
edit_menu.add_command(label="Copy    (Ctrl + C)", command=our_command)
edit_menu.add_command(label="Paste   (Ctrl + V)", command=our_command)
edit_menu.add_command(label="Undo    (Ctrl + Z)", command=our_command)
edit_menu.add_command(label="Find    (Ctrl + F)", command=our_command)
edit_menu.add_command(label="Replace (Ctrl + H)", command=our_command)

root.mainloop()
