valor = float(input('Digite o valor do produto: '))
pg = int(input('Qual será a forma de pagamento? Digite o número da opção\n'
               '\033[35m 1. \033[m À vista dinheiro/ cheque \n'
               '\033[35m 2. \033[m À vista no cartão \n'
               '\033[35m 3. \033[m Em até 2x no cartão \n'
               '\033[35m 4. \033[m Em 3x ou mais no cartão\n'
               ' '))
a = 10/100*valor
b = 5/100*valor
c = 20/100*valor
if pg == 1:
    print('Você recebe 10% de desconto, valor final com desconto: {}'.format(valor-a))
elif pg == 2:
    print('Você recebe 5% de desconto, valor final com desconto: {}'.format(valor-b))
elif pg == 3:
    print('Você não recebe descontos, nem juros')
elif pg == 4:
    print('Será cobrado 20% de juros'.format(valor+c))
