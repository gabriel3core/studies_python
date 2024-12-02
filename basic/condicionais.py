idade = int(input("Informe sua idade: "))

if idade >=18:
    print("Permitido")
else:
    print("Bloqueado")

#--------------------------------------------------#

salario = float(input("Informe o salario: "))

if salario <=3000:
    print("junior")
elif salario > 3000 and salario <=6000:
    print("pleno")
elif salario > 6000 and salario <= 15000:
    print("senior")
else:
    print("gerente de projeto")