a= float(input("valor a: "))
b= float(input("valor b: "))
c= float(input("valor c: "))
dlt= b**2 - 4*a*c
x1= (-(b) + dlt**0.5)/(2*a)
x2= (-(b) - dlt**0.5)/(2*a)

if a==0:
    print("Valor inválido")

elif dlt<0:
    print("A equação não possui raízes")

elif dlt==0:
    print(f"A equação possui apenas uma raíz real: {dlt}")

elif dlt>0:
    print(f"A equação possui mais de uma raíz real: {x1} e {x2}")

