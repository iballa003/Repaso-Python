import copy
import hashlib
import random
import os
class Car:

    def __init__(self, matrícula, color):
        self.matrícula = matrícula
        self.color = color

    def imprimir(self):
        print(f"La matrícula del coche es {self.matrícula} y su color es {self.color}")

    def cambiarColor(self,color):
        self.color = color

    def cambiarMatricula(self,matrícula):
        self.matrícula = matrícula


def Sha512Hash(Password):
    HashedPassword=hashlib.sha512(Password.encode('utf-8')).hexdigest()
    return HashedPassword
#2.- Tarea:
def sumarNumeros(a,b):
    return a+b

def duplicarElementos(lista):
    #listaModificada = copy.copy(lista)
    lista = [item for item in lista for _ in range(2)]
    print(lista)


def duplicarElementos2(lista):
    listaModificada = [item for item in lista for _ in range(2)]
    return listaModificada

#3.- Tarea:
def menuUsuarioLista(usuarios):
    #usuarios = [["Pepe","1234"],["Juan","5678"],["Carmen","9101112"],["Sara","131415"],["Jose","161718"]]
    
    print("1- Crear un usuario\n2- Consultar un usuario\n3- Salir")
    menuInput = input('Elige una opción : ')
    match menuInput:
        case "1":
            crearUsuarioLista(usuarios)
        case "2":
            consultarUsuarioLista(usuarios)
        case "3":
            print("Adios")
        case _:
            print("Number not between 1 and 3")

def crearUsuarioLista(usuarios):
    listaUsuarios = usuarios
    for i in range(5):
        usuario = input('Nombre de usuario: ')
        contraseña = input('Contraseña: ')
        contraseñaConHash = Sha512Hash(contraseña)
        nuevoUsuario = [usuario,contraseñaConHash]
        listaUsuarios.append(nuevoUsuario)

def consultarUsuarioLista(usuarios):
    for i in range(2):
        usuario = input('¿Qué usuario quieres consultar? ')
        res = any(usuario in sublist for sublist in usuarios)
        if res == True:
            print("Si existe")
        else:
            print("No existe")

def crearUsuarioDiccionario(usuarios):
    listaUsuarios = usuarios
    #usuarios = [["Pepe","1234"],["Juan","5678"],["Carmen","9101112"],["Sara","131415"],["Jose","161718"]]
    
    #print("1- Crear un usuario\n2- Consultar un usuario\n3- Salir")
    for i in range(5):
        usuario = input('Nombre de usuario: ')
        contraseña = input('Contraseña: ')
        contraseñaConHash = Sha512Hash(contraseña)
        usuarios[usuario] = contraseñaConHash
    print(listaUsuarios)


def consultarUsuarioDiccionario(usuarios):
    print(usuarios)
    for i in range(2):
        usuario = input('¿Qué usuario quieres consultar? ')
        if usuario in usuarios == True:
            print("Si existe")
        else:
            print("No existe")

#6.- Tarea:
def tarea6Funcion():
    lista = [[1.67,68],[1.86,94],[1.40,60],[1.40,70],[1.67,68.4],[1.90,99]]
    print(lista)
    listaOrdenada = sorted(lista, key=lambda peso: peso[0],reverse=True)
    # El argumento reverse te permite ordenar la lista de mayor a menor.
    # El argumento key te permite especificar una función para ordenar.
    # Lambda te permite crear funciones pequeñas y anónimas.
    print(listaOrdenada)

#7.- Tarea:
def tarea7Funcion():
    count = int(input('¿Cuántos coches quieres crear? '))
    colores = ["red", "white", "black", "pink", "blue"]
    for i in range(count):
        coche = Car(consecutiveNumbers(i+1),random.choice(colores))
        if(i < 10):
            coche.imprimir()
        else:
            break
        

def consecutiveNumbers(limit):
    numbers = ""
    for i in range(limit):
        numbers = numbers+str(i+1)
    return numbers

#8.- Tarea:
def comprobarNumeros(number):
    if number >=10:
          return True  

    return False 

def tarea8Funcion():
    # Usando “map()” (y “list()” e “int()”
    cadena = input('Escribe números separados por espacio ')
    listaCadena = cadena.split(" ")
    listaCadena = list(map(lambda n: int(n), listaCadena))
    print(listaCadena)
    listaCadena2 = list(filter(comprobarNumeros, listaCadena))
    print(listaCadena2)

def tarea9Funcion():
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

def tarea10Funcion():
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



#Ejercicios
#1.- Tarea:
print("---Reciban 2 números y devuelvan la suma.---")
print(f"La suma de los dos numeros es {sumarNumeros(3,6)}")
print("-----------------------------------------------")
print("---Reciban una lista y modifiquen esa misma lista (referencia) duplicando los valores de todos los elementos. No debe devolver nada.---")
nuevalista = ["a","b","c"]
duplicarElementos(nuevalista)
print("-----------------------------------------------")
print("---Reciban una lista y devuelvan una copia de esa misma lista (referencia) duplicando los valores de todos los elementos. La lista original no debe modificarse.---")
#print(f"Lista {duplicarElementos(nuevalista)}")
print(f"Original {nuevalista} y modificada {duplicarElementos2(nuevalista)}")
print("-----------------------------------------------")
print("---Usando una lista.---")
usuariosLista = []
menuUsuarioLista(usuariosLista)
print("-----------------------------------------------")
#consultarUsuarioLista(usuariosLista)
print("-----------------------------------------------")
print("---Usando un diccionario.---")
usuariosDiccionario = {}
#crearUsuarioDiccionario(usuariosDiccionario)
print("-----------------------------------------------")
#consultarUsuarioDiccionario(usuariosDiccionario)
#tarea6Funcion()
print("-----------------------------------------------")
# coche = Car(123443443, "rojo")
# coche.imprimir()
# coche.cambiarColor("verde")
# coche.imprimir()
print("-----------------------------------------------")
#tarea7Funcion()
#tarea8Funcion()
#tarea9Funcion()
