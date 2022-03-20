#- Conjunto de datos que no van a cambiar
#quiere decir que son inmutables
#- Son muchos más rapidas que las listas, porque ocupan menos
#espacio en la memoria

#Definiendo Tuplas
x = (1, 2, 3)
y = tuple((1, 2, 3))
print(x)
print(y)

#Crear tupla de un solo elemento
z = (1, ) #Colocar la coma si es de un solo elemento.
print(z)

#Obtener el Valor de indice 2 de un elemento
print("Valor del indice 2: ", x[2])

#No soporta reasignaciones
#x[2] = 9 #Es Incorrecto
#print(x)

#Eliminar una Tupla
del x # "x" es la Tupla
#print(x)

#Las Tuplas se utilizan para almacenar valores que no van
#a cambiar nunca en la aplicación
months = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
print(months)