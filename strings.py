#Variable que guarda una cadena
myStr = "Hello World"
myName= "WeenoO"

#FORMAS DE IMPRIMIR UNA VARIABLE DE STRING CONCATENANDO
#FORMA #1:
print("Hola " + myName)

#FORMA #2:
print(f"Hola {myName}")

#FORMA #3:
print("Hola {0}".format(myName))

#Funcion que describre las propiedades y metodos
#de un objeto
#print(dir(myStr))

#A Mayusculas
print("upper: ", myStr.upper())

#A minusculas
print("lower: ", myStr.lower())

#Invierte las Minusculas a Mayusculas y viceverza
print("swapcase: ", myStr.swapcase())

#Coloca la primera letra a Mayuscula
print("capitalize: ", myStr.capitalize())

#Remplaza el 1er por el 2do
print("replace: ", myStr.replace("Hello", "Bey"))

#Cuenta la cantidad de caracteres pasados por
#parametros
print("count: ", myStr.count('l'))

#Verifica si comienza por el caracter pasado
#por parametros
print("stratrswith: ", myStr.startswith("He"))

#Verifica si termina por el caracter pasado
#por parametro
print("endswith: ", myStr.endswith("World"))

#Fracciona y crea un list apartir del caracter
#pasado por parametro
print("split: ", myStr.split("o"))

#Encuentra el caracter pasado por parametro y
#devuelve la posicion del mismo en la primera
#coincidencia
print("find: ", myStr.find('l'))

#Devuelve la posicion del caracter pasado por
#parametro
#print("index: ", myStr.index('l'))

#len() devuelve el tamaño de la cadena
print("len()", len(myStr))

#Verifica si es una cadena numerica
print("isnumeric: ", myStr.isnumeric())

#Verifica si es una cadena con simbolos y numeros
print("isalpha: ", myStr.isalpha())

#Para ingresar a cualquier caracteres de la cadena
print(myStr[0])
print(myStr[4])
print(myStr[5])

#Para recorrer de forma inversa cada caracter
print(myStr[-1])
print(myStr[-3])
print(myStr[-5])