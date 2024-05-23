import datetime

movimentacoes = []
saques_diarios = 0
limite_saques_dia = 3
limite_valor_saque = 500

def mostrar_extrato(movimentacoes):
    if movimentacoes:
        print("Extrato da conta:")
        for transacao in movimentacoes:
            print(transacao)
    else:
        print("Não foram realizadas movimentações.")

def mostrar_saldo(saldo):
    print(f"Seu saldo atual é: R${saldo:.2f}")

def menu_inicial():
     saldo = 0
     saques_diarios = 0
     data_ultimo_saque = datetime.date.today()
    
     print("Banco BagDIO!")

     while True:
         
        operacao_selecionada = input("Selecione a operação desejada: digite 1 para extrato, 2 para depósito e 3 para saque. ")

        if operacao_selecionada == '1':
            mostrar_extrato(movimentacoes)
            mostrar_saldo(saldo)
        elif operacao_selecionada == '2':
            valor_deposito = input("Valor do depósito: R$")
            try:
                valor_deposito = float(valor_deposito)
                if (valor_deposito > 0):
                    saldo += valor_deposito
                    now = datetime.datetime.now()
                    movimentacoes.append(f"+R${valor_deposito:.2f} ({now.strftime('%d-%m-%Y %H:%M')})")
                    print(f"Operação realizada com sucesso. Seu saldo atual é R${saldo:.2f}.")
                else:
                    print("Não é possível inserir um valor negativo, tente novamente.")
            except ValueError:
                print("Por favor, insira um número válido.")
        elif operacao_selecionada == '3':
            today = datetime.date.today()
            if today != data_ultimo_saque:
                saques_diarios = 0
                data_ultimo_saque = today

            if saques_diarios >= limite_saques_dia:
                print("Você atingiu o limite de saques diários.")
                continue

            valor_saque = input("Valor do saque: R$")
            try:
                valor_saque = float(valor_saque)
                if valor_saque > limite_valor_saque:
                    print(f"O limite por saque é de R${limite_valor_saque:.2f}. Tente novamente.")
                elif valor_saque > saldo:
                    print(f"Saldo insuficiente. Seu saldo é de R${saldo:.2f}.")
                else:
                    saldo -= valor_saque
                    saques_diarios += 1
                    now = datetime.datetime.now()
                    movimentacoes.append(f"-R${valor_saque:.2f} ({now.strftime('%d-%m-%Y %H:%M')})")
                    print(f"Operação realizada com sucesso. Seu saldo atual é R${saldo:.2f}.")
            except ValueError:
                print("Por favor, insira um número válido.")
        else:
            print("Opção inválida, tente novamente.")

menu_inicial()