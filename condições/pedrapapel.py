from random import randint
opcao = ('pedra','papel','tesoura')
maquina = randint(0,2)

print('''
0 - pedra
1 - papel
2 - tesoura
''')
jogador = int(input('Escolha uma opção: '))

if maquina == 0:
    if jogador == 0:
        print('Empate')
    elif jogador == 1:
        print('Jogador venceu')
    elif jogador == 2:
        print('computador venceu')
    else:
        print('Escolha inválida')

elif maquina == 1:
    if jogador == 0:
        print('Máquina venceu')
    elif jogador == 1:
        print('Empate')
    elif jogador == 2:
        print('jogador venceu')
    else:
        print('Escolha inválida')

elif maquina == 2:
    if jogador == 0:
        print('Jogador venceu')
    elif jogador == 1:
        print('Computador venceu')
    elif jogador == 2:
        print('Empate')
    else:
        print('Escolha inválida')







 

