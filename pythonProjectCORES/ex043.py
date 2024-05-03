peso = float(input('Digite seu peso em kg: '))
altura = float(input('Digite sua altura em metros: '))
imc = peso/ (altura*altura)
if imc < 18.6:
    print('Abaixo do peso')
elif 18.6 < imc < 26:
    print('Peso ideal')
elif 26 < imc < 31:
    print('Sobrepeso')
elif 31 < imc > 41:
    print('Obesidade')
elif imc > 40:
    print('Obesidade mórbida')
