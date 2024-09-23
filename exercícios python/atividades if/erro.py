# Sistema de cadastro de usuários

usuario1_nome = "alice"
usuario1_senha = "1234"

usuario2_nome = "bob"
usuario2_senha = "abcd"

usuario3_nome = "carol"
usuario3_senha = "9876"

print("Bem-vindo ao sistema de cadastro de usuários!")

opcao = (input("Escolha uma opção - 1: Login, 2: Cadastro:, 3: Calcular Consumo de Água: "))

if opcao == "1":
    usuario = input("Digite seu nome de usuário: ")
    senha = input("Digite sua senha: ")

    if (usuario == usuario1_nome and senha == usuario1_senha) or (usuario == usuario2_nome and senha == usuario2_senha) or (usuario == usuario3_nome and senha == usuario3_senha):
        print("Login bem-sucedido!") 
    
    else:
        print("Nome de usuário ou senha incorretos!")
if opcao == "2":
    print("Cadastre-se") 
    novo_usuario_nome = input("Digite seu novo nome de usuário: ")
    novo_usuario_senha = input("Digite sua nova senha: ")

    print("Cadastro realizado com sucesso!")

if opcao == "3":
     consumo_total = float(input("Digite o consumo total de água (em metros cúbicos): "))
     numero_pessoas = int(input("Digite o número de pessoas na residência: "))
     dias = (input("Digite o número de dias do período de consumo: "))
     consumo_por_pessoa_por_dia = consumo_total / int(numero_pessoas * dias)

     if consumo_por_pessoa_por_dia > 200:
        print("O consumo de água da residência está elevado.")
     elif consumo_por_pessoa_por_dia <= 100:
         print("O consumo de água da residência está moderado.")
     else:
         print(("O consumo de água da residência está abaixo da média."))

print("Obrigado por utilizar nosso sistema!")