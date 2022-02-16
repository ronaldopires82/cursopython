# aula sobre operadores aritméticos
"""
+: adição, soma valores inteiros ou reais (float). Também serve para concatenar textos (strings)
-: subtração, subtrai valores inteiros ou reais (float).
*: multiplicação, multiplica valores inteiros ou reais. Também serve para repetir textos (strings)
/: divisão, divide valores inteiros ou reais, retornando valores reais (float)
//: divisão inteiro, divide valores inteiros ou reais, retornando valores inteiros ou reais (arredondados)
**: potenciação, eleva um número a outro, retornando um valor real (float)
%: módulo, calcula o resto da divisão entre dois valores inteiros ou reais, retornando valores inteiros (int)
(): altera a precedência entre operadores aritméticos, igual à matemática
A relação completa dos operadores e suas precedências está em:
https://docs.python.org/3/reference/expressions.html#operator-precedence
"""
print('exemplos de utilização do operador adição (+)')
print(10+10, type(10+10))  # soma dois números inteiros, retornando número inteiro
print(10+10.5, type(10+10.5))  # soma um inteiro com um real, retornando um real
print('Ronaldo' + '39', type('Ronaldo' + '39'))  # concatena o texto "Ronaldo" com o número 10 retornando texto
# para concatenar com o operador aritmético "+" deve-se utilizar somente strings
print('Ronaldo' + str(39), type('Ronaldo' + str(39)))  # ou assim, convertendo o valor de
# int para str através do typecasting

print('\n')

print('exemplos de utilização do operador subtração (-)')
print(10-10, type(10-10))  # subtrai dois números inteiros, retornando número inteiro
print(10.27-5.357, type(10.27-5.357))  # subtrai dois números reais, retornando número real
print(500-27.35, type(500-27.35))  # subtrai um número real de um número inteiro, retornando real

print('\n')

print('exemplos de utilização do operador multiplicação (*)')
print(10 * 10, type(10 * 10))  # multiplica dois inteiros, retornando inteiro
print(10.34 * 3.5, type(10.34 * 3.5))  # multiplica dois números reais, retornando real
print(1.5 * 35, type(1.5 * 35))  # multiplica um número real por um inteiro, retornando real
print(10 * 'Ronaldo', type(10 * 'Ronaldo'))  # repete o texto pela quantidade de vezes determinada
# por um inteiro, retornando um texto (str) - (não funfa com número real)

print('\n')

print('exemplos de utilização do operador divisão (/)')
print(10/2, type(10/2))  # divide dois inteiros, retorna real
print(10.7/4.2, type(10.7/4.2))  # divide dois reais, retorna real
print(10/3.2, type(10/3.2))  # divide um inteiro por um real, retorna real
print(10.7/3, type(10.7/3))  # divida um real por um inteiro, retorna real

print('\n')

print('exemplos de utilização do operador divisão inteiro (//)')
print(10//5, type(10//5))  # divide dois inteiros de resto 0, retorna int
print(10//3, type(10//3))  # divide dois inteiros de resto <> 0 (arredonda), retorna int
print(100//0.25, type(100//0.25))  # divide um inteiro por um real, com resto = 0, retorna float
print(100//0.83, type(100//0.83))  # divide um inteiro por um real, com resto <> 0 (arredonda), retorna float
print(3.5//3.5, type(3.5//3.5))  # divide dois reais, com resto = 0, retorna float
print(10.7//3.45, type(10.7//3.45))  # divide dois reais com resto <> 0 (arredonda), retorna float

print('\n')

print('exemplos de utilização do operador potenciação (**)')
print(2**10, type(2**10))  # eleva um inteiro a outro inteiro, retorna inteiro
print(2**3.4, type(2**3.4))  # eleva um inteiro a um real, retorna real

print('\n')

print('exemplos de utilização do operador módulo (%)')
print(10%2, type(10%2))  # módulo de dois inteiros com resto zero, retorna inteiro
print(10%3, type(10%3))  # módulo de dois inteiros com resto <> 0, retorna inteiro
print(10.4%5, type(10.4%5))  # módulo de um real por um inteiro, com resto <> 0, retorna real (float)
print(10.5%10.5, type(10.5%10.5))  # módulo de dois reais com resto = 0, retorna real

print('\n')

print('exemplos de utilização de precedência entre operadores ()')
print((2+5-3)*8/2)  # multiplicação e divisão antes de adição/subtração
print(2+5-3*8/2)  # multiplicação e divisão antes de adição/subtração
print(2**3/2*4)  # potenciação antes de divisão/multiplicação


