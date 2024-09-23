
popA= 80000
popB= 200000
anos= 0
cA= 0.03
cB= 0.015

while popA < popB:
    anos = anos + 1
    popA = popA + (popA * cA)
    popB = popB + (popB * cB)

print(f"Após {anos} anos, o país A ultrapassou o país B em número de habitantes.")
