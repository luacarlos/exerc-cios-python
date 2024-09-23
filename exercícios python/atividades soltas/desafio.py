carrinho= []
valores=[]

prodhigiene= ["Sabonete", "Shampoo", "Pasta de Dente"]
pHigiene= [1.99, 15.50, 4.75]
subHigiene= ["Higiene Pessoal"]
codHigiene=[101, 102, 103]

prodalimento= ["Arroz", "Feijão", "Macarrão"]
pAlimento= [10.90, 8.50, 5.75]
subAlimento=["Grãos","Massas"]
codAlimento=[201, 202, 203]

produtosCasa= ["Detergente", "Esponja", "Desinfetante"]
pCasa= [2.50, 1.75, 6.90]
subCasa=["Limpeza"]
codCasa=[301, 302, 303]

print("==Supermercado==")
print("")
print('você é: ')
print("a- usuário")
print("b- funcionário")
print("")
pf= input("qual a alternativa correspondente ao seu perfil: ")

if pf=="a" or pf=="A":
    input("seu nome: ")
    input("cpf válido: ")
elif pf=="b" or pf=="B":
    int(input("qual a sua matrícula: "))
    input("seu nome: ")
    input("data de nascimento (formato dd/mm/aaaa): ")
    input("cpf válido: ")

while True: 
    if pf=="a" or pf=="A":
        print("MENU: ")
        print("")
        print("1- produtos")
        print("2- carrinho")
        print("3- finalizar compra")
        print("")
        categoria_cliente= int(input('qual a alternativa correspondente a opção desejada: '))
        if categoria_cliente==1:
            print("qual a categoria que você deseja ver: ")
            print("")
            print("1- higiene")
            print("2- alimentos")
            print("3- produtos de casa")
            escolha= int(input('qual a alternativa correspondente a opção desejada: '))
            contE= 1
            if escolha==1:
                print("subcategorias: ")
                contS=0
                for i in subHigiene:
                    print(f"{contS}. {i}")
                    contS+=1
                print('=======================================')
                while True: 
                    print("os produtos dessa categoria, registrados no sistema são: ")
                    cont=0
                    for i in prodhigiene:
                        cont+=1
                        print(f"{cont}. {i}")
                        
                    a=int(input("qual produto você deseja adicionar ao carrinho (para finalizar a escolha digite 0): "))
                    if a==0:
                        break
                    if a>len(prodhigiene) or a<1:
                        print('erro')
                    else:
                        carrinho.append(prodhigiene[a-1])
                        valores.append(pHigiene[a-1])
            elif escolha==2:
                print("subcategorias: ")
                contS=1
                for i in subAlimento:
                    print(f"{contS}. {i}")
                    contS+=1
                print('=======================================')
                while True: 
                    print("os produtos dessa categoria, registrados no sistema são: ")
                    cont=0
                    for i in prodalimento:
                        cont+=1
                        print(f"{cont}. {i}")
                    a=int(input("qual produto você deseja adicionar ao carrinho (para finalizar a escolha digite 0): "))
                    if a==0:
                        break
                    if a>len(prodalimento) or a<1:
                        print('erro')
                    else:
                        carrinho.append(prodalimento[a-1])
                        valores.append(pAlimento[a-1])
            elif escolha==3:
                contS=1
                print("subcategorias: ")
                for i in subCasa:
                    contS=1
                    print(f"{contS}. {i}")
                    contS+=1
                print('=======================================')
                while True: 
                    cont=1
                    for i in produtosCasa:
                        print(f"{cont}. {i}")
                        cont+=1
                    a=int(input("qual produto você deseja adicionar ao carrinho (para finalizar a escolha digite 0): "))
                    if a==0:
                        break
                    if a>len(produtosCasa) or a<1:
                        print('erro')
                    else:
                        carrinho.append(produtosCasa[a-1])
                        valores.append(pCasa[a-1])
            else:
                print("escolha uma opção válida")
                categoria_cliente= int(input('qual a alternativa correspondente a opção desejada: '))
        elif categoria_cliente==2: 
            print("os produtos  adicionados no carrinho foram: ")
            print(carrinho)
            print("Deseja remover algum item? (s/n)")
            if input().lower() == 's':
                while True:
                    print(carrinho)
                    r = int(input("Qual item deseja remover (0 para sair): "))
                    if r == 0:
                        break
                    if r > len(carrinho) or r < 1:
                        print("Erro")
                    else:
                        carrinho.pop(r-1)
                        valores.pop(r-1)
        elif categoria_cliente==3:
            print("os produtos adicionados no carrinho foram: ")
            contador= 0
            for i in carrinho:
                print(contador+1, ". ",i)
                contador+=1
            print("")
            valor_total= sum(valores)
            print(f"o valor total dos produtos foi: R${valor_total:.2f}")
            forma_pagamento = input("Escolha a forma de pagamento (dinheiro, pix, cartão): ")
            if forma_pagamento.lower() == "dinheiro":
                valor_entregue = float(input("pagamento em dinheiro: "))
                pag = "dinheiro"
                if valor_entregue > valor_total:
                    troco = valor_entregue - valor_total
                    print(f"Troco: R${troco:.2f}")
                elif valor_entregue == valor_total:
                    print("Sem troco.")
                else:
                    print("Valor insuficiente. Compra não autorizada.")
                    continue
            elif forma_pagamento.lower() == "pix":
                pag = "pix"
                valor_entregue = float(input("pagamento em pix: "))
                if valor_entregue >= valor_total:
                    print("compra aprovada.")
                else:
                    print("erro! Saldo insuficiente.")
                    continue
            elif forma_pagamento.lower() == "cartão":
                pag = "cartão"
                tipo_cartao = input("qual o tipo do cartão (débito/crédito): ")
                valor_entregue = float(input("Informe o saldo disponível: "))
                if valor_entregue >= valor_total:
                    print("compra finalizada.")
                else:
                    print("erro! Saldo insuficiente")
                    continue
            else:
                print("forma de pagamento inválida")
                continue
            
            imposto_nacional = valor_total * 0.05
            imposto_estadual = valor_total * 0.08
            imposto_municipal = valor_total * 0.12
            valor_impostos = imposto_nacional + imposto_estadual + imposto_municipal
            valor_final = valor_total + valor_impostos
            
            print("NOTA FISCAL: ")
            print("===============================")
            print(f"valor total da compra: R${valor_total:.2f}")
            print(f"forma de pagamento: {pag}")
            print(f"valor entregue:  R${valor_entregue:.2f}")
            print("impostos totais: 5% nacional, 8% estadual, 12% municipal")
            print(f"Imposto Nacional: R${imposto_nacional:.2f}")
            print(f"Imposto Estadual: R${imposto_estadual:.2f}")
            print(f"Imposto Municipal: R${imposto_municipal:.2f}")
            print(f"Valor Final com Impostos: R${valor_final:.2f}")
            print("===============================")
            print("PRODUTOS")
            cont= 0
            for i in carrinho: 
                cont+=1
                print(cont, ".", i)
            print("===============================")
            break
        else:
            print("inválido")
    elif pf=="b" or pf=="B":
        print("o que você deseja fazer: ")
        print("")
        print("1- consultar estoque")
        print("2- atualizar estoque")
        print("3- finalizar sessão")
        print("")
        estq= int(input("qual a alternativa da opção desejada: "))
        print("")
        if estq==1:
            print('qual categoria do estoque você deseja visualizar: ')
            print("")
            print("1- higiene")
            print("2- alimentos")
            print("3- produtos para casa")
            print("")
            cat= int(input("qual a alternativa da categoria desejada: "))
            print("")
            if cat==1:
                print("")
                print("produtos: ")
                for i in prodhigiene:
                    print(i)
                print("códigos: ")
                for i in codHigiene:
                    print(i)
                print("subcategoria: ")
                for i in subHigiene:
                    print(i)
                print("preços: ")
                for i in pHigiene:
                    print(i)
            elif cat==2:
                print("produtos: ")
                for i in prodalimento:
                    print(i)
                print("códigos: ")
                for i in codAlimento:
                    print(i)
                print("subcategoria: ")
                for i in subAlimento:
                    print(i)
                print("preços: ")
                for i in pAlimento:
                    print(i)
            elif cat==3:
                print("produtos: ")
                for i in produtosCasa:
                    print(i)
                print("códigos: ")
                for i in codCasa:
                    print(i)
                print("preços: ")
                for i in pCasa:
                    print(i)
            else:
                print("")
                print("inválido")
                print("")
        elif estq==2:
            print("1- higiene")
            print("2- alimentos")
            print("3- produtos para casa")
            print("")
            catProd= (int(input("qual a categoria do produto a ser adicionado: ")))
        
            if catProd==1: 
                nProd= input("qual o nome do produto a ser adicionado: ")
                codigo= int(input("qual o código do produto: "))
                subcat= (input("qual a subcategoria do produto "))
                preco= float(input("qual o preço do produto: "))
                pHigiene.append(preco)
                prodhigiene.append(nProd)
                subHigiene.append(subcat)
                codHigiene.append(codigo)
            elif catProd==2:
                nProd= input("qual o nome do produto a ser adicionado: ")
                codigo= int(input("qual o código do produto: "))
                subcat= (input("qual a subcategoria do produto "))
                preco= float(input("qual o preço do produto: "))
                prodalimento.append(nProd)
                pAlimento.append(preco)
                subAlimento.append(subcat)
                codAlimento.append(codigo)
            elif catProd==3:
                nProd= input("qual o nome do produto a ser adicionado: ")
                codigo= int(input("qual o código do produto: "))
                subcat= (input("qual a subcategoria do produto "))
                preco= float(input("qual o preço do produto: "))
                produtosCasa.append(nProd)
                pCasa.append(preco)
                subCasa.append(subcat)
                codCasa.append(codigo)
            else: 
                print("inválido")
        elif estq==3:
            print("==Supermercado==")
            print("")
            print('você é: ')
            print("a- usuário")
            print("b- funcionário")
            print("")
            pf= input("qual a alternativa correspondente ao seu perfil: ")
        else:
            print("inválido")