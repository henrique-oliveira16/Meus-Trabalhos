#Exercício Python 24: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.
cid = str(input("Qual a cidade: ")).strip()
print(cid[:5].upper() == 'Santo')
