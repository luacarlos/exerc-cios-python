
sl= float(input("Salário atual: "))

if sl<500.00:
    print(f"O valor com reajuste de 15% é: R${sl + (sl*0.15)}")
elif sl>1000.00:
    print(f"O valor com o reajuste de 10% é: R${sl + (sl*0.1)}")
elif 500<sl<1000:
    print(f"O valor com o reajuste de 5% é: R${sl + (sl*0.05)}")
