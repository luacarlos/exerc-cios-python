produtos_disponiveis = []
carrinho_de_compras = []
tipo_usuario = ""

while True:
    print("Você é funcionário (1) ou cliente (2)?")
    escolha_usuario = input("Escolha uma opção: ")
    if escolha_usuario == "1":
        matricula_func = int(input("Digite sua matrícula: "))
        nome_func = input("Digite seu nome: ")
        nascimento_func = input("Digite sua data de nascimento (DD/MM/AAAA): ")
        cpf_func = input("Digite seu CPF: ")
        tipo_usuario = "funcionario"
    elif escolha_usuario == "2":
        nome_cliente = input("Digite seu nome: ")
        cpf_cliente = input("Digite seu CPF: ")
        tipo_usuario = "cliente"

    if tipo_usuario == "funcionario":
        while True:
            print("1. Consultar Produtos")
            print("2. Atualizar Estoque")
            print("3. Adicionar Produtos")
            print("4. Sair")
            opcao_func = int(input("Escolha uma opção: "))
            if opcao_func == 1:
                for item in produtos_disponiveis:
                    print(f"Código: {item['codigo']} | Nome: {item['nome']} | Preço: {item['preco']} | Estoque: {item['estoque']}")
            elif opcao_func == 2:
                cod_produto = int(input("Digite o código do produto para atualizar o estoque: "))
                nova_quantidade = int(input("Digite a nova quantidade: "))
                for item in produtos_disponiveis:
                    if item["codigo"] == cod_produto:
                        item["estoque"] = nova_quantidade
                        print("Estoque atualizado.")
            elif opcao_func == 3:
                cod_novo = int(input("Digite o código do novo produto: "))
                nome_novo = input("Digite o nome do novo produto: ")
                desc_novo = input("Digite a descrição do novo produto: ")
                tipo_novo = input("Digite o tipo do novo produto: ")
                subtipo_novo = input("Digite o subtipo do novo produto: ")
                preco_novo = float(input("Digite o preço do novo produto: "))
                estoque_novo = int(input("Digite a quantidade em estoque: "))
                produtos_disponiveis.append({"codigo": cod_novo, "nome": nome_novo, "descricao": desc_novo, "tipo": tipo_novo, "subtipo": subtipo_novo, "preco": preco_novo, "estoque": estoque_novo})
                print("Novo produto adicionado.")
            elif opcao_func == 4:
                tipo_usuario = ""
                break

    elif tipo_usuario == "cliente":
        while True:
            lista_secoes = []
            for item in produtos_disponiveis:
                found = False
                for secao in lista_secoes:
                    if item["tipo"] == secao:
                        found = True
                        break
                if not found:
                    lista_secoes.append(item["tipo"])

            print("Seções: ")
            for i in range(len(lista_secoes)):
                print(f"{i + 1}. {lista_secoes[i]}")
            print(f"{len(lista_secoes) + 1}. Finalizar Compra")
            print(f"{len(lista_secoes) + 2}. Ver Carrinho")
            secao_escolhida = input("Escolha uma seção: ")

            if int(secao_escolhida) - 1 >= len(lista_secoes):
                if int(secao_escolhida) == len(lista_secoes) + 1:
                    print("Carrinho: ")
                    valor_total = 0
                    for item in carrinho_de_compras:
                        prod = item["produto"]
                        qtd = item["quantidade"]
                        subtotal = prod["preco"] * qtd
                        valor_total += subtotal
                        print(f"Produto: {prod['nome']} - Quantidade: {qtd} - Subtotal: R${subtotal}")
                    print(f"Total: R${valor_total}")

                    forma_pagamento = input("Escolha a forma de pagamento (dinheiro, pix, cartão): ")
                    if forma_pagamento == "dinheiro":
                        valor_entregue = float(input("Informe o valor entregue: "))
                        if valor_entregue > valor_total:
                            troco = valor_entregue - valor_total
                            print(f"Compra aprovada. Troco: R${troco}")
                        elif valor_entregue == valor_total:
                            print("Compra aprovada. Sem troco.")
                        else:
                            print("Valor insuficiente. Compra não autorizada.")
                    elif forma_pagamento == "pix":
                        saldo_pix = float(input("Informe o saldo disponível: "))
                        if saldo_pix >= valor_total:
                            print("Compra aprovada.")
                        else:
                            print("Saldo insuficiente. Compra não autorizada.")
                    elif forma_pagamento == "cartão":
                        tipo_cartao = input("Informe o tipo de cartão (débito, crédito, voucher): ")
                        saldo_cartao = float(input("Informe o saldo disponível: "))
                        if saldo_cartao >= valor_total:
                            print("Compra aprovada.")
                        else:
                            print("Saldo insuficiente. Compra não autorizada.")
                    else:
                        print("Forma de pagamento inválida. Compra não autorizada.")

                    print("Nota Fiscal: ")
                    total_impostos = valor_total * 0.25
                    imposto_nacional = valor_total * 0.05
                    imposto_estadual = valor_total * 0.08
                    imposto_municipal = valor_total * 0.12
                    for item in carrinho_de_compras:
                        prod = item["produto"]
                        qtd = item["quantidade"]
                        subtotal = prod["preco"] * qtd
                        print(f"Produto: {prod['nome']} - Quantidade: {qtd} - Subtotal: R${subtotal}")
                    print(f"Total: R${valor_total}")
                    print(f"Imposto Nacional (5%): R${imposto_nacional}")
                    print(f"Imposto Estadual (8%): R${imposto_estadual}")
                    print(f"Imposto Municipal (12%): R${imposto_municipal}")
                    print(f"Total de Impostos: R${total_impostos}")
                    break
                elif int(secao_escolhida) == len(lista_secoes) + 2:
                    print("Carrinho: ")
                    valor_total = 0
                    for item in carrinho_de_compras:
                        prod = item["produto"]
                        qtd = item["quantidade"]
                        subtotal = prod["preco"] * qtd
                        valor_total += subtotal
                        print(f"Produto: {prod['nome']} - Quantidade: {qtd} - Subtotal: R${subtotal}")
                    print(f"Total: R${valor_total}")
                else:
                    print("Seção inválida.")
            else:
                tipo_secao = lista_secoes[int(secao_escolhida) - 1]
                lista_subtipos = []
                for item in produtos_disponiveis:
                    if item["tipo"] == tipo_secao:
                        found = False
                        for subtipo in lista_subtipos:
                            if item["subtipo"] == subtipo:
                                found = True
                                break
                        if not found:
                            lista_subtipos.append(item["subtipo"])

                print("Subtipos: ")
                for i in range(len(lista_subtipos)):
                    print(f"{i + 1}. {lista_subtipos[i]}")
                subtipo_escolhido = input("Escolha um subtipo: ")

                if int(subtipo_escolhido) - 1 >= len(lista_subtipos):
                    print("Subtipo inválido.")
                else:
                    tipo_subtipo = lista_subtipos[int(subtipo_escolhido) - 1]
                    print("Produtos: ")
                    for item in produtos_disponiveis:
                        if item["tipo"] == tipo_secao and item["subtipo"] == tipo_subtipo:
                            print(f"Código: {item['codigo']} - Nome: {item['nome']} - Preço: R${item['preco']} - Estoque: {item['estoque']}")

                    codigo_produto = input("Informe o código do produto para adicionar ao carrinho: ")
                    codigo_produto = int(codigo_produto)
                    for item in produtos_disponiveis:
                        if item["codigo"] == codigo_produto:
                            qtd_produto = int(input(f"Quantos {item['nome']} você deseja adicionar? "))
                            if qtd_produto <= item["estoque"]:
                                carrinho_de_compras.append({"produto": item, "quantidade": qtd_produto})
                                item["estoque"] -= qtd_produto
                                print(f"{qtd_produto} {item['nome']} adicionado(s) ao carrinho.")
                            else:
                                print("Quantidade indisponível no estoque.")