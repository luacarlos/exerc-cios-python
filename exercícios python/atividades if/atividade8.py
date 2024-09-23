print('saque minimo: 10, saque máximo: 600')
s=input('Qual o valor do saque: ')

if int(s)>99:
    nota100= int(s[0])
    nota10=int(s[1])
    nota1=int(s[2])
elif int(s) >9 and int(s) :
    nota100=0
    nota10=int(s[0])
    nota1=int(s[1])
else:
    nota100=0
    nota10=0
    nota1=int(s[0])



if int(s)<10 or int(s)>600:
    print('Não é possível sacar esse valor')
elif nota10>5:
    nota50= (nota10 -(nota10-5))/5 
elif nota10==5:
    nota50=1
else:
    nota50=0

if nota1>5:
        nota5= (nota1 -(nota1-5))/5
elif nota1==5:
    nota5=1
else:
    nota5=0

if nota10>5:
    nota10=nota10-5
else:
    nota10=nota10
if nota1>5:
    nota1=nota1-5
else:
    nota1=nota1

texto100=f"{nota100} notas de 100,00R$"
texto50=f"{nota50} notas de 50,00R$"
texto10=f"{nota10} notas de 10,00R$"
texto5=f"{nota5} notas de 5,00R$ "
texto1=f"{nota1} notas de 1,00R$"

print(texto100)
print(texto50)
print(texto10)
print(texto5)
print(texto1)