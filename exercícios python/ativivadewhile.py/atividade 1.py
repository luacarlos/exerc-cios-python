while True:
    n= int(input("informe uma nota de 0 a 10: "))
    if n<0 or n>10:
        print("por favor insira um valor válido")
    else:
        print("valor válido")
        break