l1 = float(input('Digite um número: '))
l2 = float(input('Digite um número: '))
l3 = float(input('Digite um número: '))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('É possível formar um triângulo ', end='')
    if l1 == l2 == l3:
        print('Equilátero')
    elif l1 != l2 != l3 != l1:
        print('Escaleno')
    else:
        print('Isósceles')
    
else:
    print('Não é possível formar um triângulo')