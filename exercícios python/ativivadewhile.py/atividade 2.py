while True:
    u= input("nome de usuário: ")
    s= input("senha: ")
    if u==s:
        print("o nome de usuário e a senha não podem ser iguais.")
    else:
        print("sucesso!")
        break