import random

jogador = str(input('Digite pedra/ papel/ tesoura: '))
acoes = ['pedra','papel','tesoura']
computador = random.choice(acoes)
print('Eu escolhi {}'.format(computador))

if jogador == 'pedra' and computador == 'papel':
    print('Você perdeu!')
elif jogador == 'papel' and computador == 'tesoura':
    print('Você perdeu!')
elif jogador == 'tesoura' and computador == 'pedra':
    print('Você perdeu!')
elif computador == 'pedra' and jogador == 'papel':
    print('Você venceu!')
elif computador == 'papel' and jogador == 'tesoura':
    print('Você venceu!')
elif computador == 'tesoura' and jogador == 'pedra':
    print('Você venceu!')
else:
    print('É um empate')