listas = [1, 2, 3]

print(listas[0])
print(listas[1])
print(listas[2])

#-------------------------#

listas_numeros = [1, 2, 3]

listas_numeros[0] = 5

print("\n")
print(listas_numeros[0])
print(listas_numeros[1])
print(listas_numeros[2])

#-------------------------#

#uma lista pode ter qualquer tipo de dados 

number = [1, 2, 3]
strings = ["Luffy", "Goku", "Naruto"]
decimais = [10.8, 15.5, 34.5]

#-------------------------------------#

lista_vazia = []

lista_vazia.append("Ola")
lista_vazia.append("Mundo")

print("\n")
print(lista_vazia)

#----------------------------------------#

number = (10, 9, 8, 7, 6)

print("\n")
print("Total: ", len(number))
print("Menor valor: ", min(number))
print("Maior valor: ", max(number))