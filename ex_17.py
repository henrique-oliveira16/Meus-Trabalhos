#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
#  Calcule e mostre o comprimento da hipotenusa.
from math import hypot # importando apenas e nescessario para o progama
co = float(input("Qual o comprimento do cateto oposto: "))
ca = float(input("Qual o comprimento do cateto adicente"))
hi = hypot(co,ca)
print("A hipotenusa ira medir {:.2f}".format(hi))