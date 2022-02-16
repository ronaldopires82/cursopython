# operadores lógicos + if / elif / else
"""
Operadores lógicos

and -   adiciona uma expressão para ser testada e só retorna verdadeiro se ambas forem verdadeiras
or  -   adiciona uma exppressão para ser testada e retorna verdadeiro caso uma delas seja verdadeira
not -   nega a expressão, ou seja, retorna o valor booleano INVERSO do resultado

in  -   identifica se há uma sequência de caracteres no valor pesquisado, retorna
        verdadeiro se encontrar
not in  -   identifica se NÃO há uma sequência de caracteres no valor pesquisado, retorna
            verdadeiro se não encontrar
"""
# exemplo de utilização do and em um sistema de usuário e senha:
usuario = input('Digite seu nome de usuário: ')
senha = int(input('Digite sua senha NUMÉRICA de 6 dígitos: '))  # typecast para converter o string para inteiro

usuario_bd = 'Ronaldo'
senha_bd = 123456

if usuario == usuario_bd and senha == senha_bd:
    print('Acesso liberado!')
else:
    print('Usuário ou senha inválido.')

# exemplo de utilização do operador lógico not
a = int(input('Qual o valor de a? '))
b = 2

if b > a:
    print('B é maior do que A')
else:
    print('B não é maior do que A')

# agora com o not:
if not b > a:
    print('B é maior do que A')
else:
    print('B não é maior do que A')

# é muito utilizado para verificar se a variável está vazia (ou com zero), por exemplo:

if not a:
    a = input('Por favor, preencha o valor de A: ')
    print(a)

# os operadores lógicos in e not in são utilizados para pesquisa, da seguinte forma:
nome = input('Qual o seu nome? ')
letra = input('Digite uma letra que deseja pesquisar: ')
if letra in nome:
    print(f'A letra {letra} existe em seu nome')

