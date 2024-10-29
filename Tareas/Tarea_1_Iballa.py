import copy
# 1.- Prepara un ejemplo donde expliques cómo hacer en Python 3 lo siguiente:
# Clonar una lista.

# Con el metodo .copy():
this_list = ["apple","banana","cherry"]
this_list_copy = this_list.copy()
print("Lista copiada: "+str(this_list_copy))

# Añadir un elemento a una lista.

# Con el método .append():
this_list_copy = ["apple","banana","cherry"]
this_list_copy.append("orange")
print("Añadido el elemento orange: "+str(this_list_copy))

# Quitar un elemento de una lista.

# Con el método .remove():
this_list_copy.remove("orange")
print("Eliminado el elemento orange"+str(this_list_copy))

# Crear una nueva lista con los 4 últimos elementos de una lista.

#Creamos más elementos para llenar la lista
this_list_copy.append("kiwi")
this_list_copy.append("melon")
#Conseguimos los 4 últimos elementos
new_list = this_list_copy[-4:]
print(new_list)

#Comentarios multilínea:
"""
this_list_copy.append("kiwi")
this_list_copy.append("melon")
"""

