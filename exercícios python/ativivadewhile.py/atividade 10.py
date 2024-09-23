qtd= 0
qtcad=0
qtcan=0
qtlap=0
qtbor=0
qtreg=0

while  True:
    print('------------------------------------------------------')
    print("E- Entrada no estoque")
    print("S- Saída no estoque")
    print("R- Relatório")
    print("X- Sair")
    op= input("Escolha a operação conforme as opções acima: ")


    print('------------------------------------------------------')
    print(f"cadernos: {qtcad}")
    print(f"canetas: {qtcan}")
    print(f"lápis: {qtlap}")
    print(f"borrachas: {qtbor}")
    print(f"réguas: {qtreg}")
    cod= int(input("insira o código do produto: "))
    qtd= int(input("insira a quanditidade de produtos: "))

    

    if op=="E" or op=="e":
        if cod==10:
            print("caderno")
            if qtcad<0:
                print('------------------------------------------------------')
                print("erro")
                print('------------------------------------------------------')
            else:
                qtcad=+qtd
        elif cod==20:
            print("caneta")
            if qtcan<0:
                print('------------------------------------------------------')
                print("erro")
                print('------------------------------------------------------')
            else:
                qtcan=+qtd
        elif cod==30:
            print("lápis")
            if qtlap<0:
                print('------------------------------------------------------')
                print("erro")
                print('------------------------------------------------------')
            else:
                qtlap=+qtd
        elif cod==30:
            print("borracha")
            if qtbor<0:
                print('------------------------------------------------------')
                print("erro")
                print('------------------------------------------------------')
            else:
                qtbor=+qtd
        elif cod==40:
            print("régua")
            if qtreg<0:
                print('------------------------------------------------------')
                print("erro")
                print('------------------------------------------------------')
            else:
                qtreg=+qtd
        
    if op=="S" or op=="s":
        if cod==10:
            print("caderno")
            if qtcad<qtd:
                print('------------------------------------------------------')
                print("erro")
                print('------------------------------------------------------')
            else:
                qtcad-=qtd
                if qtcad<0:
                    print('quantidade inválida')
        elif cod==20:
            print("caneta")
            if qtcan<0:
                print('------------------------------------------------------')
                print("erro")
                print('------------------------------------------------------')
            else:
                qtcan-=qtd
                if qtcad<0:
                    print('quantidade inválida')
        elif cod==30:
            print("lápis")
            if qtlap<0:
                print('------------------------------------------------------')
                print("erro")
                print('------------------------------------------------------')
            else:
                qtlap-=qtd
                if qtcad<0:
                    print('quantidade inválida')
        elif cod==30:
            print("borracha")
            if qtbor<0:
                print('------------------------------------------------------')
                print("erro")
                print('------------------------------------------------------')
            else:
                qtbor-=qtd
                if qtcad<0:
                    print('quantidade inválida')
        elif cod==40:
            print("régua")
            if qtreg<0:
                print('------------------------------------------------------')
                print("erro")
                print('------------------------------------------------------')
            else:
                qtreg=-qtd
                if qtcad<0:
                    print('quantidade inválida')
    
    if op=="r" or op=="R":
        print('------------------------------------------------------')
        print(f"cadernos: {qtcad}")
        print(f"canetas: {qtcan}")
        print(f"lápis: {qtlap}")
        print(f"borrachas: {qtbor}")
        print(f"réguas: {qtreg}")
        print('------------------------------------------------------')
    if op=="x" or op=="X":
        break