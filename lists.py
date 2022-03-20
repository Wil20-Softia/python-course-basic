# [1, 'hello', True, 1.34, [1,2,3]] : Es una lista con distintos elementos

demo_list = [1, 'hello', True, 1.34, [1, 2, 3]]
colors = ["Red", "Green", "Blue"]

#lista con constructor
new_list = list((1,2,3,4)) #Pasar un Tupla con los elementos a contener la lista

print(new_list)
print(type(new_list)) #tipo de dato

#lista con rango
range_list = list(range(1,11)) #Crea una lista del inicio a final-1 numero
print(range_list)

#tipo de dato de colors
print(type(colors))
#Los metodos y propiedades que se pueden utilizar de una lista
print(dir(colors))

#longitud de una lista
print("longitud de la lista colors: ", len(colors))

#Obtener un elemento especifico de la lista
print("Elemento en la posicion 1 de la lista colors: ", colors[1])
print("Elemento en la posicion -1 de la lista colors: ", colors[-1])

#Saber si un elemento existe en una lista
print("Green" in colors) #Devuelve un Booleano

#Reasignar un elemento en la lista
colors[1] = "Yellow"
print(colors)

#Agregar un nuevo elemento
colors.append('Violet')
print(colors)

#Agregar varios elementos al arreglo
colors.extend(['Pink', "Black"])
print(colors)

#Insertar un elemento en una posicion dada
colors.insert(1, "Orange")
print(colors)

#Si se quiere insertar al ultimo
colors.insert(len(colors), "White")
print(colors)

#Remover un elemento de la lista
colors.pop() #Elimina el ultimo elemento de la lista.
print(colors)

#Eliminar un item o elemento especifico
colors.remove('Violet')
print(colors)

#Eliminar a partir de un indice
colors.pop(2)
print(colors)

#Eliminar todos los elementos de la lista o limpear
#colors.clear()
#print(colors)

#Ordenamiento de lista
colors.sort() #Orden Normal Ascendente
print(colors)
colors.sort(reverse=True) #Orden a la Inverza Descendente
print(colors)

#Obtener el Indice de un item de la lista
print("Indice del Item 'Red': ", colors.index('Red'))

colors.append('Orange')
print(colors)

#Contador de elementos en la lista
print("Cantidad de Orange existentes: ", colors.count("Orange")) #Cuenta cuantos Orange existe.
