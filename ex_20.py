#Exercício Python 20: O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random
print("Digite o nome de 4 alunos")
n1 = str(input("primeiro aluno: "))
n2 = str(input("segundo aluno: "))
n3 = str(input("terceiro aluno: "))
n4 = str(input("quarto aluno: "))
lista = [n1,n2,n3,n4]
random.shuffle(lista)
print("A ordem de apresentação será: ")
print(lista)

