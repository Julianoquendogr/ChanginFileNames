from datetime import datetime
import os
folder = 'E:\\Users\\JULIAN\\Pictures\\TESORO\\'
Cont = 0
UpperFormat = ".JPG"
Contain = ""
FileName = "OtroFormato_"
CompleteName = os.path.join(folder,FileName)

#creating timestamp to add to the file name in order to not create duplicates files
time = datetime.now()
timestamp = str(time.year)+str(time.month)+str(time.day)+str(time.hour)+str(time.minute)+str(time.second)

#creates the file
txtFile = open(CompleteName + timestamp + ".txt", "w+")

print("Ingrese nombre para los archivos")
#Convert to upperCase
NewName = input()
NewName = NewName.upper()

with os.scandir(folder) as ListFolder:
    for file in ListFolder:
            Contain = file.name
            Contain = Contain.upper()
            if UpperFormat in Contain:
                Cont = Cont + 1
                os.rename(folder + "\\" + file.name,
                          folder + "\\" + NewName + "_" + str(Cont) + UpperFormat)
            else:
                print("Formato no valido: " + Contain)
                txtFile.write(Contain + '\n')
    else:
        pass
        print("Se han cambiado los nombres de la carpeta :" + folder)

path = os.path.realpath(folder)
os.startfile(path)
txtFile.close()
