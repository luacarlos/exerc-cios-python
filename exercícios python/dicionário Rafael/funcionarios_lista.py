func= []
func_MS= 0

for i in range(4): 
    funcionario= {}
    funcionario["nome"]= input("nome: ")
    funcionario["funcao"]= input("função: ")
    funcionario["salario"]= int(input("salário: "))
    func.append(funcionario)
    if funcionario["salario"]> func_MS: 
        maior_salario= funcionario['salario']
        nome_maiorS= funcionario['nome']


print("==FUNCIONÁRIOS==")
print(func)
print("")
print(f"o funcionário com o maior salário é: {maior_salario}, do funcionário: {nome_maiorS} ")