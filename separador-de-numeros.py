print("Bem-vindo ao programa separador de digitos de um número!\n")

numero = int(input("Digite um número: "))

u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10

print("Analisando o número {}".format(numero))
print("Unidade: {}".format(u))
print("Dezena: {}".format(d))
print("Centena: {}".format(c))
print("Milhar: {}".format(m))