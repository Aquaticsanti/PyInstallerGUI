from tkinter import *
from tkinter.filedialog import *
from tkinter.ttk import *
from PIL import Image, ImageTk

# create root window
root = Tk()



root.title("PyInstallerGUI")
root.geometry('700x400')
root.resizable(False, False)


def openScript():
    global scriptLocationEntry
    file = askopenfile(filetypes=[("Python script file", ".py"), ("PyInstaller spec files", ".spec")])
    if file is None:
        pass
    else:
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


appNameFrame = Frame(root, padding=(15, 25))
appNameFrame.pack(side=TOP, anchor=W)

appNameLabel = Label(appNameFrame, text="App Name:")
appNameLabel.pack(side=LEFT, anchor=N)

appNameEntry = Entry(appNameFrame, width=30)
appNameEntry.pack(side=LEFT, anchor=N)


appLogoFrame = Frame(root, padding=(15, 0))
appLogoFrame.pack(side=TOP, anchor=W)

appLogoLabel = Label(appLogoFrame, text="App Logo:")
appLogoLabel.pack(side=TOP, anchor=N)

def getAppLogo():
    global appLogo, appLogoImage, appLogoButton
    file = askopenfilename(filetypes=[("Icon files", ".ico"), ("Image files", ".png .jpg .jpeg .webp .bmp .gif")])
    if file is not None:
        appLogo = file
        appLogoImage = ImageTk.PhotoImage(Image.open(appLogo).resize((160, 160)))
        appLogoButton.config(image=appLogoImage)
appLogo = "pyinstaller-default.png"
appLogoImage = ImageTk.PhotoImage(Image.open(appLogo).resize((160, 160)))
appLogoButton = Button(appLogoFrame, image=appLogoImage, compound=CENTER, text="", command=getAppLogo)
appLogoButton.pack(side=TOP, anchor=N, ipadx=40, ipady=40)

# Execute Tkinter
root.mainloop()