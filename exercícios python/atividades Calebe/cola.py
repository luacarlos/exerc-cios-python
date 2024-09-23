codigo_mais_gordo = 0
codigo_mais_magro = 0
codigo_mais_alto = 0
codigo_mais_baixo = 0

# ? No lugar de -math.inf e math.inf, vão os valores 0 e 1000 pois
# ? Não dá pra alguém pesar menos que 0kg
peso_mais_gordo = 0
# ? Não deve ter alguém que pese mais que 1 tonelada
peso_mais_magro = 1000
# ? Mesma ideia pro peso serve para a altura
altura_mais_alto = 0
altura_mais_baixo = 5  # * Altura vai ser em centímetros

soma_dos_pesos = 0
soma_das_alturas = 0
quantidade_de_clientes = 0

while True:
    codigo = input("Digite o codigo do cliente: ")
    if codigo == "0":
        break

    quantidade_de_clientes += 1
    altura = float(input("Digite a altura do cliente (em metros): "))
    peso = float(input("Digite o peso do cliente (em kg): "))

    soma_dos_pesos += peso
    soma_das_alturas += altura

    if altura > altura_mais_alto:
        altura_mais_alto = altura
        codigo_mais_alto = codigo

    if altura < altura_mais_baixo:
        altura_mais_baixo = altura
        codigo_mais_baixo = codigo

    if peso > peso_mais_gordo:
        peso_mais_gordo = peso
        codigo_mais_gordo = codigo

    if peso < peso_mais_magro:
        peso_mais_magro = peso
        codigo_mais_magro = codigo

media_das_alturas = soma_das_alturas / quantidade_de_clientes
media_dos_pesos = soma_dos_pesos / quantidade_de_clientes

print(
    f"O cliente mais alto é o que tem o código {codigo_mais_alto}"
    f" e ele possui {altura_mais_alto}m de altura\n"
    f"O cliente mais baixo é o que tem o código {codigo_mais_baixo}"
    f" e ele possui {altura_mais_baixo}m de altura\n"
    f"O cliente mais gordo é o que tem o código {codigo_mais_gordo}"
    f" e ele pesa {peso_mais_gordo:.2f}kg\n"
    f"O cliente mais magro é o que tem o código {codigo_mais_magro}"
    f" e ele pesa {peso_mais_magro:.2f}kg\n"
    f"A média de altura dos clientes é de {media_das_alturas:.2f}m\n"
    f"A média de peso dos clientes é de {media_dos_pesos:.2f}kg"
)