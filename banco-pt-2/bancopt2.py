import datetime

usuarios = []
contas = []
numero_conta_sequencial = 1

def mostrar_extrato(saldo, /, *, extrato):
    if extrato:
        print("Extrato da conta:")
        for transacao in extrato:
            print(transacao)
    else:
        print("Não foram realizadas movimentações.")
    print(f"Seu saldo atual é: R${saldo:.2f}")

def depositar(saldo, valor, extrato, /):
    try:
        valor_deposito = float(valor)
        if valor_deposito > 0:
            saldo += valor_deposito
            now = datetime.datetime.now()
            extrato.append(f"+R${valor_deposito:.2f} ({now.strftime('%d-%m-%Y %H:%M')})")
        else:
            print("Não é possível inserir um valor negativo, tente novamente.")
    except ValueError:
        print("Por favor, insira um número válido.")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    try:
        valor_saque = float(valor)
        if valor_saque > saldo:
            print(f"Saldo insuficiente. Seu saldo é R${saldo:.2f}.")
        elif valor_saque > limite:
            print(f"Limite de saque excedido. Limite é R${limite:.2f}.")
        elif numero_saques >= limite_saques:
            print("Número de saques diários excedido.")
        else:
            saldo -= valor_saque
            now = datetime.datetime.now()
            extrato.append(f"-R${valor_saque:.2f} ({now.strftime('%d-%m-%Y %H:%M')})")
            numero_saques += 1
            print(f"Operação realizada com sucesso. Seu saldo atual é R${saldo:.2f}.")
    except ValueError:
        print("Por favor, insira um número válido.")
    return saldo, extrato, numero_saques

def validar_nome(nome):
    return (nome.isalpha() or ' ' in nome) and len(nome) > 2

def validar_data_nascimento(data_nascimento):
    try:
        datetime.datetime.strptime(data_nascimento, '%d/%m/%Y')
        return True
    except ValueError:
        return False

def validar_cpf(cpf):
    return len(cpf) == 11 and cpf.isdigit()

def validar_endereco(endereco):
    return len(endereco) >= 5

def cadastrar_usuario():
    while True:
        nome = input("Nome: ")
        if validar_nome(nome):
            break
        else:
            print("Nome inválido. Deve conter pelo menos duas letras.")

    while True:
        data_nascimento = input("Data de Nascimento (dd/mm/aaaa): ")
        if validar_data_nascimento(data_nascimento):
            break
        else:
            print("Data de nascimento inválida. Use o formato dd/mm/aaaa.")

    while True:
        cpf = input("CPF: ")
        cpf = ''.join(filter(str.isdigit, cpf))
        if validar_cpf(cpf):
            if any(usuario['cpf'] == cpf for usuario in usuarios):
                print("Esse CPF está vinculado a outra conta.")
            else:
                break
        else:
            print("CPF inválido. Deve conter exatamente 11 dígitos.")

    while True:
        endereco = input("Endereço (logradouro, nº - bairro - cidade/sigla do estado): ")
        if validar_endereco(endereco):
            break
        else:
            print("Endereço inválido. Insira pelo menos cinco caracteres.")

    usuario = {
        'nome': nome,
        'data_nascimento': data_nascimento,
        'cpf': cpf,
        'endereco': endereco,
        'contas': []
    }
    usuarios.append(usuario)
    print("Usuário cadastrado com sucesso.")
    return usuario

def cadastrar_conta(usuario):
    global numero_conta_sequencial
    conta = {
        'agencia': '0001',
        'numero_conta': numero_conta_sequencial,
        'usuario': usuario,
        'saldo': 0,
        'extrato': [],
        'limite': 500,
        'limite_saques': 3,
        'numero_saques': 0
    }
    usuario['contas'].append(conta)
    contas.append(conta)
    numero_conta_sequencial += 1
    print("Conta cadastrada com sucesso.")
    return conta

def listar_contas():
    if not contas:
        print("Nenhuma conta cadastrada.")
    else:
        for conta in contas:
            usuario = conta['usuario']
            print(f"Agência: {conta['agencia']}, Número da Conta: {conta['numero_conta']}, Usuário: {usuario['nome']}")

