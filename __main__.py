from tkinter import *
from tkinter.filedialog import *
from tkinter.font import *
from tkinter.ttk import *
from PIL import Image, ImageTk

# create root window
root = Tk()
root.iconphoto(True, PhotoImage(file="pyinstaller-default.png"))
style = Style()
root.title("PyInstallerGUI")
root.geometry('825x605')
root.resizable(False, False)

canvas = Canvas(root, width=root.winfo_width()-20, height=root.winfo_height(), highlightthickness=0)
canvas.pack(side="left", fill="both", expand=True)

scrollbar = Scrollbar(root, orient="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")



def on_scroll(first, last): # This function was made with AI
    scrollbar.set(first, last)

    if float(first) == 0.0 and float(last) == 1.0:
        scrollbar.pack_forget()
    else:
        scrollbar.pack(side="right", fill="y")

canvas.configure(yscrollcommand=on_scroll)

frame = Frame(canvas)
canvas.create_window((0, 0), window=frame, anchor="nw")

frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

def openScript():
    global scriptLocationEntry
    file = askopenfile(filetypes=[("Python script file", ".py"), ("PyInstaller spec files", ".spec")])
    if file is None:
        pass
    else:
        scriptLocationEntry.delete(0, END)
        scriptLocationEntry.insert(0, file.name)

scriptLocationFrame = Frame(frame)
scriptLocationFrame.pack(side=TOP)

mandatoryFont = nametofont(style.lookup("TLabel", "font")).copy()
mandatoryFont.configure(underline=True)
style.configure("Mandatory.TLabel", font=mandatoryFont)
scriptLocationLabel = Label(scriptLocationFrame, text="Script File:", style="Mandatory.TLabel")
scriptLocationLabel.pack(side=LEFT, anchor=N)

scriptLocationEntry = Entry(scriptLocationFrame, width=90)
scriptLocationEntry.pack(side=LEFT, anchor=N)

scripLocationOpenButton = Button(scriptLocationFrame, text="Open", command=openScript)
scripLocationOpenButton.pack(side=LEFT, anchor=N)

notScriptLocationFrame = Frame(frame)
notScriptLocationFrame.pack(side=TOP, anchor=W)

leftFrame = Frame(notScriptLocationFrame, padding=(15, 0))
leftFrame.grid(column=0, row=0, rowspan=100, sticky=N)

appNameFrame = Frame(leftFrame, padding=(0, 5))
appNameFrame.grid(column=0, row=0, sticky=N)

appNameLabel = Label(appNameFrame, text="App Name:")
appNameLabel.pack(side=LEFT, anchor=N)

appNameEntry = Entry(appNameFrame, width=30)
appNameEntry.pack(side=LEFT, anchor=N)


appLogoFrame = Frame(leftFrame, padding=(0, 0))
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



rightFrame = Frame(notScriptLocationFrame)
rightFrame.grid(column=1, row=0, rowspan=100, sticky=N)


def getDistFolder():
    global distFolder, distpathEntry
    distFolder = askdirectory()
    if distFolder is None:
            pass
    else:
        distpathEntry.delete(0, END)
        distpathEntry.insert(0, distFolder)

distpathFrame = Frame(rightFrame)
distpathFrame.grid(column=0, row=0, sticky="w")

distpathLabel = Label(distpathFrame, text="Bundled app destination:", style="Mandatory.TLabel")
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

workpathFrame = Frame(rightFrame)
workpathFrame.grid(column=0, row=1, sticky="w")

workpathLabel = Label(workpathFrame, text="Temporary files destination:", style="Mandatory.TLabel")
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

specpathFrame = Frame(rightFrame)
specpathFrame.grid(column=0, row=2, sticky="w")

specpathLabel = Label(specpathFrame, text=".spec file destination:", style="Mandatory.TLabel")
specpathLabel.pack(side=LEFT)

specpathEntry = Entry(specpathFrame, width=36)
specpathEntry.pack(side=LEFT)

specpathOpenButton = Button(specpathFrame, text="Open", command=getspecFolder)
specpathOpenButton.pack(side=LEFT, anchor=N)

