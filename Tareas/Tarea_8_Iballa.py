from functools import reduce


def comprobarNumeros(number):
   if number >=10:
         return True
   return False


cadena = input('Escribe números separados por espacio ')
listaCadena = cadena.split(" ")
listaCadena = list(map(lambda n: int(n), listaCadena))
print(listaCadena)
#Usando “filter()”, elimina de la cadena anterior los números menores que 10.

listaCadena2 = list(filter(comprobarNumeros, listaCadena))
print(listaCadena2)

listaCadena3 = reduce(lambda x, y: x*y, listaCadena2, 1)
print(f"EL resultado sería: {listaCadena3}")
