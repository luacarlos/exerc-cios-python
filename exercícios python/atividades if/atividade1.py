import time 

a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))

if a==b:
        print ("ambos têm o mesmo valor")
else:
    if a > b:
        print(f"O maior número é {a}")
    else:
        print(f"O maior número é {b}")
    
time.sleep (10)