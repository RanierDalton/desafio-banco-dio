from Conta import Conta
from Cliente import Cliente
from Historico import Historico

class ContaCorrente(Conta):
    def __init__(self, 
                 cliente:Cliente, 
                 numero:int, 
                 agencia:str, 
                 historico:Historico, 
                 limite:float, 
                 limite_saques:int):
        super().__init__(cliente, numero, agencia, historico)
        self._limite = limite
        self._limite_saques = limite_saques