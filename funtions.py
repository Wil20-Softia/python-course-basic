#Funciones predefinidas por el lenguaje
#print() imprime por consola
#dir() retorna un string con propiedades y metodos de un objeto
# type() retorna un string con el tipo de dato

#Funciones propias:
def helloWorld():
    print("Hello World")
#llamada a la función
helloWorld()

#Funcion con parametros:
def saludoObejtivo(name):
    print("Hola " + name + ", ¿te gusta el helado de vainilla?, ¿Cómo estas " + name + "?")
saludoObejtivo("Bethania")

#Funcion con parametro con valor con defecto
def saludoEspecifico(name="Person"):
    print("Hola " + name + ", que tal?")
saludoEspecifico()

#Funcion que retorna un valor
def add(n1, n2):
    return n1 + n2
print("La suma es igual a: ", add(12, 15))

#Función lambda
suma = lambda numberOne, numberTwo: numberOne + numberTwo
print(suma(55,36))