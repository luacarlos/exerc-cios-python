def calculo(larg,comp):
    area= larg*comp
    return area

def qtd(area,watts):
    quantidade= (area*watts)/60
    return quantidade

while True: 
    print('Tabela de tipos')
    print('tipo-------------------potencia(watts)')
    print('  0-------------------     12')
    print('  1-------------------     15')
    print('  2-------------------     18')
    print('  3-------------------     20')
    print('  4-------------------     22')

    tipo= int(input('qual o tipo do cômodo de acordo com a tabela: '))
    if tipo==-1:
        print('encerrando sistema...')
        break
    Largura= int(input('qual a largura do cômodo: '))
    Comprimento= int(input('qual o comprimento do cômodo: '))

    area=calculo(Largura,Comprimento)


   
    if tipo==0:
        watts= 12
        quantidade=qtd(area,watts)
        print('============================')
        print(f'a quantidade necessária de lâmpadas é: {quantidade}')
        print('')
    elif tipo==1:
        watts= 15
        quantidade=qtd(area,watts)
        print('============================')
        print(f'a quantidade necessária de lâmpadas é: {quantidade}')
        print('')
    elif tipo==2:
        watts= 18
        quantidade=qtd(area,watts)
        print('============================')
        print(f'a quantidade necessária de lâmpadas é: {quantidade}')
        print('')
    elif tipo==3:
        watts= 20 
        quantidade=qtd(area,watts)
        print('============================')
        print(f'a quantidade necessária de lâmpadas é: {quantidade}')
        print('')
    elif tipo==4:
        watts= 22
        quantidade=qtd(area,watts)
        print('============================')
        print(f'a quantidade necessária de lâmpadas é: {quantidade}')
        print('')
    else:
        print('por favor, selecione uma opção válida...')