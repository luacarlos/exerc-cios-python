popA= 80000
popB= 200000
anos= 0
cA= 3
cB= 1.5

while popA < popB:
    anos = anos + 1
    popA = popA + (popA * (cA/100))
    popB = popB + (popB * (cB/100))

print(f"Após {anos} anos, o país A ultrapassou o país B em número de habitantes.")
