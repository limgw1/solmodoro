from tkinter import *

#Load settings window
def loadSettings():
  settingsWindow.geometry("500x500")
  settingsWindow = Toplevel()
  settingsWindow.title('Settings')

  #Variables
  options = ["rain_and_thunder.mp3", "lofi_hiphop_beats.mp3", "white_noise.mp3"] #Placeholder for now, I think need to read a json file when uploading real .mp3 files
  vardrop1 = StringVar() #StringVar() is specific to tkinter
  vardrop2 = StringVar() #StringVar() is specific to tkinter
  vardrop3 = StringVar() #StringVar() is specific to tkinter
  vardrop4 = StringVar() #StringVar() is specific to tkinter
  vardrop1.set(options[0])
  vardrop2.set(options[0])
  vardrop3.set(options[0])
  vardrop4.set(options[0])

  firstLabel = Label(settingsWindow, text="Study Session BGM: ").grid(row=0, column=0, columnspan=5, rowspan=2)
  drop1 = OptionMenu(settingsWindow, vardrop1, *options).grid(row=2, column=0, columnspan=2)
  drop2 = OptionMenu(settingsWindow, vardrop2, *options).grid(row=3, column=0, columnspan=2)
  firstStudyWidget = Scale(settingsWindow, from_=0, to=100, orient=HORIZONTAL).grid(row=2, column=2, columnspan=3)
  secondStudyWidget = Scale(settingsWindow, from_=0, to=100, orient=HORIZONTAL).grid(row=3, column=2, columnspan=3)
  secondLabel = Label(settingsWindow, text="Break Session BGM: ").grid(row=4, column=0, columnspan=5, rowspan=2)
  drop3 = OptionMenu(settingsWindow, vardrop3, *options).grid(row=6, column=0, columnspan=2)
  drop4 = OptionMenu(settingsWindow, vardrop4, *options).grid(row=7, column=0, columnspan=2)
  firstStudyWidget = Scale(settingsWindow, from_=0, to=100, orient=HORIZONTAL).grid(row=6, column=2, columnspan=3)
  secondStudyWidget = Scale(settingsWindow, from_=0, to=100, orient=HORIZONTAL).grid(row=7, column=2, columnspan=3)
  saveButton = Button(settingsWindow, text="Save Settings").grid(row=8, column=1, columnspan=3)
  exitButton = Button(settingsWindow, text="Exit", command=settingsWindow.destroy).grid(row=8, column=4, columnspan=1)
