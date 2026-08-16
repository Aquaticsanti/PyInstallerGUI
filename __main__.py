from tkinter import *
from tkinter.filedialog import *
from tkinter.ttk import *

# create root window
root = Tk()



root.title("PyInstallerGUI")
root.geometry('700x400')
root.resizable(False, False)


def openScript():
    global scriptLocationEntry
    file = askopenfile()
    scriptLocationEntry.delete(0, -1)
    scriptLocationEntry.insert(0, file.name)

scriptLocationFrame = Frame(root)
scriptLocationFrame.pack(side=TOP)

scriptLocationLabel = Label(scriptLocationFrame, text="Script File:")
scriptLocationLabel.pack(side=LEFT, anchor=N)

scriptLocationEntry = Entry(scriptLocationFrame, width=90)
scriptLocationEntry.pack(side=LEFT, anchor=N)

scripLocationOpenButton = Button(scriptLocationFrame, text="Open", command=openScript)
scripLocationOpenButton.pack(side=LEFT, anchor=N)



# Execute Tkinter
root.mainloop()