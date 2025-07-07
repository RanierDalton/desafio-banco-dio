from abc import ABC, abstractmethod
from Conta import Conta

class Transacao(ABC):
    @abstractmethod
    def registrar(self, conta:Conta) -> None:
        """
        Método abstrato que deve ser implementado por todas as transações. 
        Recebe uma instância de Conta e realiza a transação.
        """
        pass