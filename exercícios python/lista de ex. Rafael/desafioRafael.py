carrinho = []
valores = []

prodhigiene = ["Sabonete", "Shampoo", "Pasta de Dente"]
pHigiene = [1.99, 15.50, 4.75]
subHigiene = ["Higiene Pessoal"]
codHigiene = [101, 102, 103]

prodalimento = ["Arroz", "Feijão", "Macarrão"]
pAlimento = [10.90, 8.50, 5.75]
subAlimento = ["Grãos", "Massas"]
codAlimento = [201, 202, 203]

produtosCasa = ["Detergente", "Esponja", "Desinfetante"]
pCasa = [2.50, 1.75, 6.90]
subCasa = ["Limpeza"]
codCasa = [301, 302, 303]

print("==Supermercado==")
print("")
print('Você é: ')
print("a- Usuário")
print("b- Funcionário")
print("")
pf = input("Qual a alternativa correspondente ao seu perfil: ")

if pf.lower() == "a":
    nome = input("Seu nome: ")
    cpf = input("CPF válido: ")
elif pf.lower() == "b":
    matricula = int(input("Qual a sua matrícula: "))
    nome = input("Seu nome: ")
    data_nascimento = input("Data de nascimento (formato dd/mm/aaaa): ")
    cpf = input("CPF válido: ")

