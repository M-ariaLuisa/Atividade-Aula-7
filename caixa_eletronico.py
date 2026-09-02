
while True:
    try:
        saldo_disponível = float(input("Digite seu saldo: "))
        valor_do_saque = float(input("Digite o valor do saque: "))
        if(valor_do_saque <= saldo_disponível):
            saldo_disponível -= valor_do_saque
            print(f"Saque realizado com sucesso! ")
            print(f"Saldo atual: {saldo_disponível:.2f}")
        else:
            print("Saldo insuficiente para realizar o saque.")
        break
    except:
        print("Erro: digite apenas números.")