#Exercício Python 23: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separado
num = int(input("Digite um número: "))
u = num // 1 % 10
d = num //10 % 10
c = num // 100 % 10 
m = num // 1000 % 10
print("Analisando o número {}".format(num))
print("A unidade {}".format(u))
print("A dezena {}".format(d))
print("A centena {}".format(c))
print("A milahar {}".format(m))
