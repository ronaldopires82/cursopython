# introdução à formatação de Strings
"""
f-strings é uma forma de formatar uma string de um jeito mais fácil de escrever
"""
nome = 'Ronaldo Pires'
idade = 39
altura = 1.82
e_maior = idade > 18
peso = 103.5
imc = peso / altura ** 2

print('\n')

print('Nome: ', nome, type(nome))
print('Idade: ', idade, type(idade))
print('Altura: ', altura, type(altura))
print('É maior de idade?', e_maior, type(e_maior))

# cálculo do IMC - divide o peso pela altura ao quadrado
print('Seu IMC é de: ',imc)
print(nome, 'tem', idade, 'anos de idade e seu IMC é de:', imc)

print(f'{nome} tem {idade} anos de idade e seu IMC é de: {imc}')  # dessa forma não precisa
# ficar abrindo e fechando aspas e usando vírgulas para separar textos de variáveis

# dá pra diminuir a quantidade de casa decimais da variável imc da forma abaixo:
print(f'{nome} tem {idade} anos de idade e seu IMC é de: {imc}')

# outra forma de fazer é com a sintaxe abaixo:
print('{} tem {} anos e seu IMC é de {}'.format(nome, idade, imc))  # as chaves consideram, implicitamente,
# as variáveis 0, 1 e 2
print('{0} tem {1} anos e seu IMC é de {2}'.format(nome, idade, imc))  # assim é o explícito
# a vantagem de incluir os números dentro das chaves é que podemos colocá-las em qualquer ordem que interessar.

print('{0} tem {1} anos. O IMC de {0} é {2}'.format(nome, idade, imc))

# dá pra fazer da seguinte forma também:
print('{n} tem {i} anos e seu IMC é de: {im}'.format(n=nome, i=idade, im=imc))

print('\n')

# para formatar a quantidade de casas decimais, utilize a seguinte sintaxe:
print('{0:.2f}'.format(imc))  # ou:
print(f'{imc:.2f}')

print('\n')

# aí a string ficaria da seguinte forma:
print(f'{nome} tem {idade} anos e seu IMC é de: {imc:.2f}')
# ou assim:
print('{0} tem {1} anos e seu IMC é de: {2:.2f}'.format(nome, idade, imc))