def menu_usuario(usuario, conta):
    while True:
        print(f"\nBem-vindo(a), {usuario['nome']}!")
        print(f"Número da conta: {conta['numero_conta']}, Agência: {conta['agencia']}")
        print("1 - Extrato")
        print("2 - Depósito")
        print("3 - Saque")
        print("4 - Sair")

        operacao_selecionada = input("Selecione a operação desejada: ")
        
        if operacao_selecionada == '1':
            mostrar_extrato(conta['saldo'], extrato=conta['extrato'])
        elif operacao_selecionada == '2':
            valor = float(input(f"Valor do depósito para conta {conta['numero_conta']}: R$"))
            conta['saldo'], conta['extrato'] = depositar(conta['saldo'], valor, conta['extrato'])
        elif operacao_selecionada == '3':
            valor = input(f"Valor do saque para conta {conta['numero_conta']}: R$")
            conta['saldo'], conta['extrato'], conta['numero_saques'] = sacar(saldo=conta['saldo'], valor=valor, extrato=conta['extrato'], limite=conta['limite'], numero_saques=conta['numero_saques'], limite_saques=conta['limite_saques'])
        elif operacao_selecionada == '4':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida, tente novamente.")

def encontrar_usuario_por_cpf(entrada):
    entrada = ''.join(filter(str.isdigit, entrada))
    usuario = next((usuario for usuario in usuarios if usuario['cpf'] == entrada), None)

    return usuario

def encontrar_conta_por_numero(numero_conta):
    for conta in contas:
        if str(conta['numero_conta']) == numero_conta:
            return conta
    return None

def mostrar_contas():
    if not usuarios:
        print("Nenhum usuário cadastrado.")
    else:
        for usuario in usuarios:
            print(f"\nNome: {usuario['nome']}")
            print(f"Data de Nascimento: {usuario['data_nascimento']}")
            print(f"CPF: {usuario['cpf']}")
            print(f"Endereço: {usuario['endereco']}")
            if usuario['contas']:
                print("Contas:")
                for conta in usuario['contas']:
                    print(f"Agência: {conta['agencia']}, Número da Conta: {conta['numero_conta']}, Saldo: R${conta['saldo']:.2f}")
            else:
                print("Nenhuma conta cadastrada para este usuário.")

def menu_inicial():
    print("Banco BagDIO!")

while True:
    menu_inicial()
    print("\nSe é seu primeiro acesso, selecione Novo Usuário. Ao se cadastrar, uma conta será automaticamente vinculada ao seu CPF. Se já possui conta e deseja criar uma adicional, selecione a opção Nova Conta. Para acessar suas contas, selecione a terceira opção.")
    print("1 - Novo Usuário")
    print("2 - Nova Conta")
    print("3 - Acessar Conta")
    print("4 - Listar Contas")

    operacao_selecionada = input("Selecione a operação desejada: ")

    if operacao_selecionada == '1':
        usuario = cadastrar_usuario()
        if usuario:
            conta = cadastrar_conta(usuario)
            print(f"Conta cadastrada com sucesso! Número da conta: {conta['numero_conta']}, Agência: {conta['agencia']}")
            print(f"Nome: {usuario['nome']}, Data de Nascimento: {usuario['data_nascimento']}, CPF: {usuario['cpf']}, Endereço: {usuario['endereco']}")
    elif operacao_selecionada == '2':
        cpf = input("Digite seu CPF: ")
        usuario = encontrar_usuario_por_cpf(cpf)
        if usuario:
            conta = cadastrar_conta(usuario)
            print(f"Conta cadastrada com sucesso! Número da conta: {conta['numero_conta']}, Agência: {conta['agencia']}")
        else:
            print("Usuário não encontrado.")
    elif operacao_selecionada == '3':
        numero_conta = input("Digite o número da Conta: ")
        conta = encontrar_conta_por_numero(numero_conta)
        if conta:
            usuario = conta['usuario']
            menu_usuario(usuario, conta)
        else:
            print("Conta não encontrada.")
    elif operacao_selecionada == '4':
        mostrar_contas()

    else:
        print("Opção inválida, tente novamente.")

menu_inicial()
