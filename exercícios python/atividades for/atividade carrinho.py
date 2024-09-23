#faça um programa que mostra um menu, onde o usuário consiga ver o carrinho de compra e uma lista de produtos, e selecionar os produtos no carrinho
lista=[]


while True:
    print("")
    print("o que você deseja fazer")
    print("")
    print("A) ver carrinho")
    print("B) ver produtos")
    print("C) sair")
    print("")
    op= input("qual a letra da alternativa que você deseja: ")
    if op=="c" or op=="C":
        break
    elif op=="b" or op=="B":
        print("produtos: ")
        print("")
        print("1) caneta")
        print("2) lápis")
        print("3) borracha")
        print("")
        sel= int(input("qual o número do produto desejado: "))
        print("")
        if sel==1:  
            lista.append("caneta")
        elif sel==2:
            lista.append("lápis")
        elif sel==3:
            lista.append("borracha")
        else:
            print("inválido")
    elif op=="a" or op=="A":
        print("os itens adicionados ao carrinho foram: ")
        print(lista )
    else: 
        print("inválido")