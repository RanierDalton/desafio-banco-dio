from Transacao import Transacao
from Conta import Conta

class Deposito(Transacao):
    def __init__(self, valor: float):
        self._valor = valor

    def registrar(self, conta: Conta) -> None:
        if conta.depositar(self._valor):
            print(f"Depósito realizado com sucesso!")
        else:
            print(f"Falha ao realizar depósito. Verifique os dados da conta.")