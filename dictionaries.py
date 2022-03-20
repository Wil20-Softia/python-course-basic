#Nos permite definir un conjunto de datos
#que contienen clave:valor
#Funciona muy bien para listas de productos
#y listas que tienen varios datos gerarquicos
#sirven para definir propiedades de un objeto
#de la vida real
product = {
    "name": 'book',
    "quantity": 3,
    "price": 4.99
}

person = {
    "firtsname": 'Wilson',
    "lastname": 'Escalona'
}

#Tipo de dato
print(type(product)) #Imprime "dict"

#Para ver todos los metodos y propiedades
print(dir(person))

#Mostrar las llaves, claves o keys
print(person.keys())

#Mostrar los items
print(person.items())

#Limpear el Diccionario de sus elementos
person.clear()
print(person)

#Eliminar un Diccionario
#del person
#print(person) #Error porque no existe

#Uno o varios diccionarios se pueden incluir dentro de una lista
#para formar un listado de datos iguales
products = [
    {"name":'book', "quantity":12, "price": 139000.50},
    {"name":'laptop', "quantity":1, "price": 8000000.90}
]
print(products)