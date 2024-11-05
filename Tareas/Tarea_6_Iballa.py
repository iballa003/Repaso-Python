lista = [[1.67,68],[1.86,94],[1.40,60],[1.40,70],[1.67,68.4],[1.90,99]]
print(lista)
listaOrdenada = sorted(lista, key=lambda peso: peso[0],reverse=True)
# El argumento reverse te permite ordenar la lista de mayor a menor.
# El argumento key te permite especificar una función para ordenar.
# Lambda te permite crear funciones pequeñas y anónimas.
print(listaOrdenada)
