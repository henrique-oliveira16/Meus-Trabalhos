#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
print("Digite um número quebrado")
from math import trunc # ou podera ser usado import math
num = float(input("Digite um número: "))
print("O valor digitado foi: {} o valor inteiro será: {}".format(num,trunc(num)))
