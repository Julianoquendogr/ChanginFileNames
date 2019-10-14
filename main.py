
import os
folder = 'E:\\Users\\JULIAN\\Pictures\\TESORO'
path = os.path.realpath(folder)
os.startfile(path)
Cont = 0
Format = ".JPG"

print("Ingrese nombre para los archivos")
NewName = input()
NewName = NewName.upper()   

with os.scandir(folder) as ListFolder:
    for file in ListFolder:
        Cont = Cont + 1
        os.rename(folder + "\\" + file.name , 
                  folder + "\\"  + NewName + "_" + str(Cont) + Format)

print("Se han cambiado los nombres de la carpeta :" + folder)
print("adios")

