#Sive para crear una aplicación real
#Existen 3 tipos de modulos:
#Own Modules: Creados por nosotros mismos
#Thirdy Party Modules: Descargados de Internet. De Terceros
#Python Modules: Modulos preconstruidos de python

#Ejemplo 1: Python Modules
#Buscar los Python Modules en internet
#Python Modules: Python Modules Index

#Modulos de Terceros
#Buscar: Pypi Modules

#Para Buscar la documentación de un Modulo Python
#buscador: python datatime
#Buscar por la version que utilizas

#Importar toda la biblioteca datatime
# ----   import detatime
#importar especificamente modulos de la biblioteca
from datetime import timedelta, date
from fmath import add, substract
from colorama import Fore, Back, Style, init
init(convert=True) #Para activar las variables de entorno para Windows

#desde datatime importar modulo1, modulo2, moduloN, . . .
print("Fecha actual: ", date.today())
print("Transformando 80 minutos a formato hh:mm: ", timedelta(minutes=80))

#Utilizando el modulo fmath creados por nosotros en el archivo principal
add(1, 6)
substract(5, 6)

#"pip": comando de consola que funciona para descargar modulos de terceros
#Para instalar un modulo de tercero solo situarse por consola en la ruta
#del proyecto y tipear:
#pip install colorama  --->  "colorama es un modulo de terceros"

#Para utilizarlo solo importarlo en el proyecto en la parte superior:
print(Fore.RED + "Hello World") #Pintar el texto de rojo
print(Back.GREEN + "Hello World")

#django: framework para aplicaciones web
#flask: frameworf para servidores web
#tkinter: para crear aplicaciones de escritorio
