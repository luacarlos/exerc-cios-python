comeco= int(input("você é usuário(1) ou médico(2): "))
consultas= []
historico= []

while True:
    if comeco==1: 
            print("=OPÇÕES=")
            print("(1) agendar consulta")
            print("(2) ver histórico de consultas")
            print("(3) voltar")
            selecionar= int(input("o que você deseja fazer: "))

            if selecionar==1: 
                print("preencha os dados a seguir para marcar a consulta: ")
                dado= {}
                dado['nome']= input("seu nome: ")
                dado['cpf']= int(input("seu cpf: "))
                dado['idade']= int(input("sua idade: "))
                if dado['idade']<1 or dado['idade']>1000:
                    print("por favor, digite uma idade válida")
                    dado['idade']= int(input("sua idade: "))
                dado['horario']= (input("horário da consulta: "))
                historico.append(dado['nome'])
                historico.append(dado['horario'])
                consultas.append(dado)
                print("consulta maracada")
            elif selecionar==2: 
                if historico==[]:
                    print("não há consultas no seu histórico")
                    print("")
                    print("=OPÇÕES=")
                    print("(1) agendar consulta")
                    print("(2) ver histórico de consultas")
                    print("(3) voltar")
                    selecionar= int(input("o que você deseja fazer: "))
                else: 
                    print("===histórico de consultas===")
                    print(historico)
                    print("")
                    print("=OPÇÕES=")
                    print("(1) agendar consulta")
                    print("(2) ver histórico de consultas")
                    print("(3) voltar")
                    selecionar= int(input("o que você deseja fazer: "))
            elif selecionar==3: 
                comeco= int(input("você é usuário(1) ou médico(2): "))
            else:
                print("erro")
    elif comeco==2: 
        print("=OPÇÕES=")
        print("(1)ver lista de consultas")
        print("(2)realizar ")
        print("(3)voltar")
        consulta= int(input("o que você deseja fazer:"))
        if consulta==1: 
            print("as consultas registradas até o momento são: ")
            print("")
            print(consultas)
        elif consulta==2: 
            print("qual das seguintes consultas você irá atender: ")
            cont=0
            for i in consultas: 
                cont+=1
                print(f"{cont} - {consultas[cont-1]}")
            atender= int(input("qual o número da consulta que será atendida: "))
            if atender>len(consultas) or atender<0: 
                print("erro")
            else: 
                consultas.pop(atender-1)
                print("consulta realizada")
        elif consulta==3: 
            comeco= int(input("você é usuário(1) ou médico(2): "))