noConfirmFrame = Frame(leftFrame)
noConfirmFrame.grid(column=0, row=3, sticky="w")

noConfirm = BooleanVar(root, False)
noConfirmCheckbox = Checkbutton(noConfirmFrame, variable=noConfirm, text="Replace output directory without confirmation")
noConfirmCheckbox.pack(side=LEFT)


cleanFrame = Frame(leftFrame)
cleanFrame.grid(column=0, row=4, sticky="w")

clean = BooleanVar(root, False)
cleanCheckbox = Checkbutton(cleanFrame, variable=clean, text="Clean cache and remove temporary files before building")
cleanCheckbox.pack(side=LEFT)


logFrame = Frame(leftFrame)
logFrame.grid(column=0, row=5, sticky="w")

logLabel = Label(logFrame, text="Log level:")
logLabel.pack(side=LEFT)

logLevel = StringVar(value="INFO")
logOptionsMenu = Combobox(logFrame, textvariable=logLevel, values=["TRACE", "DEBUG", "INFO", "WARN", "DEPRECATION", "ERROR", "FATAL"],
                          state="readonly", width=10)
logOptionsMenu.pack(side=LEFT)

debugFrame = Frame(leftFrame)
debugFrame.grid(column=0, row=6, sticky="w")

debugLabel = Label(debugFrame, text="Debug level:")
debugLabel.pack(side=LEFT)

debugLevel = StringVar(value="None")
debugOptionsMenu = Combobox(debugFrame, textvariable=debugLevel, values=["None", "All", "Imports", "Bootloader", "NoArchive"],
                          state="readonly", width=10)
debugOptionsMenu.pack(side=LEFT)

bundleTypeFrame = Frame(leftFrame)
bundleTypeFrame.grid(column=0, row=7, sticky="w")

bundleType = StringVar()

bundleTypeOneFileRadioButton = Radiobutton(bundleTypeFrame, text="One-file bundle", variable=bundleType, value="-F")
bundleTypeOneFileRadioButton.pack(side=TOP, anchor=W)

bundleTypeOnedirectoryRadioButton = Radiobutton(bundleTypeFrame, text="One-folder bundle", variable=bundleType, value="-D")
bundleTypeOnedirectoryRadioButton.pack(side=TOP, anchor=W)



hideConsoleFrame = Frame(leftFrame)
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

windowedFrame = Frame(leftFrame)
windowedFrame.grid(column=0, row=8, sticky="w")

windowedCheckbox = Checkbutton(windowedFrame, variable=windowed, text="Package as a windowed app (no console window)",
                                command=removeHideConsole)
windowedCheckbox.pack(side=LEFT)

noWindowedTracebackFrame = Frame(leftFrame)

noWindowedTracebackCheckbox = Checkbutton(noWindowedTracebackFrame, variable=noWindowedTraceback, 
                                        text="Replace error dump for disabled feature message")
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
UacAdminFrame = Frame(rightFrame)
UacAdminFrame.grid(column=0, row=11, sticky="w")

UacAdminCheckbox = Checkbutton(UacAdminFrame, variable=UacAdmin, text="Ask for admin elevation upon app start",
                                command=removeUacUiAccess)
UacAdminCheckbox.pack(side=LEFT)

UacUiAccessFrame = Frame(rightFrame)

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
        

AddVersionFileFrame = Frame(rightFrame)
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

VersionFileFrame = Frame(rightFrame)

VersionFileEntry = Entry(VersionFileFrame, width=60)
VersionFileEntry.pack(side=LEFT)

VersionFileOpenButton = Button(VersionFileFrame, text="Open", command=openVersionFile)
VersionFileOpenButton.pack(side=LEFT, anchor=N)

AddManifestFile = BooleanVar(root, False)
def removeManifestFileBox():
    global AddManifestFile
    if AddManifestFile.get() == True:
        ManifestFileFrame.grid(column=0, row=16, sticky="w")
    else:
        ManifestFileEntry.delete(0, END)  
        ManifestFileFrame.grid_remove()
        

