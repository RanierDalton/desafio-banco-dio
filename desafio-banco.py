MENU = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
LIMITE = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(MENU)

    if opcao == "d":
        deposito = float(input("Informe o valor do depósito: "))

        if deposito <= 0:
            print("Operação falhou! O valor do depósito deve ser positivo.")
            continue
        saldo += deposito
        extrato += f"Depósito: R$ {deposito:.2f}\n"
        print(f"Depósito de R$ {deposito:.2f} realizado com sucesso!")

    elif opcao == "s":
        saque = float(input("Informe o valor do saque: "))

        if saque <= 0:
            print("Operação falhou! O valor do saque deve ser positivo.")
            continue

        if saque > saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
            continue

        if saque > LIMITE:
            print(f"Operação falhou! O valor do saque deve ser menor ou igual a R$ {LIMITE:.2f}.")
            continue

        if numero_saques >= LIMITE_SAQUES:
            print("Operação falhou! Número máximo de saques excedido.")
            continue
        saldo -= saque
        extrato += f"Saque: R$ {saque:.2f}\n"
        numero_saques += 1
        print(f"Saque de R$ {saque:.2f} realizado com sucesso!")   
    elif opcao == "e":
        print("\n+++++++++++++++ EXTRATO +++++++++++++++")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"Saldo: R$ {saldo:.2f}")
        print("+++++++++++++++++++++++++++++++++++++++++\n")
    elif opcao == "q":
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")