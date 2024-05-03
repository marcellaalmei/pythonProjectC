idade = int(input('Por favor, digite a sua idade: '))
if 0 < idade < 10:
    print('A sua categoria é mirim')
elif 10 < idade < 15:
    print('A sua categoria é infantil')
elif 15 < idade < 20:
    print('A sua categoria é junior')
elif idade == 20:
    print('A sua categoria é sênior')
elif idade > 20:
    print('A sua categoria é master')