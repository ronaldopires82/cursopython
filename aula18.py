# aula sobre variáveis
"""
Pode conter números porém não pode começar com números. Letras minúsculas. Para separar, ideal padronizar
com _.
"""

nome = 'Ronaldo Pires'
idade = 39
altura = 1.82
e_maior = idade > 18
peso = 104
imc = peso / altura ** 2

print('\n')

print('Nome: ', nome, type(nome))
print('Idade: ', idade, type(idade))
print('Altura: ', altura, type(altura))
print('É maior de idade?', e_maior, type(e_maior))

# cálculo do IMC - divide o peso pela altura ao quadrado
print('Seu IMC é de: ',imc)