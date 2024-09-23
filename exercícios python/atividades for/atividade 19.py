lista= []

for i in range(5):
    num= int(input(f"digite o {i+1}º número: "))
    if num<0 or num>1000:
        print("termo inválido")
        break
    else: 
        lista.append(num)
print(lista)
print(f"maior termo: {max(lista)}") 
print(f"menor termo: {min(lista)}") 
print(f"soma dos termos: {sum(lista)}")

