cand1=0
cand2=0
cand3=0
cand4=0
vtnulo=0
vtbranco=0

Vt1= "1"
Vt2= "2"
Vt3= "3"
Vt4= "4"
nulo= '5'
branco= "6"

    
while True:
    print(f'Candidato 1: {cand1} votos')
    print(f'Candidato 2: {cand2} votos')
    print(f'Candidato 3: {cand3} votos')
    print(f'Candidato 4: {cand4} votos')
    print(f'votos nulos: {vtnulo}')
    print(f'votos em branco: {vtbranco}')
    print("")
    print("candidato 1: (1)")
    print("candidato 2: (2)")
    print("candidato 3: (3)")
    print("candidato 4: (4)")
    print("nulo: (5)")
    print("branco: (6)")
    print("(para sair digite 0)")
    print("")
    voto=int(input("Digite seu voto: "))
    if voto== 1:
        cand1+=1
    elif voto==2:
        cand2+=1
    elif voto==3:
        cand3+=1
    elif voto==4:
        cand4+=1
    elif voto==5:
        vtnulo+=1
    elif voto==6:
        vtbranco+=1
    elif voto==0:
        break
    else:
        print("voto inválido!")
   