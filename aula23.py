# input - entrada de dados do usuário

variavel = '5.5'
outra_variavel = int(float(variavel))  # quando o typecasting converte uma variável
# de float para int, ela arredonda o valor
print(outra_variavel, type(outra_variavel))

nome = input('Qual o seu nome? ')

print(f'O usuário digitou {nome} e o tipo da variável é', type(nome))
print(f'O usuário digitou {nome} e o tipo de variável é {type(nome)}')  # sintaxe alternativa à da linha anterior

idade = int(input('Qual a sua idade? '))  # TUDO o que é digitado pelo usuário é
# compreendido pelo Python como STRING, então caso necessário deve-se converter a
# variável para int ou float através do typecasting

print(type(idade))
ano_nascimento = 2022 - idade

print()  # print vazio faz uma quebra linha, assim como o print(\n)

print(f'{nome} tem {idade} anos. '
      f'{nome} nasceu em {ano_nascimento}')

# calculadora simples resultando em concatenação, pois qualquer entrada
# de valores pelo usuário resulta em strings

numero_1 = input('Digite um número: ')
numero_2 = input('Digite um número: ')
resultado = numero_1 + numero_2

print(resultado, type(resultado))

print()

# agora a calculadora somando os valores após typecasting
resultado = int(numero_1) + int(numero_2)
print(resultado, type(resultado))