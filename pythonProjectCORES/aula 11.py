a = 5
b = 20
print("Os nº são \033[0;35m{}\033[m e \033[0;36m{}\033[m!!!".format(a, b))
print("\033[7;30mOlá\033[m")
nome = "Marcella"
cores = {"limpa": "\033[m",
         "azul": "\033[34m",
         "cinza": "\033[37m",
         "branco": "\033[38m"}
print("Olá, muito prazer em te conhecer {}{}{}!!!".format(cores["azul"], nome, cores["cinza"]))
