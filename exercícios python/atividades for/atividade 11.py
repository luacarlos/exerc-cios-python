num1= int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
lista=[]

if num1 < num2:
   
    print(f"soma dos números no intervalo de {num1} a {num2}:")
    for i in range(num1, num2 + 1):
        
        lista.append(i)
    print(sum(lista))
