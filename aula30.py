# Exercícios propostos
"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número inteiro é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
num_inteiro = input('Digite um número inteiro: ')
if not num_inteiro.isnumeric():
    print('Este não é um número inteiro.')
else:
    num_inteiro = int(num_inteiro)
    if num_inteiro % 2 == 0:
        print('Este número é par.')
    else:
        print('Este número é ímpar.')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada. Ex.:
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23
"""
hora = input('Digite a hora deste momento (somente a hora): ')
if not hora.isnumeric() or len(hora) == '':
    print('O valor digitado não é válido.')
else:
    hora = int(hora)
    if hora > 23:
        print('O valor digitado não é válido.')
    elif hora <= 23 and hora >= 17:
        print('Boa noite!')
    elif hora <= 17 and hora >= 12:
        print('Boa tarde!')
    else:
        print('Bom dia!')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".
"""

nome = input('Escreva seu primeiro nome: ')
if len(nome) == '':
    print('O valor digitado não é válido.')
else:
    if len(nome) > 6:
        print('Seu nome é muito grande.')
    elif len(nome) >= 5:
        print('Seu nome é normal.')
    elif len(nome) > 0:
        print('Seu nome é curto.')
    else:
        print('O valor digitado não é válido.')
        