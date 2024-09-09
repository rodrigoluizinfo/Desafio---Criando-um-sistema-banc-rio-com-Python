############ DESAFIO - CRIANDO UM SISTEMA BANCÁRIO COM PYTHON (VERSÃO 1.0) ###########

# Fomos contratos por um grande banco para desenvolver o seu novo sistema. 
# Esse banco deseja monetizar suas operações e para isso escolheu a linguagem Python
# Para primeira versão do ssitema devemos implementar apenas 3 operações: depósito, saque e extrato.

# 1 - OPERAÇÃO DE DEPÓSITO

# Deve ser possível depositar valores positivos para a minha conta bancária.
# A v1 do projeto trabalha apenas com 1 usuário, dessa forma não precisamos nos preocupar em identificar qual é o número da agência e conta bancária.
# Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato.

# 2 - OPERAÇÃO DE SAQUE

# O sistema deve permitir realizar 3 saques diários com limite máximo de R$ 500,00 por saque.
# Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo.
# Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.

# 3 - OPERAÇÃO DE EXTRATO

# Essa operação deve listar todos os depósitos e saques realizados na conta. No fim da listagem deve ser exibido o saldo atual da conta.
# Os valores devem ser exibidos utilizando o formato R$ xxx.xx, exemplo: 1500,45 = R$ 1500.45

########## SOLUÇÃO ##########

#Criando o menu

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

#Variáveis

saldo = 0
limite = 500.00
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3 #Variável constante

#Laço while para selecionar o menu e fazer o código de cada situação desejada, assim como prever quando não selecionar a opção correta, além de poder sair do sistema.

while True:
  
  opcao = input(menu)
  
  if opcao == "d":
    
    # 1 - OPERAÇÃO DE DEPÓSITO

      # Deve ser possível depositar valores positivos para a minha conta bancária.
      # A v1 do projeto trabalha apenas com 1 usuário, dessa forma não precisamos nos preocupar em identificar qual é o número da agência e conta bancária.
      # Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato.
      
      valor_deposito = float(input("Digite o valor para ser depositado: "))
      
      if valor_deposito > 0:
        
        saldo += valor_deposito
        print(str(f"Depósito realizado"))
        extrato += f"Deposíto: R$ {valor_deposito:.2f}\n"
        
      else:
        print("Não é aceito valores negativos. Por favor, insira somente valores positivos!")
        
  elif opcao == "s":
    
    # 2 - OPERAÇÃO DE SAQUE

      # O sistema deve permitir realizar 3 saques diários com limite máximo de R$ 500,00 por saque.
      # Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo.
      # Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.
    
      if numero_saques >= LIMITE_SAQUES:
            print("Limite de saques atingido!")
            
      while numero_saques < LIMITE_SAQUES:
        
        menu_saque = """

          [n] Novo saque
          [q] Sair

          => """
        
        opcao_saque = input(menu_saque)
        
        if opcao_saque == "n":
          
          if saldo > 0:
            valor_saque = float(input("Digite o valor para sacar: "))
          
            if valor_saque <= saldo:
              
              if valor_saque <= limite:
                
                saldo = saldo - valor_saque
                numero_saques += 1
                extrato += f"Saque: R$ {valor_saque:.2f}\n"
                
              else:
                print(f"Saque acima do valor limite de R$ {limite:.2f}!")
                
            else:
              print("Valor do saque acima do saldo disponível!")
          
            if numero_saques >= LIMITE_SAQUES:
              print("Limite de saques atingido!")
          else:
            print("Saldo indisponível. Por favor, faça um depósito para ser possível realizar um saque!")
            break
                  
        elif opcao_saque == "q":
          break
        
        else:
          print("Operação inválida, por favor selecione novamente a operação desejada.")

  elif opcao == "e":
    
    # 3 - OPERAÇÃO DE EXTRATO

      # Essa operação deve listar todos os depósitos e saques realizados na conta. No fim da listagem deve ser exibido o saldo atual da conta.
      # Os valores devem ser exibidos utilizando o formato R$ xxx.xx, exemplo: 1500,45 = R$ 1500.45
    
    if extrato == "":
      print("Nenhuma movimentação realizada!")
    else:
      print(f"\n********* EXTRATO ********* \n\n{extrato}\n\n\n\nSaldo atual: R$ {saldo:.2f}\n****************************")
    
  elif opcao == "q":
    print("Saindo do sistema")
    break

  else:
      print("Operação inválida, por favor selecione novamente a operação desejada.")