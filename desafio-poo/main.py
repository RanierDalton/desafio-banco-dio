from Conta import Conta
from PessoaFisica import PessoaFisica
from Deposito import Deposito
from Saque import Saque

def main():
    cliente = PessoaFisica(nome="João da Silva", cpf="123.456.789-00", data_nascimento="1990-01-01", endereco="Rua A, 123")
    conta = Conta.nova_conta(cliente, numero=12345)

    cliente.adicionar_conta(conta)
    
    print(f"Conta criada com sucesso!")
    print(f"Saldo inicial: R${conta._saldo:.2f}")

    # Exemplo de transações
    deposito = Deposito(valor=100.0)
    deposito.registrar(conta)   
    saque = Saque(valor=50.0)
    saque.registrar(conta)

    print(f"Saldo final: R${conta._saldo:.2f}")
    print(f"Histórico de transações: {conta._historico._transacoes}")

if __name__ == '__main__':
    main()