maior_peso=0
menor_peso=1000
maior_altura=0
menor_altura=5
codigo_ma=0
codigo_mna=0
codigo_mnp=0
codigo_mp=0
mediaA=0
mediaP=0
contador=0

while True: 
  cod=int(input("seu código: "))
  if cod==0:
    break
  peso= float(input("seu peso (em kg): "))
  altura= int(input("sua altura (em centímetros): "))
  contador+=1
  mediaA+=altura
  mediaP+=peso

  if peso>maior_peso:
    maior_peso=peso
    codigo_mp= cod
  if altura>maior_altura:
    maior_altura=altura
    codigo_ma= cod
  if altura<menor_altura:
    menor_altura=altura
    codigo_mna=cod
  if peso<menor_peso:
    menor_peso=peso
    codigo_mnp=cod

print(contador)
print(f"maior altura: {maior_altura} cm, do cliente com o código: {codigo_ma}")
print(f"menor altura: {menor_altura} cm, do cliente com o código: {codigo_mna} ")
print(f"maior peso: {maior_peso} kg, do clienter com o código: {codigo_mp}")
print(f"menor peso: {menor_peso} kg, do clienter com o código: {codigo_mnp}")
print(f"media das alturas: {mediaA/contador} cm")
print(f"media dos pesos: {mediaP/contador} kg")