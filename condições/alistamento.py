from datetime import date
anoatual = date.today().year
nascimento = int(input('Informe o ano de nascimento: '))
idade = anoatual - nascimento

if idade == 18:
    print('Ja pode se alistar')
elif idade < 18:
    i = 18-idade
    print('Faltam {} anos para o alistamento'.format(i))
elif idade > 18:
    i = idade-18
    print('Já deveria ter se alistado há {} anos'.format(i))