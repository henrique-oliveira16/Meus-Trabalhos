#Exercício Python 30: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
num = int(input("digite um número: "))
if num//2:
    print("O número {} e PAR".format(num))
else:
    print("O número {} e IMPAR".format(num))
