#VARIABLES EN PYTHON.

#
# ES UN LENGUAJE DE TIPADO DINAMICO, O SEA QUE LA 
# VARIABLE PUEDE CAMBIAR DE TIPO FACILMENTE SIN PARCEAR
# A LA MISMA SOLO COLOCANDO OTRO VALOR.
#

#NORMAL:
nombre = "Wilson Daniel"
x = 234
libro = "La culpa es de la vaca"
print("VARIABLES SIMPLE:")
print("x = ", x)
print("nombre = ", nombre)
print("libro = ", libro)

#MULTIPLES VARIABLES EN UNA LINEA
lugar, telefono, edad = "Betijoque", "0416-1730291", 23
print("MULTIPLES VARIABLES:")

#IMPRESION DE MULTIPLES VARIABLES EN UNA SOLA SENTENCIA
print(lugar, telefono, edad)

#CONVENCIONES
book_name = "LA CULPA ES DE LA VACA"    #Snake Case
bookName = "100 años de soledad"        #Camel Case
BookName = "La Odisea"                  #Pascal Case
print("Libro 1: ", book_name)
print("Libro 2: ", bookName)
print("Libro 3: ", BookName)

#CONSTANTES: se escriben siempre por convencion en MAYUSCULAS
PI = 3.1416
E = 2.7154