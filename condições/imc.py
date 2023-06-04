import emoji
altura = float(input('Informe sua altura: '))
peso = float(input('Informe seu peso: '))

imc = peso / (altura ** 2)

if imc < 18.5:
   print(emoji.emojize('Abaixo do peso :zipper-mouth_face:'))
elif imc <= 25:
   print(emoji.emojize('Peso ideal :grinning_face:'))
elif imc <= 30:
   print(emoji.emojize('Sobrepeso :zipper-mouth_face:'))
elif imc <= 40:
   print(emoji.emojize('Obesidade :zipper-mouth_face:'))
else:
    print(emoji.emojize('Obesidade mórbida :zipper-mouth_face:'))



