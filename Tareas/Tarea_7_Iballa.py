import random
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


def tarea7Funcion():
    count = int(input('¿Cuántos coches quieres crear? '))
    colores = ["red", "white", "black", "pink", "blue"]
    for i in range(count):
        coche = Car(consecutiveNumbers(i + 1), random.choice(colores))
        if (i < 10):
            coche.imprimir()
        else:
            break


def consecutiveNumbers(limit):
    numbers = ""
    for i in range(limit):
        numbers = numbers + str(i + 1)
    return numbers

tarea7Funcion()