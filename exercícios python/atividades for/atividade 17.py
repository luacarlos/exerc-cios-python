numero= int(input("digite o número: "))
if numero == 0:
    print("fatorial: 1")
else:
    fatorial = 1
    for i in range(1, numero + 1):
        fatorial *= i
    
    print(f" o fatorial de {numero} é: {fatorial}")