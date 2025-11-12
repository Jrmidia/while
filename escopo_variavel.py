valor = 50

def mensagem():
    global valor #declara que a prioridade será a variável valor que está fora da função (global)
    print(f"Exibindo a variável valor: {valor}")

    valor = valor + 10
    print(f"valor atualizado da variável: {valor}")

mensagem()