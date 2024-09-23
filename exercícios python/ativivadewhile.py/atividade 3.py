while True:
    n= input("digite um nome com mais de três letras: ")
    i= int(input("digite a idade: "))
    sa= float(input("insira um salário maior que 0: "))
    s= input("insira o sexo: ")
    ec= input("insira o estado civil: ")
    if n==(n[0:2]):
        print("nome inválido")
        break
    elif i<=0:
        print("idade inválida")
        break
    elif sa<0:
        print("salário invalido")
        break
    elif s != "M" or s!="m" or s!="F" or s!="f" or s!="O" or s!= "o":
        print("gênero inválido")
        break
    elif ec!= "s" or ec!= "S" or ec!= "c" or ec!= "C" or ec!= "v" or ec!= "V" or ec!= "d" or ec!= "D":
        print("estado civil inválido")
        break
