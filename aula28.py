# aula sobre documentação
"""
O Python, como todas as linguages, tem sua documentação com todas as funções, descrevendo a finalidade e sintaxe.
"""
# Exemplo - fazer uma calculadora sem checagem
print('Calculadora sem checagem.')
num1 = input('Digite um número: ')
num2 = input('Digite outro número: ')
num1 = int(num1)  # não se deve fazer o typecasting direto no input, pois ali já vai dar erro e não
# tem como apresentar nenhuma alternativa para corrigir a entrada do dado
num2 = int(num2)
resultado = num1 + num2
print(resultado)
print()
# Na calculadora acima, não há checagem se o dado entrado pelo usuário é inteiro ou conversível para inteiro,
# então aí é que entra a documentação, pois lá podemos encontrar uma função que verifica o tipo do dado entrado

# Por exemplo, as funções: isnumeric isdigit isdecimal
texto = input('Digite um texto: ')
print(f'O valor digitado é um número? {texto.isnumeric()}')  # isnumeric é uma função Built In do Python,
# mas você pode criar suas próprias funções
print()

# abaixo, a calculadora faz a soma, porém primeiro verificando se os valores entrados
# são conversíveis para inteiro
print('Calculadora com checagem.')
num3 = input('Digite mais um número: ')
num4 = input('Digite mais outro número: ')
if num3.isnumeric() and num4.isnumeric():
    num3 = int(num3)
    num4 = int(num4)
    resultado2 = num3 + num4
    print(resultado2)
else:
    print("Erro. Os dois valores devem ser números para efetuar a soma!")
print()

# aqui estão códigos criados pelo professor, com a criação de funções próprias, para fazer diversas checagens:
import re


def is_float(val):
    if isinstance(val, float): return True
    if re.search(r'^\-{,1}[0-9]+\.{1}[0-9]+$', val): return True

    return False


def is_int(val):
    if isinstance(val, int): return True
    if re.search(r'^\-{,1}[0-9]+$', val): return True

    return False


def is_number(val):
    return is_int(val) or is_float(val)


###########
#  USAGE  #
###########

# Float
print(is_float('-101.0112'))  # True
# Int
print(is_int('-1010112'))  # True
# Numbers in general (float ou int)
print(is_number('-1010.112'))  # True

# False
print(is_number('123a'))  # False