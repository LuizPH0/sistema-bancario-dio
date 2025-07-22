from abc import ABC, abstractmethod
from datetime import date

class Transacao(ABC):
    @abstractmethod
    def registrar(self, conta):
        pass

class Deposito(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        conta.depositar(self.valor)

class Saque(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        conta.sacar(self.valor)

class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao):
        self.transacoes.append(transacao)

class Conta:
    def __init__(self, cliente, numero, agencia="0001"):
        self.saldo = 0
        self.numero = numero
        self.agencia = agencia
        self.cliente = cliente
        self.historico = Historico()

    def saldo_atual(self):
        return self.saldo

    def sacar(self, valor):
        if valor <= 0 or valor > self.saldo:
            print("Saque inválido ou saldo insuficiente.")
            return False

        self.saldo -= valor
        self.historico.adicionar_transacao(f"Saque: R$ {valor:.2f}")
        print("Saque realizado com sucesso.")
        return True

    def depositar(self, valor):
        if valor <= 0:
            print("Valor de depósito inválido.")
            return False

        self.saldo += valor
        self.historico.adicionar_transacao(f"Depósito: R$ {valor:.2f}")
        print("Depósito realizado com sucesso.")
        return True

class ContaCorrente(Conta):
    def __init__(self, cliente, numero, limite=500, limite_saques=3):
        super().__init__(cliente, numero)
        self.limite = limite
        self.limite_saques = limite_saques
        self.numero_saques = 0

    def sacar(self, valor):
        if self.numero_saques >= self.limite_saques:
            print("Limite de saques excedido.")
            return False

        if valor > self.limite:
            print("Valor excede o limite permitido.")
            return False

        sucesso = super().sacar(valor)
        if sucesso:
            self.numero_saques += 1
        return sucesso

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        if conta in self.contas:
            transacao.registrar(conta)
        else:
            print("Conta não pertence a este cliente.")

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, nome, cpf, data_nascimento, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento

# ======================================
# Função para simular o menu CLI
# ======================================

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

def main():
    usuarios = []
    contas = []

    cliente = PessoaFisica("João", "12345678900", date(2000, 1, 1), "Rua A")
    usuarios.append(cliente)

    while True:
        opcao = menu()

        if opcao == "1":
            if cliente.contas:
                valor = float(input("Informe o valor do depósito: "))
                cliente.realizar_transacao(cliente.contas[0], Deposito(valor))
            else:
                print("Cliente não possui conta.")

        elif opcao == "2":
            if cliente.contas:
                valor = float(input("Informe o valor do saque: "))
                cliente.realizar_transacao(cliente.contas[0], Saque(valor))
            else:
                print("Cliente não possui conta.")

        elif opcao == "3":
            if cliente.contas:
                conta = cliente.contas[0]
                print("\n===== EXTRATO =====")
                for t in conta.historico.transacoes:
                    print(t)
                print(f"Saldo atual: R$ {conta.saldo_atual():.2f}")
                print("===================")
            else:
                print("Cliente não possui conta.")

        elif opcao == "4":
            numero_conta = len(contas) + 1
            conta = ContaCorrente(cliente, numero_conta)
            cliente.adicionar_conta(conta)
            contas.append(conta)
            print("Conta criada com sucesso!")

        elif opcao == "s":
            print("Saindo... Obrigado por usar nosso sistema bancário!")
            break

        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
