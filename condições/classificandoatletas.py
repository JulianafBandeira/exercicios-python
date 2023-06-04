from datetime import date
anoatual = date.today().year
nascimento = int(input('Informe o ano de nascimento: '))
idade = anoatual - nascimento

if idade < 9:
    print('O atleta tem {} anos. (Mirim)'.format(idade))
elif idade <=14:
    print('O atleta tem {} anos. (Infantil)'.format(idade))
elif idade <=19:
    print('O atleta tem {} anos. (Júnior)'.format(idade))
elif idade <=25:
    print('O atleta tem {} anos. (Sênior)'.format(idade))

else:
    print('O atleta tem {} anos. (Master)'.format(idade))