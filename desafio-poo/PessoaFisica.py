from Cliente import Cliente
from datetime import date

class PessoaFisica(Cliente):
    def __init__(self, 
                 nome:str, 
                 cpf:str, 
                 data_nascimento:date,
                 endereco:str):
        super().__init__(endereco)
        self._nome = nome
        self._cpf = cpf
        self._data_nascimento = data_nascimento

    def __str__(self):
        return f"Pessoa Física: {self.nome}, CPF: {self.cpf}"
