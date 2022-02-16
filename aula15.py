# Aula sobre tipos primitivos

"""
Existem os seguintes tipos primitivos (4 principais):

String - str (textos, tipo "assim" ou 'assim')
Inteiro - int (número inteiro: 0, 12, -50, 1234)
Real - float (número decimal, sempre separado por ponto, e não vírgula: 0.15, 15.88, -90.01)
Booleano - bool (verdadeiro ou falso. Ex: 10 == 10)
"""

# a classe type pode ser utilizada para retornar o tipo do valor consultado, dessa forma:
print(type('Ronaldo'))
print('Ronaldo', type('Ronaldo'))  # dá pra fazer assim também, daí mostra o tipo do valor
# exatamente após o próprio valor
print(10, type(10))  # assim também, para int
print(25.23, type(25.23))  # aqui para float
print(10 == 10, type(10 == 10))  # e aqui para booleano
# o 10 == 10 é um teste condicional que o código faz, para checar se verdadeiro ou falso

# valores vazios retornam geralmente como falso em tipos booleanos
print(bool())
print(bool([]))  # lista vazia
print(bool(0))  # o número 0

# valores diferentes de zero ou não vazios retornam true

print(bool('Ronaldo'))
print(bool(123456))
print(bool(0.01))

# typecasting: conversão de valores em diferentes tipos primitivos
print('10', type('10'), type(int('10')))  # aqui converte o texto 10 em inteiro (int),
# só funciona em números, óbvio
print('10',float('10'), type('10'), type(float('10')))  # funciona assim também
print(10, float(10), type(10), type(float(10)))  # e assim também

print('10'+'10')  # dá pra concatenar textos assim
print(10+10)  # ou somar valores assim

# exercício da aula: crie um cadastro e exiba na tela seu nome, o tipo do valor, sua idade (inteiro),
# sua altura (float) e uma verificação se você é maior de idade
print('Nome:', 'Ronaldo', type('Ronaldo'))
print('Idade:', 18, type(18))
print('Altura:', 1.82, type(1.82))
print('É maior de idade?', 39 > 18, type(39 > 18))