AddManifestFileFrame = Frame(rightFrame)
AddManifestFileFrame.grid(column=0, row=15, sticky="w")
AddManifestFileCheckbox = Checkbutton(AddManifestFileFrame, variable=AddManifestFile, text="Add a Manifest file to the exe",
                                command=removeManifestFileBox)
AddManifestFileCheckbox.pack(side=LEFT)

def openManifestFile():
    global scriptLocationEntry
    file = askopenfile()
    if file is None:
        pass
    else:
        ManifestFileEntry.delete(0, END)
        ManifestFileEntry.insert(0, file.name)

ManifestFileFrame = Frame(rightFrame)

ManifestFileEntry = Entry(ManifestFileFrame, width=60)
ManifestFileEntry.pack(side=LEFT)

ManifestFileOpenButton = Button(ManifestFileFrame, text="Open", command=openManifestFile)
ManifestFileOpenButton.pack(side=LEFT, anchor=N)

AddSplashFile = BooleanVar(root, False)
def removeSplashFileBox():
    global AddSplashFile
    if AddSplashFile.get() == True:
        SplashFileFrame.grid(column=0, row=18, sticky="w")
        splashCenterFrame.grid(column=0, row=19, sticky="w")
    else:
        SplashFileEntry.delete(0, END)
        splashCenter.set("Default")  
        SplashFileFrame.grid_remove()
        splashCenterFrame.grid_remove()
        

AddSplashFileFrame = Frame(rightFrame)
AddSplashFileFrame.grid(column=0, row=17, sticky="w")
AddSplashFileCheckbox = Checkbutton(AddSplashFileFrame, variable=AddSplashFile, text="(EXPERIMENTAL) Add an splash screen to the exe",
                                command=removeSplashFileBox)
AddSplashFileCheckbox.pack(side=LEFT)

def openSplashFile():
    file = askopenfile(filetypes=[("Image files", ".png .jpg .jpeg .webp .bmp .gif")])
    if file is None:
        pass
    else:
        SplashFileEntry.delete(0, END)
        SplashFileEntry.insert(0, file.name)

SplashFileFrame = Frame(rightFrame)

SplashFileEntry = Entry(SplashFileFrame, width=60)
SplashFileEntry.pack(side=LEFT)

SplashFileOpenButton = Button(SplashFileFrame, text="Open", command=openSplashFile)
SplashFileOpenButton.pack(side=LEFT, anchor=N)

splashCenterFrame = Frame(rightFrame)


splashCenterLabel = Label(splashCenterFrame, text="Splash Center::")
splashCenterLabel.pack(side=LEFT)

splashCenter = StringVar(value="Default")
splashCenterOptionsMenu = Combobox(splashCenterFrame, textvariable=splashCenter, values=["Default", "Active", 
                                    "Primary", "Virtual"], state="readonly", width=10)
splashCenterOptionsMenu.pack(side=LEFT)

addDataFrame = Frame(rightFrame)
addDataFrame.grid(column=0, row=20, sticky="w")

additionalData = []
def addData():
    global additionalData
    additionalData.append(Frame(addDataFrame))
    additionalData[-1].pack(side=TOP)
    index = len(additionalData)-1
    indexLabel = Label(additionalData[index], text=index) # To identify it! Shouldn't be shown
    def remove():
        for i, frame in enumerate(additionalData):
            for child in frame.winfo_children():
                if child.winfo_class() == "TLabel":
                    if child["text"] == index:
                        additionalData[i].destroy()
                        additionalData.pop(i)
                        break
    removeButton = Button(additionalData[-1], text="🗑", width=2, command=remove)
    removeButton.pack(side=LEFT, anchor=N)

    sourceDirLabel = Label(additionalData[-1], text="Source:")
    sourceDirLabel.pack(side=LEFT, anchor=N)

    sourceDirEntry = Entry(additionalData[-1], width=25)
    sourceDirEntry.pack(side=LEFT, anchor=N)

    destinationDirLabel = Label(additionalData[-1], text="Destination:")
    destinationDirLabel.pack(side=LEFT, anchor=N)

    destinationDirEntry = Entry(additionalData[-1], width=25)
    destinationDirEntry.pack(side=LEFT, anchor=N)
