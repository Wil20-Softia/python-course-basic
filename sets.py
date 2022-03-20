# - Se utiliza para crear colecciones en los cuales los elementos
#no tienen un indice

#¿Por qué utilizarlos?
#R= Para cuando no se quiera tener un conjunto de datos
#ordenados, o querer cumplir funcionalidades de ordenamiento
#o por indice

colors = {'Red', 'Green', 'Blue'}

#Tipo de datos
print(type(colors))

#Si existe un elemento
print('Red' in colors)

#Para agregar un nuevo elemento
#Se agrega al inicio, ya que no tiene indice
colors.add('Violet')
print(colors)

#Para eliminar un Item
colors.remove('Red')
print(colors)

#Para limpear el Set
colors.clear()
print(colors) #devuelve set()

#Para eliminar el Set()
del colors #Lo elimina, no existe.
#print(colors)