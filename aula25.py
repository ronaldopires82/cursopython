# operadores relacionais + if, elif e else
"""
Todos os operadores relacionais abaixo retornam valores booleanos (bool - True ou False)

== - testa se dois valores são iguais (operador "=" atribui um valor a uma variável)
> - testa se o primeiro valor é maior que o segundo
>= - testa se o primeiro valor é maior ou igual ao segundo
< - testa se o primeiro valor é menor do que o segundo
<= - testa se o primeiro valor é menor ou igual ao segundo
!= - testa se o primeiro valor é diferente do segundo
"""

num_1 = 2
num_2 = 2

resultado = num_1 == num_2  # o "=" está atribuindo o valor booleano do teste se num_1 é igual a num_2
print(resultado)

# e os testes condicionais funcionam praticamente da mesma forma,
# porém com cada um dos operadores e suas funcionalidades

var_1 = "Ronaldo"
var_2 = "Roneldo"

expressao = var_1 != var_2
print(expressao)

# exercício: suponha que uma pessoa só pode pegar um
# empréstimo se ela tiver mais do que 18 anos:

nome = input('Qual o seu nome? ')
idade = int(input('Qual a sua idade? '))
idade_limite = 18  # limite inferior para pegar empréstimo

if idade >= idade_limite:
    print(f'{nome} está aprovado para pegar empréstimo com idade limite mínima.')
else:
    print(f'{nome} NÃO ESTÁ APROVADO para pegar empréstimo com idade limite mínima!')

# variante: para pegar empréstimo tem de estar entre 18 e 35 anos

idade_inferior = 18
idade_superior = 35

if idade_inferior <= idade <= idade_superior:
    print(f'{nome} está aprovado para pegar empréstimo com faixa de idade.')
else:
    print(f'{nome} NÃO ESTÁ APROVADO para pegar empréstimo com faixa de idade!')
