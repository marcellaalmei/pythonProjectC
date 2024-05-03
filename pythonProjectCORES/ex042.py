a = float(input("Digite o comprimento da primeira reta: "))
b = float(input("Digite o comprimento da segunda reta: "))
c = float(input("Digite o comprimento da teceira reta: "))
if a < b+c and b < a+c and c < a+b:
    print("Essas retas podem formar um triângulo")
else:
    print("Essas retas não podem formar um triângulo")
if a > b+c and b > a+c and c > a+b:
    print('')
elif a < b+c and b < a+c and c < a+b and a == b == c:
    print("Este é um triângulo equilátero")
elif a < b+c and b < a+c and c < a+b and a == b != c or a == c != b or c == b != a:
    print('Este é um triângulo isósceles')
elif a < b+c and b < a+c and c < a+b and a != b != c:
    print('Este é um triângulo escaleno')
