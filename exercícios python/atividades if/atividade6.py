data= input("insira a data no formato (dd/mm/aaaa)")

dia=int(data[0:2])
mes=int(data[3:5])
ano=int(data[6: ])

if data[2] and data[5]=="/" and (dia>1 and dia<=31) and (mes >0 and mes <=12) and (ano >0):
        print("data válida")

else: 
    print("data inválida")
