nmr = input('Insira um número: ')
centxt= "centenas"
dezetxt= "dezenas"
unitxt= "unidades"

if int(nmr) >= 1000:
    print("Número inválido")
else:
    if int(nmr)>=100:
        entena= int(nmr[0])
        dezena= int(nmr[1])
        unidade= int(nmr[2])
    elif int(nmr)>10 and int(nmr)<=99:
        centena=0
        dezena= int(nmr[0])
        unidade= int(nmr[1])
    else:
        centena=0
        dezena=0
        unidade= int(nmr[0])
    if centena==1:
        centxt= "centena"
    if dezena==1:
        dezetxt= "dezena"
    if unidade==1:
        unitxt= "unidade"

    print(f"o número possui: {centena} {centxt}, {dezena} {dezetxt} e {unidade} {unitxt}.")
if (int(nmr) >= 10 and int(nmr)<99):
      print (f"{dezena} {dezetxt} e {unidade} {unitxt}.")