produtos = []
carrinho = []
sub= ["verdura", "legume", "grãos", "carnes"]
tp= []
secoes=["alimentos","higiene","móveis"]
while True:
    print("Você é funcionário(1) ou cliente(2)?")
    tipo_usuario = int(input("Escolha uma opção: "))
    if tipo_usuario == 1:
        int(input("qual a sua matrícula: "))
        input("seu nome: ")
        input("data de nascimento (formato dd/mm/aaaa): ")
        input("cpf válido: ")
        usuario= "funcionário"
    elif tipo_usuario ==2:
        nome = input("Digite seu nome: ")
        cpf = input("Digite seu CPF: ")
        usuario = "cliente"

    if usuario == "funcionário":
        while True:
            print("1. Consultar estoque")
            print("2. Atualizar estoque")
            print("3. Adicionar novos produtos")
            print("4. Sair")
                  
            op = int(input("Escolha uma opção: "))
            if op == 1:
                for produto in produtos:
                    print(f"Código: {produto['codigo']} | Nome: {produto['nome']} | Preço: {produto['preco']} | Estoque: {produto['estoque']}")
            elif op == 2:
                codigo = int(input("Digite o código do produto para atualizar o estoque: "))
                quantidade = int(input("Digite a nova quantidade em estoque: "))
                for produto in produtos:
                    if produto["codigo"] == codigo:
                        produto["estoque"] = quantidade
                        print("Estoque atualizado.")
            elif op == 3:
                codigo = int(input("Digite o código do novo produto: "))
                nome = input("Digite o nome do novo produto: ")
                descricao = input("Digite a descrição do novo produto: ")
                tipo = input("Digite o tipo do novo produto: ")
                tp.append(tipo)
                secoes.append(tipo)
                subtipo = input("Digite o subtipo do novo produto: ")
                sub.append(subtipo)
                preco = float(input("Digite o preço do novo produto: "))
                estoque = int(input("Digite a quantidade em estoque: "))
                produtos.append({"codigo": codigo, "nome": nome, "descricao": descricao, "tipo": tipo, "subtipo": subtipo, "preco": preco, "estoque": estoque})
                print("Novo produto adicionado.")
            elif op == 4:
                usuario = ""
                break
    elif usuario=="cliente":
        print("Seções: ")
        print("")
        cont=0
        for i in secoes:
            cont+=1
            print(f'{cont}. {i}')
        int(input("Qual a alternativa desejada: "))
        print("Subtipos: ")
        print
        
        ("")
        cont=0
        for i in sub:
            cont+=1
            print(f'{cont}. {i}')
        int(input("Qual a alternativa desejada: "))
        