from Transacao import Transacao
from Conta import Conta

class Saque(Transacao):
    def __init__(self, valor: float):
        self._valor = valor

    def registrar(self, conta: Conta) -> None:
        if conta.sacar(self._valor):
            print(f"Saque realizado com sucesso!")
        else:
            print(f"Falha ao realizar saque. Verifique o saldo da conta.")