addDataButton = Button(addDataFrame, command=addData, text="Add additional files")
addDataButton.pack(side=TOP, anchor=W)

addBinaryFrame = Frame(rightFrame)
addBinaryFrame.grid(column=0, row=21, sticky="w")

additionalBinary = []
def addBinary():
    global additionalBinary
    additionalBinary.append(Frame(addBinaryFrame))
    additionalBinary[-1].pack(side=TOP)
    index = len(additionalBinary)-1
    indexLabel = Label(additionalBinary[index], text=index) # To identify it! Shouldn't be shown
    def remove():
        for i, frame in enumerate(additionalBinary):
            for child in frame.winfo_children():
                if child.winfo_class() == "TLabel":
                    if child["text"] == index:
                        additionalBinary[i].destroy()
                        additionalBinary.pop(i)
                        break
    removeButton = Button(additionalBinary[-1], text="🗑", width=2, command=remove)
    removeButton.pack(side=LEFT, anchor=N)

    sourceDirLabel = Label(additionalBinary[-1], text="Source:")
    sourceDirLabel.pack(side=LEFT, anchor=N)

    sourceDirEntry = Entry(additionalBinary[-1], width=25)
    sourceDirEntry.pack(side=LEFT, anchor=N)

    destinationDirLabel = Label(additionalBinary[-1], text="Destination:")
    destinationDirLabel.pack(side=LEFT, anchor=N)

    destinationDirEntry = Entry(additionalBinary[-1], width=25)
    destinationDirEntry.pack(side=LEFT, anchor=N)
addBinaryButton = Button(addBinaryFrame, command=addBinary, text="Add additional binary file")
addBinaryButton.pack(side=TOP, anchor=W)


addPathsFrame = Frame(rightFrame)
addPathsFrame.grid(column=0, row=22, sticky="w")

additionalPaths = []
def addPaths():
    global additionalPaths
    additionalPaths.append(Frame(addPathsFrame))
    additionalPaths[-1].pack(side=TOP)
    index = len(additionalPaths)-1
    indexLabel = Label(additionalPaths[index], text=index) # To identify it! Shouldn't be shown
    def remove():
        for i, frame in enumerate(additionalPaths):
            for child in frame.winfo_children():
                if child.winfo_class() == "TLabel":
                    if child["text"] == index:
                        additionalPaths[i].destroy()
                        additionalPaths.pop(i)
                        break
    removeButton = Button(additionalPaths[-1], text="🗑", width=2, command=remove)
    removeButton.pack(side=LEFT, anchor=N)

    pathsEntry = Entry(additionalPaths[-1], width=50)
    pathsEntry.pack(side=LEFT, anchor=N)
addPathsButton = Button(addPathsFrame, command=addPaths, text="Add additional import paths")
addPathsButton.pack(side=TOP, anchor=W)


hiddenImportsFrame = Frame(rightFrame)
hiddenImportsFrame.grid(column=0, row=23, sticky="w")

hiddenImports = []
def addHiddenImports():
    global hiddenImports
    hiddenImports.append(Frame(hiddenImportsFrame))
    hiddenImports[-1].pack(side=TOP)
    index = len(hiddenImports)-1
    indexLabel = Label(hiddenImports[index], text=index) # To identify it! Shouldn't be shown
    def remove():
        for i, frame in enumerate(hiddenImports):
            for child in frame.winfo_children():
                if child.winfo_class() == "TLabel":
                    if child["text"] == index:
                        hiddenImports[i].destroy()
                        hiddenImports.pop(i)
                        break
    removeButton = Button(hiddenImports[-1], text="🗑", width=2, command=remove)
    removeButton.pack(side=LEFT, anchor=N)

    hiddenImportsEntry = Entry(hiddenImports[-1], width=50)
    hiddenImportsEntry.pack(side=LEFT, anchor=N)
hiddenImportsButton = Button(hiddenImportsFrame, command=addHiddenImports, text="Add a hidden import")
hiddenImportsButton.pack(side=TOP, anchor=W)

