#Cadenas de Caracteres. string -> str
print(type("Hello World"))
print("Hello World")
print('Hello World')
print("""Hello World""")
print('''Hello World''')
print("")

#Numeros enteros. integer -> int
print(type(100))
print(100)
print(30)
print("")

#Numeros decimales. float
print(type(16.584))
print(84.954)
print(16.584)
print("")

#Booleanos -> bool
print(type(True))
print(True)
print(False)
print("")

#Listas -> list  "Una lista puede cambiar a traves del recorrido del codigo"
print(type(["hola", "adios", "chao", "bey"]))
print([1.50, 20, "Wilson", True])
print([1, 2, 3, 4, 5])
print("")

#Tuplas -> tuple "Los datos en las tuplas son inmutables"
print(type((8, 9, 10, 11, 12)))
print((8, 9, 10, 11, 12))
print(("hola", "amiga", "te quiero"))
print("")

#Diccionarios -> dict "agrupador de tipos de datos de igual o diferente indole"
print(type({
    "name": "Wilson",
    "lastname": "Escalona",
    "nickname": "WeeNoO",
    "old": 23,
    "long": 1.68
}))
print({
    "name": "Wilson",
    "lastname": "Escalona",
    "nickname": "WeeNoO",
    "old": 23,
    "long": 1.68
})
print("")

#Tipo None. No imprime None y es de tipo -> NoneType
print(type(None))
print(None)