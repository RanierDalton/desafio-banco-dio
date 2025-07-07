from Transacao import Transacao
class Historico:
    def __init__(self):
        self._transacoes = []

    def adicionar_transacao(self, transacao: Transacao) -> None:
        self._transacoes.append(transacao)