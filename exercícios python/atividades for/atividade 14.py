numero= int(input("Digite o 1º número: "))
lista= []
lista.append(numero)
impar=0 
par=0
for i in range(2, 11):
    nvnum= int(input(f"Digite o {i}º número: "))
    lista.append(nvnum)
    if nvnum % 2==1: 
        impar+= 1
    else: 
        par+=1
    
print(f"qtd números pares: {par}")
print(" ")
print(f"qtd números ímpares: {impar}")