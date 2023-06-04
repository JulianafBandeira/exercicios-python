num = int(input('Informe um número inteiro: '))
print('''Selecione uma base de conversão:
1---> Binário
2---> Octal
3---> Hexadecimal
  ''')

escolha = int(input('Sua escolha: '))

if escolha == 1:
    print('O número {} convertido para Binário é {}'.format(num, bin(num)[2:]))

elif escolha == 2:
    print('O número {} convertido para Octal é {}'.format(num, oct(num)[2:]))

elif escolha == 3:
    print('O número {} convertido para Hexadecimal é {}'.format(num, hex(num)[2:]))

else:
    print('Escolha inválida')