collectSubmodulesFrame = Frame(rightFrame)
collectSubmodulesFrame.grid(column=0, row=24, sticky="w")

collectSubmodules = []
def addCollectSubmodules():
    global collectSubmodules
    collectSubmodules.append(Frame(collectSubmodulesFrame))
    collectSubmodules[-1].pack(side=TOP)
    index = len(collectSubmodules)-1
    indexLabel = Label(collectSubmodules[index], text=index) # To identify it! Shouldn't be shown
    def remove():
        for i, frame in enumerate(collectSubmodules):
            for child in frame.winfo_children():
                if child.winfo_class() == "TLabel":
                    if child["text"] == index:
                        collectSubmodules[i].destroy()
                        collectSubmodules.pop(i)
                        break
    removeButton = Button(collectSubmodules[-1], text="🗑", width=2, command=remove)
    removeButton.pack(side=LEFT, anchor=N)

    collectSubmodulesEntry = Entry(collectSubmodules[-1], width=50)
    collectSubmodulesEntry.pack(side=LEFT, anchor=N)
collectSubmodulesButton = Button(collectSubmodulesFrame, command=addCollectSubmodules, text="Collect all submodules from module")
collectSubmodulesButton.pack(side=TOP, anchor=W)

collectDataFrame = Frame(rightFrame)
collectDataFrame.grid(column=0, row=25, sticky="w")

collectData = []
def addCollectData():
    global collectData
    collectData.append(Frame(collectDataFrame))
    collectData[-1].pack(side=TOP)
    index = len(collectData)-1
    indexLabel = Label(collectData[index], text=index) # To identify it! Shouldn't be shown
    def remove():
        for i, frame in enumerate(collectData):
            for child in frame.winfo_children():
                if child.winfo_class() == "TLabel":
                    if child["text"] == index:
                        collectData[i].destroy()
                        collectData.pop(i)
                        break
    removeButton = Button(collectData[-1], text="🗑", width=2, command=remove)
    removeButton.pack(side=LEFT, anchor=N)

    collectDataEntry = Entry(collectData[-1], width=50)
    collectDataEntry.pack(side=LEFT, anchor=N)
collectDataButton = Button(collectDataFrame, command=addCollectData, text="Collect all data from module")
collectDataButton.pack(side=TOP, anchor=W)


collectBinariesFrame = Frame(rightFrame)
collectBinariesFrame.grid(column=0, row=26, sticky="w")

collectBinaries = []
def addCollectBinaries():
    global collectBinaries
    collectBinaries.append(Frame(collectBinariesFrame))
    collectBinaries[-1].pack(side=TOP)
    index = len(collectBinaries)-1
    indexLabel = Label(collectBinaries[index], text=index) # To identify it! Shouldn't be shown
    def remove():
        for i, frame in enumerate(collectBinaries):
            for child in frame.winfo_children():
                if child.winfo_class() == "TLabel":
                    if child["text"] == index:
                        collectBinaries[i].destroy()
                        collectBinaries.pop(i)
                        break
    removeButton = Button(collectBinaries[-1], text="🗑", width=2, command=remove)
    removeButton.pack(side=LEFT, anchor=N)

    collectBinariesEntry = Entry(collectBinaries[-1], width=50)
    collectBinariesEntry.pack(side=LEFT, anchor=N)
collectBinariesButton = Button(collectBinariesFrame, command=addCollectBinaries, text="Collect all binaries from module")
collectBinariesButton.pack(side=TOP, anchor=W)

collectAllFrame = Frame(rightFrame)
collectAllFrame.grid(column=0, row=27, sticky="w")

