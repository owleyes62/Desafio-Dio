class ContaBancaria:
    LIMITE_SAQUES = 3

    def __init__(self, saldo_inicial=0):
        self.saldo = saldo_inicial
        self.saques_realizados = 0

    def deposito(self, valor):
        if int(valor) > 0:
            self.saldo += int(valor)
            return f'Depósito de R$ {valor:.2f} realizado. Novo saldo: R$ {self.saldo:.2f}'
        else:
            return 'Valor de depósito inválido.'

    def saque(self, valor):
        if self.saques_realizados < self.LIMITE_SAQUES:
            if int(valor) <= 500:
                if self.saldo >= int(valor):
                    self.saldo -= int(valor)
                    self.saques_realizados += 1
                    return f'Saque de R$ {int(valor):.2f} realizado. Novo saldo: R$ {self.saldo:.2f}'
                else:
                    return 'Saldo insuficiente'
            else:
                return 'Saques maiores que 500 não são permitidos.'
        else:
            return 'Limite de saque excedido'

    def extrato(self):
        return f'Saldo atual: R$ {self.saldo:.2f}'


# Cria a conta fora do loop para manter o estado entre as operações
conta = ContaBancaria(100)

menu = """
        
        [1] Depositar
        [2] Sacar
        [3] Extrato
        [4] Sair
        
        =>"""

msg_saque = """
Escolha o valor de saque entre 0 a 500 R$
(Você tem um limite de 3 saques por dia)
"""

while True:

    def is_valid_input(input_str):
        return input_str.isdigit()

    opcao = input(menu)

    if opcao == "3":
        print(conta.extrato())

    elif opcao == "2":
        print(msg_saque)
        valor_saque = input("Digite o valor do saque: ")
        if is_valid_input(valor_saque):
            print(conta.saque(valor_saque))
        else:
            print(
                "Valor de depósito inválido. O valor deve ser um número inteiro maior que zero.")

    elif opcao == "1":
        valor_deposito = input("Digite o valor do depósito: ")
        if is_valid_input(valor_deposito):
            print(conta.deposito(int(valor_deposito)))
        else:
            print(
                "Valor de depósito inválido. O valor deve ser um número inteiro maior que zero.")

    elif opcao == "4":
        print("Obrigado por usar nossos serviços.")
        break

    else:
        print("Opção inválida")
