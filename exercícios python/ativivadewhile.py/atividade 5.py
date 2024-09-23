
popA= int(input('insira a população do país A: '))
popB= int(input('insira a população do país B: '))
anos= 0
cA= float(input("Taxa de crescimento do país A (em porcentagem): "))
cB= float(input("Taxa de crescimento do país B (em porcentagem): "))

while popA < popB:
    anos = anos + 1
    popA = popA + (popA * (cA/100))
    popB = popB + (popB * (cB/100))

print(f"Após {anos} anos, o país A ultrapassou o país B em número de habitantes.")
