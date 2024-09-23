lista_de_tarefas= []
tarefas_concluidas= []
dicionario_tarefas= []
while True: 
    print('=====GERENCIADOR DE TAREFAS=====')
    print('')
    print('1- adicionar tarefas')
    print('2- lista de tarefas')
    print('3- marcar tarefa como concluída')
    print('4- remover tarefa')
    print('0- sair')
    op= int(input('qual opcção você deseja consultar: '))
    if op==1: 
        print('=TAREFAS=')
        tarefa= input('qual tarefa você deseja adicionar à sua lista: ')
        descricao = input('Qual a descrição da tarefa que você deseja adicionar à sua lista de tarefas: ')
        desc = {'descricao': descricao, 'concluida': False}
        dicionario_tarefas.append(desc)
        lista_de_tarefas.append(tarefa)
        print('')
    elif op==2: 
        print("=LISTA DE TAREFAS=")
        contador_tarefa= 1
        for i in range(len(lista_de_tarefas)):
            tarefa = lista_de_tarefas[i]
            descricao = dicionario_tarefas[i]['descricao']
            print(f"{i + 1}- {tarefa} / informações: {descricao}")
        print("")
        print("=TAREFAS CONCLUÍDAS=")
        for i in range(len(tarefas_concluidas)):
            tarefa = tarefas_concluidas[i]
            descricao = dicionario_tarefas[i]['descricao']
            print(f"{i + 1}- {tarefa} / informações: {descricao}")
        print('')
    elif op==3:
        print('===TAREFAS PENDENTES===')
        print('')
        contador_tarefa= 1
        for i in lista_de_tarefas: 
            print(f'{contador_tarefa} - {i}')
            contador_tarefa+=1
        
        op_concluida = int(input("Qual tarefa você deseja marcar como concluída (digite o número)? "))
        if 1 <= op_concluida <= len(lista_de_tarefas):
            tarefas_concluidas.append(lista_de_tarefas.pop(op_concluida - 1))
            dicionario_tarefas[op_concluida - 1]['concluida'] = True
        else:
            print('Por favor, escolha um item que está na lista.')
    elif op==4: 
        for i in lista_de_tarefas: 
            print(f'{contador_tarefa} - {i}')
            contador_tarefa+=1
        remover_tarefa= int(input('qual tarefa você quer remover da sua lista: '))
        if 1 < remover_tarefa <= len(lista_de_tarefas):
            lista_de_tarefas.pop(remover_tarefa - 1)
        else:
            print("por favor, escolha um item que está na lista.")
    elif op==0: 
        print("encerrando sistema...")
        break
    else:
        print("por favor, selecione uma opção válida")