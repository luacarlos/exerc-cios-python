usuario= input("digite o nome de usuário: ")
senha= input("digite a senha: ")

while usuario==senha or senha==usuario:
    print("erro")
    usuario= input("digite o nome de usuário: ")
    senha= input("digite a senha: ")