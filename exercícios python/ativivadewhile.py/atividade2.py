print("--------------------------------------------------------------------")
print("1- adição")
print("2- subtração")
print("3- multiplicação")
print("4- divisão")
op= input("Qual a operação desejada? ")
n1= float(input("Digite o primeiro valor: "))
n2= float(input("Digite o segundo valor: "))

if op=="1":
    print(f"resultado: {n1+n2}")
elif op=="2":
    print(f"resultado: {n1-n2}")
elif op=="3":
    print(f"resultado: {n1*n2}")
elif op=="4":
    print(f"resultado: {n1/n2}")
else:
    print("operação inválida")

dnv= input("gostaria de fazer mais uma operação? ")

while dnv=="sim" or dnv=="Sim" or dnv=="s" or dnv=="S":
    print("--------------------------------------------------------------------")
    print("1- adição")
    print("2- subtração")
    print("3- multiplicação")
    print("4- divisão")
    op= input("Qual a operação desejada? ")
    n1= float(input("Digite o primeiro valor: "))
    n2= float(input("Digite o segundo valor: "))

    if op=="1":
        print("adição")
        print(f"resultado: {n1+n2}")
    elif op=="2":
        print("subtração")
        print(f"resultado: {n1-n2}")
    elif op=="3":
        print("multiplicação")
        print(f"resultado: {n1*n2}")
    elif op=="4":
        print("divisão")
        print(f"resultado: {n1/n2}")
    else:
        print("operação inválida")

