# 2.- En Python 3 los tipos simples pasan por valor y los compuestos por referencia. Crea un ejemplo con 3 funciones que:

# Reciban 2 números y devuelvan la suma.

def sumarNumeros(a,b):
    return a+b
print("La suma es: "+str(sumarNumeros(6,7)))

# Reciban una lista y modifiquen esa misma lista (referencia) duplicando los valores de todos los elementos. No debe devolver nada.

def duplicarElementos(lista):
   #listaModificada = copy.copy(lista)
   lista = [item for item in lista for _ in range(2)]
   print("La lista duplicada: "+str(lista))

duplicarElementos([1,2,3])

def duplicarElementos2(lista):
   listaModificada = [item for item in lista for _ in range(2)]
   return listaModificada

print("La lista duplicada2: "+str(duplicarElementos2(["a","b","c"])))