valorproduto = float(input('Informe o valor do produto: '))
print('''Como deseja pagar?
1---> À vista dinheiro/cheque 
2---> À vista no cartão
3---> Em até 2x no cartão                          
4---> Em 3x ou mais no cartão                           
                           ''')

formapagamento = int(input('Escolha uma opção'))
if formapagamento == 1:
    vltotal = valorproduto - (valorproduto * 10 / 100)

elif formapagamento == 2:
    vltotal = valorproduto - (valorproduto * 5 / 100)

elif formapagamento == 3:
    vltotal = valorproduto
    parcela = vltotal / 2
    print('O parcelamento será feito em 2x de {:.2f} sem juros'.format(parcela))

elif formapagamento == 4:
    vltotal = valorproduto + (valorproduto * 20 / 100)
    totalpar = int(input('Em quantas parcelas? '))
    parcela = vltotal / totalpar
    print('A compra será parcelada em {}x de {:.2f} com juros')

print('Sua compra de {:.2f} vai custar {:.2f}'.format(valorproduto,vltotal))



