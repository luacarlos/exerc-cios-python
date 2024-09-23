sal= int(input("Digite o valor da hora trabalhada: "))
hr= int(input("Quantas horas foram trabalhadas no mês? "))
sb= (sal*24) * (hr/24)
fgts= sb*0.11
inss= sb*0.1

if sb<= 900:
    ir= sb*1
    pir= "insento"
elif sb<= 1500:
    ir= sb*0.05
    pir= 5
elif sb<= 2500:
    ir= sb*0.2
    pir= 20

td= (ir + inss)
sl= (sb - td)
print(f"Salário Bruto:   ({sal} * {hr}):  R${sb}")
print(f"(-)IR ({pir}%):    R$:{ir}")
print(f"(-)INSS (10%):    R${inss}")
print(f"FGTS (11%):    R${fgts}")
print(f"Total de descontos:    R${td}")
print(f"Salário Líquido:    R${sl}")