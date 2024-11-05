#Is:
#Se utiliza para comprobar si dos objetos son los mismos.
x = ["apple", "banana", "cherry"]
y = x
print(x is y)
#Esto devolverá True porque “y” hace referencia a “x”.
x = ["apple", "banana", "cherry"]
y = ["apple", "banana", "cherry"]
print(x is y)
#Aquí dará False porque aunque son iguales, no son el mismo objeto.

#Not:
#El operador not de Python le permite invertir el valor de verdad de expresiones y objetos booleanos.

x = 2
y = 5
print(x > y)
# Devolverá False
print(not x > y)
# Devolverá True

#In:
#Devuelve True si una secuencia con el valor especificado está presente en el objeto.

x = ["apple", "banana"]
print("banana" in x)

