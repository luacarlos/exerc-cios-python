print('Bem-vindo(a) à lanchonete Burgão!')
cd1= (input("Qual o codigo do Lanche? "))
l= 0
if  cd1=="100":
    l= 11.20
    n= "Cachorro quente"
elif cd1=="101":
    l= 8.30
    n= "Ovo simples"
elif cd1== "102":
    l= 11.50
    n= "Bauru com Ovo"
elif  cd1== "103":
    l= 16.20
    n= "Hambúrguer"
else:
    print("Pedido inválido.")
print(f"Seu pedido foi: Um {n}, no valor de R${l}; total: {l}.")

bb= input("Deseja algo para  beber? S/N: ")

if bb== 's' or bb=='S':
    cdb= (input("Qual o codigo da Bebida? "))
    pb=""
    be= 0
    if cdb== "201":
        be= 6.00
        pb= "Refrigerante"
    elif cdb== "202":
        be= 7.50
        pb= "Suco"
    elif cdb== "203":
        be= 4.70
        pb= "Água Mineral"
    else:
        print( 'Pedido inválido.')
    total= l + be
    print (f'Seu pedido foi: Um {n}, no valor de R${l}; E um(a) {pb}, no valor de R${be}. total: R$ {total}')

if bb== 'n' or bb=='N':
    print(f"Seu pedido foi: Um {n}, no valor de R${l}; Sem bebida. total: {l}")
