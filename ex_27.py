#Exercício Python 27: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
n = str(input("Digite seu nome completo: ")).strip()
nome = n.spliit()
print("Seu primeiro nome  e {}".format(nome[0]))
print("Seu ultimo nome e {}".format(nome[len(nome)-1]))

