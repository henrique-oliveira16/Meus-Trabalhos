#Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:
#– O nome com todas as letras maiúsculas e minúsculas.
#– Quantas letras ao todo (sem considerar espaços).
#– Quantas letras tem o primeiro nome.
nome =  str(input("Qual seu nome:"))
print("Seu nome em maiusculas é: {}".format(nome.upper()))
print("Seu nome em minusculas é: {}". format(nome.lower()))
print("Seu nome ao todo {} letras".format(len(nome)))
print("Seu primeiro nome tem:{}".format(nome.find(' ')))