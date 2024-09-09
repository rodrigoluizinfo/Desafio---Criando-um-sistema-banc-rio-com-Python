# DESAFIO - CRIANDO UM SISTEMA BANCÁRIO COM PYTHON

### Este desafio faz parte do Bootcamp DIO - NTT DATA - Engenharia de Dados com Python

#### O desafio foi desenvolvido utilizando a estrutura original fornecida pelo professor, mas com validações personalizadas para criar um sistema mais autoral.

##### A versão do Python utilizada é a 3.12.4.

#### 02/09/2024

##### Atualização do código ########

##### Anterior:
##### if numero_saques >= 3:
##### 	print("Limite de saques atingido!")

##### Agora:
##### if numero_saques >= LIMITE_SAQUES:
#####	print("Limite de saques atingido!")

#### Motivo: O código anterior estava setando um valor numérico e não a variável constante já declarada.

##### Anterior:
##### if valor_saque < saldo:

##### Agora:
##### if valor_saque <= saldo:

#### Motivo: O código anterior não possibilitava o saque do valor exato em conta. Porém, o código não tira a condição do valor limite imposto na variável limite (R$ 500,00).

#### 09/09/2024

# DESAFIO - CRIANDO UM SISTEMA BANCÁRIO COM PYTHON UTILIZANDO FUNÇÕES

### Este desafio faz parte do Bootcamp DIO - NTT DATA - Engenharia de Dados com Python

#### O desafio foi desenvolvido utilizando a estrutura original fornecida pelo professor, mas com validações personalizadas para criar um sistema mais autoral.

##### A versão do Python utilizada é a 3.12.4.