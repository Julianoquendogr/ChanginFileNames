from datetime import datetime
from tkinter.filedialog import askdirectory
import os

#Give option to open any directory and do file changes
folder = askdirectory()
folder = folder.replace("/", "\\\\")

Cont = 0
UpperFormat = ".JPG"
Contain = ""
FileName = "OtroFormato_"
CompleteName = os.path.join(folder, FileName)

#creating timestamp to add to the file name in order to not create duplicates files
time = datetime.now()
timestamp = str(time.year)+str(time.month)+str(time.day) + \
    str(time.hour)+str(time.minute)+str(time.second)

#creates the file
txtFile = open(CompleteName + timestamp + ".txt", "w+")

print("Type name to rename files")
#Convert to upperCase
NewName = input()
NewName = NewName.upper()

with os.scandir(folder) as ListFolder:
    for file in ListFolder:
            Contain = file.name
            Contain = Contain.upper()
            if UpperFormat in Contain:
                Cont = Cont + 1
                try:
                    os.rename(folder + "\\" + file.name, folder +
                              "\\" + NewName + "_" + str(Cont) + UpperFormat)
                except OSError:
                     print("Something went wrong with : " + NewName)
            elif FileName.upper() in Contain:
                    pass
            else:
                print("Format is not valid: " + Contain)
                txtFile.write(Contain + '\n')
    else:
        pass
        print("Python has changed files in selected path : " + folder)

path = os.path.realpath(folder)
os.startfile(path)
txtFile.close()
