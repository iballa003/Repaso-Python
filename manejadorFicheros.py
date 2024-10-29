import os
archivos = [f for f in os.listdir() if os.path.isfile(f)]
archivos.remove("main.py")
extensiones = []
directorios = []
for i in range(len(archivos)):
    print(archivos[i])
    extensiones.append(os.path.splitext(archivos[i])[1])
    directorios.append(extensiones[i][1:])
    if not os.path.exists("./"+directorios[i]):
        os.makedirs("./"+directorios[i])
    os.rename("./"+archivos[i], "./"+directorios[i]+"/"+archivos[i])