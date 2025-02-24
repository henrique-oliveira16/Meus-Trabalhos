#Exercício Python 33: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
n1 = float(input("Qual o primeiro número?? "))
n2 = float(input("Qual o segundo número?? "))
n3 = float(input("Qual o terceiro número?? "))
if n1>n2 and n1>n3:
    maior = n1
if n2>n1 and n2>n3:
    maior = n2
if n3>n1 and n3>n2:
    maior = n3
if n1<n2 and n1<n3:
    menor = n1
if n2<n1 and n2<n3:
    menor = n2
if n3<n1 and n3<n2:
    menor = n3
if n1 and n2 and n3 == 0 :
    menor = n1 and n2 and n3 
print("o maior número é: {}".format(maior))
print("O menor número é: {}".format(menor))
