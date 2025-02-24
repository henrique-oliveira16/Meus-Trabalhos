#Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
import random 
print("------------------------------------------------")
print("Vou pensar em um numero de 0 a 5 tente adivinhar")
n = [0,1,2,3,4,5]
escolha = random.choice(n)
usuario = int(input("Qual número você acha??"))
if escolha==usuario:
    print("Parabens você acertou o número escolido pelo pc foi {} e o seu é {}".format(escolha,usuario))
    print("------------------------------------------------")
else:
    print("Você errou meu número foi {} o seu foi {}".format(escolha,usuario))
    print("------------------------------------------------")

