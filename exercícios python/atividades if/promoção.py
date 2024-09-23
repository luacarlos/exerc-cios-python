print("1- filé duplo")
print("até 5kg: R$34,90 por KG.         acima de 5kg: R$35,80 por KG")
print("--------------------------------------------------------------------------------------------")
print("2- alcatra")
print("até 5kg: R$44,90 por KG.         acima de 5kg: R$46,80 por KG")
print("--------------------------------------------------------------------------------------------")
print("3- picanha")
print("até 5kg: R$66,90 por KG.         acima de 5kg: R$67,80 por KG")
print("--------------------------------------------------------------------------------------------")

v= 0
tp= input("qual o tipo desejado de carne? ")
if tp=="1":
    tp= 34.90
    c= "filé duplo"
elif tp=="2":
    c= "alcatra"
    tp= 44.90
elif tp=="3":
    c= "picanha"
    tp= 66.90

qt= float(input("qual a quantidade(em kg) desejada? "))
if qt>5:
    if tp=="1":
        tp= 35.80
    elif tp=="2":
        tp= 46.80
    elif tp=="3":
        tp= 67.80


pag= input("deseja realizar a compra com o nosso cartão? (S/N)")

if pag=="s" or pag=="S":
    pp= "cartão tabajara"
    v= (qt*tp)-((qt*tp)*0.05)
    d= ((qt*tp)*0.05)
else:
    pp= "outro"
    d= 0
    v= (qt*tp)

print("-----------------------------------------")
print(f"pedido: {c}")
print(f"quantidade: {qt}")
print(f"tipo de pagamento: {pp}")
print(f"valor de desconto: {d}")
print(f"valor final: {v}")
