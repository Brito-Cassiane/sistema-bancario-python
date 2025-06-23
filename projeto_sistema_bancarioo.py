saldo = 0
limite_saque = 500
saques_realizados = 0
max_saques = 3
historico = []

def mostrar_menu():
    print("\n=== MENU ===")
    print("1 - Depositar")
    print("2 - Sacar")
    print("3 - Ver Extrato")
    print("0 - Sair")

while True:
    mostrar_menu()
    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        valor = float(input("Digite o valor para depósito: "))

        if valor > 0:
            saldo += valor
            historico.append(f"Depósito: R$ {valor:.2f}")
            print("Depósito realizado com sucesso!")
        else:
            print("Valor inválido. Tente novamente.")

    elif escolha == "2":
        if saques_realizados >= max_saques:
            print("Limite de saques diários atingido.")
            continue

        valor = float(input("Digite o valor para saque: "))

        if valor > saldo:
            print("Saldo insuficiente.")
        elif valor > limite_saque:
            print(f"Limite por saque é de R$ {limite_saque:.2f}.")
        elif valor <= 0:
            print("Valor inválido. Tente novamente.")
        else:
            saldo -= valor
            saques_realizados += 1
            historico.append(f"Saque:    R$ {valor:.2f}")
            print("Saque realizado com sucesso!")

    elif escolha == "3":
        print("\n=== EXTRATO ===")
        if not historico:
            print("Não foram realizadas movimentações.")
        else:
            for operacao in historico:
                print(operacao)
        print(f"Saldo atual: R$ {saldo:.2f}")

    elif escolha == "0":
        print("Encerrando o sistema. Obrigado!")
        break

    else:
        print("Opção inválida. Tente novamente.")
