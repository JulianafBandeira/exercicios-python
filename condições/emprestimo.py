valorcasa = float(input('Informe o valor da casa: '))
salario = float(input('Informe o seu salário: '))
anos = int(input('Informe em quantos anos deseja pagar: '))

parcela = valorcasa/(anos * 12)
mim = salario * 30 / 100

if parcela > mim:
    print('Não é possível realizar esta compra')
else:
    print('Compra realizada com sucesso')
    print('O valor da parcela é de {:.2f}'.format(parcela))

