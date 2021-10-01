from tkinter import *
import time

root = Tk()

def endSession():
  # TODO Stops the endless timer in beginSession
  # TODO Maybe? Record to an excel sheet
  pass

def beginSession(studyEntry, breakEntry):
  studyDuration = 0 #Store study timer
  breakDuration = 0 #Store break timer

  startTime = time.time()
  time.sleep(studyEntry*60)
  endTime = time.time()


studyLabel = Label(root, text="Study duration").grid(row=0)
breakLabel = Label(root, text="Break duration").grid(row=1)

studyEntry = Entry(root).grid(row=0, column=1)
breakEntry = Entry(root).grid(row=1, column=1)

startButton = Button(root, text="Begin session", command=beginSession).grid(row=2, column=0)
endButton = Button(root, text="End session", command=endSession).grid(row=2, column=1)

root.mainloop()