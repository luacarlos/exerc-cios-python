salario= float(input("qual o salário inical: "))
aumento= 0.015
ano= 1996

while ano<2024:
    aumento= aumento*2
    salario= salario+(salario*aumento)
    ano+=1
print(f"salario {salario}")