cont=1
for i in lista:
    print(cont,'-',i)
    cont+=1
fruta_escol=int(input('Escolha: '))
 
valores.append(preco[fruta_escol-1])
 
print(valores)































    valor_total = 0
    for item in carrinho:
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