collectAll = []
def addCollectAll():
    global collectAll
    collectAll.append(Frame(collectAllFrame))
    collectAll[-1].pack(side=TOP)
    index = len(collectAll)-1
    indexLabel = Label(collectAll[index], text=index) # To identify it! Shouldn't be shown
    def remove():
        for i, frame in enumerate(collectAll):
            for child in frame.winfo_children():
                if child.winfo_class() == "TLabel":
                    if child["text"] == index:
                        collectAll[i].destroy()
                        collectAll.pop(i)
                        break
    removeButton = Button(collectAll[-1], text="🗑", width=2, command=remove)
    removeButton.pack(side=LEFT, anchor=N)

    collectAllEntry = Entry(collectAll[-1], width=50)
    collectAllEntry.pack(side=LEFT, anchor=N)
collectAllButton = Button(collectAllFrame, command=addCollectAll, text="Collect all (submodules, data files, and binaries) from module")
collectAllButton.pack(side=TOP, anchor=W)


copyMetadataFrame = Frame(rightFrame)
copyMetadataFrame.grid(column=0, row=28, sticky="w")

copyMetadata = []
def addCopyMetadata():
    global copyMetadata
    copyMetadata.append(Frame(copyMetadataFrame))
    copyMetadata[-1].pack(side=TOP)
    index = len(copyMetadata)-1
    indexLabel = Label(copyMetadata[index], text=index) # To identify it! Shouldn't be shown
    def remove():
        for i, frame in enumerate(copyMetadata):
            for child in frame.winfo_children():
                if child.winfo_class() == "TLabel":
                    if child["text"] == index:
                        copyMetadata[i].destroy()
                        copyMetadata.pop(i)
                        break
    removeButton = Button(copyMetadata[-1], text="🗑", width=2, command=remove)
    removeButton.pack(side=LEFT, anchor=N)

    copyMetadataEntry = Entry(copyMetadata[-1], width=50)
    copyMetadataEntry.pack(side=LEFT, anchor=N)
copyMetadataButton = Button(copyMetadataFrame, command=addCopyMetadata, text="Copy metadata for package")
copyMetadataButton.pack(side=TOP, anchor=W)


copyMetadataRecurseFrame = Frame(rightFrame)
copyMetadataRecurseFrame.grid(column=0, row=29, sticky="w")

copyMetadataRecurse = []
def addCopyMetadataRecurse():
    global copyMetadataRecurse
    copyMetadataRecurse.append(Frame(copyMetadataRecurseFrame))
    copyMetadataRecurse[-1].pack(side=TOP)
    index = len(copyMetadataRecurse)-1
    indexLabel = Label(copyMetadataRecurse[index], text=index) # To identify it! Shouldn't be shown
    def remove():
        for i, frame in enumerate(copyMetadataRecurse):
            for child in frame.winfo_children():
                if child.winfo_class() == "TLabel":
                    if child["text"] == index:
                        copyMetadataRecurse[i].destroy()
                        copyMetadataRecurse.pop(i)
                        break
    removeButton = Button(copyMetadataRecurse[-1], text="🗑", width=2, command=remove)
    removeButton.pack(side=LEFT, anchor=N)

    copyMetadataRecurseEntry = Entry(copyMetadataRecurse[-1], width=50)
    copyMetadataRecurseEntry.pack(side=LEFT, anchor=N)
copyMetadataRecurseButton = Button(copyMetadataRecurseFrame, command=addCopyMetadataRecurse, text="Recursively copy metadata for package")
copyMetadataRecurseButton.pack(side=TOP, anchor=W)


additionalHooksDirFrame = Frame(rightFrame)
additionalHooksDirFrame.grid(column=0, row=30, sticky="w")

additionalHooksDir = []
def addAdditionalHooksDir():
    global additionalHooksDir
    additionalHooksDir.append(Frame(additionalHooksDirFrame))
    additionalHooksDir[-1].pack(side=TOP)
    index = len(additionalHooksDir)-1
    indexLabel = Label(additionalHooksDir[index], text=index) # To identify it! Shouldn't be shown
    def remove():
        for i, frame in enumerate(additionalHooksDir):
            for child in frame.winfo_children():
                if child.winfo_class() == "TLabel":
                    if child["text"] == index:
                        additionalHooksDir[i].destroy()
                        additionalHooksDir.pop(i)
                        break
    removeButton = Button(additionalHooksDir[-1], text="🗑", width=2, command=remove)
    removeButton.pack(side=LEFT, anchor=N)

    additionalHooksDirEntry = Entry(additionalHooksDir[-1], width=50)
    additionalHooksDirEntry.pack(side=LEFT, anchor=N)
