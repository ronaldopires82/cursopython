# como contar a quantidade de caracteres dentro de uma string
"""
len -   função que conta a quantidade de caracteres de um valor (string ou outros tipos de dados,
        porém NÃO FUNCIONA com tipos numéricos (float e int) e booleanos
"""
# exemplo de utilização em sistema de usuário / senha:
usuario = input('Digite o seu usuário: ')
qtd_caracteres = len(usuario)
print(usuario, qtd_caracteres, type(qtd_caracteres))

if qtd_caracteres < 6:
    print('Quantidade de caracteres menor do que 6.')
else:
    print('Você foi cadastrado no sistema.')

# dá também para contar a soma de uma quantidade de caracteres:
string1 = 'Teste'
string2 = 'Abóbada'

print(len(string1 + string2))  # utilizando o operador aritmético para concatenar os valores
print(len(string1) + len(string2))  # ou somando as quantidades de caracteres de cada valor