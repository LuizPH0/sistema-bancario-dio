import textwrap

def menu():
    menu = """\nEscolha uma opção para prosseguir:
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Criar conta
    [s] Sair

    --> """
    return input(textwrap.dedent(menu))

def depositar(saldo, extrato):
    valor = float(input("Informe o valor do depósito: "))

    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("Depósito realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato

def sacar(*, saldo, extrato, limite, numero_saques, limite_saques):
    valor = float(input("Informe o valor do saque: "))

    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("Saque realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato, numero_saques

def exibir_extrato(saldo, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def criar_conta(contas, usuarios):
    numero_conta = len(contas) + 1
    cpf = input("Informe o CPF do usuário: ")

    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        conta = {"agencia": "0001", "numero_conta": numero_conta, "usuario": usuario}
        contas.append(conta)
        print("Conta criada com sucesso!")
    else:
        print("Usuário não encontrado. Criação de conta cancelada.")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    usuarios = [{"nome": "João", "cpf": "12345678900"}]  # Exemplo de usuário cadastrado
    contas = []

    while True:
        opcao = menu()

        if opcao == "1":
            saldo, extrato = depositar(saldo, extrato)

        elif opcao == "2":
            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES
            )

        elif opcao == "3":
            exibir_extrato(saldo, extrato)

        elif opcao == "4":
            criar_conta(contas, usuarios)

        elif opcao == "s":
            print("Saindo... Obrigado por usar nosso sistema bancário!")
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

if __name__ == "__main__":
    main()