additionalHooksDirButton = Button(additionalHooksDirFrame, command=addAdditionalHooksDir, text="Add a path to search for hooks")
additionalHooksDirButton.pack(side=TOP, anchor=W)


runtimeHookFrame = Frame(rightFrame)
runtimeHookFrame.grid(column=0, row=31, sticky="w")

runtimeHook = []
def addRuntimeHook():
    global runtimeHook
    runtimeHook.append(Frame(runtimeHookFrame))
    runtimeHook[-1].pack(side=TOP)
    index = len(runtimeHook)-1
    indexLabel = Label(runtimeHook[index], text=index) # To identify it! Shouldn't be shown
    def remove():
        for i, frame in enumerate(runtimeHook):
            for child in frame.winfo_children():
                if child.winfo_class() == "TLabel":
                    if child["text"] == index:
                        runtimeHook[i].destroy()
                        runtimeHook.pop(i)
                        break
    removeButton = Button(runtimeHook[-1], text="🗑", width=2, command=remove)
    removeButton.pack(side=LEFT, anchor=N)

    runtimeHookEntry = Entry(runtimeHook[-1], width=50)
    runtimeHookEntry.pack(side=LEFT, anchor=N)
runtimeHookButton = Button(runtimeHookFrame, command=addRuntimeHook, text="Add a path to a custom runtime hook file")
runtimeHookButton.pack(side=TOP, anchor=W)

excludeModuleFrame = Frame(rightFrame)
excludeModuleFrame.grid(column=0, row=32, sticky="w")

excludeModule = []
def addExcludeModule():
    global excludeModule
    excludeModule.append(Frame(excludeModuleFrame))
    excludeModule[-1].pack(side=TOP, anchor=W)
    index = len(excludeModule)-1
    indexLabel = Label(excludeModule[index], text=index) # To identify it! Shouldn't be shown
    def remove():
        for i, frame in enumerate(excludeModule):
            for child in frame.winfo_children():
                if child.winfo_class() == "TLabel":
                    if child["text"] == index:
                        excludeModule[i].destroy()
                        excludeModule.pop(i)
                        break
    removeButton = Button(excludeModule[-1], text="🗑", width=2, command=remove)
    removeButton.pack(side=LEFT, anchor=W)

    excludeModuleEntry = Entry(excludeModule[-1], width=50)
    excludeModuleEntry.pack(side=LEFT, anchor=W)
excludeModuleButton = Button(excludeModuleFrame, command=addExcludeModule, text="Add module (the Python name, not the path name) that will be ignored")
excludeModuleButton.pack(side=TOP, anchor=W)

def checkRequiredEntries(event=None):
    if all([
    len(scriptLocationEntry.get()) >= 7,
    len(distpathEntry.get()) >= 3,
    len(workpathEntry.get()) >= 3,
    len(specpathEntry.get()) >= 3]):
        buildButton.config(state="normal")
        clarifyMandatoryLabel.grid_forget()
    else:
        buildButton.config(state="disabled")
        clarifyMandatoryLabel.grid(column=0, row=102, columnspan=2)

for i in [scriptLocationEntry, distpathEntry, workpathEntry, specpathEntry]:
    i.bind("<KeyRelease>", checkRequiredEntries)
buildButtonFont = nametofont(style.lookup("TButton", "font")).copy()
buildButtonFont.configure(size=28, weight=BOLD)
style.configure("BuildButton.TButton", font=buildButtonFont)
buildButton = Button(notScriptLocationFrame, text="BUILD", style="BuildButton.TButton", width=15, state=DISABLED)
buildButton.grid(column=0, row=101, columnspan=2, pady=(15, 0))

clarifyMandatoryLabel = Label(notScriptLocationFrame, text="(Underlined items are mandatory)")
clarifyMandatoryLabel.grid(column=0, row=102, columnspan=2)


# Execute Tkinter
root.mainloop()