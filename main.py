import os
folder = 'E:\\Users\\JULIAN\\Pictures\\TESORO'
path = os.path.realpath(folder)
os.startfile(path)
Cont = 0
UpperFormat = ".JPG"
LowFormart = ".jpg"
Contain = ""

print("Ingrese nombre para los archivos")
NewName = input()
NewName = NewName.upper()   

with os.scandir(folder) as ListFolder:
    for file in ListFolder:
            Contain = file.name
            Contain = Contain.upper()
            if UpperFormat in Contain:
                Cont = Cont + 1
                os.rename(folder + "\\" + file.name , 
                        folder + "\\"  + NewName + "_" + str(Cont) + UpperFormat)
            else:
                print("Formato no valido: " + Contain)
    else:
        pass
        print("Se han cambiado los nombres de la carpeta :" + folder)

