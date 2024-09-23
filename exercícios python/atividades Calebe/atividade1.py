n1= int(input("primeiro número: "))
n2= int(input('segundo número: '))
n3= int(input('terceiro número: '))
if n1>n2 and n1>n3 and n2>n3:
    print(f"os números escritos em ordem decrescente são: {n3}, {n2} e {n1}")
elif n2>n1 and n2>n3 and n1>n3:
    print(f"os números escritos em ordem decrescente são: {n2}, {n1} e {n3}")
elif  n3>n1 and n3>n2 and n1>n2:
    print(f'os n)