n1 = int(input('Digite o primeiro número inteiro: '))
n2 = int(input('Digite o segundo número inteiro: '))
if n1 > n2:
    print('O \033[35m primeiro valor \033[m é \033[36m maior \033[m')
elif n2 > n1:
    print('O \033[35m segundo valor \033[m é \033[36m maior \033[m')
elif n1 == n2:
    print('\033[35m Não existe \033[m valor maior, os dois são \033[36m iguais \033[m')
    