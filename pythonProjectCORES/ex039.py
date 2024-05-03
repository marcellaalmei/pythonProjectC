idade = int(input('Digite sua idade: '))
if idade < 18:
    print('Você ainda não precisa de alistar no serviço militar, ainda faltam {} anos para isso'.format(18-idade))
elif idade == 18:
    print('Está na hora de se alistar no serviço militar.')
elif idade > 18:
    print('Você já passou do tempo de alistamento! Está {} anos atrasado.'.format(idade-18))
