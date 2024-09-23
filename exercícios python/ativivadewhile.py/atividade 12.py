

while True:
    num1= float(input("insira o primeiro número: "))
    num2= float(input("insira o segundo número: "))
    print('')
    print("qual a operação desejada? ")
    print('')
    print("a) adição")
    print("b) subtração")
    print("c) multiplicação")
    print("d) divisão")
    print("e) sair")
    print("")
    op= input("letra correspondente a operação: ")
    print("")
    if op=="a" or op=="A":
        result= num1+num2
    elif op=="b" or op=="B":
        result= num1-num2
    elif op=="c" or op=="C":
        result= num1*num2
    elif op=="d" or op=="D":
        result= num1/num2
    elif op=="e" or op=="E":
        break
    else: 
        print("erro")
    
    if result % 2 == 0:
        imparpar="par"
    else:
        imparpar="impar"
    

    if result>0:
        posneg= "positivo"
    elif result==0:
        posneg= "neutro"
    else:
        posneg= "negativo"
    
    if result==int:
        intdec= "inteiro"
    else:
        intdec= "decimal"
    
    print(f"o resultado da operação é {result}, o número é {imparpar}, é {posneg} e é {intdec}.")
    print("")
    print("deseja continuar?")
    print("a) sim")
    print("b) não")
    rep=input("alternativa correspondente: ")
    while True:
        if rep=="b" or rep=="B":
            break
        elif rep=="a" or rep=="A":
            break
        else:
            print("selecione uma opção válida: ")
            rep=input("alternativa correspondente: ")
    if rep=="b" or rep=="B":
        break