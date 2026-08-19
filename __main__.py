from tkinter import *
from tkinter.filedialog import *
from tkinter.ttk import *
from PIL import Image, ImageTk

# create root window
root = Tk()



root.title("PyInstallerGUI")
root.geometry('750x400')
root.resizable(False, False)


def openScript():
    global scriptLocationEntry
    file = askopenfile(filetypes=[("Python script file", ".py"), ("PyInstaller spec files", ".spec")])
    if file is None:
        pass
    else:
        scriptLocationEntry.delete(0, END)
        scriptLocationEntry.insert(0, file.name)

scriptLocationFrame = Frame(root)
scriptLocationFrame.pack(side=TOP)

scriptLocationLabel = Label(scriptLocationFrame, text="Script File:")
scriptLocationLabel.pack(side=LEFT, anchor=N)

scriptLocationEntry = Entry(scriptLocationFrame, width=90)
scriptLocationEntry.pack(side=LEFT, anchor=N)

scripLocationOpenButton = Button(scriptLocationFrame, text="Open", command=openScript)
scripLocationOpenButton.pack(side=LEFT, anchor=N)

notScriptLocationFrame = Frame(root)
notScriptLocationFrame.pack(side=TOP, anchor=W)
appNameFrame = Frame(notScriptLocationFrame, padding=(15, 5))
appNameFrame.grid(column=0, row=0, sticky=N)

appNameLabel = Label(appNameFrame, text="App Name:")
appNameLabel.pack(side=LEFT, anchor=N)

appNameEntry = Entry(appNameFrame, width=30)
appNameEntry.pack(side=LEFT, anchor=N)


appLogoFrame = Frame(notScriptLocationFrame, padding=(0, 0))
appLogoFrame.grid(column=0, row=1, sticky=N)

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



flagsFrame = Frame(notScriptLocationFrame)
flagsFrame.grid(column=1, row=0, rowspan=2, sticky=N)


def getDistFolder():
    global distFolder, distpathEntry
    distFolder = askdirectory()
    if distFolder is None:
            pass
    else:
        distpathEntry.delete(0, END)
        distpathEntry.insert(0, distFolder)

distpathFrame = Frame(flagsFrame)
distpathFrame.grid(column=0, row=0, sticky="w")

distpathLabel = Label(distpathFrame, text="Bundled app destination:")
distpathLabel.pack(side=LEFT)

distpathEntry = Entry(distpathFrame, width=32)
distpathEntry.pack(side=LEFT)

distpathOpenButton = Button(distpathFrame, text="Open", command=getDistFolder)
distpathOpenButton.pack(side=LEFT, anchor=N)


def getWorkFolder():
    global workFolder, workpathEntry
    workFolder = askdirectory()
    if workFolder is None:
            pass
    else:
        workpathEntry.delete(0, END)
        workpathEntry.insert(0, workFolder)

workpathFrame = Frame(flagsFrame)
workpathFrame.grid(column=0, row=1, sticky="w")

workpathLabel = Label(workpathFrame, text="Temporary files destination:")
workpathLabel.pack(side=LEFT)

workpathEntry = Entry(workpathFrame, width=30)
workpathEntry.pack(side=LEFT)

workpathOpenButton = Button(workpathFrame, text="Open", command=getWorkFolder)
workpathOpenButton.pack(side=LEFT, anchor=N)

def getspecFolder():
    global specFolder, specpathEntry
    specFolder = askdirectory()
    if specFolder is None:
            pass
    else:
        specpathEntry.delete(0, END)
        specpathEntry.insert(0, specFolder)

specpathFrame = Frame(flagsFrame)
specpathFrame.grid(column=0, row=2, sticky="w")

specpathLabel = Label(specpathFrame, text=".spec file destination:")
specpathLabel.pack(side=LEFT)

specpathEntry = Entry(specpathFrame, width=36)
specpathEntry.pack(side=LEFT)

specpathOpenButton = Button(specpathFrame, text="Open", command=getspecFolder)
specpathOpenButton.pack(side=LEFT, anchor=N)

noConfirmFrame = Frame(flagsFrame)
noConfirmFrame.grid(column=0, row=3, sticky="w")

noConfirm = BooleanVar(root, False)
noConfirmCheckbox = Checkbutton(noConfirmFrame, variable=noConfirm, text="Replace output directory without confirmation")
noConfirmCheckbox.pack(side=LEFT)


cleanFrame = Frame(flagsFrame)
cleanFrame.grid(column=0, row=4, sticky="w")

clean = BooleanVar(root, False)
cleanCheckbox = Checkbutton(cleanFrame, variable=clean, text="Clean cache and remove temporary files before building")
cleanCheckbox.pack(side=LEFT)


logFrame = Frame(flagsFrame)
logFrame.grid(column=0, row=5, sticky="w")

logLabel = Label(logFrame, text="Log level:")
logLabel.pack(side=LEFT)

logLevel = StringVar(value="INFO")
logOptionsMenu = Combobox(logFrame, textvariable=logLevel, values=["TRACE", "DEBUG", "INFO", "WARN", "DEPRECATION", "ERROR", "FATAL"],
                          state="readonly", width=10)
