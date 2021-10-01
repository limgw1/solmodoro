from tkinter import *
from loadSettings import loadSettings

root = Tk()
root.geometry("500x500")

#Menu code
my_menu = Menu(root)
root.config(menu=my_menu)
root.title('Solmodoro Timer')
# root.iconbitmap('C:\Users\Diana\Desktop\mywebsite\images\solmi.png')

#File Menu
file_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Set New Pomodoro Timer")
file_menu.add_command(label="Quit", command=root.quit)

#Edit Menu
edit_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="BGM Settings", command=loadSettings)
edit_menu.add_command(label="GUI Settings")

#Help Menu
help_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="Guide")


#Code
studyLabel = Label(root, text="Study duration (mins): ").grid(row=0, column=1)
breakLabel = Label(root, text="Break duration (mins): ").grid(row=2, column=1)

studyEntry = Entry(root).grid(row=1, column=1)
breakEntry = Entry(root).grid(row=3, column=1)

startButton = Button(root, text="Begin session").grid(row=4, column=0, columnspan=5)


root.mainloop()