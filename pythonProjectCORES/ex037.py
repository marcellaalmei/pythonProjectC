n = int(input("Digite um número inteiro: "))
base = int(input("Qual base de conversão você quer usar?"
      "\n Pressione \033[1;31m (1) \033[m para binário"
      "\n Pressione \033[1;31m (2) \033[m para octal"
      "\n Pressione \033[1;31m (3) \033[m para hexadecimal"
                 "\n "))
if base == 1:
    binario = bin(n)
    print("Você escolheu a opção binário, o seu resultado é {}".format(binario))
elif base == 2:
    octal = oct(n)
    print("Você escolheu a opção octal, o seu resultado é {}".format(octal))
elif base == 3:
    hexa = hex(n)
    print("Você escolheu a opção hexadecimal, o seu resultado é {}".format(hexa))