logOptionsMenu.pack(side=LEFT)

debugFrame = Frame(flagsFrame)
debugFrame.grid(column=0, row=6, sticky="w")

debugLabel = Label(debugFrame, text="Debug level:")
debugLabel.pack(side=LEFT)

debugLevel = StringVar(value="None")
debugOptionsMenu = Combobox(debugFrame, textvariable=debugLevel, values=["None", "All", "Imports", "Bootloader", "NoArchive"],
                          state="readonly", width=10)
debugOptionsMenu.pack(side=LEFT)

bundleTypeFrame = Frame(flagsFrame)
bundleTypeFrame.grid(column=0, row=7, sticky="w")

bundleType = StringVar()

bundleTypeOneFileRadioButton = Radiobutton(bundleTypeFrame, text="One-file bundle", variable=bundleType, value="-F")
bundleTypeOneFileRadioButton.pack(side=TOP, anchor=W)

bundleTypeOnedirectoryRadioButton = Radiobutton(bundleTypeFrame, text="One-folder bundle", variable=bundleType, value="-D")
bundleTypeOnedirectoryRadioButton.pack(side=TOP, anchor=W)



hideConsoleFrame = Frame(flagsFrame)
hideConsoleFrame.grid(column=0, row=9, sticky="w")

hideConsoleLabel = Label(hideConsoleFrame, text="Hide console:")
hideConsoleLabel.pack(side=LEFT)

hideConsoleLevel = StringVar(value="None")
hideConsoleOptionsMenu = Combobox(hideConsoleFrame, textvariable=hideConsoleLevel, values=["None", "Minimize Early", 
                                    "Hide Late", "Minimize Late", "Hide Early"], state="readonly", width=10)
hideConsoleOptionsMenu.pack(side=LEFT)

windowed = BooleanVar(root, False)
noWindowedTraceback = BooleanVar(root, False)
def removeHideConsole():
    global windowed
    if windowed.get() == False:
        hideConsoleFrame.grid(column=0, row=9, sticky="w")
        noWindowedTracebackFrame.grid_remove()
        noWindowedTraceback.set(False)
    else:
        hideConsoleFrame.grid_remove()
        noWindowedTracebackFrame.grid(column=0, row=10, sticky="w")

windowedFrame = Frame(flagsFrame)
windowedFrame.grid(column=0, row=8, sticky="w")

windowedCheckbox = Checkbutton(windowedFrame, variable=windowed, text="Package as a windowed app (no console window)",
                                command=removeHideConsole)
windowedCheckbox.pack(side=LEFT)

noWindowedTracebackFrame = Frame(flagsFrame)

noWindowedTracebackCheckbox = Checkbutton(noWindowedTracebackFrame, variable=noWindowedTraceback, 
                                        text="Replace traceback dump for disabled feature message (Only in windowed mode)")
noWindowedTracebackCheckbox.pack(side=LEFT)

UacAdmin = BooleanVar(root, False)
UacUiAccess = BooleanVar(root, False)
def removeUacUiAccess():
    global UacAdmin
    if UacAdmin.get() == True:
        UacUiAccessFrame.grid(column=0, row=12, sticky="w")
    else:
        UacUiAccessFrame.grid_remove()
        UacUiAccess.set(False)
UacAdminFrame = Frame(flagsFrame)
UacAdminFrame.grid(column=0, row=11, sticky="w")

UacAdminCheckbox = Checkbutton(UacAdminFrame, variable=UacAdmin, text="Ask for admin elevation upon app start",
                                command=removeUacUiAccess)
UacAdminCheckbox.pack(side=LEFT)

UacUiAccessFrame = Frame(flagsFrame)

UacUiAccessCheckbox = Checkbutton(UacUiAccessFrame, variable=UacUiAccess, text="Allow this admin app to work with Remote Desktop")
UacUiAccessCheckbox.pack(side=LEFT)


AddVersionFile = BooleanVar(root, False)
def removeVersionFileBox():
    global AddVersionFile
    if AddVersionFile.get() == True:
        VersionFileFrame.grid(column=0, row=14, sticky="w")
    else:
        VersionFileEntry.delete(0, END)  
        VersionFileFrame.grid_remove()
        

AddVersionFileFrame = Frame(flagsFrame)
AddVersionFileFrame.grid(column=0, row=13, sticky="w")
AddVersionFileCheckbox = Checkbutton(AddVersionFileFrame, variable=AddVersionFile, text="Add a version resource to the exe",
                                command=removeVersionFileBox)
AddVersionFileCheckbox.pack(side=LEFT)

def openVersionFile():
    global scriptLocationEntry
    file = askopenfile()
    if file is None:
        pass
    else:
        VersionFileEntry.delete(0, END)
        VersionFileEntry.insert(0, file.name)

VersionFileFrame = Frame(flagsFrame)

VersionFileEntry = Entry(VersionFileFrame, width=60)
VersionFileEntry.pack(side=LEFT)

VersionFileOpenButton = Button(VersionFileFrame, text="Open", command=openVersionFile)
VersionFileOpenButton.pack(side=LEFT, anchor=N)
# Execute Tkinter
root.mainloop()