n1 = float(input("Digite sua primeira nota: "))
n2 = float(input("Digite sua segunda nota: "))
media = (n1+n2)/2
if media<5:
    print('REPROVADO')
elif 5< media < 6.9:
    print('RECUPERAÇÃO')
elif media > 7:
    print('APROVADO')
