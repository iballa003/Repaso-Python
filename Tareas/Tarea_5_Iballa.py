# código
def sumar(a=None, b=None):
    # Comprueba que los dos parámetros tenga valores
    # El primer If sólo se ejecutará si sólo existe un valor.
    if a != None and b == None:
        print(a)
    # De lo contrario, si tiene dos valores, entonces suma los dos parámetros.
    else:
        print(a+b)


# Dos parámetros son pasados, imprime el resultado de la suma
sumar(2, 3)
# Un sólo parámetro es pasado, lo imprime sólo.
sumar(2)
