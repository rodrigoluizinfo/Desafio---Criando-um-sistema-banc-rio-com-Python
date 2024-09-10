# ########### DESAFIO - CRIANDO UM SISTEMA BANCÁRIO COM PYTHON (VERSÃO 2.1) ###########

# # Fomos contratos por um grande banco para desenvolver o seu novo sistema. 
# # Esse banco deseja monetizar suas operações e para isso escolheu a linguagem Python
# # Para primeira versão do ssitema devemos implementar apenas 3 operações: depósito, saque e extrato.

# # 1 - OPERAÇÃO DE DEPÓSITO -- LÓGICA

# # Deve ser possível depositar valores positivos para a minha conta bancária.
# # A v1 do projeto trabalha apenas com 1 usuário, dessa forma não precisamos nos preocupar em identificar qual é o número da agência e conta bancária.
# # Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato.

# # 1 - OPERAÇÃO DE DEPÓSITO -- FUNÇÃO

# # A FUNÇÃO DEPÓSITO DEVE RECEBER OS ARGUMENTOS APENAS POR POSIÇÃO (POSITIONAL ONLY) - EX: DEF DEPOSITO(SALDO, VALOR, EXTRATO).

# #   SUGESTÃO DE ARGUMENTOS: SALDO, VALOR, EXTRATO.
  
# #   SUGESTÃO DE RETORNO: SALDO E EXTRATO.

# # 2 - OPERAÇÃO DE SAQUE -- LÓGICA

# # O sistema deve permitir realizar 10 movimentações diárias para uma conta com limite máximo de R$ 500,00 por saque.
# # Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo.
# # Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.

# # 2 - OPERAÇÃO DE SAQUE -- FUNÇÃO

# # A FUNÇÃO SAQUE DEVE RECEBER ARGUMENTOS APENAS POR NOME (KEYWORD ONLY) - EX: DEF SAQUE(SALDO=SALDO, EXTRATO=EXTRATO ETC.). 

# #   SUGESTÃO DE ARGUMENTOS: saldo, valor, extrato, limite, numero_saques, limite_saques. 

# #   SUGESTÃO DE RETORNO: SALDO E EXTRATO.

# # 3 - OPERAÇÃO DE EXTRATO -- LÓGICA

# # Essa operação deve listar todos os depósitos e saques realizados na conta. No fim da listagem deve ser exibido o saldo atual da conta.
# # Os valores devem ser exibidos utilizando o formato R$ xxx.xx, exemplo: 1500,45 = R$ 1500.45

# # 3 - OPERAÇÃO DE EXTRATO -- FUNÇÃO

# # A FUNÇÃO EXTRATO DEVE RECEBER OS ARGUMENTOS POR POSIÇÃO E NOME (POSITIONAL ONLY E KEYWORD ONLY).

# #   ARGUMENTO POSICIONAIS: SALDO 
  
# #   NOMEADOS: EXTRATO.

# #   DEVERÁ MOSTRAR DATA E HORA DE TODAS AS TRANSAÇÕES (OU SEJA, DEVERÁ REGISTRAR DATA E HORA DE TODAS AS TRANSAÇÕES, SEJA DE DEPÓSITO OU SAQUE).

# # 4 - CRIAR USUÁRIO -- FUNÇÃO

# # O PROGRAMA DEVE ARMAZENAR OS USUÁRIOS EM UMA LISTA. 

# #   UM USUÁRIO É COMPOSTO: nome, data_nascimento, cpf E endereco.

# #   O ENDEREÇO É UMA STRING COM O FORMATO: logradouro - nro - bairro - cidade/sigla estado.
  
# #   DEVE SER ARMAZENADO SOMENTE OS NÚMEROS DO CPF.
  
# #   NÃO PODEMOS CADASTRAR 2 USUÁRIOS COM O MESMO CPF.

# # 5 - CRIAR CONTAS -- FUNÇÃO

# # O PROGRAMA DEVE ARMAZENAR CONTAS EM UMA LISTA, UMA CONTA É COMPOSTA POR: agencia, numero_conta E usuario.

# #   O NÚMERO DA CONTA É SEQUENCIAL, INICIANDO EM 1.
  
# #   O NÚMERO DA AGÊNCIA É FIXO: "0001".
  
# #   O USUÁRIO PODE TER MAIS DE UMA CONTA, MAS UMA CONTA PERTENCE A SOMENTE UM USUÁRIO.
  
# # DICA:
  
# #   PARA VINCULAR UM USUÁRIO A UMA CONTA, FILTRE A LISTA DE USUÁRIOS BUSCANDO O NÚMERO DO CPF INFORMADO PARA CADA USUÁRIO DA LISTA.

# ########## SOLUÇÃO ##########

import textwrap

