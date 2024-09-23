lista= []
num1= float(input("Digite o 1º número: "))


for i in range(2,6):
    num1= float(input(f"Digite o {i}º número: "))
    lista.append(num1)
    maior= max(lista)
print(f"o maior número da lista é: {maior}")