while True:
    if pf.lower() == "a":
        print("MENU: ")
        print("")
        print("1- Produtos")
        print("2- Carrinho")
        print("3- Finalizar Compra")
        print("")
        categoria_cliente = int(input('Qual a alternativa correspondente à opção desejada: '))
        if categoria_cliente == 1:
            print("Qual a categoria que você deseja ver: ")
            print("")
            print("1- Higiene")
            print("2- Alimentos")
            print("3- Produtos de Casa")
            escolha = int(input('Qual a alternativa correspondente à opção desejada: '))
            contE = 1
            if escolha == 1:
                print("Subcategorias: ")
                contS = 1
                for i in subHigiene:
                    print(f"{contS}. {i}")
                    contS += 1
                print('=======================================')
                while True:
                    contS=1
                    for i in subHigiene:
                        print(f"{contS}. {i}")
                        contS += 1
                    subcategoria = int(input("Escolha a subcategoria desejada (0 para voltar): "))
                    if subcategoria == 0:
                        break
                    if subcategoria > len(subHigiene) or subcategoria < 1:
                        print('Erro')
                    else: 
                        print("Os produtos dessa subcategoria são: ")
                        cont = 0
                        for i in range(len(prodhigiene)):
                            cont += 1
                            print(f"{cont}. {prodhigiene[i]}")
                        a = int(input("Qual produto você deseja adicionar ao carrinho (para finalizar digite 0): "))
                        if a == 0:
                            break
                        if a > cont or a < 1:
                            print('Erro')
                        else:
                            carrinho.append(prodhigiene[a - 1])
                            valores.append(pHigiene[a - 1])
            elif escolha == 2:
                print("Subcategorias: ")
                contS = 1
                for i in subAlimento:
                    print(f"{contS}. {i}")
                    contS += 1
                print('=======================================')
                while True:
                    contS = 1
                    for i in subAlimento:
                        print(f"{contS}. {i}")
                        contS += 1
                    subcategoria = int(input("Escolha a subcategoria desejada (0 para voltar): "))
                    if subcategoria == 0:
                        break
                    if subcategoria > len(subAlimento) or subcategoria < 1:
                        print('Erro')
                        
                    else: 
                        print("Os produtos dessa subcategoria são: ")
                        cont = 0
                        for i in range(len(prodalimento)):
                            cont += 1
                            print(f"{cont}. {prodalimento[i]}")
                        a = int(input("Qual produto você deseja adicionar ao carrinho (para finalizar digite 0): "))
                        if a == 0:
                            break
                        if a > cont or a < 1:
                            print('Erro')
                        else:
                            carrinho.append(prodalimento[a - 1])
                            valores.append(pAlimento[a - 1])
            elif escolha == 3:
                contS = 1
                print("Subcategorias: ")
                for i in subCasa:
                    print(f"{contS}. {i}")
                    contS += 1
                print('=======================================')
                while True:
                    contS=1
                    for i in subCasa:
                        print(f"{contS}. {i}")
                        contS += 1
                    subcategoria = int(input("Escolha a subcategoria desejada (0 para voltar): "))
                    if subcategoria == 0:
                        break
                    if subcategoria > len(subCasa) or subcategoria < 1:
                        print('Erro')
                    else:
                        cont = 0
                        for i in range(len(produtosCasa)):
                            cont += 1
                            print(f"{cont}. {produtosCasa[i]}")
                        a = int(input("Qual produto você deseja adicionar ao carrinho (para finalizar digite 0): "))
                        if a == 0:
                            break
                        if a > cont or a < 1:
                            print('Erro')
                        else:
                            carrinho.append(produtosCasa[a - 1])
                            valores.append(pCasa[a - 1])
            else:
                print("Escolha uma opção válida")
                categoria_cliente = int(input('Qual a alternativa correspondente à opção desejada: '))
        elif categoria_cliente == 2:
            print("Os produtos adicionados no carrinho foram: ")
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
                        carrinho.pop(r - 1)
                        valores.pop(r - 1)
        elif categoria_cliente == 3:
            print("Os produtos adicionados no carrinho foram: ")
            contador = 0
            for i in carrinho:
                print(contador + 1, ". ", i)
                contador += 1
            print("")
            valor_total = sum(valores)
            print(f"O valor total dos produtos foi: R${valor_total:.2f}")
            forma_pagamento = input("Escolha a forma de pagamento (dinheiro, pix, cartão): ")
            if forma_pagamento.lower() == "dinheiro":
                valor_entregue = float(input("Pagamento em dinheiro: "))
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
                valor_entregue = float(input("Pagamento em pix: "))
                if valor_entregue >= valor_total:
                    print("Compra aprovada.")
                else:
                    print("Erro! Saldo insuficiente.")
                    continue
            elif forma_pagamento.lower() == "cartão":
                pag = "cartão"
                tipo_cartao = input("Qual o tipo do cartão (débito/crédito): ")
                valor_entregue = float(input("Informe o saldo disponível: "))
                if valor_entregue >= valor_total:
                    print("Compra finalizada.")
                else:
                    print("Erro! Saldo insuficiente")
                    continue
            else:
                print("Forma de pagamento inválida")
                continue

            # Nota Fiscal
            imposto_nacional = valor_total * 0.05
            imposto_estadual = valor_total * 0.08
            imposto_municipal = valor_total * 0.12
            valor_impostos = imposto_nacional + imposto_estadual + imposto_municipal
            valor_final = valor_total + valor_impostos

            print("NOTA FISCAL: ")
            print("===============================")
            print(f"Valor total da compra: R${valor_total:.2f}")
            print(f"Forma de pagamento: {pag}")
            print(f"Valor entregue:  R${valor_entregue:.2f}")
            print("Impostos totais: 5% nacional, 8% estadual, 12% municipal")
            print(f"Imposto Nacional: R${imposto_nacional:.2f}")
            print(f"Imposto Estadual: R${imposto_estadual:.2f}")
            print(f"Imposto Municipal: R${imposto_municipal:.2f}")
            print(f"Valor Final com Impostos: R${valor_final:.2f}")
            print("===============================")
            print("PRODUTOS")
            cont = 0
            for i in carrinho:
                cont += 1
                print(cont, ".", i)
            print("===============================")
            break
        else:
            print("Inválido")
    elif pf.lower() == "b":
        print("O que você deseja fazer: ")
        print("")
        print("1- Consultar estoque")
        print("2- Atualizar estoque")
        print("3- Finalizar sessão")
        print("")
        estq = int(input("Qual a alternativa da opção desejada: "))
        print("")
        if estq == 1:
            print('Qual categoria do estoque você deseja visualizar: ')
            print("")
            print("1- Higiene")
            print("2- Alimentos")
            print("3- Produtos para casa")
            print("")
            cat = int(input("Qual a alternativa da categoria desejada: "))
            print("")
            if cat == 1:
                print("HIGIENE")
                print("Produtos: ", prodhigiene)
                print("Códigos: ", codHigiene)
                print("Subcategorias: ", subHigiene)
                print("Preços: ", pHigiene)
            elif cat == 2:
                print("ALIMENTOS")
                print("Produtos: ", prodalimento)
                print("Códigos: ", codAlimento)
                print("Subcategorias: ", subAlimento)
                print("Preços: ", pAlimento)
            elif cat == 3:
                print("PRODUTOS PARA CASA")
                print("Produtos: ", produtosCasa)
                print("Códigos: ", codCasa)
                print("Subcategorias: ", subCasa)
                print("Preços: ", pCasa)
            else:
                print("Inválido")
        elif estq == 2:
            print("1- Higiene")
            print("2- Alimentos")
            print("3- Produtos para casa")
            print("")
            catProd = int(input("Qual a categoria do produto a ser adicionado: "))

            if catProd == 1:
                nProd = input("Qual o nome do produto a ser adicionado: ")
                codigo = int(input("Qual o código do produto: "))
                subcat = input("Qual a subcategoria do produto ")
                preco = float(input("Qual o preço do produto: "))
                pHigiene.append(preco)
                prodhigiene.append(nProd)
                subHigiene.append(subcat)
                codHigiene.append(codigo)
            elif catProd == 2:
                nProd = input("Qual o nome do produto a ser adicionado: ")
                codigo = int(input("Qual o código do produto: "))
                subcat = input("Qual a subcategoria do produto ")
                preco = float(input("Qual o preço do produto: "))
                prodalimento.append(nProd)
                pAlimento.append(preco)
                subAlimento.append(subcat)
                codAlimento.append(codigo)
            elif catProd == 3:
                nProd = input("Qual o nome do produto a ser adicionado: ")
                codigo = int(input("Qual o código do produto: "))
                subcat = input("Qual a subcategoria do produto ")
                preco = float(input("Qual o preço do produto: "))
                produtosCasa.append(nProd)
                pCasa.append(preco)
                subCasa.append(subcat)
                codCasa.append(codigo)
            else:
                print("Inválido")
        elif estq == 3:
            print("==Supermercado==")
            print("")
            print('Você é: ')
            print("a- Usuário")
            print("b- Funcionário")
            print("")
            pf = input("Qual a alternativa correspondente ao seu perfil: ")
        else:
            print("Inválido")
