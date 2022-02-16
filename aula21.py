# desafio prático
"""
* Criar variáveis para nome (str), idade (int),
* altura (float) e peso (float) de uma pessoa
* Criar variável com o ano atual (int)
* Obter o ano de nascimento da pessoa (baseado na idade e no ano atual)
* Obter o IMC da pessoa com 2 casas decimais (peso e altura da pessoa)
* Exibir um texto com todos os valores na tela usando F-Strings (com as chaves)
"""

nome = 'Ronaldo'
idade = 39
altura = 1.82
peso = 103.5
ano_atual = 2022
ano_nascimento = ano_atual - idade
imc = peso / altura ** 2

print('{0} tem {1} anos, pois nasceu em {2}, tem {3} de altura, pesa {4}kg e seu IMC é de {5:.2f}'.format(nome, idade, ano_nascimento, altura, peso, imc))
