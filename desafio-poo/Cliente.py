from Transacao import Transacao
from Conta import Conta

class Cliente:
    def __init__(self, endereco: str, contas: list = None):
        self._endereco = endereco
        self._contas = contas if contas is not None else []

    def __str__(self):
        return f"Cliente: {self.nome}, CPF: {self.cpf}"
    
    def realizar_transacao(self, conta: Conta, transacao: Transacao) -> None:
        if conta in self._contas:
            transacao.registrar(conta)
        else:
            print(f"Conta não pertence a este cliente.")
        
    def adicionar_conta(self, conta: Conta) -> None:
        if conta not in self._contas:
            self._contas.append(conta)
            print(f"Conta {conta.numero} adicionada com sucesso.")
        else:
            print(f"Conta {conta.numero} já existe para este cliente.")
