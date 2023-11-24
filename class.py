class ContaBancaria:
    def __init__(self, titular, tipo, agencia, conta, saldo):
        self.titular = titular
        self.tipo = tipo
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    def exibirDadosConta(self):
        print(f'Titular: {self.titular}')
        print(f'Tipo de conta: {self.tipo}')
        print(f'Agência: {self.agencia}')
        print(f'Conta: {self.conta}')
        print(f'Saldo: R${self.saldo}')

    def saque(self, valor):
        if self.saldo < valor:
            print('Saldo insuficiente!')
        else:
            print(f'Realizando saque no valor de {valor}')
            self.saldo -= valor

    def deposito(self, valor):
        print(f'Realizando deposito no valor de {valor}')
        self.saldo += valor

if __name__ == '__main__':
    contaFelipe = ContaBancaria('Felipe', 'Conta Corrente', '0001', 203040, 200)
    contaDaniel = ContaBancaria('Daniel', 'Conta Poupança', '0001', 113322, 100)

    contaFelipe.exibirDadosConta()

    valorSaque = float(input('Digite o valor que deseja sacar: R$'))
    contaFelipe.saque(valorSaque)
    contaFelipe.exibirDadosConta()

    valorDeposito = float(input('Digite o valor que deseja depositar: R$'))
    contaFelipe.deposito(valorDeposito)
    contaFelipe.exibirDadosConta()