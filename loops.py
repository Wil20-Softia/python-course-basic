#Ejemplo #1: Bucle for
#Recorrer una lista
demo_list = [1, 'hello', True, 1.34, [1, 2, 3]]
for item in demo_list:
    if item == 1:
        continue
    elif item == 1.34:
        break
    print(item)

#Recorrer un rango
for number in range(1, 11):
    print(number)

#Recorrer un String
for letter in "Wilson":
    print(letter)

#Ejemplo #2: Bucle While
count = 4
while count <= 10:
    print(count)
    count+=1
