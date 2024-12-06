def soma(valor1, valor2):
    return valor1 + valor2

while True:
    valor1 = int(input("Valor 1: "))
    valor2 = int(input("Valor 2: "))

    calc = soma(valor1, valor2)
    print(calc)