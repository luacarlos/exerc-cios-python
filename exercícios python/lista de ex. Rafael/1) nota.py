nota= float(input("Digite uma nota de 0 a 10: "))
while nota<0 or nota>10:
    print("digite uma nota válida")
    nota= float(input("Digite uma nota de 0 a 10: "))
    if nota>0 and nota<=10:
        print("nota válida")