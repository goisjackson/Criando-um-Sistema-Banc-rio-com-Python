menu = """
__________MENU______

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
_____________________

    Digite uma opção:

=> """


saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)
        
    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("\033[41mOperação falhou! O valor informado é inválido.\033[0m")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("\033[41mOperação falhou! O valor informado é inválido.\033[0m")

        elif excedeu_limite:
            print("\033[41mOperação falhou! O valor informado é inválido.\033[0m")

        elif excedeu_saques:
            print("\033[41mOperação falhou! O valor informado é inválido.\033[0m")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("\033[41mOperação falhou! O valor informado é inválido.\033[0m")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("\033[41mOperação inválida, por favor selecione novamente a operação desejada.\033[0m")