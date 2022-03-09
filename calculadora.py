resultado = ''
while not resultado:
    num1 = input('Digite o primeiro número: ')
    if not num1.replace('.', '').isdigit():

        print('O valor digitado não é um número. Tente novamente.')
        continue
    else:
        num1 = float(num1)
    num2 = input('Digite o segundo número: ')
    if not num2.replace('.', '').isdigit():
        print('O valor digitado não é um número. Volte para o começo e tente novamente.')
        continue
    else:
        num2 = float(num2)
    operador = input('Digite o operador da operação matemática: [+], [-], [*] ou [/] ')
    if operador == '+':
        resultado = num1 + num2
    elif operador == '-':
        resultado = num1 - num2
    elif operador == '*':
        resultado = num1 * num2
    elif operador == '/':
        resultado = num1 / num2
    else:
        print('Operador inválido. Tente novamente')
        continue
    print(f'{resultado:.10f}')
resultado = ''
