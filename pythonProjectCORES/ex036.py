valor = int(input("Digite o valor da casa: "))
salario = int(input("Digite o seu salário: "))
anos = int(input("Em quantos anos você pretende pagar a casa? "))
parcela = valor/(12*anos)
print("O valor das parcelas serão de: R${} por mês".format(parcela))
if parcela<30/100*salario:
    print("Parabéns, o seu empréstimo está \033[42maprovado\033[m !")
    print("O valor das parcelas serão de:{} R$ por mês".format(parcela))
else:
    print("O seu empréstimo \033[41mnão foi aprovado\033[m")

