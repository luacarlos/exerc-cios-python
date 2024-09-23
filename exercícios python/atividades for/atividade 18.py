
lista= []

for i in range(5):
    num= int(input(f"digite o {i+1}º número: "))
    lista.append(num)
print(lista)
print(f"maior termo: {max(lista)}") 
print(f"menor termo: {min(lista)}") 
print(f"soma dos termos: {sum(lista)}")