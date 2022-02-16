# condições IF, ELIF e ELSE

if True:
    print("Verdadeiro.")

if False:
    print("Verdadeiro.")
elif True:
    print("Mais um verdadeiro.")
    nome = input('Qual o seu nome? ')
    print(f'Seu nome é {nome}')
    print(22 + 222)
elif False:
    print("Agora é verdadeiro.")
else:
    print("Caso passe por todas as condições falsas, "
          "ele exibe o que está no else, caso a condição"
          "seja verdadeira.")