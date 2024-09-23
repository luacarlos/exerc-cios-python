valor= float(input('Qual o valor do produto? '))
print('1- À vista em dinheiro ou pix, 10"%" de desconto')
print('2- À vista no cartão de crédito, 5"%" de desconto')
print('3- Em duas vezes, preço normal')
print('4- Em três vezes, 10"%" de juros')
pag= input('Qual a forma de pagamento? ')
if pag== "1":
    valor= valor - (valor*0.1)
elif pag=="2": 
    valor= valor - (valor*0.05)
elif pag=="3":
    valor = valor
elif pag=="4":
    valor= valor + (valor*0.1)
else:
    print("inválido")
dv= valor/2
tv= (valor + (valor*0.1))/3
if pag== "1" or pag=="2":
    print(f"Valor final do produto: R${valor}")
elif pag=="3":
    print(f"Valor final do produto: duas parcelas de R${dv}")
elif pag=="4":
    print(f"Valor final do produto: três parcelas de R${tv}")
else: print("Erro")