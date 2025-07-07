from Cliente import Cliente
from Historico import Historico

class Conta:
    def __init__(self, 
                 cliente: Cliente, 
                 numero: int, 
                 agencia: str, 
                 historico: Historico):
        self._numero = numero
        self._agencia = agencia
        self._saldo = 0.0
        self._cliente = cliente
        self._historico = historico

    def saldo(self) -> float:
        return self._saldo
    
    @classmethod
    def nova_conta(cliente: Cliente, numero: int) -> 'Conta':
        agencia = "0001"
        historico = []
        return Conta(cliente, numero, agencia, historico)

    def sacar(self, valor:float) -> bool:
        if valor <= self._saldo:
            self._saldo -= valor
            return True
        else:
            return False

    def depositar(self, valor: float) -> bool:
        if valor > 0:
            self._saldo += valor
            return True
        else:
            return False
    