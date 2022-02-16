# Aula sobre a função print
print(123456)  # aqui ele vai mostrar na tela o número 123456, como um int
print('Ronaldo', 'Pires') # o print já mostra espaço automático, não precisa incluir
# além disso, cada "nome" entre as vírgulas é um argumento
print('Ronaldo', 'Pires', sep='-')  # você pode configurar o 'sep', de separador,
# como um dos argumentos da função print
print('Ronaldo', 'Pires', end='o fodão')  # você pode incluir um argumento para
# inserir ao final do texto, porém ele não faz a quebra de linha
print('qualquer coisa só pra quebrar a linha depois deste texto')
""""
As funções no Python são case sensitive, ou seja,
a sintaxe Print('Qualquer coisa') não funciona.
"""

# exercício da aula. Escreva seu CPF com a função print utilizando os argumentos da aula
print(294, 369, 478, sep='.', end='-')
print(95)