########### Menu
def menu():
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /): # Positional Only
    # Verifica se o valor a ser depositado é positivo
    if valor > 0:
        saldo += valor  # Atualiza o saldo com o valor do depósito
        extrato += f"Depósito: R${valor:.2f}\n"  # Adiciona a transação ao extrato
        print("Depósito realizado com sucesso!")
    else:
        print("Não é aceito valores negativos. Por favor, insira somente valores positivos!")
    return saldo, extrato 

def sacar(*, saldo, valor, extrato, limite, numero_transacoes, limite_transacoes): # Keyword Only
    # Verifica se o saque excede o saldo, o limite por transação ou o limite de saques diários
    excedeu_saldo  = valor > saldo
    excedeu_limite = valor > limite
    excedeu_movimentacoes = numero_transacoes >= limite_transacoes

    if excedeu_saldo:
        print("Saldo indisponível!")
    elif excedeu_limite:
        print(f"Saque acima do valor limite de R$ {limite:.2f}!")
    elif excedeu_movimentacoes:
        print("Limite de movimentações atingido!")
    else:
        saldo -= valor  # Atualiza o saldo após o saque
        numero_transacoes += 1  # Incrementa o contador de movimentações
        extrato += f"Saque: R$ {valor:.2f}\n"  # Adiciona a transação ao extrato
        print("Saque realizado com sucesso!")
    return saldo, extrato, numero_transacoes

def exibir_extrato(saldo, /, *, extrato): # Postional Only (/) - saldo e Keyword Only (*) - extrato 
    # Exibe o extrato com todas as transações e o saldo atual
    if not extrato:
        print("Nenhuma movimentação realizada!")
    else:
        print(f"\n********* EXTRATO ********* \n\n{extrato}\n\nSaldo atual: R$ {saldo:.2f}\n****************************")

def criar_usuario(usuarios):
    # Solicita o CPF do usuário e verifica se já está cadastrado
    cpf = digita_cpf()
    if filtrar_usuario(cpf, usuarios):
        print("CPF já cadastrado!")
        return
    # Solicita informações adicionais do usuário
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (DD-MM-YYYY): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
    usuario = {
        "Nome": nome,
        "CPF": cpf,
        "Data de Nascimento": data_nascimento,
        "Endereço": endereco
    }
    usuarios.append(usuario)  # Adiciona o novo usuário à lista
    print("\n################\n\nUsuário criado com sucesso!\n\n################")

def filtrar_usuario(cpf, usuarios):
    # Filtra e retorna o usuário com o CPF fornecido
    for usuario in usuarios:
        if usuario['CPF'] == cpf:
            return usuario
    return None

def criar_conta(agencia, numero_conta, usuarios, contas):
    # Solicita o CPF do usuário para vincular a conta
    cpf = digita_cpf()
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        numero_conta += 1  # Incrementa o número da conta
        conta = {"Agência": agencia, "Número_Conta": numero_conta, "Usuário": usuario}
        contas.append(conta)  # Adiciona a nova conta à lista de contas
        print("\n################\n\nConta criada com sucesso!\n\n################")
    else:
        print("\n################\n\nUsuário não encontrado!\n\n################")
    return numero_conta  # Retorna o número da conta atualizado

def listar_contas(contas):
    # Lista todas as contas existentes
    if not contas:
        print("Nenhuma conta encontrada!")
        return
    for conta in contas:
        linha = f"""\
        # Agência:\t{conta['Agência']}
        # C/C:\t\t{conta['Número_Conta']}
        # Titular:\t{conta['Usuário']['Nome']} 
        """ # Poderia colocar o CPF para ficar visível que o registro é unico para cada conta criada
        print("#" * 50)
        print(textwrap.dedent(linha))

def digita_cpf():
    # Solicita o CPF do usuário
    return input("Informe o CPF (Somente números): ")

def main():
    ########### Variáveis
    saldo = 0
    limite = 500.00
    extrato = ""
    numero_transacoes = 0
    numero_conta = 0  # Inicializando o número da conta

    # Variáveis constantes
    LIMITE_TRANSACOES = 10
    AGENCIA = "0001"

    # Listas
    usuarios = []
    contas = []

    while True:
        opcao = menu()
        if opcao == "d":
            valor_deposito = float(input("Digite o valor para ser depositado: "))
            saldo, extrato = depositar(saldo, valor_deposito, extrato)
        elif opcao == "s":
            valor_saque = float(input("Digite o valor para sacar: "))
            saldo, extrato, numero_transacoes = sacar(
                saldo, 
                valor_saque, 
                extrato, 
                limite, 
                numero_transacoes=numero_transacoes, 
                limite_saques=LIMITE_TRANSACOES) #Rebendo os retornos da função
        elif opcao == "e":
            exibir_extrato(saldo, extrato)
        elif opcao == "nu":
            criar_usuario(usuarios)
        elif opcao == "nc":
            numero_conta = criar_conta(AGENCIA, numero_conta, usuarios, contas) # A cada conta criada, será incrementado +1 para a variável numero_conta
        elif opcao == "lc":
            listar_contas(contas)
        elif opcao == "q":
            print("Saindo do sistema")
            break
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()
