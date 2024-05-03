# if, elif, else
# elif pode repetir várias vezes
# else só uma vez
nome = str(input("Qual o seu nome?"))
if nome == "Marcella":
    print("Que nome bonito!")
elif nome == "Ana":
    print("Seu nome é comum")
else:
    print("Que nome feio!")
print("Tenha um bom dia, {}".format(nome))

