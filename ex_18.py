#Exercício Python 18: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math
angulo = float(input("Qual angulo você deseja?: "))
seno = math.sin(math.radians(angulo))
print("O âgunlo de {} tem o SENO de {:.2f} ".format(angulo,seno))
co = math.cos(math.radians(angulo))
print("O âgulo de {} tem o COSSENO de {:.2f}".format(angulo,co))
tan = math.tan(math.radians(angulo))
print("O âgulo de {} tem o TANGENTE de {:.2f} ".format(angulo,tan))