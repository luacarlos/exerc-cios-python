nt= float(input("insira uma nota de 0 a 10: "))

while True: 
    if nt>10 or nt<0:
        print('nota inválida')
        nt= float(input("insira uma nota de 0 a 10: "))

    else: 
        print('concluído')
        break