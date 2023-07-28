class Pybank:
    def __init__(self):
        self.saldo = 0

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("Valor inválido para depósito.")

    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso.")
        else:
            print("Saldo insuficiente ou valor inválido para saque.")

    def extrato(self):
        print(f"Saldo atual: R${self.saldo:.2f}")


if __name__ == "__main__":
    conta = Pybank()
    
    menu = """    
Menu:
d - Depositar
s - Sacar
e - Extrato
q - Sair

"""
    
    while True:
        print(menu)
        
        opcao = input("Digite a opção desejada: ")

        if opcao == "d":
            valor_deposito = float(input("Digite o valor a depositar: "))
            conta.depositar(valor_deposito)
        elif opcao == "s":
            valor_saque = float(input("Digite o valor a sacar: "))
            conta.sacar(valor_saque)
        elif opcao == "e":
            conta.extrato()
        elif opcao == "q":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Digite uma opção válida.")
